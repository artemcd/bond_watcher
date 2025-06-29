from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    tinvest_token: str = Field(..., env="TINVEST_TOKEN")
    database_url: str = Field("postgresql+asyncpg://postgres:postgres@db:5432/bond_watcher", env="DATABASE_URL")
    class Config:
        env_file = ".env"

settings = Settings()