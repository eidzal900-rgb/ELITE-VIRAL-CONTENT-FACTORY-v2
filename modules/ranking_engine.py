from collections import defaultdict


def rank_niches(videos):

    niches = defaultdict(list)

    for v in videos:

        niches[v["niche"]].append(v)

    ranking = {}

    for niche in niches:

        top = sorted(
            niches[niche],
            key=lambda x: x["score"],
            reverse=True
        )[:10]

        ranking[niche] = top

    return ranking
