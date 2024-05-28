import warnings

warnings.filterwarnings("ignore")
from crewai import Crew
from agents import MarketResearchAgency
from tasks import MarketResearchTasks

class MarketResearchCrew:
    def __init__(self, outputFolder: str = "outputs"):
        self.agency = MarketResearchAgency()
        self.tasks = MarketResearchTasks(outputFolder=outputFolder)

        self.researcher = self.agency.researcher()
        self.marketer = self.agency.market_analyst()
        self.content_provider = self.agency.content_coordinator()

        self.researchTask = self.tasks.research_topic(self.researcher)
        self.vetMarketMarketResearchTask = self.tasks.vet_sources(self.researcher)
        self.companyTask = self.tasks.find_companies(self.marketer)
        self.vetCompanyTask = self.tasks.vet_companies(self.marketer)
        # self.videoTask = self.tasks.find_videos(self.content_provider)

    def research(self, inputs):
        self.crew = Crew(
            agents=[self.researcher],
            tasks=[self.researchTask, self.vetMarketMarketResearchTask],
        )

        self.__run(inputs)

    def prospect(self, inputs):
        self.crew = Crew(
            agents=[self.researcher, self.marketer],
            tasks=[
                self.researchTask,
                self.vetMarketMarketResearchTask,
                self.companyTask,
                self.vetCompanyTask,
            ],
            memory=True,
        )

        self.__run(inputs)

    def __run(self, inputs):
        result = self.crew.kickoff(inputs=inputs)
        return result
