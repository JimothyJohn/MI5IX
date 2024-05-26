import warnings

warnings.filterwarnings("ignore")
from crew import ResearchCrew

def main():
    
    product = "sanitary automation equipment"
    industry = "food manufacturing"
    location = "Russelville, AR"
    buzz = '"AI", "Artifical Intelligence", "Smart Factory", "IoT", "Digital Transformation", "Internet of Things", "Digital Innovation", "collaborative", "Industry 4.0"'

    inputs = {
        "topic": f"common problems in the {industry} industry being solved by {product}",
        "buzz": buzz,
        "location": location,
    }

    crew = ResearchCrew(outputFolder=f"{industry}_{product}")

    result = crew.prospect(inputs=inputs)

    print(result)


if __name__ == "__main__":
    main()
