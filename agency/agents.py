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
    def __init__(
        self, llm=ChatOpenAI(model_name="gpt-4o-2024-05-13", temperature=0.4)
    ):
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
You specialize in finding reputable sources that will provide the most valuable and accurate information.
You search the web for these reputable sources and information.
You look through websites found in these searches to identify the highest value primary sources.
Your sources will be used by the Market Analyst. 
""",
        )

    def market_analyst(self):
        return Agent(
            name="Market Analyst",
            role="Senior Market Analyst",
            goal="Utilize research to identify key companies that may be impacted by research on {topic}",
            tools=[searchTool, scrapeTool, mapTool, contentTool],
            llm=self.llm,
            backstory="""
You are a subject matter expert in businesses relevant to the topic: {topic}.
You specialize in researching companies and parsing out the most valuable information relevant to them and the topic.
You visit these companies websites to confirm they are relevant to the topic at hand.
Your sources will be used by the Salesperson. 
""",
        )

    def salesperson(self):
        return Agent(
            name="Salesperson",
            role="Senior Advertising Agent",
            goal="Utilize marketing content to create a compelling, targeted email outreach message to companies relevant to {topic}",
            llm=self.llm,
            backstory="""
You are a subject matter expert in businesses relevant to the topic: {topic}.
You are an expert copywriter that takes an inquisitive, consultative approach to your outreaches.
You clearly explain the value proposition of the product or service you are selling and how it impacts the prospect.
You use qualified language that shows you've clearly done your research and understand the value proposition to the prospect
""",
        )

    def research(self) -> List[Agent]:
        return [self.senior_researcher()] 

    def prospect(self) -> List[Agent]:
        return [self.senior_researcher(), self.market_analyst()] 

    def outreach(self) -> List[Agent]:
        return [self.senior_researcher(), self.market_analyst(), self.salesperson()] 
