# Anime Odyssey: A Data-Driven Exploration of My Favorites

![My Image](https://github.com/Rohit04121998/Anime-Analysis/blob/main/assets/background-image.jpg)

Welcome to the Anime Analysis repository! This project leverages data from the Anilist GraphQL API to provide insights into anime lists, focusing on various statuses such as COMPLETED, CURRENT, and PLANNING. With this tool, you can explore and analyze your anime preferences effectively!

## Motivation 💪

This project provides a comprehensive analysis of my personal anime preferences. My goal was to utilize an API for querying, clean the data collected, and convert it into actionable insights to answer several questions I had. The key questions driving this analysis were:

- What is the total number of series/episodes I've watched?
- Which genres do I watch most and least often?
- What are the average scores I’ve given to different anime?
- How do my ratings compare to those from the wider community?

## Background 🌌

As a long-time anime fan, I carefully keep track of my favorite series on the platform [Anilist](https://anilist.co/). If you’d like to check out my profile, you can find it [here](https://anilist.co/user/Lucifer04/).

This practice has piqued my interest in how my perceived anime preferences align with the data I've gathered over the years. It’s worth noting that my tastes in anime have changed over time. All ratings I’ve given reflect my opinions at the time I finished watching each series. For example, ratings from a decade ago may not accurately represent how I feel now. Factors such as the release of new anime, improvements in animation quality, and changes in my personal tastes all contribute to the variability in my ratings.

## Features ✨

- Extract metadata and actual data about anime lists using GraphQL queries.
- Categorize anime based on user-defined statuses.
- Create separate DataFrames for each status and query combination.
- Allow users to select multiple statuses for data fetching.
- Error handling to default to a specified username if the input username is invalid.

## Getting Started 🚀

To get started with this project, follow the steps below:

1. Clone the repository:

```bash
git clone https://github.com/Rohit04121998/Anime-Analysis.git
cd Anime-Analysis
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Get your Anilist username:

- Go to `Settings -> Account` or click [here](https://anilist.co/settings/account).
- Create a `.env` file in the main directory and add the following:

```ini
ANILIST_USER=YOUR_USERNAME_HERE
```

4. Set data and logging paths in the `settings.yml` file or leave as it is.

5. (Optional) Change the `entries` values as required in `queries.py` file to make a custom query template. If changed, `data_process.py` file should be changed accordingly.

## Folder Structure 📁

```plaintext
Anime-Analysis/
├── app/                         # Streamlit app directory
│   ├── __init__.py
│   ├── streamlit_app.py         # Main Streamlit app file
│   └── app_utils.py             # Functions for fetching and processing data
│
├── config/                      # Configuration directory
│   └── settings.yml             # YAML config file for paths and settings
│
├── data/                        # Directory where JSON and CSV files will be stored
│   ├── json/                    # Directory for JSON files
│   └── csv/                     # Directory for CSV files
│
├── logs/                        # Directory for log files
│   └── app.log                  # Log file to track application execution
│
├── src/                         # Source code directory
│   ├── __init__.py
│   ├── utils.py                 # API requests and extraction logic
│   ├── data_processor.py        # Data processing logic
│   ├── save_data.py             # File save/load logic
│   ├── queries.py               # Query templates
│   └── logger.py                # Logging configuration
│
├── .env                         # Environment variables for paths
├── .gitignore                   # Optional: Git ignore file for not tracking certain files
├── requirements.txt             # Required Python libraries
├── main.py                      # Main script to run the project (Optional. Run to store files locally)
└── README.md                    # Project documentation
```

## Usage 🛠️

To store files locally, simply execute the main script:

```bash
python main.py
```

If you wish to just run the code and not do any changes, simply execute the following script:

```bash
streamlit run app/streamlit_app.py
```

## Data Extraction 📥

The project utilizes Python scripts to interact with the [Anilist GraphQL API](https://anilist.gitbook.io/anilist-apiv2-docs). Key steps include:

- Sending queries to fetch data based on user preferences.
- Handling API responses and transforming them into usable formats.

**Example Query**:

Here’s an example of how to fetch COMPLETED anime:

```graphql
{
  Media(status: COMPLETED) {
    title {
      romaji
      english
    }
    genres
    averageScore
  }
}
```

## DataFrames Overview 📊

The project generates separate DataFrames for each status:

- Completed: Contains data on all completed anime.
- Current: Tracks anime currently being watched.
- Planning: Lists anime that are planned for future viewing.

Each DataFrame includes essential fields like titles, genres, and average scores, making it easy to analyze your anime collection.

## Technologies Used 💻

- Python: The primary programming language for data extraction and analysis.
- Pandas: For data manipulation and DataFrame handling.
- Requests: For making API calls.
- GraphQL: To query anime data from Anilist.

## Contributing 🤝

I welcome contributions to enhance the Anime Analysis project! Please follow these steps:

- Fork the repository.
- Create a new branch for your feature/bug fix.
- Commit your changes.
- Push to the branch and open a Pull Request.

## Resources 📚

- [Anilist GraphQL Docs](https://github.com/AniList/ApiV2-GraphQL-Docs)
- [Code for parsing nested JSON](https://ankushkunwar7777.medium.com/get-data-from-large-nested-json-file-cf1146aa8c9e)

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
