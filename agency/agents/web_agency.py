# Warning control
import warnings

warnings.filterwarnings("ignore")
from langchain_openai import ChatOpenAI
from crewai import Agent
from tools.repository import *
from crewai_tools import DirectoryReadTool 

class WebDevelopmentAgency:
    def __init__(self, outputFolder: str = "outputs", llm=ChatOpenAI(model_name="gpt-4o-2024-05-13", temperature=0.2)):
        self.llm = llm
        self.outputFolder = outputFolder
        self.directory_read_tool = DirectoryReadTool(outputFolder)

    def planner(self):
        return Agent(
            name="Planner",
            role="Senior Website Designer",
            goal="Create a pseudocode website template for a product review page on {topic}",
            tools=[websiteSearchTool, self.directory_read_tool, file_read_tool],
            llm=self.llm,
            backstory="""
You are a world-class and award-winning website designer and subject matter expert on {topic}.
""",
        )

    def frontend_developer(self):
        return Agent(
            name="Frontend Developer",
            role="Senior Frontent Web Developer",
            goal="Create code for a static website",
            tools=[self.directory_read_tool, file_read_tool, websiteScrapeTool],
            llm=self.llm,
            backstory="""
You are a world-class and award-winning website developer experienced with .html, .css, and .js.
You create a single .html file that will function as the static webpage.
""",
        )
