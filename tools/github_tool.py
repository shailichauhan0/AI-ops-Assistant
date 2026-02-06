import os, requests
GITHUB_TOKEN = os.getenv("GITHUB_API_KEY")

def search_github(query):
    url = f"https://api.github.com/search/repositories?q={query}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    r = requests.get(url, headers=headers)
    data = r.json()
    return [{"name": i["full_name"], "stars": i["stargazers_count"], "url": i["html_url"]} for i in data.get("items", [])[:3]]
