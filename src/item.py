class Item():
    def __init__(self, name, description):
        self.name = name
        self.decription = description

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
