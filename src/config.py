from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    APP_TITLE: str = "FastAPI Template"
    APP_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"
    
    # Different settings for dev/prod
    @property
    def RELOAD(self):
        return self.ENVIRONMENT == "development"
    
    @property
    def WORKERS(self):
        return 1 if self.ENVIRONMENT == "development" else 4

    class Config:
        env_file = ".env"

settings = Settings()