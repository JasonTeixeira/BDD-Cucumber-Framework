from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    base_url: str = os.getenv("BASE_URL", "https://www.saucedemo.com/")
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"
    browser: str = os.getenv("BROWSER", "chromium")

settings = Settings()
