# Warning control
import warnings

warnings.filterwarnings("ignore")
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool
from crewai_tools import SerperDevTool

scrapeTool = ScrapeWebsiteTool()
searchTool = SerperDevTool()

class ResearchAgency:
    def __init__(self, llm):
        self.llm = llm

    def researcher(self):
        return Agent(
    name="Researcher",
    role="Senior Research Partner",
    goal="Discover primary sources that will provide key insights related to {topic}",
    tools=[searchTool, scrapeTool],
    llm=self.llm,
    backstory="""
You are a subject matter expert in the field of the {topic}.
You are a senior consultant that excels in research and excels at parsing out information.
You do in-depth research by searching the web for reputable information.
You look through websites and extract relevant information.
You collect information that helps the audience learn something and make informed decisions.
""",
)

    def writer(self):
        return Agent(
    name="Writer",
    role="Content Writer",
    backstory="""
You are a world-renowned technical writer that excels at summarizing complex topics.
You provide summaries from research your team has gathered.
You're working on a writing a new opinion piece about the topic: {topic}.
You base your writing on the work of the Content Planner, who provides relevant context about the topic.
You also provide objective and impartial insights and back them up with information provided by the Content Planner.
""",
    goal="""
Write insightful and factually accurate summary the topic: {topic}"
""",
    allow_delegation=False,
    verbose=True,
    llm=self.llm,
)

    def editor(self):
        return Agent(
    name="Editor",
    role="Content Editor",
    goal=f"""
You provide an edited version of the summary of research that help solve the core problem.
""",
    backstory=f"""
You are a world-renowned technical editor that works for a top scientific journal.
You edit summaries from the Content Writer.
Your goal is to review the Content Writer's summary to ensure that it follows journalistic best practices, provides balanced viewpoints when providing opinions or assertions.",
""",
    allow_delegation=True,
    verbose=True,
    llm=self.llm,
)
