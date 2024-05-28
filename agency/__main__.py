import warnings

warnings.filterwarnings("ignore")
# import os
from crews.web_design import WebDevelopmentCrew
from agency.crews.review_crew import ProductResearchCrew
# from langchain_groq import ChatGroq
# import agentops

# agentops.init(os.environ.get("AGENTOPS_API_KEY"))

def main():

    product = "Laptop"
    features = """
15 inch screen, 16 hour battery life, thin frame, 3TB SSD, 4K screen
"""
    budget = 3000
    # industry = "semiconductor manufacturing"
    location = "San Jose, CA"
    # buzz = '"AI", "Artifical Intelligence", "Smart Factory", "IoT", "Digital Transformation", "Internet of Things", "Digital Innovation", "collaborative", "Industry 4.0"'

    inputs = {
        "topic": f"{product} with these features: {features} for less than ${budget}.",
        "buzz": "",
        "location": location,
    }

    reviewCrew = ProductResearchCrew()
    """
    reviewCrew.agency.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768"
        )
    """
    webCrew = WebDevelopmentCrew()
    """
    webCrew = WebDevelopmentCrew()
    webCrew.agency.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768"
        )
    """

    reviewCrew.all(inputs=inputs)
    webCrew.all(inputs=inputs)

if __name__ == "__main__":
    main()
