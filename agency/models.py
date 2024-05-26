# Warning control
import warnings

warnings.filterwarnings("ignore")

from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime


class Source(BaseModel):
    website: HttpUrl
    title: Optional[str] = None
    author: Optional[str] = None
    abstract: str
    published_date: Optional[datetime] = None


# Define a Pydantic model that includes a list of sources
class SourceList(BaseModel):
    sources: List[Source]


class Content(BaseModel):
    name: str
    url: HttpUrl
    industry: str
    channel: Optional[int]
    relevance: str


# Define a Pydantic model that includes a list of sources
class ContentList(BaseModel):
    content: List[Content]


class Company(BaseModel):
    name: str
    website: HttpUrl
    industry: str
    hq_city: str
    hq_state: str
    employees: Optional[int]
    annual_revenue: Optional[int]
    relevance: str


# Define a Pydantic model that includes a list of sources
class CompanyList(BaseModel):
    companies: List[Company]


class Outreach(BaseModel):
    company: str
    content: HttpUrl
    message: str
    contact_role: str
    location: str


# Define a Pydantic model that includes a list of sources
class OutreachList(BaseModel):
    messages: List[Outreach]
