# Warning control
import warnings
warnings.filterwarnings('ignore')
from crewai import Agent
from crewai_tools import ScrapeWebsiteTool
from langchain_openai import ChatOpenAI
from tools.search import SearchTool

# Example of initiating tool that agents can use to search across any discovered websites
scrapeTool = ScrapeWebsiteTool()
searchTool = SearchTool()

# This is an example of how to define custom agents.
# You can define as many agents as you want.
class CustomAgents:
    def __init__(self):
        self.llm = ChatOpenAI(model_name="gpt-4o-2024-05-13", temperature=0.5)
        # self.ollm = Ollama(model="openhermes")

    def researcher(self):
        return Agent(
            name="Researcher",
            role="Senior Research Partner",       
            goal="Provide summaries of key primary sources related to {topic}",
            tools=[searchTool, scrapeTool],
            llm=self.llm,
            backstory="""
You are a McKinsey consultant that excels in research and is good at parsing out information.
You do basic research by searching the web for reputable information.
You are a subject matter expert in the field of the topic at hand.
You look through websites to extract relevant information.
You collect information that helps the audience learn something and make informed decisions.
Your work is the basis for the Content Writer to write an article on this topic.
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
Your goal is to review the blog post to ensure that it follows journalistic best practices, provides balanced viewpoints when providing opinions or assertions.",
""",
            allow_delegation=True,
            verbose=True,
            llm=self.llm,
        )
