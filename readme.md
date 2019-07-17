Before starting this assignment you should have some familiarity with
lists and iteration
if/else statements
defining classes and instantiating objects
defining and calling instance methods
using instance variables
You should also have already completed the previous assignment on class methods and class variables.

Learning Goals
class variables
class methods
Part 2: Zombie Apocalypse
It's the zombie apocalypse! But that doesn't mean we don't have time to practice using class variables and methods.

For this exercise we'll give you the beginning of a program and it's your job to add to it.

A side note on random numbers
We're going to be using the randint function from Python's random module to generate randomness in our zombie game. randint() accepts minimum and maximum integers as arguments and returns a random number that falls in that range. So randint(0, 4) would return a random number between 0 and 4, and randint(5, 10) would return a number between 5 and 10.

Before you start writing your zombie program you should go into the Python shell and try calling randint() a handful of times in order to get comfortable with how it works:

random isn't loaded by default when you start a Python program/the Python shell, so we have to tell Python so load it using import:

>>>from random import randint
>>>randint(50,100)
It's the zombie apocalypse
import random

class Zombie:

  max_speed = 5
  horde = []
  plague_level = 10
  default_speed = 1

  def __init__(self, speed):
    """Initializes zombie's speed
    """
    if speed > Zombie.max_speed:
      self.speed = Zombie.default_speed
    else:
      self.speed = speed

  @classmethod
  def spawn(cls):
    """Spawns a random number of new zombies, based on the plague level,
    adding each one to the horde.  Each zombie gets a random speed.
    """
    new_zombies = random.randint(1, Zombie.plague_level)
    count = 0

    while count < new_zombies:
      speed = random.randint(1, Zombie.max_speed)
      Zombie.horde.append(Zombie(speed))
      count += 1

  @classmethod
  def new_day(cls):
    """Represents the events of yet another day of the zombie apocalypse.
    Every day some zombies die off (phew!), some new ones show up,
    and sometimes the zombie plague level increases.
    """
    Zombie.spawn()
    Zombie.some_die_off()

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

  def encounter(self):
    """This instance method represents you coming across a zombie! This can end in two possible outcomes:
    1. You outrun the zombie and escape unscathed!
    2. You don't outrun the zombie. It eats your brains and you die. :(
    Returns a summary of what happened.
    """
    outrun = self.chase()

    if outrun:
      return 'You escaped!'
    else:
      return 'You died.'

  def chase(self):
    """Represents you trying to outrun this particular zombie.
    Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run.
    """
    your_speed = random.randint(1, Zombie.max_speed)
    return your_speed > self.speed
Copy this class into a new file called zombie.py and take a look at the code. The purpose of each method is explained with a docstring. As usual, you're encouraged to call over an instructor to discuss any parts of the code that you don't understand. You should also try calling some of the methods and printing the results to assist/verify your understanding.

Your Task
After familiarizing yourself with the code:

Implement a __str__() instance method. Try making an instance of Zombie and printing it to make sure it works.
Currently zombies have just one attribute: speed. We want to add strength as a second attribute.
There should be a max_strength class variable set to 8. This value won't change.
There should be a defaul_strength class variable set to 3. This value won't change.
__init__() should initialize the zombie's strength as well as speed. Strength should be accepted as another argument, but if the value passed in is greater than the maximum strength, the default strength should be used instead. (Hint: see how __init__ deals with speed.)
Update the doc string to reflect this new feature
Define a new instance method fight. Whereas chase() represents you trying to outrun a zombie, fight represents what happens when you try to fight a zombie.
Use Zombie.max_strength to generate a random number that represents how well you are able to fight off this zombie. This method should return True if your strength is greater than the zombie's and False otherwise.
Write a docstring explaining what this method does (see the other method's docstrings for inspiration).
We currently have an instance method encounter that represents you coming across a zombie and trying to run away. Right now there are 2 possible outcomes: you can either run away or get caught and die. We want to add fighting the zombie off as a third possible outcome:
You should only try to fight the zombie if you don't outrun it.
If you don't manage to outrun the zombie, call our new fight() method to try to fight it off.
If you lose the fight, you still die.
If you win the fight, you survive, BUT in the process you catch the zombie plague. Instantiate a new zombie object (that's you!) and add it to Zombie.horde.
Make sure encounter always returns a string summarizing what happens (e.g. "You are now a zombie. Raawwwrghh").
Update the docstring to reflect this new functionality.
Define a new class method increase_plague_level:
This class method should generate a random number between 0 and 2 and increase Zombie.plague_level by that amount.
Update the docstring to reflect this change in functionality.
Call this method from new_day(), so the plague spreads a little every day.
Update the new_day() docstring too.
Example output:
Your output may be different, since this game has elements of randomness:

print(Zombie.horde) # []
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594f0b70>, <__main__.Zombie object at 0x7f6f594f0d68>]
zombie1 = Zombie.horde[0]
print(zombie1) # Speed: 1 -- Strength: 7
zombie2 = Zombie.horde[1]
print(zombie2) # Speed: 2 -- Strength: 7
print(zombie1.encounter()) # You escaped!
print(zombie2.encounter()) # You fought the zombie and caught the plague.  You are now a zombie too.  Raaaawrgh
Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x7f6f594f0d30>, <__main__.Zombie object at 0x7f6f594efef0>, <__main__.Zombie object at 0x7f6f594f0c50>, <__main__.Zombie object at 0x7f6f594f0cc0>]
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print(zombie1.encounter()) # You died!
print(zombie2.encounter()) # You escaped!
Stretch goals:
Change the increase_plague_level method so that the amount the plague level increases is somehow based on the number of zombies in the horde, instead of being completely random.
Add a method called deadliest_zombie that returns the zombie that has the highest combination of speed and strength. Should this be a class method or an instance method?