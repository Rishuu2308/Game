"""
**FILEKEEPING HEADER**

Code Overview:
This file contains the main logic for a multiplayer game that can be played by up to 10 people.
It includes a Game class to manage the game state and player interactions.

Key Insights:
- The game supports multiple players (up to 10)
- Uses a simple turn-based structure
- Implements basic game logic with placeholders for more complex mechanics

LLM Mistakes and Explicit Instructions:
None at this time.

Explored Approaches:
Initial implementation of a basic multiplayer game structure.

Observations:
The current implementation is a skeleton and will need further development based on specific game rules and mechanics.

User Code Lock:
None at this time.

References and Resources:
None at this time.

Todo List:
- Implement specific game rules and mechanics
- Add more complex player interactions
- Implement a scoring system
- Add game end conditions
"""

import random
from typing import List, Dict

class Player:
    def __init__(self, name: str):
        self.name = name
        self.lives = 3

    def take_turn(self, last_letter: str) -> str:
        # In a real implementation, this would get input from the player
        word = input(f"{self.name}, enter a word starting with '{last_letter}': ")
        return word

class Game:
    def __init__(self, max_players: int = 10):
        self.players: List[Player] = []
        self.max_players = max_players
        self.current_word = ""
        self.used_words = set()

    def add_player(self, name: str) -> bool:
        if len(self.players) < self.max_players:
            self.players.append(Player(name))
            return True
        return False

    def start_game(self):
        if len(self.players) < 2:
            print("Not enough players to start the game.")
            return

        print("Word Chain Game started!")
        self.current_word = random.choice(["apple", "elephant", "umbrella", "xylophone"])
        print(f"The starting word is: {self.current_word}")
        self.used_words.add(self.current_word)

        while not self.is_game_over():
            self.play_round()

        self.end_game()

    def play_round(self):
        for player in self.players:
            if player.lives > 0:
                last_letter = self.current_word[-1]
                new_word = player.take_turn(last_letter)
                
                if (new_word.lower()[0] != last_letter.lower() or 
                    new_word.lower() in self.used_words):
                    print(f"Invalid word! {player.name} loses a life.")
                    player.lives -= 1
                else:
                    self.current_word = new_word
                    self.used_words.add(new_word.lower())
                    print(f"Valid word! The new word is: {self.current_word}")

    def is_game_over(self) -> bool:
        active_players = sum(1 for player in self.players if player.lives > 0)
        return active_players <= 1

    def end_game(self):
        print("Game Over!")
        for player in self.players:
            print(f"{player.name}: {player.lives} lives remaining")
        winner = next((player for player in self.players if player.lives > 0), None)
        if winner:
            print(f"The winner is {winner.name}!")
        else:
            print("It's a tie!")

def main():
    game = Game()
    
    # Add players
    num_players = int(input("Enter the number of players (2-10): "))
    for i in range(num_players):
        name = input(f"Enter name for Player {i+1}: ")
        game.add_player(name)
    
    game.start_game()

if __name__ == "__main__":
    main()
