import os

import streamlit as st
from app_utils import fetch_and_save_data
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
anilist_user_default = os.getenv("ANILIST_USER")

# Intro page
st.title("Anime Analysis")
st.write(
    "Welcome to the Anime Analysis Streamlit App! This app allows you to fetch and analyze your Anilist anime data."
)

# User input for Anilist username
anilist_user_input = st.text_input("Enter your Anilist username (leave blank to use default):", "")
anilist_user = anilist_user_input if anilist_user_input else anilist_user_default

# Fetch data button
if st.button("Fetch Data"):
    if anilist_user:
        st.write(f"Fetching data for user: {anilist_user}...")
        csv_files = fetch_and_save_data(anilist_user)

        if csv_files:
            st.success("Data has been fetched successfully!")
            for file in csv_files:
                with open(file, "rb") as f:
                    st.download_button(label=f"Download {file}", data=f, file_name=file, mime="text/csv")
        else:
            st.error("An error occurred while fetching the data.")
    else:
        st.warning("Please provide a valid Anilist username.")
