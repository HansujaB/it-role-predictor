# 🧠 IT Role Predictor

This is a Streamlit web application that predicts the most suitable IT role for a user based on their skill levels across various technical and soft skills. The prediction is powered by a trained Machine Learning model.

## 🚀 Features

- 17 skill inputs including Programming, AI/ML, Communication, and more
- Predicts ideal IT role using a trained `RandomForestClassifier` model
- Clean and interactive UI built with Streamlit
- Deployable on platforms like Render or Streamlit Cloud

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

#📁 Project Structure
  it-role-predictor/
├── app.py                   # Streamlit frontend
├── skill_prediction_model.pkl  # Trained ML model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation

