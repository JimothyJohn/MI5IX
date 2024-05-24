import warnings

warnings.filterwarnings("ignore")
from crewai import Crew
from langchain_openai import ChatOpenAI
from agents import *
from tasks import *

class ResearchCrew:
    def __init__(self, llm=ChatOpenAI(model_name="gpt-4o-2024-05-13", temperature=0.4)):  # Define your custom agents and tasks in agents.py and tasks.py
        agency = ResearchAgency(llm)

        researchAgent = agency.researcher()
        writerAgent = agency.writer()

        self.crew = Crew(
            agents=[researchAgent, writerAgent],
            tasks=[
                research_task(
                    researchAgent,
                ),
                write_report_task(
                    writerAgent,
                ),
            ],
            verbose=True,
        )

    def run(self, topic):
        result = self.crew.kickoff(inputs={"topic": topic})
        return result
