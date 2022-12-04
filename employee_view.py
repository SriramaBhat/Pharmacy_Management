import tkinter
import sqlite3
from functools import partial
import Employee_Views.all_employees as all_employees
import Employee_Views.all_admins as all_admins
import Employee_Views.all_admin_employees as all_admin_employees
import Employee_Views.all_nonadmins as all_nonadmins
import main_logic


LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 150
INPUT_DISTANCE = 250


class ViewEmp:
    def __init__(self, conn):
        self.window = tkinter.Tk()
        self.window.title("Employee View Menu")
        self.window.geometry("900x300")
        self.window.resizable(height=False, width=False)
        self.window.configure(background=DEFAULT_COLOR)
        self.conn = conn

        self.title = self.add_title("Employee View Menu", 300, 50, ("bold", 20))
        # self.tree = self.add_treeview(15)
        # self.tree.place(y=100)
        self.button1 = self.add_button("Transactions", 50, 100)
        self.button2 = self.add_button("View All Employee", 250, 100)
        self.button3 = self.add_button("View Admin Employee", 450, 100)
        self.button4 = self.add_button("View Non Admins", 650, 100)
        self.button5 = self.add_button("Logout", 250, 150)
        self.button6 = self.add_button("View Admins", 450, 150)

    def add_title(self, message, x_pos, y_pos, fonts):
        title = tkinter.Label(self.window, text=message, font=fonts, justify=tkinter.CENTER, background=DEFAULT_COLOR)
        title.place(x=x_pos, y=y_pos)
        return title

    def add_button(self, btn_text, x_pos, y_pos):
        button = tkinter.Button(self.window, text=btn_text, width=20, bg="black", fg='white', font=("arial", 13))
        button.place(x=x_pos, y=y_pos)
        return button

    def run(self):
        self.window.mainloop()

    def destruct(self):
        self.window.destroy()


def view_menu_configure(view_menu):
    view_menu.button1.configure(command=partial(main_logic.admin_trans1, view_menu))
    view_menu.button2.configure(command=partial(view_all, view_menu))
    view_menu.button3.configure(command=partial(view_admin_employees, view_menu))
    view_menu.button4.configure(command=partial(view_non_admins, view_menu))
    view_menu.button5.configure(command=partial(main_logic.logout, view_menu))
    view_menu.button6.configure(command=partial(view_admins, view_menu))


def return_db(view_menu):
    return view_menu.conn


def view_non_admins(view_menu):
    view_menu.destruct()
    all_non_admin_view = all_nonadmins.ViewAllNonAdmin(view_menu.conn)
    all_non_admin_view.button1.configure(command=partial(back_to_menu, all_non_admin_view))
    all_non_admin_view.run()


def view_admin_employees(view_menu):
    view_menu.destruct()
    all_admin_employee = all_admin_employees.ViewAllEmpAdmin(view_menu.conn)
    all_admin_employee.button1.configure(command=partial(back_to_menu, all_admin_employee))
    all_admin_employee.run()


def view_admins(view_menu):
    view_menu.destruct()
    all_admin_view = all_admins.ViewAllAdmin(view_menu.conn)
    all_admin_view.button1.configure(command=partial(back_to_menu, all_admin_view))
    all_admin_view.run()


def back_to_menu(all_view):
    all_view.destruct()
    view_menu = ViewEmp(all_view.conn)
    view_menu_configure(view_menu)
    view_menu.run()


def view_all(view_menu):
    view_menu.destruct()
    all_view = all_employees.ViewAllEmp(view_menu.conn)
    all_view.button1.configure(command=partial(back_to_menu, all_view))
    all_view.run()


if __name__ == "__main__":
    db = sqlite3.connect("pharmacy.sqlite")
    form = ViewEmp(db)
    view_menu_configure(form)
    form.run()
    db.close()
