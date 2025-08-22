import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_excel("online_course_recommendation_v2.xlsx")

df = load_data()

st.title("🎯 Online Course Recommender")

user_input = st.text_input("Enter a keyword to find relevant courses (e.g. Python, Machine, Excel):")

# Simple keyword search in course_name
def recommend_courses(query, df, top_n=5):
    mask = df['course_name'].str.contains(query, case=False, na=False)
    return df[mask].sort_values(by='rating', ascending=False).head(top_n)

if user_input:
    results = recommend_courses(user_input, df)
    if not results.empty:
        st.success("Top matching courses:")
        for _, row in results.iterrows():
            st.markdown(f"### {row['course_name']}")
            st.write(f"👨‍🏫 Instructor: {row['instructor']}")
            st.write(f"📘 Level: {row['difficulty_level']}  | ⭐ Rating: {row['rating']}")
            st.markdown("---")
    else:
        st.warning("No matching courses found. Try another keyword.")
