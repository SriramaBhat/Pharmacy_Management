import tkinter

LIGHT_GREY = "#F5F5F5"
DEFAULT_COLOR = "light green"
DEFAULT_FONT = ("Arial", 14)
LABEL_DISTANCE = 80
INPUT_DISTANCE = 350


class MedicineForm:
    def __init__(self):
        self.values = []

        self.window = tkinter.Tk()
        self.window.geometry("800x650")
        self.window.title("Add Medicine")
        self.window.resizable(width=False, height=False)
        self.window.configure(background=DEFAULT_COLOR)
        self.v = tkinter.IntVar()

        self.add_title("Medicine Addition Form", 230, 30, ("bold", 20))
        self.add_title("Medicine Name: ", LABEL_DISTANCE, 100, DEFAULT_FONT)
        self.name = self.add_input(INPUT_DISTANCE, 100)
        r1 = tkinter.Radiobutton(self.window, text="Tablet", variable=self.v, value=2,
                                 font=("Arial", 14), background=DEFAULT_COLOR)
        r1.pack(side=tkinter.RIGHT, anchor=tkinter.W)
        r1.place(x=250, y=150)
        r2 = tkinter.Radiobutton(self.window, text="Syrup", variable=self.v, value=1,
                                 font=("Arial", 14), background=DEFAULT_COLOR)
        r2.pack(side=tkinter.RIGHT, anchor=tkinter.W)
        r2.place(x=450, y=150)
        self.add_title("Composition: ", LABEL_DISTANCE, 210, DEFAULT_FONT)
        self.composition = self.add_text_input(3, 42, INPUT_DISTANCE, 200)
        self.add_title("Symptoms: ", LABEL_DISTANCE, 285, DEFAULT_FONT)
        self.symptoms = self.add_text_input(3, 42, INPUT_DISTANCE, 275)
        self.add_title("Side Effects: ", LABEL_DISTANCE, 375, DEFAULT_FONT)
        self.side_effects = self.add_text_input(3, 42, INPUT_DISTANCE, 350)
        self.add_title("Customer Unit Price: ", LABEL_DISTANCE, 425, DEFAULT_FONT)
        self.c_unit_price = self.add_input(INPUT_DISTANCE, 425)
        self.add_title("Distributor Unit Price: ", LABEL_DISTANCE, 475, DEFAULT_FONT)
        self.d_unit_price = self.add_input(INPUT_DISTANCE, 475)

        self.button1 = self.add_button("Submit", 200, 525)
        self.button2 = self.add_button("Logout", 300, 575)
        self.button3 = self.add_button("Transcations", 450, 525)

    def add_title(self, message, x_pos, y_pos, fonts):
        title = tkinter.Label(self.window, text=message, font=fonts, justify=tkinter.CENTER, background=DEFAULT_COLOR)
        title.place(x=x_pos, y=y_pos)
        return title

    def add_input(self, x_pos, y_pos):
        entry = tkinter.Entry(self.window, width=55)
        entry.place(x=x_pos, y=y_pos)
        return entry

    def add_text_input(self, height, width, x_pos, y_pos):
        txt = tkinter.Text(self.window, height=height, width=width)
        txt.place(x=x_pos, y=y_pos)
        return txt

    def add_button(self, btn_text, x_pos, y_pos):
        button = tkinter.Button(self.window, text=btn_text, width=20, bg="black", fg='white', font=("arial", 13))
        button.place(x=x_pos, y=y_pos)
        return button

    def print_input(self):
        print(self.name.get().strip())
        print(self.composition.get("1.0", "end-1c"))
        print(self.symptoms.get("1.0", "end-1c"))
        print(self.side_effects.get("1.0", "end-1c"))

    def run(self):
        self.window.mainloop()

    def destruct(self):
        self.window.destroy()


if __name__ == "__main__":
    form = MedicineForm()
    form.run()
