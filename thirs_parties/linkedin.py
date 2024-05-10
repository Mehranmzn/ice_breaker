import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_url:str, mock= True):
    
    """
    scrape linkedin profile
    """

    if mock:
        linkedin_url = "https://gist.githubusercontent.com/Mehranmzn/5b0c55f319e918bced2ec8bc11c59fb8/raw/a0580dba83a227cbec9a9669f3153d91d1bdb077/gistfile1.txt"
        response = requests.get(
            linkedin_url,
            timeout=10
            )
        
    data = response.json()

    return data    





if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_url="https://www.linkedin.com/mehran-moazeni/"
        )
    )