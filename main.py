# main.py
import logging
from src.anilist_api import make_request, extract_entries
from src.data_processor import process_metadata, process_data
from src.save_data import save_json, save_csv
from src.logger import setup_logging
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Set up logging
setup_logging()

# Fetch the Anilist user from .env
anilist_user = os.getenv("ANILIST_USER")

# Define query templates
metadata_query_template = """
{{
  MediaListCollection(userName: "{anilist_user}", type: ANIME, status: {status}) {{
    lists {{
      entries {{
        id
        mediaId
        score
      }}
    }}
  }}
}}
"""

data_query_template = """
{{
  MediaListCollection(userName: "{anilist_user}", type: ANIME, status: {status}) {{
    lists {{
      entries {{
        media {{
          id
          title {{
            romaji
            english
          }}
          episodes
          source
          genres
          meanScore
          description
          duration
          season
          seasonYear
        }}
      }}
    }}
  }}
}}
"""

statuses = ["COMPLETED", "PLANNING", "CURRENT"]

for status in statuses:
    logging.info(f"Fetching data for status: {status}")

    # Format the queries
    metadata_query = metadata_query_template.format(anilist_user=anilist_user, status=status)
    data_query = data_query_template.format(anilist_user=anilist_user, status=status)

    try:
        # Make API requests
        metadata_response = make_request(metadata_query)
        data_response = make_request(data_query)

        # Extract entries
        metadata_entries = extract_entries(metadata_response)
        data_entries = extract_entries(data_response)

        # Save JSON files
        save_json(metadata_entries, f"anilist_metadata_{status}.json")
        save_json(data_entries, f"anilist_data_{status}.json")

        # Process the entries into DataFrames
        metadata_df = process_metadata(metadata_entries)
        data_df = process_data(data_entries)

        # Save CSV files
        save_csv(metadata_df, f"anilist_metadata_{status}.csv")
        save_csv(data_df, f"anilist_data_{status}.csv")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
