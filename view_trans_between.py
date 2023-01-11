import tkinter
from tkinter import ttk
import sqlite3


LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 150
INPUT_DISTANCE = 250


class ViewTrans:
    def __init__(self, conn):
        self.window = tkinter.Tk()
        self.window.title("View Transactions")
        self.window.geometry("1000x600")
        self.window.resizable(height=False, width=False)
        self.window.configure(background=DEFAULT_COLOR)
        self.tree = ""
        self.conn = conn

        self.title = self.add_title("Transaction Summary", 400, 50, ("bold", 20))
        self.add_title("Start Date: ", 50, 100, DEFAULT_FONT)
        self.start = self.add_input(150, 105)
        self.add_title("End Date: ", 500, 100, DEFAULT_FONT)
        self.end = self.add_input(600, 105)
        self.button1 = self.add_button("Transactions", 375, 540)
        self.button2 = self.add_button("Logout", 575, 540)
        self.button3 = self.add_button("Submit", 175, 540)
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

    def create_view(self):
        d1 = self.start.get().strip().split("/")
        d1 = str(d1[2]) + "-" + str(d1[1]) + "-" + str(d1[0])
        d2 = self.end.get().strip().split("/")
        d2 = str(d2[2]) + "-" + str(d2[1]) + "-" + str(d2[0])
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM stransactions WHERE  tran_date BETWEEN '" + d1 + "' AND '" + d2 +
                    "' UNION SELECT * FROM ctransactions " +
                    "WHERE tran_date BETWEEN '" + d1 + "' AND '" + d2 + "' ;")

    def add_treeview(self, height):
        d1 = self.start.get().strip().split("/")
        d1 = str(d1[2]) + "-" + str(d1[1]) + "-" + str(d1[0])
        d2 = self.end.get().strip().split("/")
        d2 = str(d2[2]) + "-" + str(d2[1]) + "-" + str(d2[0])
        stock_tree = ttk.Treeview(self.window, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings",
                                  height=height, selectmode="browse")
        stock_tree.column("#1", anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
        stock_tree.heading("#1", text="Trans_Id")
        stock_tree.column("#2", anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
        stock_tree.heading("#2", text="Sup/Cus Id")
        stock_tree.column("#3", anchor=tkinter.CENTER, stretch=tkinter.NO, width=400)
        stock_tree.heading("#3", text="Transaction Name")
        stock_tree.column("#4", anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
        stock_tree.heading("#4", text="Trans Date")
        stock_tree.column("#5", anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
        stock_tree.heading("#5", text="Trans Time")
        stock_tree.column("#6", anchor=tkinter.CENTER, stretch=tkinter.NO, width=150)
        stock_tree.heading("#6", text="Trans Amount")

        cur = self.conn.cursor()
        res = cur.execute("SELECT * FROM stransactions UNION SELECT * FROM ctransactions " +
                          "WHERE tran_date BETWEEN '" + d1 + "' AND '" + d2 + "' ;").fetchall()

        for i in range(1, len(res)+1):
            stock_tree.insert("", "end", text=str(i), values=res[i-1])

        return stock_tree

    def add_tree(self):
        self.tree = self.add_treeview(15)
        self.tree.place(y=200)

    def run(self):
        self.window.mainloop()

    def destruct(self):
        self.window.destroy()


if __name__ == "__main__":
    db = sqlite3.connect("pharmacy.sqlite")
    form = ViewTrans(db)
    form.run()
    db.close()
