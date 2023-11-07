import tkinter.messagebox
import sqlite3
from functools import partial
import datetime
import employee_entry
import login_form
import cust_transactions
import dist_transactions
import medicine_form
import admin_addition
import view_trans_between
import emp_delete
import view_stocks
import supp_add
import employee_view
import admin_bill
import employee_bill


def logout(trans):
    trans.destruct()
    log1 = login_form.LoginForm()
    login_configure(log1)
    log1.run()


def login_configure(login):
    login.button1.configure(command=partial(btn_command, login))
    login.button2.configure(command=partial(user_signup, login))


def admin_med_configure(med):
    med.button1.configure(command=partial(med_submit, med))
    med.button2.configure(command=partial(logout, med))
    med.button3.configure(command=partial(admin_trans1, med))


def dist_trans_configure(admin):
    admin.button1.configure(command=partial(dist_tran_submit, admin))
    admin.button2.configure(command=partial(stock_view, admin, "admin", admin.conn))
    admin.button3.configure(command=partial(admin_med_form, admin))
    admin.button4.configure(command=partial(view_employees, admin))
    admin.button5.configure(command=partial(logout, admin))
    admin.button6.configure(command=partial(view_trans_range, admin))
    admin.button7.configure(command=partial(add_admin, admin))
    admin.button8.configure(command=partial(emp_del, admin))
    admin.button9.configure(command=partial(add_dist, admin))
    admin.button11.configure(command=partial(generate_admin_bill, admin))


def cust_trans_configure(employee, dbase):
    employee.button1.configure(command=partial(cust_tran_submit, employee))
    employee.button2.configure(command=partial(stock_view, employee, "employee", dbase))
    employee.button3.configure(command=partial(generate_emp_bill, employee))
    employee.button4.configure(command=partial(logout, employee))


def add_form_configure(admin_add):
    admin_add.button1.configure(command=partial(submit_admin, admin_add))
    admin_add.button2.configure(command=partial(admin_trans1, admin_add))
    admin_add.button3.configure(command=partial(logout, admin_add))


def delete_configure(employee_del):
    employee_del.button1.configure(command=partial(delete_employee, employee_del))
    employee_del.button2.configure(command=partial(admin_trans1, employee_del))
    employee_del.button3.configure(command=partial(logout, employee_del))


def emp_del(admin):
    admin.destruct()
    employee_del = emp_delete.EmpDeletion(admin.conn)
    delete_configure(employee_del)
    employee_del.run()


def admin_trans1(med):
    med.destruct()
    admin = dist_transactions.DistTransactions(med.conn)
    dist_trans_configure(admin)
    admin.run()


def submit_admin(admin_add):
    email = admin_add.email.get().strip()
    cur = db.cursor()
    cur.execute("INSERT INTO admin (aname, aphone, adob, agender, aaddress, aemail, apassword) " +
                "SELECT ename, ephone, edob, egender, eaddress, eemail, epassword FROM " +
                "employee WHERE eemail = '{}';".format(email))
    cur.execute("COMMIT;")
    admin_trans1(admin_add)


def delete_employee(employee_del):
    email = employee_del.email.get().strip()
    cur = db.cursor()
    cur.execute("DELETE FROM employee WHERE eemail = '{}';".format(email))
    cur.execute("COMMIT;")
    admin_trans1(employee_del)


def dist_tran_submit(admin):
    if admin.email.get().strip() == "" or admin.mname.get().strip() == "" or admin.quantity.get().strip() == "" \
            or admin.exp_date.get().strip() == "":
        tkinter.messagebox.showerror("Error", "The fields cannot be empty")
    else:
        dist_email = admin.email.get().strip()
        pr_date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        pr_time = datetime.datetime.now().time().strftime("%H-%M-%S")
        table_name = "d_tran" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        med_names = admin.mname.get().strip().split(", ")
        qty_values = admin.quantity.get().strip().split(", ")
        exp_date_values = admin.exp_date.get().strip().split(", ")
        date_values = []
        for i in exp_date_values:
            i = i.split("/")
            temp = str(i[2]) + "-" + str(i[1]) + "-" + str(i[0])
            date_values.append(temp)
        med_names_values = []
        for i in med_names:
            med_names_values.append(i.split("/"))
        cur = admin.conn.cursor()
        sid = cur.execute("SELECT dist_id FROM distributors WHERE dist_email = '" + dist_email + "';").fetchone()[0]
        if not sid:
            tkinter.messagebox.showerror("Error", "Supplier does not exist")
        else:
            cur.execute("CREATE TABLE  IF NOT EXISTS " + table_name +
                        "(mid INTEGER PRIMARY KEY AUTOINCREMENT, mname VARCHAR(255) NOT NULL, " +
                        "qty INTEGER NOT NULL, upr INTEGER NOT NULL, price INTEGER NOT NULL);")
            for i in range(len(med_names)):
                if med_names_values[i][1].casefold() == "s":
                    stock_id = cur.execute("SELECT sid FROM stocks WHERE syid = (SELECT " +
                                           "mid FROM syrups WHERE mname LIKE '%{}%');".format(med_names_values[i][0]))
                    try:
                        cur.execute("UPDATE stocks SET qty = qty + " + str(qty_values[i]) + ", expdate = '" +
                                    str(date_values[i]) + "' WHERE sid = " + str(stock_id.fetchone()[0]) + " ;")
                        unit_price = cur.execute("SELECT dist_unit_price FROM stocks WHERE syid = (SELECT " +
                                                 "mid FROM syrups WHERE mname LIKE '%" + str(med_names_values[i][0]) +
                                                 "%');").fetchone()[0]
                        cur.execute("INSERT INTO " + table_name + " (mname, qty, upr, price) VALUES " +
                                    "('" + str(med_names_values[i][0]) + "', " + str(qty_values[i]) + ", "
                                    + str(unit_price) + ", " + str(qty_values[i]) +
                                    " * " + str(unit_price) + ");")
                    except Exception:
                        tkinter.messagebox.showerror("Error", "The expiry date cannot be the given value")
                        cur.execute("DROP TABLE " + table_name + ";")
                    cur.execute("COMMIT;")
                else:
                    stock_id = cur.execute("SELECT sid FROM stocks WHERE tid = (SELECT " +
                                           "mid FROM tablets WHERE mname LIKE '%{}%');".format(med_names_values[i][0]))
                    try:
                        cur.execute("UPDATE stocks SET qty = qty + " + str(qty_values[i]) + ", expdate = '" +
                                    str(date_values[i]) + "' WHERE sid = " + str(stock_id.fetchone()[0]) + " ;")
                        unit_price = cur.execute("SELECT dist_unit_price FROM stocks WHERE tid = (SELECT " +
                                                 "mid FROM tablets WHERE mname LIKE '%" +
                                                 str(med_names_values[i][0]) + "%');").fetchone()[0]
                        cur.execute("INSERT INTO " + table_name + " (mname, qty, upr, price) VALUES " +
                                    "('" + str(med_names_values[i][0]) + "', " + str(qty_values[i]) + ", "
                                    + str(unit_price) + ", " + str(qty_values[i]) +
                                    " * " + str(unit_price) + ");")
                    except Exception:
                        tkinter.messagebox.showerror("Error", "The expiry date cannot be the given value")
                        cur.execute("DROP TABLE " + table_name + ";")
                    cur.execute("COMMIT;")
            try:
                total_amt = cur.execute("SELECT SUM(price) FROM " + table_name + ";").fetchone()[0]
                cur.execute("INSERT INTO stransactions (sid, strans_name, tran_date, tran_time, total_amt) VALUES " +
                            "(" + str(sid) + ", '" + table_name + "', '" + pr_date + "', '" + pr_time + "', "
                            + str(total_amt) + ");")
            except:
                cur.execute("COMMIT;")
            admin_trans1(admin)


def add_dist_submit(supp):
    supp_var = [supp.name, supp.phone, supp.email, supp.address]
    if supp_var[0].get().strip() == "" or supp_var[1].get().strip() == "" or supp_var[2].get().strip() == "" \
            or supp_var[3].get().strip() == "":
        tkinter.messagebox.showerror("Error", "The fields cannot be empty")
    else:
        values = []
        for i in supp_var:
            values.append(i.get().strip())
        values = tuple(values)
        cur = db.cursor()
        cur.execute("INSERT INTO distributors (dist_name, dist_phone, dist_email, dist_address) VALUES " +
                    str(values) + ";")
        cur.execute("COMMIT;")
        admin_trans1(supp)


def add_dist(admin):
    admin.destruct()
    supp = supp_add.DistEntry(admin.conn)
    supp.button1.configure(command=partial(add_dist_submit, supp))
    supp.button2.configure(command=partial(logout, supp))
    supp.button3.configure(command=partial(admin_trans1, supp))
    supp.run()


def stock_view(window, emp_type, dbase):
    window.destruct()
    stock_summary = view_stocks.ViewStocks(dbase, emp_type)
    if emp_type == "admin":
        stock_summary.button1.configure(command=partial(admin_trans1, stock_summary))
    else:
        stock_summary.button1.configure(command=partial(emp_trans1, stock_summary))
    stock_summary.button2.configure(command=partial(logout, stock_summary))
    stock_summary.run()


def emp_trans1(stock_summary):
    stock_summary.destruct()
    emp = cust_transactions.CustTransactions(db)
    cust_trans_configure(emp, db)
    emp.run()


def view_employees(admin):
    admin.destruct()
    view_menu = employee_view.ViewEmp(db)
    employee_view.view_menu_configure(view_menu)
    view_menu.run()


def view_trans_range(admin):
    dbase = admin.conn
    admin.destruct()
    trans = view_trans_between.ViewTrans(dbase)
    trans.button1.configure(command=partial(admin_trans1, trans))
    trans.button2.configure(command=partial(logout, trans))
    trans.run()


def add_admin(admin):
    admin.destruct()
    add_admin_form = admin_addition.AdminAddition(admin.conn)
    add_form_configure(add_admin_form)
    add_admin_form.run()


def cust_tran_submit(employee):
    if employee.name.get().strip() == "" or employee.email.get().strip() == "" or employee.mname.get().strip() == "" \
            or employee.quantity.get().strip() == "" or employee.symptoms.get().strip() == "":
        tkinter.messagebox.showerror("Error", "The fields cannot be empty")
    else:
        cust_name = employee.name.get().strip()
        cust_email = employee.email.get().strip()
        cust_symptoms = employee.symptoms.get().strip()
        pr_date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        pr_time = datetime.datetime.now().time().strftime("%H-%M-%S")
        table_name = "c_tran" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        med_names = employee.mname.get().strip().split(", ")
        qty_values = employee.quantity.get().strip().split(", ")
        med_names_values = []
        for i in med_names:
            med_names_values.append(i.split("/"))
        cur = db.cursor()
        cur.execute("INSERT INTO customers (cust_name, cust_email, cust_symptoms) VALUES " +
                    "('" + cust_name + "', '" + cust_email + "', '" + cust_symptoms + "');")
        cid = cur.execute("SELECT cust_id FROM customers WHERE cust_email = '" + cust_email + "';").fetchone()[0]
        cur.execute("CREATE TABLE  IF NOT EXISTS " + table_name +
                    "(mid INTEGER PRIMARY KEY AUTOINCREMENT, mname VARCHAR(255) NOT NULL, " +
                    "qty INTEGER NOT NULL, upr INTEGER NOT NULL, price INTEGER NOT NULL);")
        for i in range(len(med_names)):
            if med_names_values[i][1].casefold() == "s":
                stock_id = cur.execute("SELECT sid FROM stocks WHERE syid = (SELECT " +
                                       "mid FROM syrups WHERE mname LIKE '%{}%');".format(med_names_values[i][0]))
                try:
                    cur.execute("UPDATE stocks SET qty = qty - " + str(qty_values[i]) +
                                " WHERE sid = " + str(stock_id.fetchone()[0]) + " ;")
                    unit_price = cur.execute("SELECT cust_unit_price FROM stocks WHERE syid = (SELECT " +
                                             "mid FROM syrups WHERE mname LIKE '%" + str(med_names_values[i][0]) +
                                             "%');").fetchone()[0]
                    cur.execute("INSERT INTO " + table_name + " (mname, qty, upr, price) VALUES " +
                                "('" + str(med_names_values[i][0]) + "', " + str(qty_values[i]) + ", "
                                + str(unit_price) + ", " + str(qty_values[i]) +
                                " * " + str(unit_price) + ");")
                except Exception:
                    tkinter.messagebox.showerror("Error", "Insufficient stocks")
                    cur.execute("DROP TABLE " + table_name + ";")
                cur.execute("COMMIT;")
            else:
                stock_id = cur.execute("SELECT sid FROM stocks WHERE tid = (SELECT " +
                                       "mid FROM tablets WHERE mname LIKE '%{}%');".format(med_names_values[i][0]))
                try:
                    cur.execute("UPDATE stocks SET qty = qty - " + str(qty_values[i]) +
                                " WHERE sid = " + str(stock_id.fetchone()[0]) + " ;")
                    unit_price = cur.execute("SELECT cust_unit_price FROM stocks WHERE tid = (SELECT " +
                                             "mid FROM tablets WHERE mname LIKE '%" +
                                             str(med_names_values[i][0]) + "%');").fetchone()[0]
                    cur.execute("INSERT INTO " + table_name + " (mname, qty, upr, price) VALUES " +
                                "('" + str(med_names_values[i][0]) + "', " + str(qty_values[i]) + ", "
                                + str(unit_price) + ", " + str(qty_values[i]) +
                                " * " + str(unit_price) + ");")
                except Exception:
                    tkinter.messagebox.showerror("Error", "Insufficient stocks")
                    cur.execute("DROP TABLE " + table_name + ";")
                cur.execute("COMMIT;")
        try:
            total_amt = cur.execute("SELECT SUM(price) FROM " + table_name + ";").fetchone()[0]
            cur.execute("INSERT INTO ctransactions (cid, ctrans_name, tran_date, tran_time, total_amt) VALUES " +
                        "(" + str(cid) + ", '" + table_name + "', '" + pr_date + "', '" + pr_time + "', "
                        + str(total_amt) + ");")
        except Exception:
            cur.execute("COMMIT;")
        emp_trans1(employee)


def med_submit(med):
    if med.name.get().strip() == "" or med.symptoms.get("1.0", "end-1c").strip() == "" or \
            med.composition.get("1.0", "end-1c") == "":
        tkinter.messagebox.showerror("Error", "The fields cannot be empty")
    else:
        med_vars = [med.composition, med.symptoms, med.side_effects]
        values = [med.name.get().strip()]
        for i in med_vars:
            values.append(i.get("1.0", "end-1c").strip())
        med_vars1 = [med.c_unit_price, med.d_unit_price]
        values = tuple(values)
        values1 = []
        choice = 0
        for i in med_vars1:
            values1.append(i.get().strip())
        values1 = tuple(values1)
        cur = db.cursor()
        res = (cur.execute("SELECT * FROM tablets WHERE mname LIKE '%{}%' UNION " +
                           "SELECT * FROM syrups WHERE mname LIKE '%{}%';".format(values[0], values[0])).fetchall())
        if not res and str(med.v.get()) == "1":
            cur.execute("INSERT INTO syrups (mname, composition, symptoms, side_effects) VALUES " + str(values) + ";")
            cur.execute("COMMIT;")
            mid = cur.execute("SELECT mid FROM syrups WHERE mname LIKE '%{}%'".format(values[0])).fetchone()
            choice = 1
        elif not res:
            cur.execute("INSERT INTO tablets (mname, composition, symptoms, side_effects) VALUES " + str(values) + ";")
            cur.execute("COMMIT;")
            mid = cur.execute("SELECT mid FROM tablets WHERE mname LIKE '%{}%'".format(values[0])).fetchone()
        else:
            mid = cur.execute("SELECT * FROM tablets WHERE mname LIKE '%{}%'".format(values[0])).fetchone()
            if not mid:
                mid = cur.execute("SELECT * FROM syrups WHERE mname LIKE '%{}%';".format(values[0])).fetchone()
                choice = 1
        cur_date = datetime.date.today().strftime("%Y-%m-%d")
        if choice == 1:
            cur.execute("INSERT INTO stocks (tid, syid, qty, cust_unit_price, dist_unit_price, expdate) VALUES " +
                        "(NULL, {}, 0, {}, {}, '{}');".format(mid[0], values1[0], values1[1], cur_date))
        else:
            cur.execute("INSERT INTO stocks (tid, syid, qty, cust_unit_price, dist_unit_price, expdate) VALUES " +
                        "({}, NULL, 0, {}, {}, '{}');".format(mid[0], values1[0], values1[1], cur_date))
        cur.execute("COMMIT;")
        admin_med_form(med)


def admin_med_form(admin):
    admin.destruct()
    med = medicine_form.MedicineForm()
    admin_med_configure(med)
    med.run()


def admin_trans(login):
    mail = login.email.get().strip()
    p_word = login.password.get().strip()
    cur = db.cursor()
    res = cur.execute("SELECT apassword FROM admin WHERE aemail=" + '"{}"'.format(mail) + ";").fetchone()
    if not res:
        tkinter.messagebox.showerror("Error", "Invalid email!!")
    elif p_word != res[0]:
        tkinter.messagebox.showerror("Error", "Invalid password!!")
    else:
        login.destruct()
        adm = dist_transactions.DistTransactions(db)
        dist_trans_configure(adm)
        adm.run()


def employee_trans(login):
    mail = login.email.get().strip()
    p_word = login.password.get().strip()
    cur = db.cursor()
    res = cur.execute("SELECT epassword FROM employee WHERE eemail=" + '"{}"'.format(mail) + ";").fetchone()
    if not res:
        tkinter.messagebox.showerror("Error", "Invalid email!!")
    elif p_word != res[0]:
        tkinter.messagebox.showerror("Error", "Invalid password!!")
    else:
        login.destruct()
        emp = cust_transactions.CustTransactions(db)
        cust_trans_configure(emp, db)
        emp.run()


def btn_command(login):
    if login.email.get().strip() == "" or login.password.get().strip() == "":
        tkinter.messagebox.showerror("Error", "The fields should not be empty")
    elif "@" not in login.email.get().strip():
        tkinter.messagebox.showerror("Error", "Invalid Email!!")
    elif str(login.v.get()) == "1":
        login.button1.configure(command=partial(admin_trans, login))
    else:
        login.button1.configure(command=partial(employee_trans, login))


def user_submit(emp):
    emp_vars = [emp.name, emp.phone, emp.dob, emp.gender, emp.address, emp.email, emp.password]
    valid_genders = ["male", "female", "others"]
    for i in emp_vars:
        if i.get().strip() == "":
            tkinter.messagebox.showerror("Error", "The fields should not be empty")
            break
    else:
        if "@" not in emp.email.get():
            tkinter.messagebox.showerror("Error", "Wrong email format!!")
        elif len(emp.password.get()) < 8:
            tkinter.messagebox.showerror("Error", "Password must have minimum 8 characters!!")
        elif emp.password.get() != emp.password1.get():
            tkinter.messagebox.showerror("Error", "The passwords do not match!!")
        elif emp.gender.get().strip().casefold() not in valid_genders:
            tkinter.messagebox.showerror("Error", "Enter a valid gender!!")
        elif len(emp.dob.get().strip().split("/")) != 3:
            tkinter.messagebox.showerror("Error", "Wrong date of birth format!!")
        elif len(emp.dob.get().strip().split("/")[0]) != 2 or len(emp.dob.get().strip().split("/")[1]) != 2 or \
                len(emp.dob.get().strip().split("/")[2]) != 4 or int(emp.dob.get().strip().split("/")[0]) > 31 or \
                int(emp.dob.get().strip().split("/")[1]) > 12:
            tkinter.messagebox.showerror("Error", "Wrong date of birth format!!")
        else:
            values = []
            for i in emp_vars:
                if i == emp.dob:
                    temp_dob = i.get().strip().split("/")
                    temp_dob = str(temp_dob[2]) + "-" + str(temp_dob[1]) + "-" + str(temp_dob[0])
                    values.append(temp_dob)
                    continue
                values.append(i.get().strip())
            values = tuple(values)
            cur = db.cursor()
            cur.execute("INSERT INTO employee (ename, ephone, edob, egender, eaddress, eemail, epassword) VALUES "
                        + str(values) + ";")
            cur.execute("COMMIT;")
            emp.destruct()
            login = login_form.LoginForm()
            login_configure(login)
            login.run()


def back_to_login(emp):
    emp.destruct()
    login = login_form.LoginForm()
    login_configure(login)
    login.run()


def user_signup(login):
    login.destruct()
    emp = employee_entry.EmployeeEntry()
    emp.button1.configure(command=partial(user_submit, emp))
    emp.button2.configure(command=partial(back_to_login, emp))
    emp.run()


def generate_admin_bill(admin):
    admin.destruct()
    bill = admin_bill.AdminBill(db)
    bill.button1.configure(command=partial(admin_trans1, bill))
    bill.button2.configure(command=partial(logout, bill))
    bill.run()


def generate_emp_bill(emp):
    emp.destruct()
    bill = employee_bill.EmployeeBill(db)
    bill.button1.configure(command=partial(emp_trans1, bill))
    bill.button2.configure(command=partial(logout, bill))
    bill.run()


if __name__ == "__main__":
    db = sqlite3.connect("pharmacy.sqlite")
    log = login_form.LoginForm()
    login_configure(log)
    log.run()
    db.close()
