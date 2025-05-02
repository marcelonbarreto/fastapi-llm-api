# 🔮 FastAPI LLM API

A lightweight FastAPI backend that integrates with OpenAI's GPT-3.5-turbo model to provide conversational completions via a RESTful `/ask` endpoint. The project includes CI/CD with GitHub Actions, test automation using Pytest and HTTPX, and secure API key management via `.env`.

---

## 🚀 Features

- ✅ FastAPI server with clean architecture
- 🤖 Integration with OpenAI GPT-3.5-turbo (via `openai>=1.0`)
- 🔐 Environment variable-based API key loading
- 🧪 Test suite with `pytest` and `httpx`
- 🔁 GitHub Actions CI workflow
- ⚙️ Easily extendable for Claude, Mistral, or Ollama

---

## 📦 Requirements

- Python 3.8+
- OpenAI API key
- (Optional) Virtual environment

---

## 🛠 Installation

```bash
git clone https://github.com/marcelonbarreto/fastapi-llm-api.git
cd fastapi-llm-api

python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Activate (Linux/macOS)
source venv/bin/activate

pip install -r requirements.txt

---

## 🔐 Environment Variables

```env
Create a .env file at the project root:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

---

## ▶️ Running the API

```bash
uvicorn app.main:app --reload
# Access the interactive docs:
🔗 http://127.0.0.1:8000/docs
uvicorn app.main:app --reload

---

## 📬 Example Request

```json
POST /ask
{
  "prompt": "Tell me a joke!"
}

---

## 🧪 Run Tests

```bash
pytest

Includes both endpoint tests and local test scripts like test_request.py.

---

## 🔁 CI/CD via GitHub Actions

The pipeline in .github/workflows/ci.yml installs dependencies and runs all tests on each push to main.

---

## 📁 Project Structure

```bash
.
├── app/
│   ├── main.py         # FastAPI app + routes
│   └── llm.py          # LLM integration logic
├── tests/
│   └── test_main.py    # API tests with pytest + httpx
├── test_request.py     # Standalone tester
├── .env.example        # Template for secrets
├── .gitignore
├── requirements.txt
├── README.md
└── .github/workflows/ci.yml

---

## 🧠 Error Handling

Handles common OpenAI errors gracefully:

✅ Invalid or missing API key

✅ Exceeded quota / billing error

✅ Generic fallback for uncaught issues

---

## 🤝 Contributions

PRs and suggestions are welcome!
Feel free to fork and customize for Claude, Ollama, or LM Studio integrations.

---

## 🔗 Links

 - https://platform.openai.com/account/api-keys
 - https://fastapi.tiangolo.com/
 - https://github.com/openai/openai-python

```bash

---

### ✅ Next Step:
1. Open PowerShell in your project folder
2. Run:

```yaml
---
### ✅ Next Step:
1. Open PowerShell in your project folder
2. Run:

```bash
notepad README.md

- Paste the full content above, save, then:

```bash
git add README.md
git commit -m "Add complete README with features, setup, usage, and docs"
git push






