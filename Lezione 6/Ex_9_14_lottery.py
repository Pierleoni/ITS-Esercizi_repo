import random
class LotteryMachine:
    def __init__(self,) ->list:
        self.list = list(range(1,11)) + ["a", "b", "c", "d", "e"]
        # self.winning_ticket = None
    def draw_ticket(self):
        self.winning_ticket = random.sample(self.list, 4)
        return self.winning_ticket
    def display_message(self):
        print(f"If any ticket matching the winning 4 items wins a prize: {self.winning_ticket}")

lottery = LotteryMachine()  
lottery.draw_ticket()       
lottery.display_message() 
