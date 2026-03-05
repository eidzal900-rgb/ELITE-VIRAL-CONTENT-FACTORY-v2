def classify_niche(title):

    title = title.lower()

    if "ai" in title:
        return "AI Tools"

    if "money" in title or "earn" in title:
        return "Make Money Online"

    if "top" in title:
        return "Top Lists"

    if "fact" in title:
        return "Weird Facts"

    if "app" in title:
        return "Apps"

    if "life hack" in title:
        return "Life Hacks"

    if "motivation" in title:
        return "Motivation"

    return "General"
