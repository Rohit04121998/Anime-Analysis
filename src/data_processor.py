import pandas as pd

from src.utils import extract_values, item_generator


def process_metadata(entries):
    """
    Processes metadata into a Pandas DataFrame (mediaId, score).
    """
    return pd.DataFrame.from_records(entries, columns=["mediaId", "score"]).rename(
        columns={"mediaId": "media_id"},
    )


def process_data(entries):
    """
    Processes the main data into a Pandas DataFrame (media details).
    """
    data_df = pd.DataFrame(
        columns=[
            "media_id",
            "title_in_romaji",
            "title_in_english",
            "episodes",
            "source",
            "genres",
            "mean_score",
            "description",
            "duration",
            "season",
            "year_released",
        ]
    )

    data_df["media_id"] = extract_values(entries, "id")
    data_df["title_in_romaji"] = extract_values(entries, "romaji")
    data_df["title_in_english"] = extract_values(entries, "english")
    data_df["episodes"] = extract_values(entries, "episodes")
    data_df["source"] = extract_values(entries, "source")
    data_df["mean_score"] = extract_values(entries, "meanScore")
    data_df["description"] = extract_values(entries, "description")
    data_df["duration"] = extract_values(entries, "duration")
    genres_list = list(item_generator(entries, "genres"))
    data_df["genres"] = [", ".join(genres) for genres in genres_list]
    data_df["season"] = extract_values(entries, "season")
    data_df["year_released"] = pd.to_numeric(extract_values(entries, "seasonYear"), errors="coerce")

    return data_df
