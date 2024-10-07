import random


class RockPaperScissors:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0
        self.lives = 5  # You can adjust the number of lives
        self.player_moves = []  # Store player moves for prediction

    def random_choice(self):
        """
        This method represents the computer's choice.
        It starts with random selection but can later predict
        based on player's history.
        """
        # If there's enough history, the computer can predict
        if len(self.player_moves) > 3:
            predicted_move = self.predict_player_move()
            return self.counter_move(predicted_move)
        else:
            return random.choice(["ROCK", "PAPER", "SCISSORS"])

    def counter_move(self, predicted_move):
        """
        Counter the predicted move with the winning move.
        """
        if predicted_move == "ROCK":
            return "PAPER"
        elif predicted_move == "PAPER":
            return "SCISSORS"
        else:
            return "ROCK"

    def predict_player_move(self):
        """
        Simple prediction based on the player's most frequent move.
        """
        return max(set(self.player_moves), key=self.player_moves.count)

    def player_choice(self):
        """
        Validates the user's input and returns the player's choice.
        """
        while True:
            user_input = input("What will you play (Rock, Paper, Scissors): ")
            user_input.upper()
            if user_input in ["ROCK", "PAPER", "SCISSORS"]:
                self.player_moves.append(user_input)  # Track player's choice
                return user_input
            else:
                print(
                    "\nInvalid input! Please choose Rock, Paper, or Scissors."
                    )

    def play_round(self):
        """
        Plays a single round, updating scores and lives.
        """
        player_move = self.player_choice()
        computer_move = self.random_choice()
        print(f"\nYou played: {player_move}, Computer played: {computer_move}")

        if player_move == computer_move:
            print("It's a draw!")
            self.draws += 1
        elif (player_move == "ROCK" and computer_move == "SCISSORS") or \
             (player_move == "PAPER" and computer_move == "ROCK") or \
             (player_move == "SCISSORS" and computer_move == "PAPER"):
            print("You win this round!")
            self.player_score += 1
        else:
            print("Computer wins this round!")
            self.computer_score += 1
            self.lives -= 1

        print(
            f"\nScores - You: {self.player_score},"
            f"Computer: {self.computer_score}, Draws: {self.draws}"
            )
        print(f"Lives remaining: {self.lives}\n")

    def start_game(self):
        """
        Starts the game and continues until lives run out or user quits.
        """
        print("Welcome to Rock, Paper, Scissors!\n")

        while self.lives > 0:
            self.play_round()
            if self.lives == 0:
                print("\nGame Over! You've run out of lives.")
                print(
                    f"Final Scores - You: {self.player_score},"
                    f" Computer: {self.computer_score}, Draws: {self.draws}"
                    )
                break

        print("Thanks for playing! Try to outsmart the computer next time.")


# Run the game
if __name__ == "__main__":
    game = RockPaperScissors()
    game.start_game()
