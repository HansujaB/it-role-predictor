# 🧠 IT Role Predictor

This is a Streamlit web application that predicts the most suitable IT role for a user based on their skill levels across various technical and soft skills. The prediction is powered by a trained random Forest model.

## Deployed on Render
https://it-role-predictor.onrender.com/

## 🚀 Features

- 17 skill inputs including Programming, AI/ML, Communication, and more
- Predicts ideal IT role using a trained `RandomForestClassifier` model
- Clean and interactive UI built with Streamlit
- Deployed on Render

## 📊 Skills Considered

- Database Fundamentals  
- Computer Architecture  
- Distributed Computing Systems  
- Cyber Security  
- Networking  
- Software Development  
- Programming Skills  
- Project Management  
- Computer Forensics Fundamentals  
- Technical Communication  
- AI ML  
- Software Engineering  
- Business Analysis  
- Communication skills  
- Data Science  
- Troubleshooting skills  
- Graphics Designing  

Each skill is rated by the user using one of the following levels:

- Not Interested
- Poor
- Beginner
- Average
- Intermediate
- Excellent
- Professional

## 🔮 Predicted IT Roles

The app can suggest one of several IT roles, such as:

- Software Developer  
- AI/ML Specialist  
- Cyber Security Specialist  
- Project Manager  
- Data Scientist  
- Technical Writer  
- Graphics Designer  
- ...and more

## 🛠️ Technologies Used

- Python 🐍
- Streamlit
- scikit-learn
- pandas
- joblib

## 📁 Project Structure 
<br>
  it-role-predictor/  <br>
├── app.py                # Streamlit frontend  <br>  
├── skill_prediction_model.pkl  # Trained ML model  <br>  
├── requirements.txt         # Python dependencies  <br>  
└── README.md                # Project documentation  <br>  

