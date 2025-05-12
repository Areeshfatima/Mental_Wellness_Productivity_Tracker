import streamlit as st
from user import User
from entry import Entry
from tracker import Tracker
from quotes import Quotes

st.title("🌿🧠 Mental Wellness & Productivity Tracker")

# Initialize classes
tracker = Tracker()
quotes = Quotes()

# Inputs
name = st.text_input("Enter your name.")
email = st.text_input("Enter your email.")
mood = st.slider("How do you feel today?", 0, 10, 5)
stress = st.slider("Stress level?", 0, 10, 5)
tasks = st.number_input("Number of tasks completed:", min_value=0, step=1)

if st.button("Submit Entry"):
    if name and email:
        user = User(name, email)
        entry = Entry(mood, stress, tasks)
        user.add_entry(entry)
        tracker.save_entry(entry)
        st.success("Entry saved successfully!")

        st.header("Past Entries")
        entries_df = tracker.load_entries()
        if not entries_df.empty:
            st.dataframe(entries_df)
        else:
            st.info("No past entries found.")
else:
        st.warning("Please enter your name and email before submitting.")
