from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My FastAPI App"
    debug: bool = False
    database_url: str

    class Config:
        env_file = ".envs/fastapi.env"
        # env_prefix = "APP_"


settings = Settings()
