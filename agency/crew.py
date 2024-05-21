# Warning control
import warnings
warnings.filterwarnings('ignore')
from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks

class CustomCrew:
    def run(self, inputs):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        researcher = agents.researcher()
        writer = agents.writer()
        editor = agents.editor()

        do_research = tasks.do_research(
            researcher,
        )

        write_summary = tasks.write_report(
            writer,
        )

        edit_report = tasks.edit_report(
            editor,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[researcher, writer, editor],
            tasks=[do_research, write_summary, edit_report],
            verbose=True,
            memory=True,
        )

        result = crew.kickoff(inputs=inputs)
        return result
