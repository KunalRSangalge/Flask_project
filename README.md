# Flask Market - Dockerized Multi-Container Application

A fully containerized e-commerce style Flask application using MySQL, Docker, and Docker Compose.

This project demonstrates:

* Flask backend development
* MySQL database integration
* Docker containerization
* Multi-container orchestration using Docker Compose
* Automatic database initialization
* Healthchecks and startup synchronization
* Portable development environments

---

# Features

* User Registration & Login
* Password Hashing using Flask-Bcrypt
* Flask-Login Authentication
* MySQL Database Integration
* Dockerized Flask Application
* Dockerized MySQL Database
* Automatic Database Table Creation
* Automatic Demo Data Seeding
* Persistent Database Volumes
* Healthcheck-Based Service Coordination
* Cross-Machine Reproducibility
* Docker Hub Integration

---

# Tech Stack

## Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-WTF
* Flask-Login
* Flask-Bcrypt

## Database

* MySQL

## DevOps / Containerization

* Docker
* Docker Compose

## Frontend

* HTML
* Bootstrap
* Jinja2 Templates

---

# Architecture

```text
Browser
   ↓
Flask Container
   ↓
MySQL Container
```

Managed using Docker Compose.

---

# Project Structure

```bash
Flask_Market/
│
├── market/
│   ├── templates/
│   │   ├── includes/
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
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── init_db.py
├── wait-for-db.py
├── run.py
├── requirements.txt
└── README.md
```

---

# Dockerized Features

## Flask Container

Contains:

* Flask application
* Python runtime
* Dependencies
* Database initialization scripts

## MySQL Container

Contains:

* MySQL Server
* Persistent Docker volume storage

---

# Automatic Startup Flow

When running Docker Compose:

```text
Start MySQL
    ↓
Healthcheck verifies readiness
    ↓
Flask waits for DB availability
    ↓
Tables auto-created
    ↓
Demo data auto-seeded
    ↓
Flask app starts
```

---

# Requirements

* Docker Desktop installed
* Docker Compose enabled

No need to install:

* Python
* MySQL
* Flask

Everything runs inside containers.

---

# Running The Project

## Clone Repository

```bash
git clone https://github.com/KunalRSangalge/Flask_project.git
cd Flask_Market
git checkout mysql-docker 
```

---

## Start Application

```bash
docker compose up
```

Open browser:

```text
http://localhost:5000
```

---

# First Startup

On first run:

* MySQL container initializes
* Tables are created automatically
* Demo users and items are seeded automatically

---

# Demo Users

| Username | Password |
| -------- | -------- |
| kunal    | pass1    |
| alex     | pass2    |
| bot      | kaushik  |

---

# Docker Hub

Flask image hosted on Docker Hub:

```text
kunal5002/flask-market-app:latest
```

---

# Useful Docker Commands

## Stop Containers

```bash
docker compose down
```

---

## Remove Containers + Volumes

```bash
docker compose down -v
```

---

## Rebuild Containers

```bash
docker compose up --build
```

---

## Pull Latest Image

```bash
docker compose pull
```

---

# Healthchecks

The MySQL container uses Docker healthchecks to ensure Flask only starts after the database is fully ready.

---

# Persistent Storage

MySQL data is stored using Docker volumes:

```yaml
volumes:
  mysql_data:
```

This prevents data loss between container restarts.

---

# Future Improvements

* Gunicorn Integration
* Nginx Reverse Proxy
* Buy/Sell Item Functionality
* REST APIs
* JWT Authentication
* Kubernetes Deployment
* CI/CD Pipelines
* Cloud Deployment
* Redis Caching
* Admin Dashboard

---

# Author

Kunal Rajesh Sangalge

---

# License

This project is built for educational and learning purposes.
