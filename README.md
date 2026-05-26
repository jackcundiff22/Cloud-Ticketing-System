# Cloud Ticketing System

A cloud-hosted ticket management web application built using Flask, SQLite, NGINX, Gunicorn, Docker, and Azure Linux infrastructure.

This project demonstrates real-world cloud engineering, Linux administration, backend development, reverse proxy configuration, authentication, containerization, and database management.

---

# Features

- User login authentication
- Session management
- Ticket creation
- Ticket closing
- Ticket deletion
- Ticket filtering (Open / Closed)
- Ticket priority levels
- SQLite database integration
- Docker containerization
- Gunicorn production server
- NGINX reverse proxy
- systemd service management
- Azure VM deployment

---

# Technologies Used

## Cloud / Infrastructure
- Microsoft Azure
- Azure Linux Virtual Machine
- Azure NSG Firewall Rules

## Backend
- Python
- Flask
- Gunicorn
- SQLite

## Frontend
- HTML
- CSS

## Linux / DevOps
- Ubuntu Linux
- NGINX
- systemd
- Docker

---

# Architecture

Browser
↓
NGINX Reverse Proxy
↓
Gunicorn
↓
Flask Application
↓
SQLite Database

---

# Project Features Explained

## Authentication
Implemented session-based login authentication using Flask sessions.

## CRUD Functionality
- Create tickets
- Read tickets
- Update ticket status
- Delete tickets

## Database
SQLite database stores:
- ticket ID
- timestamp
- status
- priority
- issue text

## Reverse Proxy
NGINX forwards browser requests to the Flask/Gunicorn backend running locally on the VM.

## Docker
The application was containerized using Docker for portable deployments.

## systemd
Gunicorn runs persistently as a Linux service managed by systemd.

---

# Setup Instructions

## Clone Repository

```bash
git clone YOUR_GITHUB_LINK
cd ticket-backend
```

## Create Virtual Enviroment 

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies 

```bash
pip install -r requirements.txt
```

## Run Flask App

```bash
python3 app.py
```

# Docker Setup 

## Build Docker Image

```bash
sudo docker build -t ticketapp .
```

## Run Docker Container 

```bash
sudo docker run -p 5001:5000 ticketapp
```

# systemd Service Management 

## Check Status 

```bash
sudo systemctl status ticketapp
```

## Restart Service 

```bash
sudo systemctl restart ticketapp
```

# SQLite Commands 

## Open Database 

```bash
sqlite3 tickets.db
```

## View Tables 

```bash
.tables
```

## View Tickets 

```bash
SELECT * FROM tickets;
```

## Skills Demonstrated 

- Linux Administration
- Cloud Infrastructure
- Reverse Proxy Configuration
- Backend Development
- Database Management
- Authentication & Sessions
- Docker Containerization
- Service Management
- Networking
- Troubleshooting
- CRUD Operations

## Future Improvements 

- HTTPS with Let's Encrypt
- Azure SQL Database
- Terraform Infrastructure as Code
- CI/CD Pipeline
- Kubernetes Deployment
- Role-Based Authentication

## Screenshots 

(Uploaded in Repo)
