from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "anti-clone-service"

    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "anti_clone"
    db_user: str = "anti_clone_user"
    db_password: str = "anti_clone_password"

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def database_url(self):
        return f"postgresql+psycopg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

settings = Settings()
