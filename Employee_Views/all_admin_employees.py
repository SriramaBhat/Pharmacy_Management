import tkinter
from tkinter import ttk
import sqlite3

LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 150
INPUT_DISTANCE = 250


class ViewAllEmpAdmin:
    def __init__(self, conn):
        self.window = tkinter.Tk()
        self.window.title("All Admin Employees")
        self.window.geometry("1000x500")
        self.window.resizable(height=False, width=False)
        self.window.configure(background=DEFAULT_COLOR)
        self.conn = conn

        self.title = self.add_title("All Admin Employees", 350, 50, ("bold", 20))
        self.tree = self.add_treeview(15)
        self.tree.place(y=100)
        self.button1 = self.add_button("View Menu", 400, 450)

    def add_title(self, message, x_pos, y_pos, fonts):
        title = tkinter.Label(self.window, text=message, font=fonts, justify=tkinter.CENTER, background=DEFAULT_COLOR)
        title.place(x=x_pos, y=y_pos)
        return title

    def add_button(self, btn_text, x_pos, y_pos):
        button = tkinter.Button(self.window, text=btn_text, width=20, bg="black", fg='white', font=("arial", 13))
        button.place(x=x_pos, y=y_pos)
        return button

    def create_emp_view(self):
        cur = self.conn.cursor()
        cur.execute("DROP VIEW employee_view;")
        cur.execute("CREATE VIEW employee_view AS " +
                    "SELECT ename, ephone, egender, eaddress, eemail FROM employee INTERSECT " +
                    "SELECT aname, aphone, agender, aaddress, aemail FROM admin;")
        # cur.execute("COMMIT;")

    def add_treeview(self, height):
        self.create_emp_view()
        emp_tree = ttk.Treeview(self.window, columns=("c1", "c2", "c3", "c4", "c5"), show="headings",
                                height=height, selectmode="browse")
        emp_tree.column("#1", anchor=tkinter.CENTER, stretch=tkinter.NO, width=183)
        emp_tree.heading("#1", text="Employee Name")
        emp_tree.column("#2", anchor=tkinter.CENTER, stretch=tkinter.NO, width=150)
        emp_tree.heading("#2", text="Phone")
        emp_tree.column("#3", anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
        emp_tree.heading("#3", text="Gender")
        emp_tree.column("#4", anchor=tkinter.CENTER, stretch=tkinter.NO, width=350)
        emp_tree.heading("#4", text="Address")
        emp_tree.column("#5", anchor=tkinter.CENTER, stretch=tkinter.NO, width=200)
        emp_tree.heading("#5", text="Email")

        res = self.conn.cursor().execute("SELECT * FROM employee_view").fetchall()
        for i in range(1, len(res)+1):
            emp_tree.insert("", "end", text=str(i), values=res[i-1])

        tree_scroll = ttk.Scrollbar(self.window)
        tree_scroll.configure(command=emp_tree.yview)
        emp_tree.configure(yscrollcommand=tree_scroll.set)
        tree_scroll.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        emp_tree.pack()

        return emp_tree

    def run(self):
        self.window.mainloop()

    def destruct(self):
        self.window.destroy()


if __name__ == "__main__":
    db = sqlite3.connect("F:\Programs\DBMS_Project\pharmacy.sqlite")
    form = ViewAllEmpAdmin(db)
    form.run()
    db.close()
