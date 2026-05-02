import streamlit as st
import pickle

# Load model

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Career mapping

career_map = {
"tech": "💻 Software Engineer / Data Scientist",
"design": "🎨 UI/UX Designer / Graphic Designer",
"medical": "🩺 Doctor / Biotech",
"commerce": "💼 Business / MBA",
"sports": "🏋️ Athlete / Fitness Trainer",
"law": "⚖️ Lawyer / Legal Advisor"
}

# Clean text

def clean_text(text):
    return text.lower()

# Predict function

def predict_career(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]
    return career_map.get(pred, "Try something else")

# UI

st.title("🎯 AI Career Counsellor")

st.write("Enter your interests:")

user_input = st.text_input("Example: coding, business, art")

if st.button("Get Career Suggestion"):
    if user_input.strip() == "":
        st.warning("Please enter something!")
    else:
        result = predict_career(user_input)
        st.success(f"Recommended Career: {result}")
