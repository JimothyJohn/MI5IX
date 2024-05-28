# Warning control
import warnings

warnings.filterwarnings("ignore")
from crewai import Task
from models import *
from agents import contentTool
from crewai_tools import DirectoryReadTool 


class MarketResearchTasks:
    def __init__(self, outputFolder: str = "outputs"):
        self.outputFolder = outputFolder

    def research_topic(self, agent):
        return Task(
            agent=agent,
            verbose=True,
            human_input=False,
            output_pydantic=SourceList,
            output_file=f"{self.outputFolder}/sources.json",
            description="""
Discover highly credible, relevant, and reputable primary sources related to {topic}.
""",
            expected_output="""
At least 5 primary sources that will provide context around {topic} and help the audience understand how and where to do further research.
Include the website, title, author, abstract, and published date of each source.
""",
        )

    def vet_sources(self, agent):
        return Task(
            agent=agent,
            human_input=False,
            output_pydantic=SourceList,
            output_file=f"{self.outputFolder}/sources.json",
            description="""
Utilize the primary sources' titles, websites, content, and authors to find additional, similar sources relevant to {topic}.
Make sure the sources are less than 10 years old, well-respected and well-recognized, detailed, and not biased.
""",
            expected_output="""
At least 10 primary sources (with citations) that will provide context around {topic} and help the audience understand how and where to do further research.
Include the website, title, author, abstract, and published date of each source.
""",
        )

    def find_companies(self, agent):
        return Task(
            agent=agent,
            output_pydantic=CompanyList,
            output_file=f"{self.outputFolder}/companies.json",
            description="""
Utilize sources to identify key companies that are relevant to {topic}.
Avoid Fortune 500 companies and prioritize small cap businesses.
Avoid companies with less than 5 people.
Only provide companies with headquarters that are in close proximity to or within {location}.
""",
            expected_output="""
At least 5 highly-qualified companies, their website, industry, HQ location, number of employees, annual revenue, and a brief explanation of how they're relevant to {topic}.
Include each company's name, website, industry, HQ city, HQ state, number of employees, annual revenue, and a brief explanation if the company's relevance to {topic}.
""",
        )

    def vet_companies(self, agent):
        return Task(
            agent=agent,
            output_pydantic=CompanyList,
            output_file=f"{self.outputFolder}/companies.json",
            # TODO Use callback to correct list instead.
            description="""
Utilize the companies' websites, content, and employees to find similar companies relevant to {topic}.
Determine if the companies found are relevant to {topic}.
Confirm if they are a small cap company that will be easy to do business with.
Avoid companies with less than 5 people.
Do you best to add any missing information about the companies.
Only provide companies with headquarters that are in close proximity to or within {location}.
""",
            expected_output="""
At least 10 highly-qualified companies, their website, industry, HQ location, number of employees, annual revenue, and a brief explanation of how they're relevant to {topic}.
Include each company's name, website, industry, HQ city, HQ state, number of employees, annual revenue, and a brief explanation if the company's relevance to {topic}.
""",
        )

    def find_videos(self, agent):
        return Task(
            agent=agent,
            tools=[contentTool],
            output_pydantic=ContentList,
            output_file=f"{self.outputFolder}/content.json",
            description="""
Find existing videos on YouTube related to {topic} that are relevant to the companies found.
Avoid videos that use buzzwords like {buzz}.
Avoid videos that are advertisements or promotional.
Prioritize case studies and educational content.
Avoid short videos that are less than 2 minutes long.
Make sure the actual URL of the video is captured so the user can reference it later.
""",
            expected_output="""
At least 5 videos that could stimulate interest about {topic}.
Include each video's name, URL, industry, channel, and a brief explanation of how the video is relevant to {topic}.
""",
        )

    def vet_videos(self, agent):
        return Task(
            agent=agent,
            tools=[contentTool],
            output_pydantic=ContentList,
            output_file=f"{self.outputFolder}/content.json",
            description="""
Use the videos to find more on YouTube related to {topic} that are relevant to the companies found.
Avoid videos that use buzzwords like {buzz}.
Avoid videos that are advertisements or promotional.
Prioritize case studies and educational content.
Avoid short videos that are less than 2 minutes long.
Make sure the actual URL of the video is captured so the user can reference it later.
""",
            expected_output="""
At least 5 existing YouTube videos that could stimulate interest about {topic}.
Include each video's name, URL, industry, channel, and a brief explanation of how the video is relevant to {topic}.
""",
        )


class ProductResearchTasks:
    def __init__(self, outputFolder: str = "outputs"):
        self.outputFolder = outputFolder


    def research(self, agent):
        return Task(
            agent=agent,
            verbose=True,
            description="""
Discover highly credible, relevant, and reputable reviews related to {topic}.
""",
            expected_output="""
At least 5 reviews that will provide context around {topic} and help the audience understand how and where to do further research.
Include the website, title, author, abstract, and published date of each review.
""",
            human_input=False,
            output_pydantic=SourceList,
            output_file=f"{self.outputFolder}/reviews.json",
        )

    def vet_research(self, agent):

        return Task(
            agent=agent,
            verbose=True,
            description="""
Utilize the reviews.json file contents to find additional, similar reviews relevant to {topic}.
Make sure the reviews are less than 4 years old, well-respected, well-recognized, detailed, and not biased.
""",
            expected_output="""
At least 10 reviews that will provide context around {topic} and help the audience understand how and where to do further research.
Include the website, title, author, abstract, and published date of each review.
""",
            human_input=False,
            output_pydantic=SourceList,
            output_file=f"{self.outputFolder}/reviews.json",
        )

    def find_products(self, agent):
        return Task(
            agent=agent,
            verbose=True,
            description="""
Utilize reviews to identify key products that are relevant to {topic}.
Avoid obscure products that are not being mass manufactured.
Only provide products that areavailable in the United States.
""",
            expected_output="""
At least 5 highly-qualified products relevant to {topic}.
Include each product's manufacturer, website, year, model, part number, product webpage, price, features it does and doesn't have, reasoning for its selection, and consensus of reviews.
""",
            output_pydantic=ProductList,
            output_file=f"{self.outputFolder}/products.json",
        )

    def vet_products(self, agent):
        return Task(
            # TODO Use callback to correct list instead.
            agent=agent,
            verbose=True,
            description="""
Utilize products.json and reviews.json file contents to identify key products that are relevant to {topic}.
Avoid obscure products that are not being mass manufactured.
Determine if the products found are relevant to {topic}.
Do your best to add any missing information about the products.
Only provide products that are available in the United States.
""",
            expected_output="""
At least 10 highly-qualified products relevant to {topic}.
Include each product's manufacturer, website, year, model, part number, product webpage, price, features it does and doesn't have, reasoning for its selection, and consensus of reviews.
""",
            output_pydantic=ProductList,
            output_file=f"{self.outputFolder}/products.json",
        )

    def find_videos(self, agent):
        return Task(
            agent=agent,
            output_pydantic=ContentList,
            output_file=f"{self.outputFolder}/content.json",
            description="""
Utilize products.json and reviews.json file contents to identify existing videos on YouTube related to {topic} that are relevant to the products found.
Avoid videos that are advertisements or promotional.
Prioritize case studies and educational content.
Avoid short videos that are less than 2 minutes long.
Make sure the actual URL of the video is captured so the user can reference it later.
""",
            expected_output="""
At least 5 videos that could stimulate interest in {topic}.
Include each video's name, URL, industry, channel, and a brief explanation of how the video is relevant to {topic}.
""",
        )

    def vet_videos(self, agent):
        return Task(
            agent=agent,
            output_pydantic=ContentList,
            output_file=f"{self.outputFolder}/content.json",
            description="""
Utilize products.json, content.json and reviews.json file contents to identify existing videos on YouTube related to {topic} that are relevant to the products found.
Use the videos to find more on YouTube related to {topic} that are relevant to the products found.
Avoid videos that are advertisements or promotional.
Prioritize case studies and educational content.
Avoid short videos that are less than 2 minutes long.
Make sure the actual URL of the video is captured so the user can reference it later.
""",
            expected_output="""
At least 10 existing YouTube videos that could stimulate interest about {topic}.
Include each video's name, URL, industry, channel, and a brief explanation of how the video is relevant to {topic}.
""",
        )
