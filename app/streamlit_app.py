import os
import streamlit as st
import pandas as pd
from app_utils import fetch_and_save_data
from explore_stats import basic_stats, anime_watched_by_year, episodes_watched_by_year, rating_distribution, top_genres
from dotenv import load_dotenv

load_dotenv()
anilist_user_default = os.getenv("ANILIST_USER")


if "data_fetched" not in st.session_state:
    st.session_state["data_fetched"] = False
if "data_frames" not in st.session_state:
    st.session_state["data_frames"] = None


st.sidebar.title("Navigation Menu")
st.sidebar.markdown("Navigate through the app:")
navigation = st.sidebar.radio("Go to:", ["Home", "Fetch Data", "Explore Stats", "Settings", "About"])


if navigation == "Home":
    st.markdown("<h1 style='text-align: center; color: #FF4500;'>🎥 Anime Odyssey 🎥</h1>", unsafe_allow_html=True)
    st.image("https://wallpapers.com/images/featured-full/anime-4k-uvwsx2m7duh51ale.jpg", use_column_width=True)

    st.write(
        "Welcome to the **Anime Odyssey**! This app allows you to fetch and analyze your AniList anime data. "
        "This is a work in progress and more features will be added soon. For more information, visit the "
        "[GitHub repository](https://github.com/Rohit04121998/Anime-Analysis)."
    )

elif navigation == "Fetch Data":
    st.markdown("### Fetch Data from AniList 📡")
    st.write(
        "You can fetch your anime data from AniList by providing your AniList username and selecting the list you want to fetch."
    )
    anilist_user_input = st.text_input(
        "Enter your Anilist username (leave blank to use default):",
        "",
        help="Your AniList username can be found in your account settings.",
        placeholder="e.g., anime_fan_123",
    )
    anilist_user = anilist_user_input if anilist_user_input else anilist_user_default

    status_options = ["COMPLETED", "PLANNING", "CURRENT"]
    selected_statuses = st.multiselect("Select the list you want to fetch:", status_options)

    if st.button("Fetch Data"):
        if anilist_user:
            if not selected_statuses:
                st.error("Please select at least one status to fetch data.")
            else:
                st.write(f"Fetching data for user: {anilist_user} for statuses: {', '.join(selected_statuses)}...")
                with st.spinner("Fetching data..."):
                    data_frames, anilist_user = fetch_and_save_data(
                        anilist_user, anilist_user_default, selected_statuses
                    )

                if data_frames:
                    st.success("Data has been fetched successfully!")
                    st.session_state["data_fetched"] = True
                    st.session_state["data_frames"] = data_frames

                    for i, df in enumerate(data_frames):
                        status = selected_statuses[i]
                        csv = df.to_csv(index=False).encode("utf-8")
                        st.download_button(
                            label=f"⬇️ Download {anilist_user}'s ({status}) anime data",
                            data=csv,
                            file_name=f"anilist_{anilist_user}_{status}_anime.csv",
                            mime="text/csv",
                        )
                else:
                    st.error("An error occurred while fetching the data.")
        else:
            st.warning("Please provide a valid Anilist username.")

    st.markdown(
        """
        Don't know your Anilist username? You can find it in your settings page on [Anilist](https://anilist.co/settings/account) under **Profile Settings**.
        """
    )

elif navigation == "Explore Stats":
    if not st.session_state["data_fetched"]:
        st.warning("Please fetch the data first before exploring stats.")
    else:
        st.markdown("### Explore Your Anime Stats")
        data_frames = st.session_state["data_frames"]
        combined_df = pd.concat(data_frames, ignore_index=True)

        analysis_options = st.sidebar.multiselect(
            "Select the analysis you want to explore:",
            [
                "Basic Stats",
                "Anime Watched by Year",
                "Episodes Watched by Year",
                "Average Rating",
                "Rating Distribution",
                "Top Genres",
                "Genre Distribution",
                "Top Longest Anime",
                "Anime by Source",
                "Seasons Watched",
            ],
        )

        if "Basic Stats" in analysis_options:
            basic_stats(combined_df)
        if "Anime Watched by Year" in analysis_options:
            anime_watched_by_year(combined_df)
        if "Episodes Watched by Year" in analysis_options:
            episodes_watched_by_year(combined_df)
        if "Rating Distribution" in analysis_options:
            rating_distribution(combined_df)
        if "Top Genres" in analysis_options:
            top_genres(combined_df)


elif navigation == "Settings":
    st.markdown("### Settings")
    st.write("This feature is coming soon! This section can include configuration options in the future.")

    st.subheader("Theme Customization")
    theme_choice = st.selectbox("Choose your theme", ["Light Mode", "Dark Mode", "Anime Theme"])
    st.write(f"Current theme: {theme_choice}")

    st.subheader("File Download Preferences")
    file_format = st.selectbox("Preferred file format", ["CSV", "JSON", "Excel (.xlsx)"])
    st.write(f"Current file format: {file_format}")

elif navigation == "About":
    st.markdown("### About Anime Analysis App")
    st.write(
        "The **Anime Analysis App** fetches and analyzes data from AniList. "
        "It allows users to download their anime lists and explore a wide range of statistics, including watch times, "
        "ratings, and more. You can find the code for this app on GitHub."
    )
    st.markdown("Developed by Rohit Veeradhi")
