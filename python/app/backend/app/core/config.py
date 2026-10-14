from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    RESET_TOKEN_EXPIRE_MINUTES: int = 15
    FRONTEND_URL: str = "http://localhost:5173"
    UPLOAD_DIR: str = "uploads"
    MAX_UPLOAD_MB: int = 2

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
"""How it works

Settings inherits from BaseSettings, so each field is automatically filled from an environment variable of the same name (or from .env).
model_config = SettingsConfigDict(env_file=".env") tells it to read the .env file in the working directory.
settings = Settings() creates one shared instance you import anywhere in the app: from config import settings, then settings.SECRET_KEY.

Fields

DATABASE_URL: str and SECRET_KEY: str have no default, so they are required. If they’re missing, the app fails at startup with a clear validation error.
ALGORITHM = "HS256" is the JWT signing algorithm. It isn’t in your .env, so the default is used.
The other fields have defaults that match your .env, so they work even if you delete those lines.

Benefits

Type conversion: ACCESS_TOKEN_EXPIRE_MINUTES: int turns the string "30" from .env into the integer 30.
Validation: a bad value (e.g. MAX_UPLOAD_MB=abc) raises an error immediately instead of causing bugs later.
Priority: real environment variables override .env, which is handy for production."""


"""it validates the env files is having fields it checks that with there values """
