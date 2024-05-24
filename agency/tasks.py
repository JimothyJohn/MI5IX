# Warning control
import warnings

warnings.filterwarnings("ignore")
from crewai import Task

TIP = f"""
If you do your BEST WORK, I'll give you a $10,000 commission!
"""

def research_task(agent):
        return Task(
            description="""
Search the internet for information on {topic}.
Only use primary sources from reputable institutions.
Make sure to use the most recent data as possible.
Search through sites related to {topic}.
Find key pieces of information that help.
Cite your sources.
""",
            agent=agent,
            expected_output="""
Summaries of these sources that help answer {topic}.""",
        )


def write_report_task(agent):
    return Task(
            description="""
Write a summary related to {topic}.
Highlight key elements and important topics.
Cite your sources.
""",
            agent=agent,
            expected_output="""
A short, 3-pararaph summary with data provided whenever relevant. Include annotation and cite sources at the bottom.
""",
        )

def edit_report_task(agent):
    return Task(
            description="""
Edit a summary related to {topic}.
Ensure key elements and important topics are emphazised.
Verify the sources are correct and information is factual.
Ensure the summary is concise and clear.
Edit it for readability and understanding over precision.
""",
            agent=agent,
            expected_output=f"""
An edited report that is factually accurate, relevant, and understandable.
""",
        )
