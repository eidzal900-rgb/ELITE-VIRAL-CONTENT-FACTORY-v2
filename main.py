from modules.youtube_scraper import search_videos
from modules.youtube_scraper import get_video_stats
from modules.spike_detector import calculate_spike
from modules.niche_classifier import classify_niche
from modules.ranking_engine import rank_niches
from modules.script_generator import generate_script
from modules.script_variations import generate_variations
from modules.storage import save_json

import config


def run_system():

    print("START VIRAL SCAN")

    all_videos = []

    for query in config.SEARCH_QUERIES:

        print("Searching:", query)

        video_ids = search_videos(query)

        videos = get_video_stats(video_ids)

        for video in videos:

            score = calculate_spike(video)

            title = video["snippet"]["title"]

            niche = classify_niche(title)

            all_videos.append({

                "title": title,
                "video_id": video["id"],
                "score": score,
                "niche": niche

            })

    all_videos.sort(key=lambda x: x["score"], reverse=True)

    save_json("spikes.json", all_videos)

    ranking = rank_niches(all_videos)

    save_json("niche_rank.json", ranking)

    scripts = []

    for niche in ranking:

        for video in ranking[niche][:3]:

            script = generate_script(video["title"])

            variations = generate_variations(script)

            scripts.append({

                "title": video["title"],
                "script": script,
                "variations": variations

            })

    save_json("scripts.json", scripts)

    print("SYSTEM COMPLETE")


if __name__ == "__main__":
    run_system()
