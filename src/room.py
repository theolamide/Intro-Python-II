# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None, items=[]):
        # If we don't send a cardinal point movement, it defaults to none
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def __str__(self):
        return f"{self.name}"

    def displayItemsList(self):
        if len(self.items) > 1:
            output = ', '.join(map(str, self.items))
            print(f'Items in this room: {output}')
        elif len(self.items) == 1:
            print(f'The only item in this room is: {self.items[0]}')

    def removeItem(self, item):
        self.items.remove(item)
