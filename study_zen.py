import streamlit as st
import requests
import json
import random
from streamlit_lottie import st_lottie

# ✅ Secure API Key
API_KEY = "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"

# ✅ Load Lottie Animation
st.set_page_config(page_title="StudyZen: Your AI Study Planner & Note-Taking Assistant", page_icon="📚", layout="centered")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ✅ OpenRouter AI Function for Study Recommendations
@st.cache_data
def get_study_recommendations(user_input):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "deepseek/deepseek-r1:free",
                "messages": [
                    {"role": "system", "content": "You are an AI assistant that helps students plan their studies, take smart notes, and provide personalized recommendations based on their input."},
                    {"role": "user", "content": user_input}
                ]
            })
        )
        response_json = response.json()
        return response_json["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"API Error: {str(e)}"

# 🌿 Light Mode Theme Styling
st.markdown("""
    <style>
        body { background-color: #f7f9fc; }
        h1 { color: #2c3e50; font-size: 36px; font-weight: bold; text-align: center; }
        .subtitle { color: #34495e; font-size: 18px; text-align: center; margin-bottom: 30px; }
        .button-container { text-align: center; }
        .stButton>button { background-color: #4CAF50; color: white; border-radius: 8px; padding: 10px 20px; font-size: 18px; }
        .stTextArea>div>div>textarea { font-size: 16px; }
        .stMarkdown h2 { color: #2c3e50; font-size: 28px; font-weight: bold; }
        .stMarkdown h3 { color: #34495e; font-size: 22px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 🌿 Header Section
st.markdown("""
    <style>
        .subtitle { color: white; font-size: 18px; text-align: center; margin-bottom: 30px; }
    </style>
    <h1>📚 StudyZen: Your AI Study Planner & Note-Taking Assistant 🧠</h1>
    <p class='subtitle'>Empowering your academic journey with smart planning, personalized recommendations, and efficient note-taking.</p>
""", unsafe_allow_html=True)

# 🌟 Study Planner Section
st.markdown("""
    <style>
        * {
            font-family: 'Times New Roman', Times, serif;
        }
    </style>
""", unsafe_allow_html=True)
st.subheader("📅 Study Planner")
st.write("Plan your study sessions, set goals, and get personalized recommendations based on your current mood or workload.")
user_input = st.text_area("What's on your mind today?", placeholder="I need to study for my exams...", height=120)

if st.button("🚀 Get Study Plan", use_container_width=True):
    if user_input:
        with st.spinner("Generating your personalized study plan..."):
            result = get_study_recommendations(user_input)
        if "API Error" in result:
            st.error(result)
        else:
            st.success("🎯 Here's your personalized study plan:")
            st.write(result)
    else:
        st.warning("Please enter some text to generate a study plan.")

# 📝 Smart Note-Taking Section
st.subheader("📝 Smart Note-Taking")
st.write("Jot down your notes, and let StudyZen organize them for you. You can also ask for summaries or key points.")
note_input = st.text_area("Write your notes here...", placeholder="Today's lecture covered...", height=150)

if st.button("✨ Organize Notes", use_container_width=True):
    if note_input:
        with st.spinner("Organizing your notes..."):
            result = get_study_recommendations(f"Organize and summarize these notes: {note_input}")
        if "API Error" in result:
            st.error(result)
        else:
            st.success("📑 Here's your organized note:")
            st.write(result)
    else:
        st.warning("Please enter some notes to organize.")

# 🎲 Feeling Spontaneous? Get Random Study Tips
st.subheader("🎲 Feeling Spontaneous?")
if st.button("I need a Study Tip! 🎉", use_container_width=True):
    study_tips = [
        "Break your study sessions into 25-minute chunks with 5-minute breaks (Pomodoro Technique).",
        "Use flashcards to memorize key concepts and terms.",
        "Teach what you've learned to someone else—it reinforces your understanding.",
        "Create mind maps to visualize complex topics.",
        "Practice past exam papers to get familiar with the format and timing.",
        "Stay hydrated and take short walks to refresh your mind.",
        "Use mnemonic devices to remember lists or sequences.",
        "Set specific, achievable goals for each study session.",
        "Avoid multitasking—focus on one subject at a time.",
        "Review your notes within 24 hours to improve retention."
    ]
    st.write(f"💡 **Study Tip:** {random.choice(study_tips)}")

# 🌸 Final Message
st.markdown("""
<p style='text-align: center; font-size: 22px;'>
    🌱 <strong>Empowering Your Academic Journey</strong><br>
    Success is not just about hard work—it's about smart work. With StudyZen, you can plan effectively, take better notes, and stay motivated throughout your academic journey. 🌿
</p>

<p style='text-align: center; font-size: 22px;'>
    🧠 <strong>The Power of Organized Learning</strong><br>
    A well-organized study plan and efficient note-taking can transform your learning experience. Whether you're preparing for exams or working on a project, StudyZen is here to guide you every step of the way. 📚
</p>

<p style='text-align: center; font-size: 22px;'>
    🌼 <strong>Words to Remember</strong><br>
    Consistency is key—small, regular efforts lead to big results.<br>
    Focus on understanding, not just memorization.<br>
    Take care of your mind and body—they are your greatest assets.
</p>

<p style='text-align: center; font-size: 22px;'>
    🌸 Let StudyZen be your partner in achieving academic excellence. Every step forward is a step towards your goals. 🌸
</p>
<p style='text-align: center; font-size: 22px; font-weight: bold;'>
    💙 Made with love and dedication by [Your Name/Brand] 🙏
</p>
""", unsafe_allow_html=True)