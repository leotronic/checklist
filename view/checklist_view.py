from tkinter import Tk, Frame, Checkbutton, TOP, Button, LEFT


class ChecklistView:
    def __init__(self, controller, checklist):
        self.window = Tk()
        self.window.title('Checklist')
        self.window.geometry('200x500')

        self.controller = controller
        self.checklist = checklist

        self.frame = Frame(self.window)
        self.frame.pack(fill="both", expand=True)
        self.frame.grid_columnconfigure(0, weight=1)

    def update_view(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for index, item in enumerate(self.checklist.items):
            checkbutton = Checkbutton(self.frame, text=item.description,
                                      command=item.toggle)
            checkbutton.grid(row=index, column=0, sticky="W")
            delete_button = Button(self.frame, text="🗑", command=lambda
                item_to_remove=item: self.controller.remove_item(item_to_remove))
            delete_button.grid(row=index, column=1, sticky="E")

    def mainloop(self):
        self.window.mainloop()
