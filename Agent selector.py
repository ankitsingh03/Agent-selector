# Exercise 2
# Agent selector

import random


class Agent:
    def __init__(self, name, is_available, available_since, roles):
        self.name = name
        self.is_available = is_available
        self.available_since = available_since
        self.roles = roles


# Method to forward issue to all available agents.
def all_available(issue):
    forward_to = []
    for a in agents:
        if a.is_available:
            if issue in a.roles:
                forward_to.append(a.name)

    if forward_to:
        return forward_to
    else:
        return 'No agents available'


# Method to forward issue to least busy agent
def least_busy(issue):
    available_list = {}
    for a in agents:
        if a.is_available:
            if issue in a.roles:
                available_list[a.name] = a.available_since

    if available_list:
        return min(available_list, key=available_list.get)  # Getting the agent that is least busy.
    else:
        return 'No agents available'


# Method to forward issue to random agent
def random_mode(issue):
    forward_to = []
    for a in agents:
        if a.is_available:
            if issue in a.roles:
                forward_to.append(a.name)

    if forward_to:
        return random.choice(forward_to)
    else:
        return 'No agents available'


agents = [Agent('ankit', True, 2, ['sales', 'support']),
          Agent('rohit', False, 0, ['sales', 'support']),
          Agent('gaurav', True, 3, ['speaker', 'marketing']),
          Agent('shubham', True, 3, ['support', 'sales']),
          Agent('tina', True, 4, ['speaker', 'support']),
          Agent('radhika', True, 1, ['sales', 'marketing'])
          ]

print("What kind of help you want (sales, marketing, speaker, support)")
problem = input("please enter any of then: ").strip()

print('Select the mode below')
print('1 All available')
print('2 least busy')
print('3 Random mode')

choice = int(input())

# Making instance of selection mode class

if choice == 1:
    print(all_available(problem))
elif choice == 2:
    print(least_busy(problem))
elif choice == 3:
    print(random_mode(problem))
else:
    print('Enter a valid input.')
