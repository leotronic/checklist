from controller.checklist_controller import ChecklistController

if __name__ == "__main__":
    controller = ChecklistController()
    controller.add_item("Zeuch machen")
    controller.add_item("Test 2")
    controller.run()
