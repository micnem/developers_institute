# while no winner:
# 	get__user_choice
# 	generata_computer_choice
# 	determine_winner(user, computer)
# 	display_feedback  who won
# 	check_for_game_over   wins or losses = 3
	
import random as r

winner = False
class RPS  :
    TO_WIN = 3
    CHOICES = ['R', 'P', 'S']

    def __init__(self):
        self.results = {"win": 0, "loss": 0, "draws": 0}
        self.play()
    
    def get_user_choice(self):
        while True: 
            choice = input("Enter (r,p,s): ").upper()
            if choice in self.CHOICES:
                break
            print("Invalid input, try again...")
        return choice
    def get_computer_choice(self):
        computer_choice = r.choice(self.CHOICES)
        return computer_choice
    
    def decide_winner(self, choice, computer_choice):
        if choice == computer_choice:
            return "draw"
        elif choice =='r' and computer_choice == 's':
            return "win"
        elif choice =='p' and computer_choice == 'r':
            return "win"
        elif choice == 's' and computer_choice == 'p':
            return "win"
        else:
            return "loss"

    def play(self):
        while winner == False:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            outcome = self.decide_winner(user_choice, computer_choice)
            self.results[outcome] += 1
            print(self.results)
            if self.results['win'] == self.TO_WIN:
                print("you win!")
                break
            elif self.results["loss"] == self.TO_WIN:
                print("you lose!")
                break

    
g1 = RPS()







