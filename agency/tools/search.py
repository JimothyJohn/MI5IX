import os
from crewai_tools import BaseTool
from exa_py import Exa

EXA_API_KEY = os.environ.get("EXA_API_KEY")
exa = Exa(EXA_API_KEY)


class SearchTool(BaseTool):
    name: str = "Search Tool"
    description: str = (
        "This tool is used to execute a search query and return the results to the next agent"
    )

    def _run(self, query: str) -> str:
        # Perform the search with the given query
        results = exa.search(query, use_autoprompt=True)

        return results
