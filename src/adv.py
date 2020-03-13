from room import Room
from player import Player
from item import Item
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

room['outside'].items = [Item('key', 'This opens the door to the cave'), Item(
    'Rock', 'This is is a toy')]

#
# Main
#
player = Player('Olamide', room['outside'])

movement_options = ["north", "south", "east", "west", "quit"]
action_options = ["take", "drop"]


def welcome_message():
    welcome_message = (
        f'Welcome {player.name}, you are in {player.current_room}')
    print(welcome_message)
# Make a new player object that is currently in the 'outside' room.


def show_messages():
    print(f'{player.current_room.name}. {player.current_room.description}')
    player.current_room.displayItemsList()


def get_player_choice():
    return input('Explore the cave: Go north, south, east, west, or quit')


def game_actions(input):

    # What kind of action
    split = input.split(" ")
    print(split)

    # Check Length is split
    if len(split) == 2:
        # Perform Action
        print(f"Performing action {split[0]}")
    elif len(split) == 1:
        if input in movement_options:
            player.move(input)
        else:
            print("\n Invalid Choice")
    else:
        print("\n Invalid Choice")

    if input in movement_options:
        player.move(input)
    else:
        print('\ninvalid choice')
        return


welcome_message()
show_messages()
user_choice = get_player_choice()
print(user_choice)

while user_choice != 'quit':
    game_actions(user_choice)
    show_messages()
    user_choice = get_player_choice()

exit()
