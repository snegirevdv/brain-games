#!/usr/bin/env_python3
from brain_games.cli import welcome_user
from brain_games.game import start_game


def main():
    username = welcome_user()
    start_game(username=username, game="even")
