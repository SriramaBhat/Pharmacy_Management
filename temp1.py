
from tkinter import *
from tkinter import messagebox as tmsg
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector


class login:
    def _init_(self) -> None:
        self.root = Tk()
        self.Name = StringVar()
        self.pas = StringVar()

    def loginfo(self):
        self.nam = self.Name.get()
        self.passs = self.pas.get()
        if self.nam.strip() == '' or self.passs.strip() == '':
            tmsg.showerror("Error", "Cannot leave empty")

        else:
            count = 0
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='created')
            cur = conn.cursor()
            cur.execute("select*from createdinfo")
            res = cur.fetchall()
            for x in res:
                if x[0] == self.nam and x[2] == self.passs:
                    count += 1
                    if count == 1:
                        tmsg.showinfo("success", "Login successful")
                        conn = mysql.connector.connect(host='localhost', user='root', password='', database='created')
                        cur = conn.cursor()
                        cur.execute("insert into loginpage values('%s','%s')" % (self.nam, self.passs))
                        conn.commit()
                        self.root.destroy()
                        logo().main()
                        break

            else:
                tmsg.showerror("error", "Invalid username or Password")

    def main(self):
        root = self.root
        root.geometry("600x500")
        root.maxsize(600, 500)
        root.minsize(600, 500)
        Label(root, text="Employee Login", font=("arial 29"), pady=50).pack()
        f = Frame(root, width=400, height=300, relief=SUNKEN, border=15, bg='orange').place(x=100, y=100)
        Label(root, text="Name", font=("arial 20"), bg='orange').place(x=150, y=150)

        Label(root, text="Password", font=("arial 20"), bg='orange').place(x=150, y=200)
        Button(root, text="Login", font=("arial 15"), width=10, command=self.loginfo, bg='black', fg='white').place(
            x=180, y=270)
        Button(root, text="Create", width=10, font=("arial 15"), command=self.nextpage, bg='black', fg='white').place(
            x=320, y=270)
        Entry(root, textvariable=self.Name, width=30, relief=SUNKEN, border=5).place(x=280, y=155)

        Entry(root, textvariable=self.pas, width=30, relief=SUNKEN, border=5, show='*').place(x=280, y=205)
        root.mainloop()

    def nextpage(self):
        self.root.destroy()
        create().main()


class logo:
    def _init_(self) -> None:
        self.root = Tk()
        self.refno = StringVar()
        self.comname = StringVar()
        self.type = StringVar()
        self.medname = StringVar()
        self.lotno = ''
        self.issuedate = StringVar()
        self.expda = StringVar()
        self.uses = StringVar()
        self.sideffec = StringVar()
        self.prewar = StringVar()
        self.dosage = StringVar()
        self.tabletpric = StringVar()
        self.quant = StringVar()
        self.patient = StringVar()
        self.phoneno = StringVar()

    def stkk(self):
        self.root.destroy()
        fuck().main()

    def main(self):
        root = self.root
        root.geometry("1500x600")

        # def senn(self):
        #     self.msg=self.e.get()
        #     self.txt.insert(END,"\n"+self.msg)

        root.title("Pharmacy Management System")
        ibtitle = Label(root, text="Pharmacy Management System", bd=15, bg='white', fg='darkgreen',
                        font=("arial 30")).pack(side=TOP, fill=X)
        f1 = Frame(root, width=1450, height=500, bd=15, relief=RIDGE).pack(padx=20, pady=10)
        f2 = LabelFrame(f1, bd=15, text="Medicine form", width=890, height=450, padx=10, pady=30, fg='red').place(x=50,
                                                                                                                  y=120)
        self.ref = Label(f2, text="Reference_no").place(x=70, y=150)
        refff = Entry(f2, textvariable=self.refno, font=("arial", 9, "bold"), width=32, relief=SUNKEN, bd=1).place(
            x=180, y=150)
        f3 = Label(f2, text="Company Name", pady=10).place(x=70, y=170)
        self.comname = Entry(f2, textvariable=self.comname, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                             bd=1).place(x=180, y=180)

        f4 = Label(f2, text="Medicine Name", pady=10).place(x=70, y=200)
        self.mednam = Entry(f2, textvariable=self.medname, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                            bd=1).place(x=180, y=210)

        f5 = Label(f2, text="Lot_no", pady=10).place(x=70, y=230)
        self.lott = Entry(f2, textvariable=self.lotno, font=("arial", 9, "bold"), width=32, relief=SUNKEN, bd=1).place(
            x=180, y=240)

        f6 = Label(f2, text="Issue date", pady=10).place(x=70, y=260)
        self.issdat = Entry(f2, textvariable=self.issuedate, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                            bd=1).place(x=180, y=270)

        f7 = Label(f2, text="Exp date", pady=10).place(x=70, y=290)
        self.exdat = Entry(f2, textvariable=self.expda, font=("arial", 9, "bold"), width=32, relief=SUNKEN, bd=1).place(
            x=180, y=300)

        f8 = Label(f2, text="Uses", pady=10).place(x=70, y=320)
        self.use = Entry(f2, textvariable=self.uses, font=("arial", 9, "bold"), width=32, relief=SUNKEN, bd=1).place(
            x=180, y=330)

        f9 = Label(f2, text="Side effect", pady=10).place(x=70, y=350)
        self.sidd = Entry(f2, textvariable=self.sideffec, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                          bd=1).place(x=180, y=360)

        f10 = Label(f2, text="Prec&warning", pady=10).place(x=70, y=380)
        self.precc = Entry(f2, textvariable=self.prewar, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                           bd=1).place(x=180, y=390)

        f11 = Label(f2, text="Dosage", pady=10).place(x=70, y=410)
        self.dosss = Entry(f2, textvariable=self.dosage, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                           bd=1).place(x=180, y=420)

        f12 = Label(f2, text="Patient Name", pady=10).place(x=70, y=440)
        self.pat = Entry(f2, textvariable=self.patient, font=("arial", 9, "bold"), width=32, relief=SUNKEN, bd=1).place(
            x=180, y=450)

        f13 = Label(f2, text="Phone no", pady=10).place(x=70, y=470)
        self.ephonn = Entry(f2, textvariable=self.phoneno, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                            bd=1).place(x=180, y=480)

        f14 = Label(f2, text="Tablet price", pady=10).place(x=500, y=135)
        self.tabpri = Entry(f2, textvariable=self.tabletpric, width=42, relief=SUNKEN).place(x=600, y=145)

        f15 = Label(f2, text="Quantity", pady=10).place(x=500, y=165)
        self.qua = Entry(f2, textvariable=self.quant, width=42, relief=SUNKEN).place(x=600, y=175)

        self.b3 = Button(f2, text="Submit", bg="red", fg='white', width=20, command=self.valll).place(x=70, y=520)
        self.yy = Button(f2, text="Stock", bg="red", fg='white', width=20, command=self.stkk).place(x=250, y=520)
        self.img = Image.open(r"C:\Users\user\Downloads\flask\phr.jpg")
        self.img = self.img.resize((420, 280), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(self.img)
        self.b1 = Button(root, image=self.photoimg, borderwidth=0, relief=RIDGE, border=5)
        self.b1.place(x=480, y=220)
        # tree=ttk.Treeview(root)
        # tree['columns']=('Brand Name','Generic Name','Your price','Savings','Quantity','Dose')
        # tree.column("Brand Name",width=200,anchor='center')
        # tree.column("Generic Name",width=200,anchor='center')
        # tree.column("Your price",width=200,anchor='center')
        # tree.column("Savings",width=200,anchor="center")
        # tree.column("Quantity",width=200,anchor="center")
        # tree.column("Dose",width=200,anchor="center")
        # tree['show']='headings'

        # tree.heading("Brand Name",text="Brand_Name",anchor='center')
        # tree.heading("Generic Name",text="Generic_Name",anchor='center')
        # tree.heading("Your price",text="Price",anchor="center")
        # tree.heading("Savings",text="Saving",anchor="center")
        # tree.heading("Quantity",text="Quantity",anchor="center")
        # tree.heading("Dose",text="Dose",anchor="center")
        # tree.pack()

        root.mainloop()

        # self.txt=Text(root,width=55,height=17,bd=15,relief=RIDGE)
        # self.txt.place(x=970,y=115)
        # self.btn=Button(root,text="send",relief=SUNKEN,border=5)
        # # self.btn.place(x=1180,y=460)
        # self.btn.place(x=1000,y=400)
        # self.e=Entry(root,width=50,relief=SUNKEN,border=5)
        # self.e.place(x=1050,y=430)

    # def stock(self):
    #     self.root.destroy()
    #     stk().main()
    # class stk:
    #     def _init_(self) -> None:
    #         self.root=Tk()

    #     def main(self):
    #         root=self.root
    #         root.mainloop("600x600")
    #         root.mainloop()

    def valll(self):
        self.ref = self.refno.get()
        self.use = self.uses.get()
        self.tabpric = self.tabletpric.get()
        self.quan = self.quant.get()
        self.conn = mysql.connector.connect(host='localhost', database='dondolly', password='', user='root')
        self.cur = self.conn.cursor()
        self.cur.execute("insert into jio values(%s,%s,%s,%s)", (self.ref, self.use, self.tabpric, self.quan))
        self.cur.execute("select*from jio")
        self.conn.commit()

        # root=self.root
        # tree=ttk.Treeview(root)
        # tree['columns']=('reference_no','uses','Tablet_price','Quantity')
        # tree.column("reference_no",width=200,anchor='center')
        # tree.column("sname",width=200,anchor='center')
        # tree.column("uses",width=200,anchor='center')
        # tree.column("Tablet_price",width=200,anchor="center")
        # tree.column("Quantity",width=200,anchor="center")
        # tree['show']='headings'
        # root=self.root
        # tree=ttk.Treeview(root)
        # tree['columns']=('Brand Name','Generic Name','Your price','Savings','Quantity','Dose')
        # tree.column("Brand Name",width=200,anchor='center')
        # tree.column("Generic Name",width=200,anchor='center')
        # tree.column("Your price",width=200,anchor='center')
        # tree.column("Savings",width=200,anchor="center")
        # tree.column("Quantity",width=200,anchor="center")
        # tree.column("Dose",width=200,anchor="center")
        # tree['show']='headings'

        # tree.heading("Brand Name",text="Brand_Name",anchor='center')
        # tree.heading("Generic Name",text="Generic_Name",anchor='center')
        # tree.heading("Your price",text="Price",anchor="center")
        # tree.heading("Savings",text="Saving",anchor="center")
        # tree.heading("Quantity",text="Quantity",anchor="center")
        # tree.heading("Dose",text="Dose",anchor="center")
        # tree.pack()


class create:
    def _init_(self) -> None:
        self.root = Tk()
        self.nam = StringVar()
        self.emai = StringVar()
        self.Pas = StringVar()
        self.phon = StringVar()
        self.gend = StringVar()
        self.Addr = StringVar()
        self.dob = StringVar()

    def checkk(self):
        self.namm = self.nam.get()
        self.email = self.emai.get()
        self.passs = self.Pas.get()
        self.phh = self.phon.get()
        self.gen = self.gend.get()
        self.add = self.Addr.get()
        self.dateof = self.dob.get()
        if self.namm.strip() == '' or self.email.strip() == '' or self.passs.strip() == '' or self.phh.strip() == '' or self.gen.strip() == '' or self.add.strip() == '' or self.dateof.strip() == '' or self.gen.strip() != 'male' or self.gen.strip() == 'female' or self.gen.strip() == 'Male' or self.gen.strip() == 'Female' or len(
                self.phh) < 10:
            tmsg.showerror("error", "cannot leave empty")
        elif "@" not in self.email:
            tmsg.showerror("error", "Invalid Email")
        elif len(self.passs) < 6:
            tmsg.showerror("error", "Password must be greater than 6")

        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='created')
            cur = conn.cursor()
            cur.execute("select*from createdinfo")
            res = cur.fetchall()
            for x in res:
                if x[0] == self.namm:
                    tmsg.showerror("error", "Username already exist")
                    break
            else:
                conn = mysql.connector.connect(host='localhost', user='root', password='', database='created')
                cur = conn.cursor()
                cur.execute("insert into createdinfo values('%s','%s','%s','%s','%s','%s','%s')" % (
                self.namm, self.email, self.passs, self.phh, self.add, self.dateof, self.gen))
                conn.commit()
                tmsg.showinfo("success", "Created  successfully")

    def relog(self):
        self.root.destroy()
        login().main()

    def main(self):
        root = self.root
        root.geometry("800x900")
        # root.maxsize(600,500)
        # root.minsize(600,500)
        Label(root, text="Employee Registration form", font=("arial 29"), pady=30).pack()
        f = Frame(root, width=600, height=600, relief=SUNKEN, border=15, padx=50, bg='lightblue').pack()
        Label(root, text="Name", font=("arial 20"), bg='lightblue').place(x=150, y=150)
        Label(root, text="Email", font=("arial 20"), bg='lightblue').place(x=150, y=200)
        Label(root, text="Password", font=("arial 20"), bg='lightblue').place(x=150, y=250)
        Label(root, text="Phone_no", font=("arial 20"), bg='lightblue').place(x=150, y=300)
        Label(root, text="Gender", font=("arial 20"), bg='lightblue').place(x=150, y=350)
        Label(root, text="Birth Date", font=("arial 20"), bg='lightblue').place(x=150, y=400)
        Label(root, text="Address", font=("arial 20"), bg='lightblue').place(x=150, y=450)

        # Checkbutton(root,text="I agree with the above information provided",font=("arial 10")).place(x=150,y=300)

        Entry(root, textvariable=self.nam, width=35, relief=SUNKEN, border=5).place(x=340, y=155)
        Entry(root, textvariable=self.emai, width=35, relief=SUNKEN, border=5).place(x=340, y=205)
        Entry(root, textvariable=self.Pas, width=35, relief=SUNKEN, border=5, show='*').place(x=340, y=255)
        Entry(root, textvariable=self.phon, width=35, relief=SUNKEN, border=5).place(x=340, y=305)
        Entry(root, textvariable=self.gend, width=35, relief=SUNKEN, border=5).place(x=340, y=355)
        Entry(root, textvariable=self.dob, width=35, relief=SUNKEN, border=5).place(x=340, y=405)
        Entry(root, textvariable=self.Addr, width=35, relief=SUNKEN, border=5).place(x=340, y=455)

        Button(root, text="Create", font=("arial 15"), relief=RIDGE, command=self.checkk, border=5, width=25,
               bg='black', fg='white').place(x=240, y=550)
        Button(root, text="Already have account", width=25, font=("arial 15"), relief=RIDGE, border=5,
               command=self.relog, bg='black', fg='white').place(x=240, y=600)


class fuck:
    def _init_(self) -> None:
        self.root = Tk()

    def retu(self):
        self.root.destroy()
        retuu().main()

    def main(self):
        root = self.root
        root.geometry("900x650")
        root.title("Stocks available")
        tree = ttk.Treeview(root)
        self.s = ttk.Style(root)
        self.s.theme_use("clam")
        self.s.configure(".", font=("Helvetica", 11))
        self.s.configure("Treeview.Heading", foreground='red')
        tree['columns'] = ('Brand Name', 'Generic Name', 'Your price', 'Savings', 'Quantity', 'Dose')
        tree.column("Brand Name", width=150, anchor='center')
        tree.column("Generic Name", width=150, anchor='center')
        tree.column("Your price", width=150, anchor='center')
        tree.column("Savings", width=150, anchor="center")
        tree.column("Quantity", width=150, anchor="center")
        tree.column("Dose", width=150, anchor="center")
        tree['show'] = 'headings'

        tree.heading("Brand Name", text="Brand_Name", anchor='center')
        tree.heading("Generic Name", text="Generic_Name", anchor='center')
        tree.heading("Your price", text="Price", anchor="center")
        tree.heading("Savings", text="Saving", anchor="center")
        tree.heading("Quantity", text="Quantity", anchor="center")
        tree.heading("Dose", text="Dose", anchor="center")
        tree.pack()
        Button(root, text="Back", font=("arial 10"), command=self.retu).pack()

        # Button(root,text="Back",font=("arial 10"),command=self.retu).pack()
        conn = mysql.connector.connect(host='localhost', database='created', password='', user='root')
        cur = conn.cursor()
        # cur.execute("insert into jio values(%s,%s,%s,%s)",(ref,use,tabpric,quan))
        cur.execute("select*from medicine")
        u = cur.fetchall()
        i = 0
        for x in u:
            tree.insert('', i, text="", values=(x[0], x[1], x[2], x[3], x[4], x[5]))

        root.mainloop()


class retuu:
    def _init_(self) -> None:
        self.root = Tk()
        self.refno = StringVar()
        self.comname = StringVar()
        self.type = StringVar()
        self.medname = StringVar()
        self.lotno = ''
        self.issuedate = StringVar()
        self.expda = StringVar()
        self.uses = StringVar()
        self.sideffec = StringVar()
        self.prewar = StringVar()
        self.dosage = StringVar()
        self.tabletpric = StringVar()
        self.quant = StringVar()
        self.patient = StringVar()
        self.phoneno = StringVar()

    def vallll(self):
        self.ref = self.refno.get()
        self.use = self.uses.get()
        self.tabpric = self.tabletpric.get()
        self.quan = self.quant.get()
        self.conn = mysql.connector.connect(host='localhost', database='dondolly', password='', user='root')
        self.cur = self.conn.cursor()
        self.cur.execute("insert into jio values(%s,%s,%s,%s)", (self.ref, self.use, self.tabpric, self.quan))
        self.cur.execute("select*from jio")
        self.conn.commit()

    def stkkk(self):
        self.root.destroy()
        fuck().main()

    def main(self):
        root = self.root
        root.geometry("1500x800")

        # def senn(self):
        #     self.msg=self.e.get()
        #     self.txt.insert(END,"\n"+self.msg)

        root.title("Pharmacy Management System")
        ibtitle = Label(root, text="Pharmacy Management System", bd=15, bg='white', fg='darkgreen',
                        font=("arial 30")).pack(side=TOP, fill=X)
        f1 = Frame(root, width=1450, height=500, bd=15, relief=RIDGE).pack(padx=20, pady=10)
        f2 = LabelFrame(f1, bd=15, text="Medicine form", width=890, height=450, padx=10, pady=30, fg='red').place(x=50,
                                                                                                                  y=120)
        self.ref = Label(f2, text="Reference_no").place(x=70, y=150)
        refff = Entry(f2, textvariable=self.refno, font=("arial", 9, "bold"), width=32, relief=SUNKEN, bd=1).place(
            x=180, y=150)
        f3 = Label(f2, text="Company Name", pady=10).place(x=70, y=170)
        self.comname = Entry(f2, textvariable=self.comname, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                             bd=1).place(x=180, y=180)

        f4 = Label(f2, text="Medicine Name", pady=10).place(x=70, y=200)
        self.mednam = Entry(f2, textvariable=self.medname, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                            bd=1).place(x=180, y=210)

        f5 = Label(f2, text="Lot_no", pady=10).place(x=70, y=230)
        self.lott = Entry(f2, textvariable=self.lotno, font=("arial", 9, "bold"), width=32, relief=SUNKEN, bd=1).place(
            x=180, y=240)

        f6 = Label(f2, text="Issue date", pady=10).place(x=70, y=260)
        self.issdat = Entry(f2, textvariable=self.issuedate, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                            bd=1).place(x=180, y=270)

        f7 = Label(f2, text="Exp date", pady=10).place(x=70, y=290)
        self.exdat = Entry(f2, textvariable=self.expda, font=("arial", 9, "bold"), width=32, relief=SUNKEN, bd=1).place(
            x=180, y=300)

        f8 = Label(f2, text="Uses", pady=10).place(x=70, y=320)
        self.use = Entry(f2, textvariable=self.uses, font=("arial", 9, "bold"), width=32, relief=SUNKEN, bd=1).place(
            x=180, y=330)

        f9 = Label(f2, text="Side effect", pady=10).place(x=70, y=350)
        self.sidd = Entry(f2, textvariable=self.sideffec, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                          bd=1).place(x=180, y=360)

        f10 = Label(f2, text="Prec&warning", pady=10).place(x=70, y=380)
        self.precc = Entry(f2, textvariable=self.prewar, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                           bd=1).place(x=180, y=390)

        f11 = Label(f2, text="Dosage", pady=10).place(x=70, y=410)
        self.dosss = Entry(f2, textvariable=self.dosage, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                           bd=1).place(x=180, y=420)

        f12 = Label(f2, text="Patient Name", pady=10).place(x=70, y=440)
        self.pat = Entry(f2, textvariable=self.patient, font=("arial", 9, "bold"), width=32, relief=SUNKEN, bd=1).place(
            x=180, y=450)

        f13 = Label(f2, text="Phone no", pady=10).place(x=70, y=470)
        self.ephonn = Entry(f2, textvariable=self.phoneno, font=("arial", 9, "bold"), width=32, relief=SUNKEN,
                            bd=1).place(x=180, y=480)

        f14 = Label(f2, text="Tablet price", pady=10).place(x=500, y=135)
        self.tabpri = Entry(f2, textvariable=self.tabletpric, width=42, relief=SUNKEN).place(x=600, y=145)

        f15 = Label(f2, text="Quantity", pady=10).place(x=500, y=165)
        self.qua = Entry(f2, textvariable=self.quant, width=42, relief=SUNKEN).place(x=600, y=175)

        self.b3 = Button(f2, text="Submit", bg="red", fg='white', width=20, command=self.vallll).place(x=70, y=520)
        self.yy = Button(f2, text="Stock", bg="red", fg='white', width=20, command=self.stkkk).place(x=250, y=520)
        self.img = Image.open(r"C:\Users\user\Downloads\flask\phr.jpg")
        self.img = self.img.resize((420, 280), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(self.img)
        self.b1 = Button(root, image=self.photoimg, borderwidth=0, relief=RIDGE, border=5)
        self.b1.place(x=480, y=220)

        root.mainloop()


log = login()
log.main()
