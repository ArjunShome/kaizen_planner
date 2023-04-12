from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv()


class GlobalConfig(BaseSettings):
    """Global configurations."""

    # define global variables with the Field class
    ENV_NAME: str = Field('dev', env='ENV_NAME')
    DB_USERNAME: str = Field(None, env='DB_USERNAME')
    DB_PASSWORD: str = Field(None, env='DB_PASSWORD')
    DB_HOST: str = Field(None, env='DB_HOST')
    DB_PORT: str = Field(None, env='DB_PORT')
    DB_NAME: str = Field(None, env='DB_NAME')
    DB_ENGINE: str = Field('postgresql', env='DB_ENGINE')
    SQLALCHEMY_DATABASE_URI: str = Field(None, env='SQLALCHEMY_DATABASE_URI')

    MAIL_SERVER: str = Field(None, env='MAIL_SERVER')
    MAIL_USERNAME: str = Field(None, env='MAIL_USERNAME')
    MAIL_PORT: str = Field(None, env='MAIL_PORT')
    MAIL_PASSWORD: str = Field(None, env='MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER: str = Field(None, env='MAIL_DEFAULT_SENDER')
    DEVELOPER_EMAIL: str = Field(None, env='DEVELOPER_EMAIL')
    MAIL_USE_SSL: bool = Field(False, env='MAIL_USE_SSL')
    MAIL_USE_TLS: bool = Field(False, env='MAIL_USE_TLS')

    WEB_API_PROTOCOL: str = Field(None, env='WEB_API_PROTOCOL')
    WEB_API_HOST: str = Field(None, env='WEB_API_HOST')
    WEB_API_PORT: str = Field(None, env='WEB_API_PORT')

    REDIS_HOST: str = Field(None, env='REDIS_HOST')
    REDIS_PORT: str = Field(None, env='REDIS_PORT')
    REDIS_CACHE_URL: str = Field(None, env='REDIS_CACHE_URL')

    class Config:
        """Loads the dotenv file."""

        env_file: str = ".env"

    def get_config(self):
        self.SQLALCHEMY_DATABASE_URI = f'{self.DB_ENGINE}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

        return self


class DevConfig(GlobalConfig):
    """Development configurations."""

    class Config:
        env_prefix: str = "DEV_"
        env_file: str = ".env"


class ProdConfig(GlobalConfig):
    """Prod configurations."""

    class Config:
        env_prefix: str = "PROD_"


class FactoryConfig:
    """Returns a config instance depending on the ENV variable."""
    @staticmethod
    def generate_config():
        env_name = GlobalConfig().ENV_NAME
        if env_name == "dev":
            return DevConfig()

        elif env_name == "prod":
            return ProdConfig()


app_config = FactoryConfig.generate_config().get_config()
