from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    DATABASE_URL: str
    TEST_DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()