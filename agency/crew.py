import warnings

warnings.filterwarnings("ignore")
from crewai import Crew
from agents import *
from tasks import *


class ResearchCrew:
    def __init__(self, outputFolder: str = "outputs"):
        self.agency = ResearchAgency()
        self.tasks = ResearchTasks(outputFolder=outputFolder)

        self.researcher = self.agency.senior_researcher()
        self.marketer = self.agency.market_analyst()
        self.content_provider = self.agency.content_coordinator()
        self.analyst = self.agency.financial_analyst()

        self.researchTask = self.tasks.research_topic(self.researcher)
        self.vettingTask = self.tasks.vet_sources(self.researcher)
        self.videoTask = self.tasks.find_videos(self.content_provider)
        self.companyTask = self.tasks.find_companies(self.marketer)
        self.vetCompanyTask = self.tasks.vet_companies(self.analyst)

    def research(self, inputs):
        self.crew = Crew(
            agents=[self.researcher],
            tasks=[self.researchTask, self.vettingTask],
            verbose=True,
        )

        self.__run(inputs)

    def prospect(self, inputs):
        self.crew = Crew(
            agents=[self.researcher, self.content_provider, self.marketer, self.analyst],
            tasks=[self.researchTask, self.vettingTask, self.videoTask, self.companyTask, self.vetCompanyTask],
            verbose=True,
            memory=True,
        )

        self.__run(inputs)

    def __run(self, inputs):
        result = self.crew.kickoff(inputs=inputs)
        return result
