# wanderingMonster.py

import random
import gamefunctions

class WanderingMonster:
    """
    wandering monster class
    """
    def __init__(self, name, description, health_range, power_range, Gold_range, color, position=None):
        self.name = name
        self.desc = description
        self.health = random.randint(*health_range)
        self.power = random.randint(*power_range)
        self.Gold = random.randint(*Gold_range)
        self.color = color  

        self.position = position or [random.randint(0, 9), random.randint(0, 9)]

    def move(self):
        """
        This is how the monster moves around
        I don't think there is anything that stops a monster from just wandering off the screen but I don't think that matters
        """
        move_dir = random.choice(['up', 'down', 'left', 'right'])

        if move_dir == 'up' and self.position[1] > 0:
            self.position[1] -= 1
        elif move_dir == 'down' and self.position[1] < 9:
            self.position[1] += 1
        elif move_dir == 'left' and self.position[0] > 0:
            self.position[0] -= 1
        elif move_dir == 'right' and self.position[0] < 9:
            self.position[0] += 1


    def get_info(self):
        """
        Returns a dictionary of the monster's stats.
        """
        return {
            'name': self.name,
            'desc': self.desc,
            'health': self.health,
            'power': self.power,
            'Gold': self.Gold,
            'position': self.position,
            'color': self.color 
        
            
        }


    def new_random_monster():
        """
        makes a new monster.
        """
        monster = gamefunctions.new_random_monster()

        return WanderingMonster(
            name=monster['name'],
            description=monster['desc'],
            health_range=(monster['health'], monster['health']),  
            power_range=(monster['power'], monster['power']),     
            Gold_range=(monster['Gold'], monster['Gold']),        
            color=monster['color']
        )
