import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import Tool
from dotenv import load_dotenv

load_dotenv()

def get_profile_url_tavily(name):
    """This Function Searches for LinkedinPage."""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res

linkedin_url=Tool(
            name="Crawl Google for linkedin profile page",
            func=get_profile_url_tavily,
            description="This tool is useful  when you need get the Linkedin Page URL for a user",
        )

print(get_profile_url_tavily("Shagun Nagpal"))



