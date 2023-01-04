import tkinter
from tkinter import ttk
import sqlite3


LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 150
INPUT_DISTANCE = 250


class StocksBetweenPrice:
    def __init__(self, conn, emp_type):
        self.window = tkinter.Tk()
        self.window.title("Stocks between")
        self.window.geometry("1000x600")
        self.window.resizable(height=False, width=False)
        self.window.configure(background=DEFAULT_COLOR)
        self.tree = ""
        self.conn = conn
        self.emp_type = emp_type

        self.title = self.add_title("Stocks Summary", 400, 50, ("bold", 20))
        self.add_title("Minimum Price: ", 50, 100, DEFAULT_FONT)
        self.minimum = self.add_input(200, 105)
        self.add_title("Maximum Price: ", 525, 100, DEFAULT_FONT)
        self.maximum = self.add_input(675, 105)
        self.button1 = self.add_button("Submit", 350, 540)
        self.button2 = self.add_button("Logout", 550, 540)
        self.button3 = self.add_button("Back", 150, 540)
        self.button1.configure(command=self.add_tree)

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
        max_value = self.maximum.get().strip()
        min_value = self.minimum.get().strip()
        cur = self.conn.cursor()
        if self.emp_type.casefold() == "admin":
            cur.execute("DROP VIEW IF EXISTS admin_stock_view;")
            cur.execute("CREATE VIEW admin_stock_view AS " +
                        "SELECT stocks.sid, tablets.mname, tablets.composition, " +
                        "stocks.qty, stocks.dist_unit_price, stocks.expdate"
                        + " FROM stocks INNER JOIN tablets ON stocks.tid = tablets.mid WHERE "
                        + "stocks.dist_unit_price BETWEEN " + str(min_value) + " AND " +
                        str(max_value) + " UNION " +
                        "SELECT stocks.sid, syrups.mname, syrups.composition, " +
                        "stocks.qty, stocks.dist_unit_price, stocks.expdate" +
                        " FROM stocks INNER JOIN syrups ON stocks.syid = syrups.mid WHERE " +
                        "stocks.dist_unit_price BETWEEN " + str(min_value) + " AND " + str(max_value) + ";")
        else:
            cur.execute("DROP VIEW IF EXISTS emp_stock_view;")
            cur.execute("CREATE VIEW emp_stock_view AS " +
                        "SELECT stocks.sid, tablets.mname, tablets.composition, " +
                        "stocks.qty, stocks.cust_unit_price, stocks.expdate"
                        + " FROM stocks INNER JOIN tablets ON stocks.tid = tablets.mid WHERE " +
                        "stocks.cust_unit_price BETWEEN " + str(min_value) + " AND " +
                        str(max_value) + " UNION " +
                        "SELECT stocks.sid, syrups.mname, syrups.composition, stocks.qty," +
                        " stocks.cust_unit_price, stocks.expdate" +
                        " FROM stocks INNER JOIN syrups ON stocks.syid = syrups.mid WHERE "
                        + "stocks.cust_unit_price BETWEEN " + str(min_value) + " AND " + str(max_value) + ";")
        # cur.execute("COMMIT;")

    def add_treeview(self, height):
        self.create_view()
        stock_tree = ttk.Treeview(self.window, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show="headings",
                                  height=height, selectmode="browse")
        stock_tree.column("#1", anchor=tkinter.CENTER, stretch=tkinter.NO, width=50)
        stock_tree.heading("#1", text="St_Id")
        stock_tree.column("#2", anchor=tkinter.CENTER, stretch=tkinter.NO, width=200)
        stock_tree.heading("#2", text="Medicine Name")
        stock_tree.column("#3", anchor=tkinter.CENTER, stretch=tkinter.NO, width=400)
        stock_tree.heading("#3", text="Composition")
        stock_tree.column("#4", anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
        stock_tree.heading("#4", text="Quantity")
        stock_tree.column("#5", anchor=tkinter.CENTER, stretch=tkinter.NO, width=90)
        stock_tree.heading("#5", text="Unit Price")
        stock_tree.column("#6", anchor=tkinter.CENTER, stretch=tkinter.NO, width=150)
        stock_tree.heading("#6", text="Expiry Date")

        if self.emp_type == "admin":
            res = self.conn.cursor().execute("SELECT * FROM admin_stock_view").fetchall()
        else:
            res = self.conn.cursor().execute("SELECT * FROM emp_stock_view").fetchall()

        for i in range(1, len(res) + 1):
            stock_tree.insert("", "end", text=str(i), values=res[i - 1])

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
    form = StocksBetweenPrice(db, "admin")
    form.run()
    db.close()
