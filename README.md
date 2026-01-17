# OnTopic.ai: NL2SQL Database Explorer

A FastAPI-based application that translates Natural Language (English) into SQL queries to interact with the **Chinook** and **Student** databases.

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.9+
* MySQL Server (with Chinook database loaded)
* Virtual Environment (venv)

### 2. Installation
Install the required dependencies using the virtual environment's pip:
```bash
./venv/bin/python3 -m pip install fastapi uvicorn jinja2 aiofiles mysql-connector-python