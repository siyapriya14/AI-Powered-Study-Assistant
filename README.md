# 📚 AI-Powered Study Assistant

[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)

A Flask-based web application designed to accelerate student learning workflows by processing PDF notes, extracting contextual information, generating summaries, and dynamically creating interactive quizzes.

---

## 💡 Key Features

- **PDF Text Extraction:** High-accuracy PDF parsing and document text processing via `pdfplumber`.
- **Automated Summarization:** Algorithmic summary generation to distill long lecture notes into key insights.
- **Dynamic Quiz Generator:** Instant generation of quiz questions based on uploaded study materials.
- **Interactive Contextual Q&A:** Query interface allowing students to interact directly with uploaded documents.
- **Modern Dark UI:** Clean, modern HTML5/CSS3 frontend interface.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Text Processing & Parsing:** `pdfplumber`
- **Frontend:** HTML5, CSS3, JavaScript
- **Infrastructure:** Gunicorn (ASGI/WSGI), Render Cloud Hosting

---

## ⚡ Local Installation

### 1. Clone & Setup Environment
```bash
git clone [https://github.com/siyapriya14/AI-Powered-Study-Assistant.git](https://github.com/siyapriya14/AI-Powered-Study-Assistant.git)
cd AI-Powered-Study-Assistant
python -m venv .venv
.venv\Scripts\activate
