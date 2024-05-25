# Warning control
import warnings

warnings.filterwarnings("ignore")
from crewai import Task
from models import SourceList, CompanyList, OutreachList, ContentList
from agents import contentTool

class ResearchTasks:
    def research_topic(self, agent):
        return Task(
            description="""
Discover key words, context, sources, and terminology related to {topic}.
Avoid sources that use buzzwords like {buzz}.
Search the internet for information.
Only use primary sources from reputable institutions and cite them accordingly.
Only use the most recent data as possible.
""",
            agent=agent,
            expected_output="""
At least 5 primary sources that will provide context around {topic} and help the audience understand how and where to do further research.
""",
            human_input=False,
            output_pydantic=SourceList,
            output_file="outputs/sources.json",
        )

    def find_companies(self, agent):
        return Task(
            description="""
Utilize sources to identify key companies that are relevant to the topic: {topic}.
Only provide companies wth locations that are in close proximity to or within {location}.
""",
            agent=agent,
            expected_output="""
5 highly-qualified companies with their basic information and explanations of how they're relevant to {topic}
""",
            output_pydantic=CompanyList,
            output_file="outputs/companies.json",
        )

    def find_content(self, agent):
        return Task(
            description="""
Find videos on YouTube related to {topic} that are relevant to the companies found.
""",
            agent=agent,
            expected_output="""
At least 5 videos that could stimulate interest about {topic} and explanations of how they're relevant to the companies.
""",
            tools=[contentTool],
            output_pydantic=ContentList,
            output_file="outputs/content.json",
        )

    def craft_outreach(self, agent):
        return Task(
            description="""
Create a compelling, targeted email outreach message to companies relevant to {topic} utilizing the research and content gathered previously.
""",
            agent=agent,
            expected_output="""
An email message for each company that is compelling, targeted, and relevant to the companies found and includes at least one video along with a problem statement of what you're trying to solve.
""",
            output_pydantic=OutreachList,
            output_file="outputs/outreaches.json",
        )
