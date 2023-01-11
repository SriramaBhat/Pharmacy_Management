import tkinter
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
import sqlite3


LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 150
INPUT_DISTANCE = 250


class AdminBill:
    def __init__(self, conn):
        self.window = tkinter.Tk()
        self.window.title("View Transactions")
        self.window.geometry("650x600")
        self.window.resizable(height=False, width=False)
        self.window.configure(background=DEFAULT_COLOR)
        self.tree = ""
        self.file_name = ""
        self.conn = conn

        self.title = self.add_title("Bill Summary", 250, 50, ("bold", 20))
        self.add_title("Transaction id: ", 50, 100, DEFAULT_FONT)
        self.tran_id = self.add_input(200, 105)
        self.button1 = self.add_button("Transactions", 450, 540)
        self.button2 = self.add_button("Logout", 250, 540)
        self.button3 = self.add_button("Generate", 50, 540)
        self.button3.configure(command=self.generate)

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
        stock_tree = ttk.Treeview(self.window, columns=("c1", "c2", "c3", "c4", "c5"), show="headings",
                                  height=height, selectmode="browse")
        stock_tree.column("#1", anchor=tkinter.CENTER, stretch=tkinter.NO, width=50)
        stock_tree.heading("#1", text="Sl no.")
        stock_tree.column("#2", anchor=tkinter.CENTER, stretch=tkinter.NO, width=200)
        stock_tree.heading("#2", text="Medicine Name")
        stock_tree.column("#3", anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
        stock_tree.heading("#3", text="Quantity")
        stock_tree.column("#4", anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
        stock_tree.heading("#4", text="Unit Price")
        stock_tree.column("#5", anchor=tkinter.CENTER, stretch=tkinter.NO, width=100)
        stock_tree.heading("#5", text="Price")

        if self.tran_id.get().strip() == "":
            messagebox.showerror("Error", "Enter the transaction id")
        else:
            cur = self.conn.cursor()
            res = cur.execute("SELECT * FROM " + str(self.tran_id.get().strip()) + ";").fetchall()
            self.file_name = self.tran_id.get().strip()

            for i in range(1, len(res)+1):
                stock_tree.insert("", "end", text=str(i), values=res[i-1])

            if self.tran_id.get().strip()[0] == "c":
                total = cur.execute("SELECT total_amt FROM ctransactions WHERE ctrans_name='" +
                                    str(self.tran_id.get().strip()) + "';").fetchone()
                stock_tree.insert("", "end", text=str(len(res)+1), values=["", "", "", "", ""])
                stock_tree.insert("", "end", text=str(len(res)+2), values=["", "Total", "", "", total])
            else:
                total = cur.execute("SELECT total_amt FROM stransactions WHERE strans_name='" +
                                    str(self.tran_id.get().strip()) + "';").fetchone()
                stock_tree.insert("", "end", text=str(len(res)+1), values=["", "", "", "", ""])
                stock_tree.insert("", "end", text=str(len(res)+2), values=["", "Total", "", "", total])

        return stock_tree

    def generate_invoice(self):
        c = canvas.Canvas(self.file_name + ".pdf", pagesize=(200, 250), bottomup=0)
        c.setFillColor("green")
        c.line(70, 22, 180, 22)
        c.line(5, 45, 195, 45)
        c.line(15, 120, 185, 120)
        c.line(35, 108, 35, 220)
        c.line(115, 108, 115, 220)
        c.line(135, 108, 135, 220)
        c.line(160, 108, 160, 220)
        c.line(15, 220, 185, 220)
        c.translate(10, 40)
        c.scale(1, -1)
        c.drawImage("F:\\Programs\\DBMS_Project\\rod_of_ascelipius.jpg", 0, 0, width=50, height=30)
        c.scale(1, -1)
        c.translate(-10, -40)
        c.setFont("Times-Bold", 10)
        c.drawCentredString(125, 20, "Pharmacy")
        c.setFont("Times-Bold", 8)
        c.drawCentredString(90, 55, "INVOICE")
        c.setFont("Times-Bold", 5)
        c.drawRightString(90, 70, "Bill Id: " + self.file_name)
        c.drawRightString(40, 80, "Date :")
        cur = self.conn.cursor()
        date = cur.execute("SELECT tran_date FROM ctransactions WHERE ctrans_name='" + str(self.file_name)
                           + "' UNION SELECT tran_date FROM stransactions WHERE strans_name='" +
                           str(self.file_name) + "';").fetchone()
        date = date[0].split("-")
        c.drawRightString(65, 80, date[2] + "/" + date[1] + "/" + date[0])
        if self.file_name[0] == "c":
            c.drawRightString(65, 90, "Customer Name :")
            cname = cur.execute("SELECT cust_name, cust_email FROM customers WHERE cust_id=(SELECT cid FROM " +
                                " ctransactions WHERE ctrans_name='" + str(self.file_name) + "');").fetchone()
            c.drawRightString(80, 90, cname[0])
            c.drawRightString(40, 100, "Email:")
            c.drawRightString(80, 100, cname[1])
        else:
            c.drawRightString(60, 90, "Supplier Name :")
            sname = cur.execute("SELECT dist_name, dist_email FROM distributors WHERE dist_id=(SELECT sid FROM " +
                                " stransactions WHERE strans_name='" + str(self.file_name) + "');").fetchone()
            c.drawRightString(120, 90, sname[0])
            c.drawRightString(40, 100, "Email:")
            c.drawRightString(100, 100, sname[1])
        c.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
        c.drawCentredString(25, 118, "S.No.")
        c.drawCentredString(75, 118, "Medicine")
        c.drawCentredString(125, 118, "Price")
        c.drawCentredString(148, 118, "Qty.")
        c.drawCentredString(173, 118, "Total")
        res = cur.execute("SELECT * FROM " + str(self.tran_id.get().strip()) + ";").fetchall()
        place = 130
        for i in res:
            c.drawCentredString(25, place, str(i[0]))
            c.drawCentredString(75, place, str(i[1]))
            c.drawCentredString(125, place, str(round(i[2], 2)))
            c.drawCentredString(148, place, str(i[3]))
            c.drawCentredString(173, place, str(round(i[4], 2)))
            place += 10
        if self.tran_id.get().strip()[0] == "c":
            total = cur.execute("SELECT total_amt FROM ctransactions WHERE ctrans_name='" +
                                str(self.tran_id.get().strip()) + "';").fetchone()
        else:
            total = cur.execute("SELECT total_amt FROM stransactions WHERE strans_name='" +
                                str(self.tran_id.get().strip()) + "';").fetchone()
        c.drawCentredString(100, 230, "Total")
        c.drawCentredString(173, 230, str(round(total[0], 2)))
        c.showPage()
        c.save()

    def generate(self):
        self.add_tree()
        self.generate_invoice()

    def add_tree(self):
        self.tree = self.add_treeview(15)
        self.tree.place(x=50, y=200)

    def run(self):
        self.window.mainloop()

    def destruct(self):
        self.window.destroy()


if __name__ == "__main__":
    db = sqlite3.connect("pharmacy.sqlite")
    form = AdminBill(db)
    form.run()
    db.close()
