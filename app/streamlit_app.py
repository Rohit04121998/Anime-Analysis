import os
import streamlit as st
from app_utils import fetch_and_save_data
from dotenv import load_dotenv

load_dotenv()
anilist_user_default = os.getenv("ANILIST_USER")

st.title("Anime Analysis")
st.write(
    "Welcome to the Anime Analysis Streamlit App! This app allows you to fetch and analyze your Anilist anime data."
)

anilist_user_input = st.text_input("Enter your Anilist username (leave blank to use default):", "")
anilist_user = anilist_user_input if anilist_user_input else anilist_user_default

if st.button("Fetch Data"):
    if anilist_user:
        st.write(f"Fetching data for user: {anilist_user}...")
        data_frames, anilist_user = fetch_and_save_data(anilist_user, anilist_user_default)

        if data_frames:
            st.success("Data has been fetched successfully!")

            for i, df in enumerate(data_frames):
                status = ["COMPLETED", "PLANNING", "CURRENT"][i]
                csv = df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label=f"Download {anilist_user}'s ({status} anime data)",
                    data=csv,
                    file_name=f"anilist_{anilist_user}_{status}_anime.csv",
                    mime="text/csv",
                )
        else:
            st.error("An error occurred while fetching the data.")
    else:
        st.warning("Please provide a valid Anilist username.")
