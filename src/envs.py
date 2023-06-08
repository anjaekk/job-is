import argparse
from os import getenv


envs = {
    "DATABASE_URL": getenv("DATABASE_URL"),
    "ALLOW_ORIGINS": getenv("ALLOW_ORIGINS"),
    "ALLOW_METHODS": getenv("ALLOW_METHODS"),
    "ALLOW_HEADERS": getenv("ALLOW_HEADERS"),
    "ALLOW_CREDENTIALS": getenv("ALLOW_CREDENTIALS"),
}
config = argparse.Namespace(**envs)