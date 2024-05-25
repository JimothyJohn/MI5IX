import warnings

warnings.filterwarnings("ignore")
from crewai import Crew
from langchain_openai import ChatOpenAI
from agents import *
from tasks import *


class ResearchCrew:
    def build(self, agents, tasks) -> None:
        self.crew = Crew(
            agents=agents,
            tasks=tasks,
            verbose=True,
        )


    def run(self, inputs):
        result = self.crew.kickoff(inputs=inputs)
        return result
