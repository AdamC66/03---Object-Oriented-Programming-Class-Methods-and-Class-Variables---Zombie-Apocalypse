import random

class Zombie:
    max_speed = 5
    max_strength = 8
    horde = []
    plague_level = 10
    default_speed = 1
    default_strength = 3
#TEST TEST TEST
    def __init__(self, speed, strength):
        """Initializes zombie's speed and zombies strength
        """
        if speed > Zombie.max_speed:
            self.speed = Zombie.default_speed
        else:
            self.speed = speed

        if strength > Zombie.max_strength:
            self.strength = Zombie.default_strength
        else:
            self.strength = strength
    def __str__(self):
        return f'Speed:{self.speed}, Strength: {self.strength}'
    @classmethod
    def spawn(cls):
        """Spawns a random number of new zombies, based on the plague level,
        adding each one to the horde.  Each zombie gets a random speed.
        """
        new_zombies = random.randint(1, Zombie.plague_level)
        count = 0
        while count < new_zombies:
            speed = random.randint(1, Zombie.max_speed)
            strength = random.randint(1,Zombie.max_strength)
            Zombie.horde.append(Zombie(speed,strength))
            count += 1

    @classmethod
    def new_day(cls):
        """Represents the events of yet another day of the zombie apocalypse.
        Every day some zombies die off (phew!), some new ones show up,
        and sometimes the zombie plague level increases.
        """
        Zombie.spawn()
        Zombie.some_die_off()
        Zombie.increase_plague_level()
    @classmethod
    def some_die_off(cls):
        """Removes a random number (between 0 and 10) of zombies from the horde.
        """
        how_many_die = random.randint(0, 10)
        counter = 0
        while counter < how_many_die and len(Zombie.horde) > 0:
            random_zombie = random.randint(0,len(Zombie.horde) - 1)
            Zombie.horde.pop(random_zombie)
            counter += 1

    @classmethod
    def increase_plague_level(cls):
        """Increases the plague level by 0,1,or 2 when called """
        cls.plague_level += random.randint(0,2)

    def encounter(self):
        """This instance method represents you coming across a zombie! This can end in two possible outcomes:
        1. You outrun the zombie and escape unscathed!
        2. You don't outrun the zombie. you try and fight it. if you lose the fight you die. if you win. well you
        still die. but you become a zombie too!
        """
        outrun = self.chase()

        if outrun:
            return 'You escaped!'
        else:
            fight = self.fight()
            if fight:
                speed = random.randint(1, Zombie.max_speed)
                strength = random.randint(1,Zombie.max_strength)
                Zombie.horde.append(Zombie(speed,strength))
                return 'You manage to fight the zombie off, but got bit in the process. you are now a zombie!'
            else:
                return 'You died'

    def chase(self):
        """Represents you trying to outrun this particular zombie.
        Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run.
        """
        your_speed = random.randint(1, Zombie.max_speed)
        return your_speed > self.speed
    def fight(self):
        """Represents you trying to fight this particular zombie.
        Uses `Zombie.max_strength` to generate a random number that represents how strong you manage to fight.
        """
        your_strength = random.randint(1,Zombie.max_strength)
        return your_strength > self.strength

print(Zombie.horde) # []
Zombie.new_day()
#print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594f0b70>, <__main__.Zombie object at 0x7f6f594f0d68>]
zombie1 = Zombie.horde[0]
print(zombie1) # Speed: 1 -- Strength: 7
zombie2 = Zombie.horde[1]
print(zombie2) # Speed: 2 -- Strength: 7
print(zombie1.encounter()) # You escaped!
print(zombie2.encounter()) # You fought the zombie and caught the plague.  You are now a zombie too.  Raaaawrgh
Zombie.new_day()
#print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594efef0>, <__main__.Zombie object at 0x7f6f594f0c50>, <__main__.Zombie object at 0x7f6f594f0cc0>]
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print(zombie1.encounter()) # You died!
print(zombie2.encounter()) # You escaped!