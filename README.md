# Chat Project

This is a simple chat application built with Django. Users can register, log in, and send messages to each other.


# Features

- User Registration and Authentication: Secure sign-up and sign-in process.

- Real-time Messaging: Send and receive messages instantly.

- Responsive Design: Works seamlessly on desktop and mobile devices.

- User Profiles: Create and customize user profiles.

- Search Functionality: Easily find and chat with other users.

- Notifications: Get notified of new messages.

- Group Chats: Create and participate in group conversations.

# Technologies Used
- Backend: Django (Python)

- Frontend: HTML, CSS, JavaScript

- Database: SQLite (default for Django)

- Websockets: Django Channels for real-time communication

- Authentication: Django's built-in authentication system


# Installation

### 1. Clone the repository:

```sh
git clone https://github.com/Karthi2112/chat_project.git
cd chat_project
```
### 2. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the dependencies:
```
pip install -r requirements.txt
```

### 4. Apply the migrations:
```
python manage.py migrate
```

### 5. Run the development server:

```
python manage.py runserver
```

#### 6. Open your browser and go to ```http://127.0.0.1:8000/``` to see the application.

---

# Deployment

The application is hosted on **PythonAnywhere**. You can access it using the following link:

[Live App on PythonAnywhere](https://karthi028.pythonanywhere.com/)

---


# Usage
- Register a New User: Create a new account to start using the chat application.

- Log In with the Registered User: Access your account by logging in.

- Start Chatting: Send and receive messages with other registered users.


# Contributing
Contributions are welcome! Please follow these steps:

- Fork the Repository: Click on the 'Fork' button on GitHub.

- Clone Your Fork:
  ```
  git clone https://github.com/Karthi2112/chat_project.git
  cd chat_project
  ```
- Create a New Branch:
  ```
  git checkout -b feature-name
  ```
- Make Your Changes: Implement your feature or fix.

- Commit Your Changes:
  ```
  git commit -m "Add feature or fix"
  ```
- Push to Your Branch:
  ```
  git push origin feature-name
  ```
