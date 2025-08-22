import os 
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.project_name = "FAST API PROJECT"
        self.api_key = os.getenv("API_KEY", 'demo-key')
        self.jwt_secret = os.getenv("JWT_SECRET", 'secret')
        self.algorithm = 'HS256'
        self.redis_url = os.getenv("REDIS_URL", 'redis://localhost:6379')
        self.model_path = os.path.join('app/models', 'model.pkl')

settings = Settings()
