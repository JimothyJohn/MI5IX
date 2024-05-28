# Warning control
import warnings

warnings.filterwarnings("ignore")
from crewai import Task
from models import *

class ProductReviewTasks:
    def __init__(self, outputFolder: str = "outputs"):
        self.outputFolder = outputFolder


    def research(self, agent):
        return Task(
            agent=agent,
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
