import argparse
from os import getenv


envs = {
    "DATABASE_URL": getenv("DATABASE_URL"),
}
config = argparse.Namespace(**envs)