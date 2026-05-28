# Flask Market

A simple e-commerce style web application built using Flask, SQLAlchemy, WTForms, and Flask-Login.

Users can:

* Register and Login
* Browse Market Items
* Own Purchased Items
* View User Budget
* Manage Authentication Sessions

---

# Features

* User Authentication System
* Password Hashing using Flask-Bcrypt
* SQLite Database Integration
* Flask-Login Session Management
* Dynamic Market Page
* Item Ownership Relations
* Bootstrap Styled UI
* Modular Flask Project Structure
* Flash Message Notifications

---

# Tech Stack

## Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-WTF
* Flask-Login
* Flask-Bcrypt

## Frontend

* HTML
* Bootstrap
* Jinja2 Templates

## Database

* SQLite

---

# Project Structure

```bash
Flask_Market/
│
├── market/
│   ├── templates/
│   │   ├── includes/
│   │   │   ├── items_modals.html
│   │   │   └── owned_items_modals.html
│   │   │
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── market.html
│   │   └── register.html
│   │
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── routes.py
│
├── instance/
│   └── market.db
│
├── add_items.py
├── seed.py
├── test_db.py
├── run.py
├── requirements.txt
└── .gitignore
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/KunalRSangalge/Flask_project.git
cd Flask_Market
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Start the Flask server:

```bash
python run.py
```

Open in browser:

```bash
http://127.0.0.1:5000
```

---

# Database Setup

## Create Database Tables

```bash
python seed.py
```

---

## Add Market Items

```bash
python add_items.py
```

---

## Test Database Contents

```bash
python test_db.py
```

---

# Authentication

The application supports:

* User Registration
* User Login
* User Logout
* Session Management

Passwords are securely hashed using Flask-Bcrypt.

---

# Models

## User Model

```python
class User(db.Model):
```

Stores:

* Username
* Email
* Password Hash
* Budget
* Owned Items

---

## Item Model

```python
class Item(db.Model):
```

Stores:

* Item Name
* Price
* Barcode
* Description
* Owner Relation

---

# Future Improvements

* Buy/Sell Functionality
* Wallet Transactions
* Product Images
* Search & Filtering
* Admin Dashboard
* REST APIs
* Docker Support
* PostgreSQL Migration
* Kubernetes Deployment

---

# Requirements

Example `requirements.txt`

```txt
flask
flask-sqlalchemy
flask-wtf
flask-login
flask-bcrypt
email-validator
```

---

# Author

Kunal Rajesh Sangalge

---

# License

This project is built for learning and educational purposes.
