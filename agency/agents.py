# Warning control
import warnings

warnings.filterwarnings("ignore")
from typing import List
from langchain_openai import ChatOpenAI
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool, SerperDevTool, YoutubeVideoSearchTool
from langchain_community.tools import GooglePlacesTool


scrapeTool = ScrapeWebsiteTool()
searchTool = SerperDevTool()
mapTool = GooglePlacesTool()
contentTool = YoutubeVideoSearchTool()


class ResearchAgency:
    def __init__(self, llm=ChatOpenAI(model_name="gpt-4o-2024-05-13", temperature=0.4)):
        self.llm = llm

    def senior_researcher(self):
        return Agent(
            name="Senior Researcher",
            role="Senior Researcher",
            goal="Discover primary sources and information for further research on {topic}",
            tools=[searchTool, scrapeTool],
            llm=self.llm,
            backstory="""
You are a subject matter expert in the field of the {topic}.
You only use primary sources from reputable institutions and cite them accordingly.
You avoid sources that use buzzwords like {buzz}.
You avoid company publications and secondary sources.
You search the web for sources and information.
You look through websites to find relevant information.
You prefer academic, non-corporate, unbiased information from other experts.
Your sources only include articles, blog posts, research papers, and transcripts, not whole websites or publications.
You only use the most recent data as possible.
Your sources will be used by the Market Analyst. 
""",
        )

    def market_analyst(self):
        return Agent(
            name="Market Analyst",
            role="Senior Market Analyst",
            goal="Utilize research to identify key companies and organizations that may be impacted by {topic}",
            tools=[searchTool, scrapeTool, mapTool],
            llm=self.llm,
            backstory="""
You use sources provided by the Senior Researcher.
You are a subject matter expert in businesses relevant to {topic}.
You specialize in researching relevant companies and organizations and finding information about their business and employees.
You do not include suppliers, only include companies that would have demand.
You visit company and organization websites to confirm they are relevant to the topic at hand.
These companies and organizations will be used by the Financial Analyst. 
""",
        )

    def content_coordinator(self):
        return Agent(
            name="Content Coordinator",
            role="Senior Content Provider",
            goal="Find educational content relevant to {topic}",
            tools=[searchTool, scrapeTool, contentTool],
            llm=self.llm,
            backstory="""
You use sources provided by the Senior Researcher.
You are a subject matter expert in businesses relevant to the topic: {topic}.
You specialize in finding videos, articles, and media that helps educate audiences about {topic}.
You prioritize educational content from individuals or public instututions.
Your content is used by the Salesperson.
""",
        )

    def financial_analyst(self):
        return Agent(
            name="Financial Analyst",
            role="Senior Financial Analyst",
            goal="Utilize publicly available financial information to determine if companies are financially healthy and actively investing",
            tools=[searchTool, scrapeTool],
            llm=self.llm,
            allow_delegation=True,
            backstory="""
You are an experienced business adept at analyzing financial information.
You specialize in researching companies and parsing out the most valuable information relevant to their finances.
Utilize earnings reports and news articles to make your judgements.
""",
        )
