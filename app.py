import streamlit as st
import joblib
import pandas as pd

st.title("🧠 IT Role Prediction App")
st.subheader("Discover your ideal IT career path based on your skill levels")

st.markdown("""
This app helps you find the most suitable IT role for you by analyzing your self-assessed skill levels 
in various tech and soft skills. Select your current proficiency in each skill from the dropdowns below, 
and get a personalized career recommendation.
""")

# Load model
model = joblib.load("it_role_prediction_model.pkl")

# Define skill mappings
skill_mapping = {
'Not Interested':0, 'Poor':1, 'Beginner':2, 'Average':3, 'Intermediate':4,
       'Excellent':5, 'Professional':6
}

it_role_mapping = {
    3: "Database Administrator", 6: "Hardware Engineer",
    0: "Application Support Engineer", 2: "Cyber Security Specialist",
    9: "Networking Engineer", 14: "Software Developer",
    1: "API Specialist", 11: "Project Manager",
    7: "Information Security Specialist", 16: "Technical Writer",
    15: "AI ML Specialist", 13: "Software Tester",
    4: "Business Analyst", 5: "Customer Service Executive",
    8: "Data Scientist", 10: "Helpdesk Engineer",
    12: "Graphics Designer"
}

skill_features = [
    "Database Fundamentals", "Computer Architecture", "Distributed Computing Systems", "Cyber Security",
    "Networking", "Software Development", "Programming Skills", "Project Management",
    "Computer Forensics Fundamentals", "Technical Communication", "AI ML", "Software Engineering",
    "Business Analysis", "Communication skills", "Data Science", "Troubleshooting skills", "Graphics Designing"
]

st.subheader("Predict Now!")

# User input
user_skills = {}
for skill in skill_features:
    user_skills[skill] = st.selectbox(skill, list(skill_mapping.keys()), key=skill)

# Prediction
if st.button("Predict Role"):
    input_values = [skill_mapping.get(user_skills.get(skill, "Not Interested"), 0) for skill in skill_features]
    input_df = pd.DataFrame([input_values], columns=skill_features)
    predicted_role_num = model.predict(input_df)[0]
    predicted_role = it_role_mapping.get(predicted_role_num, "Unknown Role")
    st.success(f"Predicted Role: {predicted_role}")