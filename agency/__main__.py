import warnings

warnings.filterwarnings("ignore")
import os
from crew import ResearchCrew
from agents import ResearchAgency
from tasks import ResearchTasks
import streamlit as st
from langchain_openai import AzureChatOpenAI

def main():
    st.title("The Sales Agency")

    agency = ResearchAgency()
    researchTasks = ResearchTasks()
    crew = ResearchCrew()
    if st.selectbox("Select an endpoint:", ["OpenAI", "Azure"]) == "Azure":
        agency.llm = AzureChatOpenAI(
                azure_endpoint=f"https://{os.environ.get('AZURE_OPENAI_RESOURCE')}.openai.azure.com",
                api_version=os.environ.get("OPENAI_API_VERSION"),
                api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
                azure_deployment="oboi",
                temperature=0.3,
            )

    task = st.selectbox("What tasks do you want to perform?", ["Research", "Prospecting", "Outreach"])
    product = st.text_input("What are you trying to sell?", "robots")
    industry = st.text_input("Which industry are you trying to sell to?", "")
    location = st.text_input("Where are you trying to sell it?", "North Texas")
    # buzz = st.text_input("Are there any buzzwords I should ignore?", '"AI", "Smart Factory", "IoT", "Digital Transformation", "Industry 4.0"')

    agents = agency.research()
    tasks = [researchTasks.research_topic(agents[0])]
        
    if task == "Prospecting":
        agents = agency.prospect()
        tasks = [researchTasks.research_topic(agents[0]), researchTasks.find_companies(agents[1])]
    elif task == "Outreach":
        agents = agency.outreach()
        tasks = [researchTasks.research_topic(agents[0]), researchTasks.find_companies(agents[1]), researchTasks.find_content(agents[1]), researchTasks.craft_outreach(agents[2])]

    crew.build(agents, tasks)

    if st.button("Do research"):
        if product != "" or industry != "":
            result = crew.run(
                {
                    "topic": f"common problems in the {industry} industry being solved by {product}",
                    "buzz": '"AI", "Smart Factory", "IoT", "Digital Transformation", "Industry 4.0"',
                    "location": location,
                }
            )

            st.write(f"{result.messages[0].message}")
        else:
            st.write("Please enter a topic to research")


if __name__ == "__main__":
    main()
