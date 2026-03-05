import requests
import config

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
VIDEO_URL = "https://www.googleapis.com/youtube/v3/videos"


def search_videos(query):

    params = {

        "key": config.YOUTUBE_API_KEY,
        "part": "snippet",
        "q": query,
        "maxResults": config.MAX_RESULTS,
        "type": "video",
        "order": "date"

    }

    r = requests.get(SEARCH_URL, params=params)

    data = r.json()

    videos = []

    for item in data["items"]:

        videos.append(item["id"]["videoId"])

    return videos


def get_video_stats(video_ids):

    params = {

        "key": config.YOUTUBE_API_KEY,
        "part": "statistics,snippet",
        "id": ",".join(video_ids)

    }

    r = requests.get(VIDEO_URL, params=params)

    return r.json()["items"]
