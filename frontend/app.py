import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()



BACKEND_URL = os.getenv("BACKEND_URL")



st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get AI feedback instantly 🚀")


uploaded_file = st.file_uploader("Upload pdf only",type=["pdf"],max_upload_size=2,label_visibility="collapsed")

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing with AI..."):

            files = {
                "file": (uploaded_file.name, uploaded_file, "application/pdf")
            }

            try:
                response = requests.post(
                    BACKEND_URL,
                    files=files,
                    timeout=30
                )

                if response.status_code == 200:
                    data = response.json()
                    analysis = data.get("analysis", {})

                    # 📊 SCORE 
                    score = analysis.get("score", 0)

                    st.subheader("📊 ATS Score")
                    if score >= 80:
                        st.success(f"{score}")
                    elif score >= 60:
                        st.warning(f"{score}")
                    else:
                        st.error(f"{score}")

                    # ✅ STRENGTHS
                    st.subheader("✅ Strengths")
                    for s in analysis.get("strengths", []):
                        st.write(f"- {s}")

                    # ⚠️ WEAKNESSES
                    st.subheader("⚠️ Weaknesses")
                    for w in analysis.get("weaknesses", []):
                        st.write(f"- {w}")

                    # 💡 SUGGESTIONS
                    st.subheader("💡 Suggestions")
                    for sug in analysis.get("suggestions", []):
                        st.write(f"- {sug}")

                    # 🔍 MISSING KEYWORDS 
                    missing_keywords = analysis.get("missing_keywords", [])
                    if missing_keywords:
                        st.subheader("🔍 Missing Keywords")
                        st.caption("Add these to improve your ATS score")

                        cols = st.columns(3)
                        for i, kw in enumerate(missing_keywords):
                            cols[i % 3].warning(kw)

                    # 💼 RECOMMENDED ROLES 
                    recommended_roles = analysis.get("recommended_roles", [])
                    if recommended_roles:
                        st.subheader("💼 Recommended Roles")
                        st.caption("Roles that match your profile")

                        for role in recommended_roles:
                            st.success(role)

                elif response.status_code == 429:
                    st.error("🚫 Rate limit reached. Please wait and try again.")

                elif response.status_code == 401:
                    st.error("🔐 Unauthorized. Check your API key.")

                else:
                    st.error("Something went wrong. Please try again later.")

            except requests.exceptions.Timeout:
                st.error("⏳ Request timed out. Try again.")

            except Exception as e:
                st.error("⚠️ Failed to connect to server.")
