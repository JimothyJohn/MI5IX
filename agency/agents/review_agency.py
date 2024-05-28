# Warning control
import warnings

warnings.filterwarnings("ignore")
from langchain_openai import ChatOpenAI
from crewai import Agent
from tools.repository import *

class ProductReviewAgency:
    def __init__(self, outputFolder: str = "outputs", llm=ChatOpenAI(model_name="gpt-4o-2024-05-13", temperature=0.2)):
        self.llm = llm
        self.directory_read_tool = DirectoryReadTool(outputFolder)

    def researcher(self):
        return Agent(
            name="Researcher",
            role="Senior Researcher",
            goal="Discover reputable reviews and information on {topic}",
            tools=[searchTool, websiteSearchTool, self.directory_read_tool, file_read_tool],
            llm=self.llm,
            backstory="""
You are a subject matter expert in the field of the {topic}.
You only use reviews and information from reputable institutions and cite them accordingly.
You avoid company publications and secondary sources.
You search the web for reviews and information.
You look through websites to find relevant information.
You prefer non-corporate, unbiased information from experts.
Your sources only include articles, blog posts, and consumer reviews, not whole websites or publications.
You only use the most recent data as possible.
Your sources will be used by the Analyst. 
""",
        )

    def analyst(self):
        return Agent(
            name="Analyst",
            role="Senior Analyst",
            goal="Utilize research to identify the best products that are most relevant to {topic}",
            tools=[searchTool, websiteSearchTool, mapTool, self.directory_read_tool, file_read_tool],
            llm=self.llm,
            backstory="""
You use sources provided by the Researcher.
You are a subject matter expert in products relevant to {topic}.
You specialize in researching relevant products and finding information about them.
You do not include customers, only include suppliers that would have products.
You visit company websites to confirm they are relevant to the topic at hand.
""",
        )

    def content_creator(self):
        return Agent(
            name="Content Creator",
            role="Senior Content Creator",
            goal="Find educational content relevant to {topic}",
            tools=[searchTool, websiteSearchTool, contentTool, self.directory_read_tool, file_read_tool],
            llm=self.llm,
            backstory="""
You use sources provided by the Researcher.
You are a subject matter expert in products relevant to the topic: {topic}.
You specialize in finding videos, articles, and media that helps educate audiences about {topic}.
You prioritize educational content from individuals or public instututions.
""",
        )