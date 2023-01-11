import sqlite3
import tkinter

LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 80
INPUT_DISTANCE = 350


class CustTransactions:
    def __init__(self, conn):
        self.values = []

        self.window = tkinter.Tk()
        self.window.geometry("800x600")
        self.window.title("Customer Transactions")
        self.window.resizable(width=False, height=False)
        self.window.configure(background=DEFAULT_COLOR)
        self.v = tkinter.IntVar()
        self.conn = conn

        self.add_title("Customer Transaction Form", 230, 30, ("bold", 20))
        self.add_title("Customer Name: ", LABEL_DISTANCE, 100, DEFAULT_FONT)
        self.name = self.add_input(INPUT_DISTANCE, 100)
        self.add_title("Email: ", LABEL_DISTANCE, 150, DEFAULT_FONT)
        self.email = self.add_input(INPUT_DISTANCE, 150)
        self.add_title("Symptoms: ", LABEL_DISTANCE, 200, DEFAULT_FONT)
        self.symptoms = self.add_input(INPUT_DISTANCE, 200)
        self.add_title("Medicine Name: ", LABEL_DISTANCE, 250, DEFAULT_FONT)
        self.mname = self.add_input(INPUT_DISTANCE, 250)
        # r1 = tkinter.Radiobutton(self.window, text="Tablet", variable=self.v, value=2,
        #                          font=("Arial", 14), background=DEFAULT_COLOR)
        # r1.pack(side=tkinter.RIGHT, anchor=tkinter.W)
        # r1.place(x=250, y=350)
        # r2 = tkinter.Radiobutton(self.window, text="Syrup", variable=self.v, value=1,
        #                          font=("Arial", 14), background=DEFAULT_COLOR)
        # r2.pack(side=tkinter.RIGHT, anchor=tkinter.W)
        # r2.place(x=450, y=350)
        self.add_title("Quantity: ", LABEL_DISTANCE, 300, DEFAULT_FONT)
        self.quantity = self.add_input(INPUT_DISTANCE, 300)

        self.button1 = self.add_button("Submit", 100, 400)
        self.button2 = self.add_button("View Stocks", 300, 400)
        self.button4 = self.add_button("Logout", 275, 450)
        self.button3 = self.add_button("Generate Bill", 500, 400)

    def add_title(self, message, x_pos, y_pos, fonts):
        title = tkinter.Label(self.window, text=message, font=fonts, justify=tkinter.CENTER, background=DEFAULT_COLOR)
        title.place(x=x_pos, y=y_pos)
        return title

    def add_input(self, x_pos, y_pos):
        entry = tkinter.Entry(self.window, width=55)
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
    db = sqlite3.connect("pharmacy.sqlite")
    form = CustTransactions(db)
    form.run()
    db.close()
