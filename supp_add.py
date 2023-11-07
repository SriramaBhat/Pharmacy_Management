import tkinter

LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 100
INPUT_DISTANCE = 300


class DistEntry:
    def __init__(self, conn):
        self.conn = conn
        self.values = []

        self.window = tkinter.Tk()
        self.window.geometry("600x500")
        self.window.title("Distributor Entry")
        self.window.resizable(width=False, height=False)
        self.window.configure(background=DEFAULT_COLOR)

        self.add_title("Distributor Registration form", 120, 30, ("bold", 20))
        self.add_title("Name: ", LABEL_DISTANCE, 100, DEFAULT_FONT)
        self.name = self.add_input(INPUT_DISTANCE, 100)
        self.add_title("Phone: ", LABEL_DISTANCE, 150, DEFAULT_FONT)
        self.phone = self.add_input(INPUT_DISTANCE, 150)
        self.add_title("Address: ", LABEL_DISTANCE, 200, DEFAULT_FONT)
        self.address = self.add_input(INPUT_DISTANCE, 200)
        self.add_title("Email: ", LABEL_DISTANCE, 250, DEFAULT_FONT)
        self.email = self.add_input(INPUT_DISTANCE, 250)

        self.button1 = self.add_button("Submit", 100, 325)
        self.button2 = self.add_button("Logout", 200, 375)
        self.button3 = self.add_button("Transactions", 300, 325)

    def add_title(self, message, x_pos, y_pos, fonts):
        title = tkinter.Label(self.window, text=message, font=fonts, justify=tkinter.CENTER, background=DEFAULT_COLOR)
        title.place(x=x_pos, y=y_pos)
        return title

    def add_input(self, x_pos, y_pos):
        entry = tkinter.Entry(self.window, width=40)
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
    form = DistEntry()
    form.run()
