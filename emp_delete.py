import tkinter

LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 150
INPUT_DISTANCE = 250


class EmpDeletion:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Delete Employee")
        self.window.geometry("600x400")
        self.window.resizable(height=False, width=False)
        self.window.configure(background=DEFAULT_COLOR)

        self.add_title("Delete Employee", 225, 30, ("bold", 20))
        self.add_title("Email: ", LABEL_DISTANCE, 130, DEFAULT_FONT)
        self.email = self.add_input(INPUT_DISTANCE, 130)
        # self.add_title("Confirm Password: ", LABEL_DISTANCE, 175, DEFAULT_FONT)
        # self.password = self.add_input(INPUT_DISTANCE, 175)
        # self.password.config(show="*")

        self.button1 = self.add_button("Delete Employee", 100, 225)
        self.button2 = self.add_button("Transactions", 300, 225)
        self.button3 = self.add_button("Logout", 200, 275)

    def add_title(self, message, x_pos, y_pos, fonts):
        title = tkinter.Label(self.window, text=message, font=fonts, justify=tkinter.CENTER, background=DEFAULT_COLOR)
        title.place(x=x_pos, y=y_pos)
        return title

    def add_input(self, x_pos, y_pos):
        entry = tkinter.Entry(self.window, width=50)
        entry.place(x=x_pos, y=y_pos)
        return entry

    def add_button(self, btn_text, x_pos, y_pos):
        button = tkinter.Button(self.window, text=btn_text, width=20, bg="black", fg='white', font=("arial", 13))
        button.place(x=x_pos, y=y_pos)
        return button

    def run(self):
        self.window.mainloop()

    def destruct(self):
        self.window.destroy()


if __name__ == "__main__":
    form = EmpDeletion()
    form.run()
