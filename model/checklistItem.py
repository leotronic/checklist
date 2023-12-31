class ChecklistItem:
    def __init__(self, description):
        self.description = description
        self.done = False

    def set_to_done(self):
        self.done = True

    def set_to_not_done(self):
        self.done = False

    def toggle(self):
        self.done = not self.done
        print(f"toggled DONE of {self.description} to {self.done}")