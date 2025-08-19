# 🤖 AI-Powered Code Reviewer for Pull Requests

## 📌 Project Overview
Traditional code reviews are slow, manual, and error-prone, leading to bugs slipping into production.  
This project is an **AI-powered automated code reviewer** that integrates with GitHub Pull Requests to:
- Detect **security flaws**
- Highlight **complex code**
- Flag **style/standard violations**
- Provide **AI-generated suggestions**

> ⚡ Built to save developers' time and improve code quality with automated intelligence.

---

## 🚀 Features
- 🔍 **Static Code Analysis** – Parse Python code using AST & detect issues  
- 🤖 **LLM-Powered Suggestions** – Use an AI model to suggest improvements  
- 🔒 **Security Checks** – Detect SQL injections, hardcoded secrets, unsafe imports  
- 📊 **Complexity Analysis** – Flag overly complex functions/classes  
- 🔗 **GitHub Integration** – Automatically runs on Pull Requests (via webhook or GitHub Actions)  

---

## 🛠 Tech Stack
- **Python 3.9+**
- **Flask / FastAPI** (API service)
- **OpenAI / Code LLM APIs** (for AI suggestions)
- **AST & Radon** (code parsing & complexity analysis)
- **GitHub API / Webhooks** (integration)
- **Docker** (containerization)

---

## 📂 Project Structure
****
