# Warning control
import warnings

warnings.filterwarnings("ignore")
from crewai import Task
from models import SourceList, CompanyList, ContentList
from agents import contentTool

class ResearchTasks:
    def __init__(self, outputFolder: str = "outputs"):
        self.outputFolder = outputFolder

    def research_topic(self, agent):
        return Task(
            description="""
Discover highly credible, relevant, and reputable primary sources related to {topic}.
""",
            agent=agent,
            expected_output="""
At least 5 primary sources (with citations) that will provide context around {topic} and help the audience understand how and where to do further research.
""",
            human_input=False,
            output_pydantic=SourceList,
            output_file=f"{self.outputFolder}/sources.json",
        )

    def vet_sources(self, agent):
        return Task(
            description="""
Utilize the primary sources' titles, websites, content, and authors to find additional, similar sources relevant to {topic}.
Make sure the sources are less than 10 years old, well-respected and well-recognized, detailed, and not biased.
""",
            agent=agent,
            expected_output="""
At least 10 primary sources (with citations) that will provide context around {topic} and help the audience understand how and where to do further research.
""",
            human_input=False,
            output_pydantic=SourceList,
            output_file=f"{self.outputFolder}/new_sources.json",
        )


    def find_videos(self, agent):
        return Task(
            description="""
Find videos on YouTube related to {topic} that are relevant to the companies found.
Avoid videos that use buzzwords like {buzz}.
Avoid videos that are advertisements or promotional.
Prioritize case studies and educational content.
Avoid short videos that are less than 2 minutes long.
Make sure the URL of the video is captured so the user can reference it later.
""",
            agent=agent,
            expected_output="""
At least 5 videos that could stimulate interest about {topic}, their URL's, the channel that posted them, and an explanation of how they're relevant.
""",
            tools=[contentTool],
            output_pydantic=ContentList,
            output_file=f"{self.outputFolder}/content.json",
        )

    def find_companies(self, agent):
        return Task(
            description="""
Utilize sources to identify key companies that are relevant to {topic}.
Avoid Fortune 500 companies and prioritize small cap businesses.
Only provide companies with headquarters that are in close proximity to or within {location}.
""",
            agent=agent,
            expected_output="""
At least 5 highly-qualified companies, their website, industry, HQ location, number of employees, annual revenue, and a brief explanation of how they're relevant to {topic}.
""",
            output_pydantic=CompanyList,
            output_file=f"{self.outputFolder}/companies.json",
        )

    def vet_companies(self, agent):
        return Task(
            # TODO Use callback to correct list instead.
            description="""
Utilize the companies' websites, content, and employees to find similar companies relevant to {topic}.
Determine if the companies found are relevant to {topic}.
Confirm if they are a small cap company that will be easy to do business with.
Remove companies with less than 5 people.
Fill out any missing information about the companies.
Only provide companies with headquarters that are in close proximity to or within {location}.
""",
            agent=agent,
            expected_output="""
At least 10 highly-qualified companies, their website, industry, HQ location, number of employees, annual revenue, and a brief explanation of how they're relevant to {topic}.
""",
            output_pydantic=CompanyList,
            output_file=f"{self.outputFolder}/new_companies.json",
        )
