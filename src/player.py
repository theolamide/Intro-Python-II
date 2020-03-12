# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, user_input):
        print("Your Choice", user_input)
        if user_input == 'north' and self.current_room.n_to != None:
            self.current_room = self.current_room.n_to

        elif user_input == 'south' and self.current_room.s_to != None:
            self.current_room = self.current_room.s_to

        elif user_input == 'east' and self.current_room.e_to != None:
            self.current_room = self.current_room.e_to

        elif user_input == 'west' and self.current_room.w_to != None:
            self.current_room = self.current_room.w_to
        else:
            print('Error, invalid choice')
