import tkinter

LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 100
INPUT_DISTANCE = 250


class LoginForm:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Login")
        self.window.geometry("600x400")
        self.window.resizable(height=False, width=False)
        self.window.configure(background=DEFAULT_COLOR)
        self.v = tkinter.IntVar()

        self.add_title("Login", 275, 30, ("bold", 20))
        # frame = tkinter.Frame(self.window, width=400, height=20)
        # frame.place(y=70)
        r1 = tkinter.Radiobutton(self.window, text="Employee", variable=self.v, value=2,
                                 font=("Arial", 14), background=DEFAULT_COLOR)
        r1.pack(side=tkinter.RIGHT, anchor=tkinter.W)
        r1.place(x=150, y=85)
        r2 = tkinter.Radiobutton(self.window, text="Admin", variable=self.v, value=1,
                                 font=("Arial", 14), background=DEFAULT_COLOR)
        r2.pack(side=tkinter.RIGHT, anchor=tkinter.W)
        r2.place(x=350, y=85)
        self.add_title("Email: ", LABEL_DISTANCE, 130, DEFAULT_FONT)
        self.email = self.add_input(INPUT_DISTANCE, 130)
        self.add_title("Password: ", LABEL_DISTANCE, 175, DEFAULT_FONT)
        self.password = self.add_input(INPUT_DISTANCE, 175)
        self.password.config(show="*")

        self.button1 = self.add_button("Login", 225, 225)
        self.button2 = self.add_button("Sign Up", 225, 275)

    def add_title(self, message, x_pos, y_pos, fonts):
        title = tkinter.Label(self.window, text=message, font=fonts, justify=tkinter.CENTER, background=DEFAULT_COLOR)
        title.place(x=x_pos, y=y_pos)
        return title

    def add_input(self, x_pos, y_pos):
        entry = tkinter.Entry(self.window, width=45)
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
    form = LoginForm()
    form.run()
