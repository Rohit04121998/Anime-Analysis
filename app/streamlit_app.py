import os

import streamlit as st
from app_utils import fetch_and_save_data
from dotenv import load_dotenv

load_dotenv()
anilist_user_default = os.getenv("ANILIST_USER")


st.sidebar.title("Navigation Menu")
st.sidebar.markdown("Navigate through the app:")
navigation = st.sidebar.radio("Go to:", ["Home", "Fetch Data", "Explore Stats", "Settings", "About"])

if navigation == "Home":
    st.markdown("<h1 style='text-align: center; color: #FF4500;'>🎥 Anime Odyssey 🎥</h1>", unsafe_allow_html=True)
    st.image("https://wallpapers.com/images/featured-full/anime-4k-uvwsx2m7duh51ale.jpg", use_column_width=True)

    st.write(
        "Welcome to the **Anime Odyssey**! This app allows you to fetch and analyze your AniList anime data. This is a work in progress and more features will be added soon. For more information, visit the [GitHub repository](https://github.com/Rohit04121998/Anime-Analysis)."
    )

elif navigation == "Fetch Data":
    st.markdown("### Fetch Data from AniList 📡")
    st.write(
        "You can fetch your anime data from AniList by providing your AniList username and selecting the list you want to fetch. As of now you can fetch onlu your anime statuses:"
    )
    st.write("- **COMPLETED**: Anime that you have completed watching.")
    st.write("- **PLANNING**: Anime that you are planning to watch.")
    st.write("- **CURRENT**: Anime that you are currently watching.")

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
    st.markdown("### Explore Your Anime Stats")
    st.write(
        "This feature is coming soon! You'll be able to visualize your anime data with interactive charts and graphs."
    )

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
        "It allows users to download their anime data in CSV format and visualize their anime stats."
    )
    st.markdown(
        """
        **Key Features:**
        - Fetch AniList anime data for different statuses.
        - Download anime data as CSV files.
        - Explore stats and insights (upcoming feature).
        
        For more details and updates, check out the [GitHub repository](https://github.com/Rohit04121998/Anime-Analysis).
        """
    )
