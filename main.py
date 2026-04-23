# Zxxcxc

class Door:
    def __init__(self, is_open):
        self.is_open = is_open

    def check(self):
        return "Eshik ochiq" if self.is_open else "Eshik yopiq"
