import tkinter
from tkinter import ttk
import sqlite3


LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 150
INPUT_DISTANCE = 250


class StocksDPrice:
    def __init__(self, conn):
        self.window = tkinter.Tk()
        self.window.title("View Transactions")
        self.window.geometry("650x600")
        self.window.resizable(height=False, width=False)
        self.window.configure(background=DEFAULT_COLOR)
        self.tree = ""
        self.conn = conn

        self.title = self.add_title("Stock Quantity", 250, 50, ("bold", 20))
        self.add_title("Stock Count: ", 50, 100, DEFAULT_FONT)
        self.count = self.add_input(200, 105)
        self.button1 = self.add_button("Transactions", 450, 540)
        self.button2 = self.add_button("Logout", 250, 540)
        self.button3 = self.add_button("Submit", 50, 540)
        self.button3.configure(command=self.add_tree)

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

    def add_treeview(self, height):
        count = self.count.get().strip()
        stock_tree = ttk.Treeview(self.window, columns=("c1", "c2"), show="headings",
                                  height=height, selectmode="browse")
        stock_tree.column("#1", anchor=tkinter.CENTER, stretch=tkinter.NO, width=200)
        stock_tree.heading("#1", text="Distributor Price")
        stock_tree.column("#2", anchor=tkinter.CENTER, stretch=tkinter.NO, width=200)
        stock_tree.heading("#2", text="Number of medicines")

        cur = self.conn.cursor()
        res = cur.execute("SELECT dist_unit_price, COUNT(sid) FROM stocks GROUP BY dist_unit_price " +
                          "HAVING COUNT(sid) >=" + str(count) + ";").fetchall()

        for i in range(1, len(res)+1):
            stock_tree.insert("", "end", text=str(i), values=res[i-1])

        return stock_tree

    def add_tree(self):
        self.tree = self.add_treeview(15)
        self.tree.place(x=150, y=200)

    def run(self):
        self.window.mainloop()

    def destruct(self):
        self.window.destroy()


if __name__ == "__main__":
    db = sqlite3.connect("pharmacy.sqlite")
    form = StocksDPrice(db)
    form.run()
    db.close()
