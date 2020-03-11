from room import Room
from player import Player
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
player = Player('Olamide', room['outside'])

choice_options = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "q": "quit"
}


def welcome_message():
    welcome_message = (
        f'Welcome {player.name}, you are in {player.current_room}')
    print(welcome_message)
# Make a new player object that is currently in the 'outside' room.


def show_messages():
    # os.system('cls')
    print(f'{player.current_room.name}. {player.current_room.description}')


def get_player_choice():
    choice = input('Explore the cave: Go n,s,e,w, or q')
    if choice in choice_options:
        return choice_options[str(choice)]
    else:
        print('invalid choice')


def user_navigation(user_input):
    print("Your Choice", user_input)
    if user_input == 'north' and player.current_room.n_to != None:
        player.current_room = player.current_room.n_to

    elif user_input == 'south' and player.current_room.s_to != None:
        player.current_room = player.current_room.s_to

    elif user_input == 'east' and player.current_room.e_to != None:
        player.current_room = player.current_room.e_to

    elif user_input == 'west' and player.current_room.w_to != None:
        player.current_room = player.current_room.w_to
    else:
        print('Error')


welcome_message()
show_messages()
user_choice = get_player_choice()
print(user_choice)

while user_choice != 'quit':
    user_navigation(user_choice)
    show_messages()
    user_choice = get_player_choice()

exit()
