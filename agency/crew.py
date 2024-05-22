import warnings

warnings.filterwarnings("ignore")
from crewai import Crew
from agents import *
from tasks import CustomTasks


class ResearchCrew:
    def __init__(self):  # Define your custom agents and tasks in agents.py and tasks.py
        tasks = CustomTasks()

        self.crew = Crew(
            agents=[researchAgent, writerAgent, editorAgent],
            tasks=[
                tasks.do_research(
                    researchAgent,
                ),
                tasks.write_report(
                    writerAgent,
                ),
                tasks.edit_report(
                    editorAgent,
                ),
            ],
            verbose=True,
        )

    def run(self, topic):

        result = self.crew.kickoff(inputs={"topic": topic})

        return result
