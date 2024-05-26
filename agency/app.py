import warnings

warnings.filterwarnings("ignore")
import os
from crew import ResearchCrew
import streamlit as st
from langchain_openai import AzureChatOpenAI


def main():
    st.title("The Sales Agency")

    crew = ResearchCrew()
    if st.selectbox("Select an endpoint:", ["OpenAI", "Azure"]) == "Azure":
        crew.agency.llm = AzureChatOpenAI(
            azure_endpoint=f"https://{os.environ.get('AZURE_OPENAI_RESOURCE')}.openai.azure.com",
            api_version=os.environ.get("OPENAI_API_VERSION"),
            api_key=os.environ.get("AZURE_OPENAI_API_KEY"),
            azure_deployment="oboi",
            temperature=0.7,
        )

    task = st.selectbox(
        "What tasks do you want to perform?", ["Research", "Prospecting", "Outreach"]
    )
    product = st.text_input("What are you trying to sell?", "robots")
    industry = st.text_input("Which industry are you trying to sell to?", "")
    location = st.text_input("Where are you trying to sell it?", "North Texas")
    # buzz = st.text_input("Are there any buzzwords I should ignore?", '"AI", "Smart Factory", "IoT", "Digital Transformation", "Industry 4.0"')

    inputs = {
        "topic": f"common problems in the {industry} industry being solved by {product}",
        "buzz": '"AI", "Smart Factory", "IoT", "Digital Transformation", "Industry 4.0"',
        "location": location,
    }

    if st.button("Run"):
        if product != "" or industry != "":
            result = ""
            if task == "Prospecting":
                result = crew.prospect(inputs=inputs)
            elif task == "Outreach":
                result = crew.outreach(inputs=inputs)
            elif task == "Research":
                result = crew.research(inputs=inputs)

            st.write(f"{result}")
        else:
            st.write("Please enter a topic to research")


if __name__ == "__main__":
    main()
