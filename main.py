import json
from argparse import ArgumentParser
from gpiozero import Button

from game.game import Game

if __name__ == "__main__":
    parser = ArgumentParser(description='Play the game with no name.')
    parser.add_argument('config', type=str, help='Path to the config file.')
    args = parser.parse_args()
    with open(args.config, 'r') as f:
        config = json.load(f)
    game = Game(config=config)
    start_button = Button(config["button"], pull_up=False)
    start_button.wait_for_release()
    game.configure()
    game.start()
