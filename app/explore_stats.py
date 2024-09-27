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


def average_rating(df):
    """Displays the average rating of all watched anime."""
    st.header("⭐ Average Rating")
    avg_rating = df["score"].mean()
    st.write(f"**Average Rating**: {avg_rating:.2f}/10")


def rating_distribution(df):
    """Visualizes the distribution of ratings given by the user."""
    st.header("⭐ Rating Distribution")
    fig = px.histogram(df, x="score", nbins=10, labels={"score": "Rating"})
    st.plotly_chart(fig)


def top_genres(df):
    """Displays the top genres based on the number of anime watched."""
    st.header("🎬 Top Genres")

    df["genres"] = df["genres"].str.split(", ")

    genre_df = df["genres"].explode()

    genre_count = genre_df.value_counts().head(10).reset_index()
    genre_count.columns = ["Genre", "Count"]

    fig = px.bar(genre_count, x="Genre", y="Count", title="Top 10 Genres")
    st.plotly_chart(fig)


def top_longest_anime(df):
    """Displays the top longest anime by episode count."""
    st.header("📏 Top Longest Anime (by Episode Count)")
    longest_anime = df.nlargest(10, "episodes")[["title_in_romaji", "title_in_english", "episodes"]]
    st.table(longest_anime)


def anime_by_source(df):
    """Displays the count of anime by source (e.g., manga, novel)."""
    st.header("📚 Anime by Source")
    source_df = df["source"].value_counts().reset_index()
    source_df.columns = ["Source", "Count"]
    fig = px.bar(source_df, x="Source", y="Count", labels={"Source": "Source", "Count": "Anime Count"})
    st.plotly_chart(fig)


def seasons_watched(df):
    """Displays the number of anime watched by season."""
    st.header("🌸 Anime Watched by Season")
    season_df = df.groupby("season").size().reset_index(name="count")
    fig = px.bar(season_df, x="season", y="count", labels={"season": "Season", "count": "Anime Count"})
    st.plotly_chart(fig)


# More analyses like top longest anime, anime by source, etc. coming!
