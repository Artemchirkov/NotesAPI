# 📝 Notes Management REST API
[English](README.md) | [Русский](README_RU.md)

---

A fully-featured REST API service for managing notes, built with **Django REST Framework**, **PostgreSQL**, and **JWT Authentication**. The project is fully containerized using **Docker**.

## 🚀 Tech Stack

* **Backend:** Python 3.11, Django 5.x, Django REST Framework
* **Auth:** SimpleJWT (JWT Access / Refresh Tokens)
* **Database:** PostgreSQL
* **API Documentation:** OpenAPI 3.0 / Swagger UI (drf-spectacular)
* **DevOps:** Docker, Docker Compose

---

## 🛠️ Quick Start (Docker Compose)

### 1. Clone the repository
```bash
git clone [https://github.com/Artemchirkov/NotesAPI](https://github.com/Artemchirkov/NotesAPI)
cd NotesAPI
docker compose up --build -d
```
Live SwaggerUI
You can test the deployed API directly at:
http://193.23.218.26:3000/api/docs
