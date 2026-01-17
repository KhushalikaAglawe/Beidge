import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Import your custom modules
from reasoning.reasoning_engine import get_reasoning
from sql_engine.sql_generator import generate_sql
from sql_engine.sql_validator import validate_sql
from sql_engine.sql_executor import execute_sql
from database.mysql_connector import get_connection

app = FastAPI(title="OnTopic NL2SQL")

# Security and Static Files
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
templates = Jinja2Templates(directory="frontend")

# --- Page Routes ---
@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/settings", response_class=HTMLResponse)
async def settings(request: Request):
    return templates.TemplateResponse("settings.html", {"request": request})

# --- API Endpoint ---
@app.post("/query")
async def query_question(request: Request):
    try:
        data = await request.json()
        question = data.get("question", "")
        if not question: return {"error": "Empty question"}

        plan = get_reasoning(question)
        sql = generate_sql(question)
        
        if not validate_sql(sql):
            return {"error": "Security violation: Query rejected."}

        conn, cursor = get_connection()
        result = execute_sql(sql, cursor)
        cursor.close()
        conn.close()

        return {"logical_plan": plan.get("steps", []), "sql": sql, "result": result}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)