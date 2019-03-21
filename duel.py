import random
import time


class Duel:

    def __init__(self, name):

        guns = {
            0: 'AK-47',
            1: 'M4A1',
            2: 'SCAR-L',
            3: 'AUG',
            4: 'AKM'
        }

        self.name = name
        self.gun = guns[random.randrange(5)]

    @classmethod
    def count_down(cls):
        counter = random.randrange(3, 11)
        while counter > 0:
            print(counter)
            counter -= 1
            time.sleep(1)
            if counter == 0:
                print('Let\'s start!')

    def shoot_speed(self):
        speed = random.randrange(2000, 2500, 50)
        print(f'{self.name} have {self.gun} with shoot speed {speed}km/h')


first_player = Duel('Michael')
second_player = Duel('John')
first_player.shoot_speed()
second_player.shoot_speed()
Duel.count_down()
