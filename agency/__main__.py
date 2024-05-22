import warnings

warnings.filterwarnings("ignore")
from crew import ResearchCrew
import streamlit as st

crew = ResearchCrew()


def main():
    st.title("The Research Agency")

    topic = st.text_input("What is the topic you would like me to research?", "")

    if st.button("Do research"):
        if topic != "":
            result = crew.run(topic)

            st.write(
                f"""
            
########################

## Here is your custom crew run result: 

########################

{result}

"""
            )
        else:
            st.write("Please enter a topic to research")


if __name__ == "__main__":
    main()
