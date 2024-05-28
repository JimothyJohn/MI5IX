import warnings

warnings.filterwarnings("ignore")
from crewai import Crew
from agents.review_agency import ProductReviewAgency
from tasks.review_tasks import ProductReviewTasks

class ProductResearchCrew:
    def __init__(self, outputFolder: str = "outputs"):
        self.agency = ProductReviewAgency()
        self.tasks = ProductReviewTasks(outputFolder=outputFolder)

        self.researcher = self.agency.researcher()
        self.analyst = self.agency.analyst()
        self.content_creator = self.agency.content_creator()

        self.researchTask = self.tasks.research(self.researcher)
        self.vetResearchTask = self.tasks.vet_research(self.researcher)
        self.productTask = self.tasks.find_products(self.analyst)
        self.vetProductTask = self.tasks.vet_products(self.analyst)
        self.contentTask = self.tasks.find_videos(self.content_creator)
        self.vetContentTask = self.tasks.vet_videos(self.content_creator)

    def research(self, inputs):
        self.crew = Crew(
            agents=[self.researcher],
            tasks=[self.researchTask, self.vetResearchTask],
            memory=True,
        )

        self.__run(inputs)

    def prospect(self, inputs):
        self.crew = Crew(
            agents=[self.analyst],
            tasks=[
                self.productTask,
                self.vetProductTask,
            ],
            memory=True,
        )

        self.__run(inputs)

    def content(self, inputs):
        self.crew = Crew(
            agents=[self.content_creator],
            tasks=[
                self.contentTask,
                self.vetContentTask,
            ],
            memory=True,
        )

        self.__run(inputs)

    def all(self, inputs):
        self.crew = Crew(
            agents=[self.researcher, self.analyst, self.content_creator],
            tasks=[
                self.researchTask,
                self.vetResearchTask,
                self.productTask,
                self.vetProductTask,
                self.contentTask,
                self.vetContentTask,
            ],
            memory=True,
        )

        self.__run(inputs)

    def __run(self, inputs):
        result = self.crew.kickoff(inputs=inputs)
        return result
