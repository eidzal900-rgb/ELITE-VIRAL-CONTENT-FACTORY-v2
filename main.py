# AI SOURCING AGENT BACKEND (EXTREME SPY LEVEL)

# =========================
# SYSTEM ARCHITECTURE
# =========================

# Modules:
# 1. Scraper Engine (Shopee, Lazada, Alibaba, Taobao)
# 2. AI Matching Engine (semantic + fuzzy match)
# 3. Visual Search Engine (image similarity)
# 4. Product Aggregator API
# 5. Profit Calculator Engine


# =========================
# 1. SCRAPER ENGINE (Shopee Example)
# =========================

import requests

def search_shopee(query):
    url = "https://shopee.com.my/api/v4/search/search_items"
    params = {
        "by": "relevancy",
        "keyword": query,
        "limit": 20,
        "newest": 0
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, params=params, headers=headers)
    data = res.json()

    results = []
    for item in data.get("items", []):
        info = item.get("item_basic", {})
        results.append({
            "title": info.get("name"),
            "price": info.get("price") / 100000,
            "sold": info.get("historical_sold"),
            "shopid": info.get("shopid"),
            "itemid": info.get("itemid")
        })

    return results


# =========================
# 2. AI MATCHING ENGINE
# =========================

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_match(query, product_list):
    query_vec = model.encode([query])
    product_titles = [p['title'] for p in product_list]
    product_vecs = model.encode(product_titles)

    scores = cosine_similarity(query_vec, product_vecs)[0]

    ranked = sorted(zip(product_list, scores), key=lambda x: x[1], reverse=True)

    return ranked


# =========================
# 3. VISUAL SEARCH ENGINE (CLIP)
# =========================

import torch
import clip
from PIL import Image

clip_model, preprocess = clip.load("ViT-B/32")

def image_search(image_path, product_images):
    image = preprocess(Image.open(image_path)).unsqueeze(0)
    image_features = clip_model.encode_image(image)

    similarities = []

    for p in product_images:
        img = preprocess(Image.open(p['img'])).unsqueeze(0)
        feat = clip_model.encode_image(img)
        sim = torch.cosine_similarity(image_features, feat)
        similarities.append((p, float(sim)))

    return sorted(similarities, key=lambda x: x[1], reverse=True)


# =========================
# 4. PROFIT CALCULATOR
# =========================

def calculate_profit(selling_price, cost_price, ads_cost=5):
    profit = selling_price - cost_price - ads_cost
    margin = (profit / selling_price) * 100

    return {
        "profit": round(profit, 2),
        "margin": round(margin, 2)
    }


# =========================
# 5. AGGREGATOR PIPELINE
# =========================

def run_pipeline(query):
    shopee_data = search_shopee(query)

    ranked = semantic_match(query, shopee_data)

    final = []
    for product, score in ranked[:10]:
        profit_data = calculate_profit(product['price'], product['price'] * 0.4)

        final.append({
            "title": product['title'],
            "price": product['price'],
            "score": score,
            "profit": profit_data
        })

    return final


# =========================
# 6. FASTAPI SERVER
# =========================

from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search(query: str):
    return run_pipeline(query)


# =========================
# NEXT UPGRADE (TO IMPLEMENT)
# =========================

# - Add Lazada / Alibaba / Taobao scrapers
# - Add Redis caching (speed)
# - Add PostgreSQL (store products + history)
# - Add Ads scraping (TikTok / FB)
# - Add Ranking AI (detect winning product)
# - Deploy via Docker + VPS


# =========================
# END
# =========================
