from tools.github_tool import search_github
from tools.weather_tool import get_weather
from tools.news_tool import get_news

class ExecutorAgent:
    def execute(self, plan):
        results = []
        for step in plan["steps"]:
            tool = step["tool"]
            action = step["action"]
            if tool == "github":
                results.append(search_github(action))
            elif tool == "weather":
                results.append(get_weather(action))
            elif tool == "news":
                results.append(get_news(action))
        return results
