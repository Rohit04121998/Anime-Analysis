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
