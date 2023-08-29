from tkinter import Tk, Frame, Checkbutton, TOP, LEFT


class ChecklistView:
    def __init__(self, checklist):
        self.window = Tk()
        self.window.title('Checklist')
        self.window.geometry('300x500')

        self.checklist = checklist

        self.frame = Frame(self.window)
        self.frame.pack()

    def update_view(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for item in self.checklist.items:
            checkbutton = Checkbutton(self.frame, text=item.description)
            checkbutton.pack(side=TOP, anchor="w")

    def mainloop(self):
        self.window.mainloop()