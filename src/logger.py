import logging
import os

from yaml import safe_load


def setup_logging():
    """
    Configures logging based on settings.
    """
    with open("./config/settings.yml", "r") as f:
        config = safe_load(f)

    log_file = config["paths"]["log_file"]
    log_dir = os.path.dirname(log_file)

    os.makedirs(log_dir, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
    )
    logging.info("Logging setup complete.")
