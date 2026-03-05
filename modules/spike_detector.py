import datetime


def calculate_spike(video):

    stats = video["statistics"]
    snippet = video["snippet"]

    views = int(stats.get("viewCount", 0))
    likes = int(stats.get("likeCount", 0))
    comments = int(stats.get("commentCount", 0))

    published = snippet["publishedAt"]

    upload_time = datetime.datetime.fromisoformat(
        published.replace("Z", "+00:00")
    )

    hours = (datetime.datetime.utcnow() - upload_time).total_seconds() / 3600

    if hours <= 0:
        hours = 1

    like_ratio = likes / views if views else 0

    engagement = (likes + comments) / views if views else 0

    velocity = views / hours

    spike_score = velocity * like_ratio * engagement

    return spike_score
