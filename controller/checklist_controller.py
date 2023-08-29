from model.checklist import Checklist
from model.checklistItem import ChecklistItem
from view.checklist_view import ChecklistView


class ChecklistController:
    def __init__(self):
        self.checklist = Checklist()
        self.view = ChecklistView(self.checklist)

    def add_item(self, description):
        item = ChecklistItem(description)
        self.checklist.add_item(item)
        self.view.update_view()

    def run(self):
        self.view.mainloop()
