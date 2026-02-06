import os, requests
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_news(topic):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}"
    r = requests.get(url).json()
    return [{"title": a["title"], "source": a["source"]["name"], "url": a["url"]} for a in r.get("articles", [])[:3]]
