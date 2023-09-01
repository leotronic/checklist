from tkinter import Tk, Frame, Checkbutton, TOP, Button, LEFT


class ChecklistView:
    def __init__(self, controller, checklist):
        self.window = Tk()
        self.window.title('Checklist')
        self.window.geometry('300x500')

        self.controller = controller
        self.checklist = checklist

        self.frame = Frame(self.window)
        self.frame.pack()

    def update_view(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for item in self.checklist.items:
            item_frame = item_frame = Frame(self.frame)
            checkbutton = Checkbutton(item_frame, text=item.description,
                                      command=item.toggle)
            checkbutton.pack(side=LEFT)
            Button(item_frame, text="🗑",
                   command=lambda item=item: self.controller.remove_item(item)
                   ).pack(side=LEFT)
            item_frame.pack(side=TOP)

    def mainloop(self):
        self.window.mainloop()
