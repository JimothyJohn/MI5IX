# Warning control
import warnings

warnings.filterwarnings("ignore")
from crewai import Task
from models import *

class WebDevelopmentTasks:
    def __init__(self, outputFolder: str = "outputs"):
        self.outputFolder = outputFolder

    def layout(self, agent):
        return Task(
            agent=agent,
            description="""
Use reviews.json, products.json, and content.json to plan and map out the webpage showcasing the best products.
Design a single, static webpage that will show a user various products, reviews, and content for {topic}.
Describe the key elements, their layout, and how they fit together.
Include all content that will be on the webpage, do not ask the user to fill in any gaps.
""",
            expected_output="""
A markdown file that describes the design of the webpage and its key elements.
Does not include any html code, just a description of the layout with intimate detail.
""",
            human_input=False,
            output_file=f"{self.outputFolder}/layout.md",
        )

    def design(self, agent):
        return Task(
            agent=agent,
            description="""
Design a single, static webpage that will show a user various products, reviews, and content for {topic}.
Add to the layout.md file and include stylistic design choices.
Keep the website very visual where the images standout and the videos are embedded. Emphasize quantified features so that it's easier for the user to quantiy key differences. Keep text to short, punchy headlines that make it clear how they stand out against each other.
Include all content that will be on the webpage, do not ask the user to fill in any gaps.
""",
            expected_output="""
The contents of the newly edited layout.md file that describes the design of the webpage and its key elements.
Does not include any html code, just a description of the layout with intimate detail.
""",
            human_input=False,
            output_file=f"{self.outputFolder}/layout.md",
        )

    def develop(self, agent):
        return Task(
            agent=agent,
            description="""
Use the layout.md file, reviews.json, content.json, and products.json to create a single, static HTML webpage that will show a user various products, reviews, and content for {topic}.
""",
            expected_output="""
The contents of a single index.html file that will serve as the static webpage. Does not include any markdown formatting, only HTML.
""",
            human_input=False,
            output_file=f"{self.outputFolder}/index.html",
        )

    def review(self, agent):
        return Task(
            agent=agent,
            description="""
Correct the index.html file to function as an index.html page and edit for best practices.
Verify all links work correctly and do not include them if they don't.
Make sure all relevant content from the JSON files are included.
""",
            expected_output="""
The contents of the newly edited index.html file that will serve as the static webpage. Does not include any markdown formatting, only HTML.
""",
            human_input=False,
            output_file=f"{self.outputFolder}/index.html",
        )
