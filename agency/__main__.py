import warnings

warnings.filterwarnings("ignore")
import os
from crew import ResearchCrew
import streamlit as st
from langchain_openai import AzureChatOpenAI

def main():
    st.title("The Research Agency")

    llm = st.selectbox("Select an endpoint:", ["OpenAI", "Azure"])

    if llm == "OpenAI":
        crew = ResearchCrew()
    else:
        crew = ResearchCrew(llm=AzureChatOpenAI(
    azure_endpoint=f"https://{os.environ.get('AZURE_OPENAI_RESOURCE')}.openai.azure.com",
    api_version=os.environ.get("OPENAI_API_VERSION"),
    api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
    azure_deployment="oboi",
    temperature=0.3)
        )

    topic = st.text_input("What is the topic you would like me to research?", "")

    if st.button("Do research"):
        if topic != "":
            result = crew.run(topic)

            st.write(f"{result}")
        else:
            st.write("Please enter a topic to research")


if __name__ == "__main__":
    main()
