import tkinter

LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 100
INPUT_DISTANCE = 300


class EmployeeEntry:
    def __init__(self):
        self.values = []

        self.window = tkinter.Tk()
        self.window.geometry("600x600")
        self.window.title("Employee Entry")
        self.window.resizable(width=False, height=False)
        self.window.configure(background=DEFAULT_COLOR)

        self.add_title("Employee Registration form", 120, 30, ("bold", 20))
        self.add_title("Name: ", LABEL_DISTANCE, 100, DEFAULT_FONT)
        self.name = self.add_input(INPUT_DISTANCE, 100)
        self.add_title("Phone: ", LABEL_DISTANCE, 150, DEFAULT_FONT)
        self.phone = self.add_input(INPUT_DISTANCE, 150)
        self.add_title("Birth Date: ", LABEL_DISTANCE, 200, DEFAULT_FONT)
        self.dob = self.add_input(INPUT_DISTANCE, 200)
        self.add_title("Gender: ", LABEL_DISTANCE, 250, DEFAULT_FONT)
        self.gender = self.add_input(INPUT_DISTANCE, 250)
        self.add_title("Address: ", LABEL_DISTANCE, 300, DEFAULT_FONT)
        self.address = self.add_input(INPUT_DISTANCE, 300)
        self.add_title("Email: ", LABEL_DISTANCE, 350, DEFAULT_FONT)
        self.email = self.add_input(INPUT_DISTANCE, 350)
        self.add_title("Password: ", LABEL_DISTANCE, 400, DEFAULT_FONT)
        self.password = self.add_input(INPUT_DISTANCE, 400)
        self.password.config(show="*")
        self.add_title("Confirm Password: ", LABEL_DISTANCE, 450, DEFAULT_FONT)
        self.password1 = self.add_input(INPUT_DISTANCE, 450)
        self.password1.config(show="*")

        self.button1 = self.add_button("Submit", 235, 500)
        self.button2 = self.add_button("Go to Login", 235, 540)

    def add_title(self, message, x_pos, y_pos, fonts):
        title = tkinter.Label(self.window, text=message, font=fonts, justify=tkinter.CENTER, background=DEFAULT_COLOR)
        title.place(x=x_pos, y=y_pos)
        return title

    def add_input(self, x_pos, y_pos):
        entry = tkinter.Entry(self.window, width=40)
        entry.place(x=x_pos, y=y_pos)
        return entry

    def add_button(self, btn_text, x_pos, y_pos):
        button = tkinter.Button(self.window, text=btn_text, width=20, bg="black", fg='white')
        button.place(x=x_pos, y=y_pos)
        return button

    def run(self):
        self.window.mainloop()

    def destruct(self):
        self.window.destroy()


if __name__ == "__main__":
    form = EmployeeEntry()
    form.run()
