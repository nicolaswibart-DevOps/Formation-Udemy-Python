"""Module to generate random users"""
from faker import Faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent



logging.basicConfig(level=logging.INFO,
                    filename= BASE_DIR / "user.log",
                    filemode= "w")





#Création de l'instance

fake = Faker(locale = "fr_FR")


def get_user():
    """Generate a single user

    Args:
        (int): number of user

    Returns:
        str: user
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(n):
    """Generate a list of users

    Args:
        n (int): number of user to generate

    Returns:
        list[str] : users
    """
    logging.info(f"Generating a list of {n} users.")
    return [get_user() for _ in range(n)]


if __name__ == "__main__":
    user = get_users(n=4)
    print (user)
