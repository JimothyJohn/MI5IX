import warnings

warnings.filterwarnings("ignore")
from crewai import Crew
from agents.web_agency import WebDevelopmentAgency 
from tasks.web_tasks import WebDevelopmentTasks

class WebDevelopmentCrew:
    def __init__(self, outputFolder: str = "outputs"):
        self.agency = WebDevelopmentAgency(outputFolder=outputFolder)
        self.tasks = WebDevelopmentTasks(outputFolder=outputFolder)

        self.planner = self.agency.planner()
        self.developer = self.agency.frontend_developer()

        self.planningTask = self.tasks.layout(self.planner)
        self.designTask = self.tasks.design(self.planner)
        self.developmentTask = self.tasks.develop(self.developer)
        self.reviewingTask = self.tasks.review(self.developer)

    def design(self, inputs):
        self.crew = Crew(
            agents=[self.planner],
            tasks=[
                self.planningTask,
                self.designTask,
            ],
            memory=True,
        )

        self.__run(inputs)

    def develop(self, inputs):
        self.crew = Crew(
            agents=[self.developer],
            tasks=[
                self.developmentTask,
                self.reviewingTask,
            ],
            memory=True,
        )

        self.__run(inputs)

    def all(self, inputs):
        self.crew = Crew(
            agents=[self.planner, self.developer],
            tasks=[
                self.planningTask,
                self.designTask,
                self.developmentTask,
                self.reviewingTask,
            ],
            memory=True,
        )

        self.__run(inputs)

    def __run(self, inputs):
        result = self.crew.kickoff(inputs=inputs)
        return result
