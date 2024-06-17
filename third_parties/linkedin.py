import requests
import os
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool=False):
    """"Scrape information from Linkedin profiles,
        Manually scrape the information from the Linkedin profile
    """ 

