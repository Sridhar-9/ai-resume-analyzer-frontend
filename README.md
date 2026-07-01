# 📄 AI Resume Analyzer — Frontend
 
A Streamlit-based web app that lets users upload their resume and instantly receive AI-powered feedback using Google Gemini 2.5 Flash.
 
🔗 **Live App**: [View on Streamlit](https://ai-resume-analyzer-bv2s755bacrazfmrpzbuf2.streamlit.app)  

 
---
 
## ✨ Features
 
- Upload a PDF resume (up to 2MB)
- Instant AI analysis powered by Gemini 2.5 Flash
- Results include:
  - ✅ ATS Score
  - 💪 Strengths
  - ⚠️ Weaknesses
  - 💡 Suggestions
  - 🔑 Missing Keywords
  - 🎯 Recommended Roles
---
 
## 🛠️ Tech Stack
 
| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| AI Model | Google Gemini 2.5 Flash |
| Backend | FastAPI (separate repo) |
| Deployment | Streamlit Community Cloud |
 
---
 
## 🚀 Run Locally
 
**1. Clone the repo**
```bash
git clone https://github.com/Sridhar-9/ai-resume-analyzer-frontend.git
cd ai-resume-analyzer-frontend
```
 
**2. Install dependencies**
```bash
pip install -r frontend/requirements.txt
```
 
**3. Create a `.env` file inside `frontend/`**
```env
BACKEND_URL=http://localhost:8000
API_SECRET_KEY=your_secret_key
```
 
**4. Run the app**
```bash
streamlit run frontend/app.py
```
 
> Make sure the backend is running locally before starting the frontend.
 
---
 
## 🔐 Environment Variables
 
| Variable | Description |
|---|---|
| `BACKEND_URL` | URL of the deployed or local FastAPI backend |
| `API_SECRET_KEY` | Shared secret key for backend authentication |
 
For Streamlit Cloud deployment, add these under **App Settings → Secrets** in TOML format:
```toml
BACKEND_URL = "https://your-render-url.onrender.com"
API_SECRET_KEY = "your_secret_key"
```
 
---
 
## 📁 Project Structure
 
```
frontend/
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── .env                # Local env variables (gitignored)
```
 
---
 
## 🌐 Deployment
 
Deployed on [Streamlit Community Cloud] for free.  
Auto-deploys on every push to the `main` branch.
 
---
 
## 🤝 Related
 
- [Backend Repo](https://github.com/Sridhar-9/ai-resume-analyzer-backend) — FastAPI backend deployed on Render
 
