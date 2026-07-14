import streamlit as st
import google.generativeai as genai



# Gemini API Key
api_key = st.secrets[ "GEMINI_API_KEY"]
genai.configure(api_key=api_key)
google_api_key=st.secrets["GOOGLE_MAP_API_KEY"]
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🎓 AI Student Result Analyzer")

# Student Details
name = st.text_input("Student Name")
age = st.number_input("Age", min_value=15, max_value=30, value=18)

english = st.number_input("English Marks", 0, 100)
physics = st.number_input("Physics Marks", 0, 100)
chemistry = st.number_input("Chemistry Marks", 0, 100)
maths = st.number_input("Maths Marks", 0, 100)
computer = st.number_input("Computer Marks", 0, 100)

if st.button("Analyze Result"):

    total = english + physics + chemistry + maths + computer
    percentage = total / 5

    prompt = f"""
    Analyze this student's 12th board result.

    Name: {name}
    Age: {age}

    Marks:
    English: {english}
    Physics: {physics}
    Chemistry: {chemistry}
    Maths: {maths}
    Computer: {computer}

    Total Marks: {total}/500
    Percentage: {percentage:.2f}%

    Give:
    1. Performance Analysis
    2. Strong Subjects
    3. Weak Subjects
    4. Career Suggestions
    5. Improvement Tips
    6. Motivational Message

    Use simple English.
    """

    response = model.generate_content(prompt)

    st.subheader("📊 Result")
    st.write(f"Total Marks: {total}/500")
    st.write(f"Percentage: {percentage:.2f}%")

    st.subheader("🤖 AI Analysis")
    st.markdown(response.text)
