import logging
import os

from dotenv import load_dotenv

from src.data_processor import process_data, process_metadata
from src.logger import setup_logging
from src.queries import data_query_template, metadata_query_template
from src.save_data import save_csv, save_json
from src.utils import extract_entries, make_request

load_dotenv()
setup_logging()

anilist_user = os.getenv("ANILIST_USER")
statuses = ["COMPLETED", "PLANNING", "CURRENT"]

for status in statuses:
    logging.info(f"Fetching data for status: {status}")

    metadata_query = metadata_query_template.format(anilist_user=anilist_user, status=status)
    data_query = data_query_template.format(anilist_user=anilist_user, status=status)

    try:

        metadata_response = make_request(metadata_query)
        data_response = make_request(data_query)

        metadata_entries = extract_entries(metadata_response)
        data_entries = extract_entries(data_response)

        save_json(metadata_entries, f"anilist_metadata_{status}.json")
        save_json(data_entries, f"anilist_data_{status}.json")

        metadata_df = process_metadata(metadata_entries)
        data_df = process_data(data_entries)

        merged_df = metadata_df.merge(data_df, on="media_id")

        save_csv(merged_df, f"anilist_merged_{status}.csv")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
