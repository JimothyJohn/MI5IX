# Warning control
import warnings
warnings.filterwarnings('ignore')
from crew import CustomCrew

RESEARCH = f"""

I AM A WORLD CLASS RESEARCHER!!!
-------------------------------
Give me a subject to research: """

GENERIC_CAR = """
Find suitable SUV's for a couple that is having their first baby in September 2024.
We only want to consider SUV's that are 2022 models or newer.
The SUV must have 3 rows of seats where the middle seats are captain chairs.
We want a moonroof.
It must be under $60,000.
The only brands we want are Toyota, Acura, or Mazda.
We prefer a plug-in electric hybrid vehicle.
We want rear ventilation.
We'd prefer a towing option.
We'd like insight into the trim packages that meet these requirements.
We'd like to know which dealerships near our zip code of 76021 in Bedford, TX are.
"""

SPECIFIC_CAR = """
Give me a summary of the similarities and differences between the 2024 models of the Toyota Grand Highlander Hybrid, Acura MDX, and Mazda CX-90 PHEL.
We prefer a hybrid vehicle to save on gas.
We want rear ventilation.
We'd like insight into the trim package we should buy.
"""

def main():
    custom_crew = CustomCrew()
    result = custom_crew.run(inputs={"topic": GENERIC_CAR})

    print(
        f"""
          
########################

## Here is your custom crew run result: 

########################

{result}

"""
    )


if __name__ == "__main__":
    main()
