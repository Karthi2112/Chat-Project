from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q  
from .models import Message
from .forms import CustomUserCreationForm, CustomAuthenticationForm
import json  

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat_home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def chat_home(request):
    users = User.objects.exclude(id=request.user.id) 
    return render(request, 'chat_home.html', {'users': users})

@login_required
def fetch_messages(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        messages = Message.objects.filter(
            (Q(sender=request.user) & Q(receiver=user)) | (Q(sender=user) & Q(receiver=request.user))
        ).order_by('timestamp')
        message_data = [
            {
                'id': msg.id,
                'sender_id': msg.sender.id,
                'receiver_id': msg.receiver.id,
                'content': msg.content,
                'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            }
            for msg in messages
        ]
        return JsonResponse({'messages': message_data})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@login_required
def send_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  
            receiver_id = data.get('receiver_id')
            content = data.get('content')

            if not receiver_id or not content:
                return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)

            receiver = User.objects.get(id=receiver_id)
            Message.objects.create(sender=request.user, receiver=receiver, content=content)
            return JsonResponse({'status': 'Message sent successfully!'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Receiver not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
