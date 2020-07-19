from random import choice


class Player: 
    def __init__(self, Name):
        self.Name = Name 
        self.move = self.shoot()
    
    def shoot(self):
        possible_moves = ['Rock', 'Paper', 'Scissors']
        self.move = choice(possible_moves) 