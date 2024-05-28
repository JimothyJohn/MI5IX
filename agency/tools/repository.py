from crewai_tools import WebsiteSearchTool, ScrapeWebsiteTool, SerperDevTool, YoutubeVideoSearchTool, DirectoryReadTool, FileReadTool 
from langchain_community.tools import GooglePlacesTool

websiteScrapeTool = ScrapeWebsiteTool()
websiteSearchTool = WebsiteSearchTool()
searchTool = SerperDevTool()
mapTool = GooglePlacesTool()
contentTool = YoutubeVideoSearchTool()
file_read_tool = FileReadTool()
