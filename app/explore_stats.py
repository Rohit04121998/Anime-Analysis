# explore_stats.py
import pandas as pd
import plotly.express as px
import streamlit as st


def basic_stats(df):
    """Displays basic statistics such as total anime watched, total episodes, and total watch time."""
    st.header("📊 Basic Stats")
    total_anime = df["media_id"].nunique()
    total_episodes = df["episodes"].sum()
    total_watch_time_hours = (df["episodes"] * df["duration"]).sum() / 60

    st.write(f"**Total Anime Watched**: {total_anime}")
    st.write(f"**Total Episodes Watched**: {total_episodes}")
    st.write(f"**Total Watch Time**: {total_watch_time_hours:.2f} hours")


def anime_watched_by_year(df):
    """Visualizes the number of anime watched by year."""
    st.header("📅 Anime Watched by Year")
    year_df = df.groupby("year_released").size().reset_index(name="count")
    fig = px.bar(year_df, x="year_released", y="count", labels={"year_released": "Year", "count": "Anime Count"})
    st.plotly_chart(fig)


def episodes_watched_by_year(df):
    """Visualizes the number of episodes watched by year."""
    st.header("🎞 Episodes Watched by Year")
    year_df = df.groupby("year_released")["episodes"].sum().reset_index()
    fig = px.bar(
        year_df, x="year_released", y="episodes", labels={"year_released": "Year", "episodes": "Total Episodes"}
    )
    st.plotly_chart(fig)


def rating_distribution(df):
    """Visualizes the distribution of ratings given by the user."""
    st.header("⭐ Rating Distribution")
    fig = px.histogram(df, x="score", nbins=10, labels={"score": "Rating"})
    st.plotly_chart(fig)


def top_genres(df):
    """Displays the top genres based on the number of anime watched."""
    st.header("🎬 Top Genres")
    genre_df = df["genres"].explode().value_counts().head(10).reset_index()
    genre_df.columns = ["Genre", "Count"]
    fig = px.bar(genre_df, x="Genre", y="Count")
    st.plotly_chart(fig)


# More analyses like top longest anime, anime by source, etc. coming!
