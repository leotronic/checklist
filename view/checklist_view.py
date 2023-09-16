from tkinter import Tk, Frame, Checkbutton, TOP, Button, LEFT

FULL_WIDTH = "x"

STICK_LEFT = "W"

STICK_RIGHT = "E"


class ChecklistView:
    def __init__(self, controller, checklist):
        self.window = Tk()
        self.window.title('Checklist')
        self.window.geometry('200x500')

        self.controller = controller
        self.checklist = checklist

        self.frame = Frame(self.window)
        self.frame.pack(fill="both", expand=True, side='top')
        self.frame.grid_columnconfigure(0, weight=1)

        self.new_item_button = Button(self.window, text="New Item",
                                      command=self.add_new_item)
        self.new_item_button.pack(side='bottom',
                                  fill=FULL_WIDTH)

    def update_view(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for index, item in enumerate(self.checklist.items):
            checkbutton = Checkbutton(self.frame, text=item.description,
                                      command=item.toggle)
            checkbutton.grid(row=index, column=0, sticky=STICK_LEFT)
            delete_button = Button(self.frame, text="🗑", command=lambda
                item_to_remove=item: self.controller.remove_item(
                item_to_remove))
            delete_button.grid(row=index, column=1, sticky=STICK_RIGHT)

    def add_new_item(self):

        print("Add new item!")

    def mainloop(self):
        self.window.mainloop()
