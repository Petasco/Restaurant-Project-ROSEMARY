from tkinter import *
import pymysql
from PIL import Image, ImageTk
import random
import time
from tkinter import filedialog, messagebox
import tkinter as tk

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN & SIGN UP")
        self.root.geometry('1366x700+0+0')
        self.root.resizable(False, False)
        self.loginform()

    def loginform(self):
        LoginFrame = Frame(self.root, bg='white')
        LoginFrame.place(x=0, y=0, height=700, width=1366)
        self.img = ImageTk.PhotoImage(file='en75-hero.jpg')
        img = Label(LoginFrame, image=self.img)
        img.place(x=0, y=0, width=1366, height=700)
        frame_input = Frame(self.root, bg='white')
        frame_input.place(x=320, y=130, height=450, width=350)

        loginlbl = Label(frame_input, text='LOGIN', font=('impact', 30, 'bold'), fg='black', bg='white')
        loginlbl.place(x=120, y=20)
        usernamelbl = Label(frame_input, text='Username', font=('Goudy old style', 18, 'bold'), fg='orangered',
                            bg='white')
        usernamelbl.place(x=30, y=95)
        self.UsernameEntry = Entry(frame_input, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.UsernameEntry.place(x=30, y=145, width=270, height=35)

        Passwwordlbl = Label(frame_input, text='Password', font=('Goudy old style', 18, 'bold'), fg='orangered',
                             bg='white')
        Passwwordlbl.place(x=30, y=195)
        self.password = Entry(frame_input, font=('times new roman', 16, 'bold'), bg='lightgray', show='.')
        self.password.place(x=30, y=245, width=270, height=35)

        def Checkfxn():
            try:
                if CheckBtnVar.get() == 1:
                    self.password.config(show='')
                else:
                    self.password.config(show='.')
            except Exception as es:
                messagebox.askretrycancel('Oops!',f'Error due to {str(es)}! Please try again')

        CheckBtnVar = IntVar()
        self.CheckBtn = Checkbutton(frame_input, text='Show Password', font=('times new roman', 10, 'bold'), bd=0,
                                    bg='white', command=Checkfxn, onvalue=1, offvalue=0, variable=CheckBtnVar)
        self.CheckBtn.place(x=30, y=280)

        loginbtn = Button(frame_input, text='Login', font=('times new roman', 15), command=self.login, cursor='hand2',
                          fg='white', bg='orangered', bd=0, width=15, height=1)
        loginbtn.place(x=90, y=340)

        btn1 = Button(frame_input, text='Forget Password?', cursor='hand2', font=('calibri', 10), bg='white',
                      fg='black', bd=0)
        btn1.place(x=125, y=305)

        signupbtn = Button(frame_input, text='New Here? Sign Up', command=self.Register, font=('calibri', 10),
                           bg='white', fg='black', bd=0, cursor='hand2')
        signupbtn.place(x=110, y=390)

    def login(self):
        if self.UsernameEntry.get() == "" or self.password.get() == "":
            messagebox.showerror("Error!", "All fields Required!", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Rock1844', database='python')
                cur = con.cursor()
                username = self.UsernameEntry.get()
                password = self.password.get()
                sql = "select * from register where username = %s and password =%s"
                cur.execute(sql, [(username), (password)])
                results = cur.fetchall()

                if results:
                    messagebox.showinfo('Success', 'Login Successful')
                    self.managementSystem()
                    con.close()
                else:
                    messagebox.showerror('Error', 'Incorrect Password or Username')

            except Exception as es:
                messagebox.showerror('Error', f'Error due to : {str(es)}', parent=self.root)

    def Register(self):

        Frame_login1 = Frame(self.root, bg='white')
        Frame_login1.place(x=0, y=0, height=700, width=1366)

        self.img = ImageTk.PhotoImage(file='en75-hero.jpg')
        Label(Frame_login1, image=self.img).place(x=0, y=0, height=700, width=1366)

        frame_input2 = Frame(self.root, bg='white')
        frame_input2.place(x=320, y=130, height=450, width=630)

        label1 = Label(frame_input2, text='Register Here', font=('impact', 32, 'bold'), fg='black', bg='white')
        label1.place(x=180, y=20)

        Usernamelabel2 = Label(frame_input2, text='Useranme', font=('Goudy old style', 20, 'bold'), fg='orangered',
                               bg='white')
        Usernamelabel2.place(x=30, y=95)
        self.UsernameEntry = Entry(frame_input2, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.UsernameEntry.place(x=30, y=145, width=270, height=35)

        Passwordlabel3 = Label(frame_input2, text='Email', font=('Goudy old style', 20, 'bold'), fg='orangered',
                               bg='white')
        Passwordlabel3.place(x=30, y=195)
        self.PasswordEntry2 = Entry(frame_input2, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.PasswordEntry2.place(x=30, y=245, width=270, height=35)

        label4 = Label(frame_input2, text='Password', font=('Goudy old style', 20, 'bold'), fg='orangered', bg='white')
        label4.place(x=330, y=95)
        self.entry3 = Entry(frame_input2, font=('times new roman', 15, 'bold'), bg='lightgray', show='*')
        self.entry3.place(x=330, y=145, width=270, height=35)

        label5 = Label(frame_input2, text='Confirm Password', font=('Goudy old style', 20, 'bold'), fg='orangered',
                       bg='white')
        label5.place(x=330, y=195)
        self.entry4 = Entry(frame_input2, font=('times new roman', 15, 'bold'), bg='lightgray', show='*')
        self.entry4.place(x=330, y=245, width=270, height=35)

        def ReShow_Password():
            try:

                if checkvar.get() == 1:
                    self.entry3.config(show='')
                    self.entry4.config(show='')
                else:
                    self.entry4.config(show='.')
                    self.entry3.config(show='.')
            except Exception as es:
                messagebox.askretrycancel('Oops!',f'Error due to {str(es)}! Please try again')

        checkvar = IntVar()
        checkbtn = Checkbutton(frame_input2, font=('times new roman', 10, 'bold'), text='Show Password',
                               command=ReShow_Password, onvalue=1, offvalue=0, variable=checkvar, bd=0, bg='white')
        checkbtn.place(x=330, y=280)

        SignUpbtn2 = Button(frame_input2, command=self.register, text='Sign Up', cursor='hand2',
                            font=('times new roman', 15), fg='white', bg='orangered',
                            bd=0, width=15, height=1)
        SignUpbtn2.place(x=250, y=340)

        btn3 = Button(frame_input2, command=self.loginform, cursor='hand2', font=('calibri', 10),
                      text='Already Register? Login', fg='black', bg='white', bd=0)
        btn3.place(x=260, y=390)

    def register(self):
        if self.UsernameEntry.get() == '' or self.PasswordEntry2.get() == '' or self.entry3.get() == '' or self.entry4.get() == '':
            messagebox.showerror("Error", 'All fields required!', parent=self.root)
        elif self.entry3.get() != self.entry4.get():
            messagebox.showerror("Error", "Passwords Mismatch!", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Rock1844', database='python')
                cur = con.cursor()
                cur.execute('select * from Register where email=%s', self.entry3.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", 'User already exist! Please try with different email')
                else:
                    cur.execute('insert into Register values(%s,%s,%s,%s)', (
                        self.UsernameEntry.get(), self.PasswordEntry2.get(), self.entry3.get(), self.entry4.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success!", 'Registration Successful', parent=self.root)
                    self.managementSystem()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    def managementSystem(self):
        try:
            petasco = Tk()
            petasco.geometry('1350x690+0+0')
            petasco.config(bg='DarkOrange')
            petasco.title('PETASCO RESTAURANT')

            TopFrame = Frame(petasco, bd=10, relief=RAISED)
            TopFrame.pack(side=TOP)

            Title_lbl = Label(TopFrame, text='RESTAURANT MANAGEMENT SYSTEM', font=('arial', 30, 'bold'), bg='Orange',
                              fg='Blue',
                              width=55)
            Title_lbl.grid(row=0, column=0)

            menuFrame = Frame(petasco, bd=5, relief=RIDGE)
            menuFrame.pack(side=LEFT)

            cost_ServiceFrame = Frame(menuFrame, bd=0, relief=RIDGE)
            cost_ServiceFrame.pack(side=BOTTOM)
            ordersFrame = LabelFrame(cost_ServiceFrame, bd=3, text='Orders', font=('times', 16, 'bold italic'),
                                     relief=RIDGE, pady=5)
            ordersFrame.pack(side=LEFT)
            costFrame = Frame(cost_ServiceFrame, bd=4, relief=RIDGE, pady=2)
            costFrame.pack(side=LEFT)
            servicesFrame = LabelFrame(cost_ServiceFrame, bd=3, text='Services', font=('times', 16, 'bold italic'),
                                       relief=RIDGE, pady=10)
            servicesFrame.pack(side=LEFT)

            totalbtnFrame = Frame(cost_ServiceFrame, bd=0, relief=RAISED)
            totalbtnFrame.pack(side=TOP)

            foodFrame = LabelFrame(menuFrame, text='Food', font=('times', 20, "bold italic"), bd=10, relief=RIDGE)
            foodFrame.pack(side=LEFT)

            drinkFrame = LabelFrame(menuFrame, text='Drinks', font=('times', 20, 'bold italic'), bd=10, relief=RIDGE)
            drinkFrame.pack(side=LEFT)

            cakesFrame = LabelFrame(menuFrame, text='Cakes', font=('times', 20, 'bold italic'), bd=10, relief=RIDGE)
            cakesFrame.pack(side=LEFT)

            rightSide = Frame(petasco, bd=15, relief=RIDGE)
            rightSide.pack()

            calFrame = Frame(rightSide, bd=2, relief=RIDGE)
            calFrame.pack(side=TOP)

            receiptFrame = LabelFrame(rightSide, bd=5, text='Receipt', font=('arial', 15, 'bold italic'), relief=RIDGE)
            receiptFrame.pack()

            BtnFrame = Frame(rightSide, bd=4, relief=RIDGE)
            BtnFrame.pack()

            def send():
                # os.system('KFC.py')
                messagebox.showinfo('Wait', 'Coming soon!!!!')

            def reset():
                messagebox.showinfo('Wait', 'Coming soon!!!!')

            def save():
                url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
                bill_data = txtReceipt.get(1.0, END)
                url.write(bill_data)
                url.close()
                messagebox.showinfo('Info', 'Data Saved Succefully')

            # ======================================= Buttons Functions ====================================================
            def total_cost():
                global sum, priceofFood, priceofDrinks, priceofCakes, elavy, Total
                try:
                    fufu = int(txtfufu.get())
                    frice = int(txtfrice.get())
                    waakye = int(txtwaakye.get())
                    jollof = int(txtjollof.get())
                    konkonte = int(txtkonkonte.get())
                    banku = int(txtbanku.get())
                    gob3 = int(txtgob3.get())
                    kelewele = int(txtkelewele.get())
                    riceball = int(txtriceball.get())
                    kenkey = int(txtkenkey.get())
                    yaw = int(txtyaw.get())
                    # ==========================================Drinks ==============================================
                    cock = int(txtcock.get())
                    coke = int(txtcoke.get())
                    pepsi = int(txtpepsi.get())
                    orange = int(txtorange.get())
                    don = int(txtdon.get())
                    pineaple = int(txtpineaple.get())
                    beet = int(txtbeet.get())
                    tampico = int(txttampico.get())
                    apple = int(txtapple.get())
                    redwine = int(txtredwine.get())
                    lemon = int(txtlemon.get())
                    # ==========================================Cakes ==============================================
                    cheese = int(txtcheese.get())
                    ice = int(txtice.get())
                    pizzza = int(txtpizzza.get())
                    choco = int(txtchoco.get())
                    vanilla = int(txtvanilla.get())
                    sponge = int(txtsponge.get())
                    banana = int(txtbanana.get())
                    red = int(txtred.get())
                    black = int(txtblack.get())
                    oreo = int(txtoreo.get())
                    blue = int(txtblue.get())

                    # ===================== Buttons ==================================

                    priceofFood = float(
                        (fufu * 15) + (frice * 20) + (waakye * 15) + (jollof * 20) + (konkonte * 10) + (banku * 10) + (
                                gob3 * 15) + (kelewele * 10) + (kenkey * 10) + (yaw * 10) + (riceball * 10))

                    priceofDrinks = float(
                        (cock * 25) + (coke * 20) + (pepsi * 10) + (orange * 20) + (don * 30) + (pineaple * 25) + (
                                beet * 35) + (tampico * 10) + (redwine * 50) + (apple * 25) + (lemon * 20))

                    priceofCakes = float(
                        (cheese * 30) + (ice * 50) + (pizzza * 40) + (choco * 25) + (vanilla * 35) + (sponge * 45) + (
                                banana * 30) + (red * 35) + (oreo * 30) + (blue * 40) + (black * 45))
                    sum = float(priceofCakes + priceofDrinks + priceofFood)

                    if priceofCakes == 0 and priceofFood == 0 and priceofDrinks == 0:
                        messagebox.showerror("Order", 'Please make an order !!!')
                    else:
                        elavy = (sum * 0.01).__round__(2)
                        Total = sum - elavy
                        foodcost.set('Ghc ' + str(priceofFood) + '0')
                        drinkcost.set('Ghc ' + str(priceofDrinks) + '0')
                        cakescost.set('Ghc ' + str(priceofCakes) + '0')
                        subtotal.set('Ghc ' + str(sum) + '0')
                        tax.set('Ghc ' + str(elavy))
                        total.set('Ghc ' + str(Total))
                except Exception as es:
                    messagebox.showwarning("Error", f'Error due to {str(es)}!\nPlease Enter Only Integers!!!')

            def Receipt():
                global total, foodcost, drinkcost, cakescost
                if total.get() == 0:
                    messagebox.showerror('No Order', 'Please make an order to get a receipt!\n Thank You !!!')
                try:
                    txtReceipt.delete(1.0, END)
                    x = random.randint(1000, 100000)
                    billnumber = 'Bill : ' + str(x)
                    date = time.strftime('%d/%m/%Y')
                    txtReceipt.insert(END, 'Receipt Ref : \t\t' + billnumber + '\t\t' + date + '\n')
                    txtReceipt.insert(END, '*********************************************\n')
                    txtReceipt.insert(END, 'Items:\t\tCost (Ghc)\n')
                    if foodcost.get() >= '1':
                        txtReceipt.insert(END,
                                          '-------------------------------- Food -------------------------------\n')
                    if txtfufu.get() != '0':
                        txtReceipt.insert(END, f'Fufu\t\t\t{int(txtfufu.get()) * 15}\n')
                    if txtfrice.get() != '0':
                        txtReceipt.insert(END, f'Fried Rice\t\t\t{int(txtfrice.get()) * 20}\n')
                    if txtwaakye.get() != '0':
                        txtReceipt.insert(END, f'Waakye\t\t\t{int(txtwaakye.get()) * 15}\n')
                    if txtjollof.get() != '0':
                        txtReceipt.insert(END, f'Jollof\t\t\t{int(txtjollof.get()) * 20}\n')
                    if txtkonkonte.get() != '0':
                        txtReceipt.insert(END, f'Konkonte\t\t\t{int(txtkonkonte.get()) * 10}\n')
                    if txtbanku.get() != '0':
                        txtReceipt.insert(END, f'Banku\t\t\t{int(txtbanku.get()) * 10}\n')
                    if txtgob3.get() != '0':
                        txtReceipt.insert(END, f'Gari & Beans\t\t\t{int(txtgob3.get()) * 15}\n')
                    if txtkelewele.get() != '0':
                        txtReceipt.insert(END, f'Kelewele\t\t\t{int(txtkelewele.get()) * 10}\n')
                    if txtkenkey.get() != '0':
                        txtReceipt.insert(END, f'Kenkey\t\t\t{int(txtkenkey.get()) * 10}\n')
                    if txtyaw.get() != '0':
                        txtReceipt.insert(END, f'Fried Yaw\t\t\t{int(txtyaw.get()) * 10}\n')
                    if txtriceball.get() != '0':
                        txtReceipt.insert(END, f'Rice Ball\t\t\t{int(txtriceball.get()) * 10}\n')

                    if drinkcost.get() >= '1':
                        txtReceipt.insert(END,
                                          '--------------------------------- Drinks ----------------------------\n')
                    if txtcock.get() != '0':
                        txtReceipt.insert(END, f'Cocktail\t\t\t{int(txtcock.get()) * 25}\n')
                    if txtcoke.get() != '0':
                        txtReceipt.insert(END, f'Coka Cola\t\t\t{int(txtcoke.get()) * 20}\n')
                    if txtpepsi.get() != '0':
                        txtReceipt.insert(END, f'Pepsi\t\t\t{int(txtpepsi.get()) * 10}\n')
                    if txtorange.get() != '0':
                        txtReceipt.insert(END, f'Orange Juice\t\t\t{int(txtorange.get()) * 20}\n')
                    if txtdon.get() != '0':
                        txtReceipt.insert(END, f'Don Simon\t\t\t{int(txtdon.get()) * 30}\n')
                    if txtpineaple.get() != '0':
                        txtReceipt.insert(END, f'Pineapple Juice\t\t\t{int(txtpineaple.get()) * 25}\n')
                    if txtbeet.get() != '0':
                        txtReceipt.insert(END, f'Beet Juice\t\t\t{int(txtbeet.get()) * 35}\n')
                    if txttampico.get() != '0':
                        txtReceipt.insert(END, f'Tampico\t\t\t{int(txttampico.get()) * 10}\n')
                    if txtredwine.get() != '0':
                        txtReceipt.insert(END, f'Red Wine\t\t\t{int(txtredwine.get()) * 50}\n')
                    if txtlemon.get() != '0':
                        txtReceipt.insert(END, f'Lemon Juice\t\t\t{int(txtlemon.get()) * 20}\n')
                    if txtapple.get() != '0':
                        txtReceipt.insert(END, f'Apple Juice\t\t\t{int(txtapple.get()) * 25}\n')

                    if cakescost.get() >= '1':
                        txtReceipt.insert(END, '---------------------------------- Cakes ---------------------------\n')
                    if txtcheese.get() != '0':
                        txtReceipt.insert(END, f'Cheese\t\t\t{int(txtcheese.get()) * 30}\n')
                    if txtice.get() != '0':
                        txtReceipt.insert(END, f'Ice Cream\t\t\t{int(txtice.get()) * 50}\n')
                    if txtpizzza.get() != '0':
                        txtReceipt.insert(END, f'Pizza\t\t\t{int(txtpizzza.get()) * 40}\n')
                    if txtchoco.get() != '0':
                        txtReceipt.insert(END, f'Chocolate\t\t\t{int(txtchoco.get()) * 25}\n')
                    if txtvanilla.get() != '0':
                        txtReceipt.insert(END, f'Vanilla\t\t\t{int(txtvanilla.get()) * 35}\n')
                    if txtsponge.get() != '0':
                        txtReceipt.insert(END, f'Sponge\t\t\t{int(txtsponge.get()) * 45}\n')
                    if txtbanana.get() != '0':
                        txtReceipt.insert(END, f'Banana\t\t\t{int(txtbanana.get()) * 30}\n')
                    if txtred.get() != '0':
                        txtReceipt.insert(END, f'Red Velvet\t\t\t{int(txtred.get()) * 35}\n')
                    if txtoreo.get() != '0':
                        txtReceipt.insert(END, f'Oreo\t\t\t{int(txtoreo.get()) * 30}\n')
                    if txtblue.get() != '0':
                        txtReceipt.insert(END, f'Blueberry\t\t\t{int(txtblue.get()) * 40}\n')
                    if txtblack.get() != '0':
                        txtReceipt.insert(END, f'Black Forest\t\t\t{int(txtblack.get()) * 45}\n')

                    txtReceipt.insert(END, '*********************************************\n')
                    if foodcost.get() != '0':
                        txtReceipt.insert(END, f'Cost of Food\t\t\tGhc {priceofFood}\n')
                    if drinkcost.get() != '0':
                        txtReceipt.insert(END, f'Cost of Drinks\t\t\tGhc {priceofDrinks}\n')
                    if cakescost.get() != '0':
                        txtReceipt.insert(END, f'Cost of Cakes\t\t\tGhc {priceofCakes}\n')
                    txtReceipt.insert(END, f'Sub Total\t\t\tGhc {sum}\n')
                    txtReceipt.insert(END, f'Discount\t\t\tGhc {elavy}\n')
                    txtReceipt.insert(END, f'Total\t\t\tGhc {Total}\n')
                    txtReceipt.insert(END, '*********************************************\n')

                    txtReceipt.config(state='disabled')
                except Exception as es:
                    messagebox.showerror('Order Error!', f'Error due to {str(es)}')

            btnReceipt = Button(BtnFrame, text='Receipt', font=('arial', 14, 'bold'), bd=3, command=Receipt)
            btnReceipt.grid(row=0, column=1)

            # ================================ Variables ===========================
            fufuvar = IntVar()
            fricevar = IntVar()
            waakyevar = IntVar()
            jollofvar = IntVar()
            konkontevar = IntVar()
            bankuvar = IntVar()
            gob3var = IntVar()
            kelewelevar = IntVar()
            riceballvar = IntVar()
            kenkeyvar = IntVar()
            yawvar = IntVar()

            # =============================================Food Menu Functions ================================================
            def Fufufxn():
                if fufuvar.get() == 1:
                    fufuEntry.config(state=NORMAL)
                    fufuEntry.delete(0, END)
                    fufuEntry.focus()
                else:
                    fufuEntry.config(state=DISABLED)
                    txtfufu.set('0')

            def fricefxn():
                if fricevar.get() == 1:
                    friceEntry.config(state=NORMAL)
                    friceEntry.delete(0, END)
                    friceEntry.focus()
                else:
                    friceEntry.config(state=DISABLED)
                    txtfrice.set('0')

            def waakyefxn():
                if waakyevar.get() == 1:
                    waakyeEntry.config(state=NORMAL)
                    waakyeEntry.delete(0, END)
                    waakyeEntry.focus()
                else:
                    waakyeEntry.config(state=DISABLED)
                    txtwaakye.set('0')

            def jolloffxn():
                if jollofvar.get() == 1:
                    jollofEntry.config(state=NORMAL)
                    jollofEntry.delete(0, END)
                    jollofEntry.focus()
                else:
                    jollofEntry.config(state=DISABLED)
                    txtjollof.set('0')

            def konkontefxn():
                if konkontevar.get() == 1:
                    konkonteEntry.config(state=NORMAL)
                    konkonteEntry.delete(0, END)
                    konkonteEntry.focus()
                else:
                    konkonteEntry.config(state=DISABLED)
                    txtkonkonte.set('0')

            def bankufxn():
                if bankuvar.get() == 1:
                    bankuEntry.config(state=NORMAL)
                    bankuEntry.delete(0, END)
                    bankuEntry.focus()
                else:
                    bankuEntry.config(state=DISABLED)
                    txtbanku.set('0')

            def gob3fxn():
                if gob3var.get() == 1:
                    gob3Entry.config(state=NORMAL)
                    gob3Entry.delete(0, END)
                    gob3Entry.focus()
                else:
                    gob3Entry.config(state=DISABLED)
                    txtgob3.set('0')

            def kelewelefxn():
                if kelewelevar.get() == 1:
                    keleweleEntry.config(state=NORMAL)
                    keleweleEntry.delete(0, END)
                    keleweleEntry.focus()
                else:
                    keleweleEntry.config(state=DISABLED)
                    txtkelewele.set('0')

            def kenkeyfxn():
                if kenkeyvar.get() == 1:
                    kenkeyEntry.config(state=NORMAL)
                    kenkeyEntry.delete(0, END)
                    kenkeyEntry.focus()
                else:
                    kenkeyEntry.config(state=DISABLED)
                    txtkenkey.set('0')

            def yawfxn():
                if yawvar.get() == 1:
                    yawEntry.config(state=NORMAL)
                    yawEntry.delete(0, END)
                    yawEntry.focus()
                else:
                    yawEntry.config(state=DISABLED)
                    txtyaw.set('0')

            def riceballfxn():
                if riceballvar.get() == 1:
                    riceballEntry.config(state=NORMAL)
                    riceballEntry.delete(0, END)
                    riceballEntry.focus()
                else:
                    riceballEntry.config(state=DISABLED)
                    txtriceball.set('0')

            # ================================ Food ================================
            Fufu = Checkbutton(foodFrame, text='Fufu\t\tGhc 15', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                               variable=fufuvar, command=Fufufxn)
            Fufu.grid(row=0, column=0, sticky=W)
            Frice = Checkbutton(foodFrame, text='Fried Rice\tGhc 20', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                variable=fricevar, command=fricefxn)
            Frice.grid(row=1, column=0, sticky=W)
            Waakye = Checkbutton(foodFrame, text='Waakye \t\tGhc 15', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                 variable=waakyevar, command=waakyefxn)
            Waakye.grid(row=2, column=0, sticky=W)
            Jollof = Checkbutton(foodFrame, text='Jollof\t\tGhc 20', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                 variable=jollofvar, command=jolloffxn)
            Jollof.grid(row=3, column=0, sticky=W)
            Konkonte = Checkbutton(foodFrame, text='Konkonte\tGhc 10', font=('times', 15, 'bold'), onvalue=1,
                                   offvalue=0,
                                   variable=konkontevar, command=konkontefxn)
            Konkonte.grid(row=4, column=0, sticky=W)
            Banku = Checkbutton(foodFrame, text='Banku\t\tGhc 10', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                variable=bankuvar, command=bankufxn)
            Banku.grid(row=5, column=0, sticky=W)
            Gob3 = Checkbutton(foodFrame, text='Gari & Beans\tGhc 15', font=('times', 15, 'bold'), onvalue=1,
                               offvalue=0,
                               variable=gob3var, command=gob3fxn)
            Gob3.grid(row=6, column=0, sticky=W)
            Kelewele = Checkbutton(foodFrame, text='Kelewele\t\tGhc 10', font=('times', 15, 'bold'), onvalue=1,
                                   offvalue=0,
                                   variable=kelewelevar, command=kelewelefxn)
            Kelewele.grid(row=7, column=0, sticky=W)
            RiceBall = Checkbutton(foodFrame, text='Rice Ball\t\tGhc 10', font=('times', 15, 'bold'), onvalue=1,
                                   offvalue=0,
                                   variable=riceballvar, command=riceballfxn)
            RiceBall.grid(row=10, column=0, sticky=W)
            Kenkey = Checkbutton(foodFrame, text='Kenkey\t\tGhc 10', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                 variable=kenkeyvar, command=kenkeyfxn)
            Kenkey.grid(row=8, column=0, sticky=W)
            Yaw = Checkbutton(foodFrame, text='Fried Yaw\tGhc 10', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                              variable=yawvar, command=yawfxn)
            Yaw.grid(row=9, column=0, sticky=W)

            # ======================================= Entry ========================================================================
            # ----------------------------------------- Variables -------------------------------------------------------------------
            txtfufu = StringVar()
            txtfrice = StringVar()
            txtwaakye = StringVar()
            txtjollof = StringVar()
            txtkonkonte = StringVar()
            txtbanku = StringVar()
            txtgob3 = StringVar()
            txtkelewele = StringVar()
            txtriceball = StringVar()
            txtkenkey = StringVar()
            txtyaw = StringVar()

            txtfufu.set('0')
            txtfrice.set('0')
            txtwaakye.set('0')
            txtjollof.set('0')
            txtkonkonte.set('0')
            txtbanku.set('0')
            txtgob3.set('0')
            txtkelewele.set('0')
            txtriceball.set('0')
            txtkenkey.set('0')
            txtyaw.set('0')

            fufuEntry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                              textvariable=txtfufu)
            fufuEntry.grid(row=0, column=1)
            friceEntry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                               textvariable=txtfrice)
            friceEntry.grid(row=1, column=1)
            waakyeEntry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                textvariable=txtwaakye)
            waakyeEntry.grid(row=2, column=1)
            jollofEntry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                textvariable=txtjollof)
            jollofEntry.grid(row=3, column=1)
            konkonteEntry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                  textvariable=txtkonkonte)
            konkonteEntry.grid(row=4, column=1)
            bankuEntry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                               textvariable=txtbanku)
            bankuEntry.grid(row=5, column=1)
            gob3Entry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                              textvariable=txtgob3)
            gob3Entry.grid(row=6, column=1)
            keleweleEntry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                  textvariable=txtkelewele)
            keleweleEntry.grid(row=7, column=1)
            riceballEntry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                  textvariable=txtriceball)
            riceballEntry.grid(row=10, column=1)
            kenkeyEntry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                textvariable=txtkenkey)
            kenkeyEntry.grid(row=8, column=1)
            yawEntry = Entry(foodFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED, textvariable=txtyaw)
            yawEntry.grid(row=9, column=1)

            # ==================================== Drinks List=================================================
            def cockfxn():
                if cockvar.get() == 1:
                    cockEntry.config(state=NORMAL)
                    cockEntry.delete(0, END)
                    cockEntry.focus()
                else:
                    cockEntry.config(state=DISABLED)
                    txtcock.set('0')

            def cokefxn():
                if cokevar.get() == 1:
                    cokeEntry.config(state=NORMAL)
                    cokeEntry.delete(0, END)
                    cokeEntry.focus()
                else:
                    cokeEntry.config(state=DISABLED)
                    txtcoke.set('0')

            def pepsifxn():
                if pepsivar.get() == 1:
                    pepsiEntry.config(state=NORMAL)
                    pepsiEntry.delete(0, END)
                    pepsiEntry.focus()
                else:
                    pepsiEntry.config(state=DISABLED)
                    txtpepsi.set('0')

            def orangefxn():
                if orangevar.get() == 1:
                    orangeEntry.config(state=NORMAL)
                    orangeEntry.delete(0, END)
                    orangeEntry.focus()
                else:
                    orangeEntry.config(state=DISABLED)
                    txtorange.set('0')

            def donfxn():
                if donvar.get() == 1:
                    donEntry.config(state=NORMAL)
                    donEntry.delete(0, END)
                    donEntry.focus()
                else:
                    donEntry.config(state=DISABLED)
                    txtdon.set('0')

            def pineaplefxn():
                if pineaplevar.get() == 1:
                    pineapleEntry.config(state=NORMAL)
                    pineapleEntry.delete(0, END)
                    pineapleEntry.focus()
                else:
                    pineapleEntry.config(state=DISABLED)
                    txtpineaple.set('0')

            def beetfxn():
                if beetvar.get() == 1:
                    beetEntry.config(state=NORMAL)
                    beetEntry.delete(0, END)
                    beetEntry.focus()
                else:
                    beetEntry.config(state=DISABLED)
                    txtbeet.set('0')

            def tampicofxn():
                if tampicovar.get() == 1:
                    tampicoEntry.config(state=NORMAL)
                    tampicoEntry.delete(0, END)
                    tampicoEntry.focus()
                else:
                    tampicoEntry.config(state=DISABLED)
                    txttampico.set('0')

            def redwinefxn():
                if redwine.get() == 1:
                    redwineEntry.config(state=NORMAL)
                    redwineEntry.delete(0, END)
                    redwineEntry.focus()
                else:
                    redwineEntry.config(state=DISABLED)
                    txtredwine.set('0')

            def applefxn():
                if applevar.get() == 1:
                    appleEntry.config(state=NORMAL)
                    appleEntry.delete(0, END)
                    appleEntry.focus()
                else:
                    appleEntry.config(state=DISABLED)
                    txtapple.set('0')

            def lemonfxn():
                if lemonvar.get() == 1:
                    lemonEntry.config(state=NORMAL)
                    lemonEntry.delete(0, END)
                    lemonEntry.focus()
                else:
                    lemonEntry.config(state=DISABLED)
                    txtlemon.set('0')

            # ----------------------------------- Variables -----------------------------------------------
            cockvar = IntVar()
            cokevar = IntVar()
            pepsivar = IntVar()
            orangevar = IntVar()
            donvar = IntVar()
            pineaplevar = IntVar()
            beetvar = IntVar()
            lemonvar = IntVar()
            tampicovar = IntVar()
            applevar = IntVar()
            redwine = IntVar()

            Cocktail = Checkbutton(drinkFrame, text='Cocktail\t\tGhc 25', font=('times', 15, 'bold'), onvalue=1,
                                   offvalue=0,
                                   variable=cockvar, command=cockfxn)
            Cocktail.grid(row=0, column=0, sticky=W)
            Coke = Checkbutton(drinkFrame, text='Coka Cola\tGhc 20', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                               variable=cokevar, command=cokefxn)
            Coke.grid(row=1, column=0, sticky=W)
            Pepsi = Checkbutton(drinkFrame, text='Pepsi\t\tGhc 10', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                variable=pepsivar, command=pepsifxn)
            Pepsi.grid(row=2, column=0, sticky=W)
            orange = Checkbutton(drinkFrame, text='Orange Juice\tGhc 20', font=('times', 15, 'bold'), onvalue=1,
                                 offvalue=0,
                                 variable=orangevar, command=orangefxn)
            orange.grid(row=3, column=0, sticky=W)
            Don = Checkbutton(drinkFrame, text='Don Simon\tGhc 30', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                              variable=donvar, command=donfxn)
            Don.grid(row=4, column=0, sticky=W)
            Pineaple = Checkbutton(drinkFrame, text='Pineaple Juice\tGhc 25', font=('times', 15, 'bold'), onvalue=1,
                                   offvalue=0,
                                   variable=pineaplevar, command=pineaplefxn)
            Pineaple.grid(row=5, column=0, sticky=W)
            Beet = Checkbutton(drinkFrame, text='Beet Juice\tGhc 35', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                               variable=beetvar, command=beetfxn)
            Beet.grid(row=6, column=0, sticky=W)
            Tampico = Checkbutton(drinkFrame, text='Tampico Juice\tGhc 10', font=('times', 15, 'bold'), onvalue=1,
                                  offvalue=0,
                                  variable=tampicovar, command=tampicofxn)
            Tampico.grid(row=7, column=0, sticky=W)
            Apple = Checkbutton(drinkFrame, text='Apple Juice\tGhc 25', font=('times', 15, 'bold'), onvalue=1,
                                offvalue=0,
                                variable=applevar, command=applefxn)
            Apple.grid(row=10, column=0, sticky=W)
            Wine = Checkbutton(drinkFrame, text='Red Wine\tGhc 50', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                               variable=redwine, command=redwinefxn)
            Wine.grid(row=8, column=0, sticky=W)
            Lemon = Checkbutton(drinkFrame, text='Lemon Juice\tGhc 20', font=('times', 15, 'bold'), onvalue=1,
                                offvalue=0,
                                variable=lemonvar, command=lemonfxn)
            Lemon.grid(row=9, column=0, sticky=W)

            # ======================================= Entry ========================================================================
            # ----------------------------------------- Variables -------------------------------------------------------------------
            txtcock = StringVar()
            txtcoke = StringVar()
            txtpepsi = StringVar()
            txtorange = StringVar()
            txtdon = StringVar()
            txtpineaple = StringVar()
            txtbeet = StringVar()
            txtredwine = StringVar()
            txttampico = StringVar()
            txtapple = StringVar()
            txtlemon = StringVar()

            txtcock.set('0')
            txtcoke.set('0')
            txtpepsi.set('0')
            txtorange.set('0')
            txtdon.set('0')
            txtpineaple.set('0')
            txtbeet.set('0')
            txtredwine.set('0')
            txttampico.set('0')
            txtapple.set('0')
            txtlemon.set('0')

            cockEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                              textvariable=txtcock)
            cockEntry.grid(row=0, column=1)
            cokeEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                              textvariable=txtcoke)
            cokeEntry.grid(row=1, column=1)
            pepsiEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                               textvariable=txtpepsi)
            pepsiEntry.grid(row=2, column=1)
            orangeEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                textvariable=txtorange)
            orangeEntry.grid(row=3, column=1)
            donEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                             textvariable=txtdon)
            donEntry.grid(row=4, column=1)
            pineapleEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                  textvariable=txtpineaple)
            pineapleEntry.grid(row=5, column=1)
            beetEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                              textvariable=txtbeet)
            beetEntry.grid(row=6, column=1)
            tampicoEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                 textvariable=txttampico)
            tampicoEntry.grid(row=7, column=1)
            appleEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                               textvariable=txtapple)
            appleEntry.grid(row=10, column=1)
            redwineEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                 textvariable=txtredwine)
            redwineEntry.grid(row=8, column=1)
            lemonEntry = Entry(drinkFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                               textvariable=txtlemon)
            lemonEntry.grid(row=9, column=1)

            # ==============================Cakes Functions =============================
            def cheesefxn():
                if cheesevar.get() == 1:
                    cheeseEntry.config(state=NORMAL)
                    cheeseEntry.delete(0, END)
                    cheeseEntry.focus()
                else:
                    cheeseEntry.config(state=DISABLED)
                    txtcheese.set('0')

            def icefxn():
                if icevar.get() == 1:
                    iceEntry.config(state=NORMAL)
                    iceEntry.delete(0, END)
                    iceEntry.focus()
                else:
                    iceEntry.config(state=DISABLED)
                    txtice.set('0')

            def pizzafxn():
                if pizzavar.get() == 1:
                    pizzzaEntry.config(state=NORMAL)
                    pizzzaEntry.delete(0, END)
                    pizzzaEntry.focus()
                else:
                    pizzzaEntry.config(state=DISABLED)
                    txtpizzza.set('0')

            def chocofxn():
                if chocovar.get() == 1:
                    chocoEntry.config(state=NORMAL)
                    chocoEntry.delete(0, END)
                    chocoEntry.focus()
                else:
                    chocoEntry.config(state=DISABLED)
                    txtchoco.set('0')

            def vanillafxn():
                if vanillavar.get() == 1:
                    vanillaEntry.config(state=NORMAL)
                    vanillaEntry.delete(0, END)
                    vanillaEntry.focus()
                else:
                    vanillaEntry.config(state=DISABLED)
                    txtvanilla.set('0')

            def spongefxn():
                if spongevar.get() == 1:
                    spongeEntry.config(state=NORMAL)
                    spongeEntry.delete(0, END)
                    spongeEntry.focus()
                else:
                    spongeEntry.config(state=DISABLED)
                    txtsponge.set('0')

            def bananafxn():
                if bananavar.get() == 1:
                    bananaEntry.config(state=NORMAL)
                    bananaEntry.delete(0, END)
                    bananaEntry.focus()
                else:
                    bananaEntry.config(state=DISABLED)
                    txtbanana.set('0')

            def redfxn():
                if redvar.get() == 1:
                    redEntry.config(state=NORMAL)
                    redEntry.delete(0, END)
                    redEntry.focus()
                else:
                    redEntry.config(state=DISABLED)
                    txtred.set('0')

            def blackfxn():
                if blackvar.get() == 1:
                    blackEntry.config(state=NORMAL)
                    blackEntry.delete(0, END)
                    blackEntry.focus()
                else:
                    blackEntry.config(state=DISABLED)
                    txtblack.set('0')

            def oreofxn():
                if oreovar.get() == 1:
                    oreoEntry.config(state=NORMAL)
                    oreoEntry.delete(0, END)
                    oreoEntry.focus()
                else:
                    oreoEntry.config(state=DISABLED)
                    txtoreo.set('0')

            def bluefxn():
                if Bluevar.get() == 1:
                    blueEntry.config(state=NORMAL)
                    blueEntry.delete(0, END)
                    blueEntry.focus()
                else:
                    blueEntry.config(state=DISABLED)
                    txtblue.set('0')

            # ================================ Cakes Variables ===========================
            cheesevar = IntVar()
            icevar = IntVar()
            pizzavar = IntVar()
            chocovar = IntVar()
            vanillavar = IntVar()
            spongevar = IntVar()
            bananavar = IntVar()
            redvar = IntVar()
            blackvar = IntVar()
            oreovar = IntVar()
            Bluevar = IntVar()

            # ================================ Cakes ================================
            cheese = Checkbutton(cakesFrame, text='Cheese\t\tGhc 30', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                 variable=cheesevar, command=cheesefxn)
            cheese.grid(row=0, column=0, sticky=W)
            ice = Checkbutton(cakesFrame, text='Ice cream\tGhc 50', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                              variable=icevar, command=icefxn)
            ice.grid(row=1, column=0, sticky=W)
            pizzza = Checkbutton(cakesFrame, text='Pizza\t\tGhc 40', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                 variable=pizzavar, command=pizzafxn)
            pizzza.grid(row=2, column=0, sticky=W)
            choco = Checkbutton(cakesFrame, text='Chocolate\tGhc 25', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                variable=chocovar, command=chocofxn)
            choco.grid(row=3, column=0, sticky=W)
            vanilla = Checkbutton(cakesFrame, text='Vanilla\t\tGhc 35', font=('times', 15, 'bold'), onvalue=1,
                                  offvalue=0,
                                  variable=vanillavar, command=vanillafxn)
            vanilla.grid(row=4, column=0, sticky=W)
            sponge = Checkbutton(cakesFrame, text='Sponge\t\tGhc 45', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                 variable=spongevar, command=spongefxn)
            sponge.grid(row=5, column=0, sticky=W)
            banana = Checkbutton(cakesFrame, text='Banana\t\tGhc 30', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                                 variable=bananavar, command=bananafxn)
            banana.grid(row=6, column=0, sticky=W)
            red = Checkbutton(cakesFrame, text='Red Velvet\tGhc 35', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                              variable=redvar, command=redfxn)
            red.grid(row=7, column=0, sticky=W)
            black = Checkbutton(cakesFrame, text='Black Forest\tGhc 45', font=('times', 15, 'bold'), onvalue=1,
                                offvalue=0,
                                variable=blackvar, command=blackfxn)
            black.grid(row=10, column=0, sticky=W)
            oreo = Checkbutton(cakesFrame, text='Oreo\t\tGhc 30', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                               variable=oreovar, command=oreofxn)
            oreo.grid(row=8, column=0, sticky=W)
            blue = Checkbutton(cakesFrame, text='Blueberry\tGhc 40', font=('times', 15, 'bold'), onvalue=1, offvalue=0,
                               variable=Bluevar, command=bluefxn)
            blue.grid(row=9, column=0, sticky=W)
            # ======================================= Entry ========================================================================
            # ----------------------------------------- Variables -------------------------------------------------------------------
            txtcheese = StringVar()
            txtice = StringVar()
            txtpizzza = StringVar()
            txtchoco = StringVar()
            txtvanilla = StringVar()
            txtsponge = StringVar()
            txtbanana = StringVar()
            txtred = StringVar()
            txtblack = StringVar()
            txtoreo = StringVar()
            txtblue = StringVar()

            txtcheese.set('0')
            txtice.set('0')
            txtpizzza.set('0')
            txtchoco.set('0')
            txtvanilla.set('0')
            txtsponge.set('0')
            txtbanana.set('0')
            txtred.set('0')
            txtblack.set('0')
            txtoreo.set('0')
            txtblue.set('0')

            cheeseEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                textvariable=txtcheese)
            cheeseEntry.grid(row=0, column=1)
            iceEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                             textvariable=txtice)
            iceEntry.grid(row=1, column=1)
            pizzzaEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                textvariable=txtpizzza)
            pizzzaEntry.grid(row=2, column=1)
            chocoEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                               textvariable=txtchoco)
            chocoEntry.grid(row=3, column=1)
            vanillaEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                 textvariable=txtvanilla)
            vanillaEntry.grid(row=4, column=1)
            spongeEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                textvariable=txtsponge)
            spongeEntry.grid(row=5, column=1)
            bananaEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                                textvariable=txtbanana)
            bananaEntry.grid(row=6, column=1)
            redEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                             textvariable=txtred)
            redEntry.grid(row=7, column=1)
            blackEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                               textvariable=txtblack)
            blackEntry.grid(row=10, column=1)
            oreoEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                              textvariable=txtoreo)
            oreoEntry.grid(row=8, column=1)
            blueEntry = Entry(cakesFrame, font=('tahoma', 12, 'bold'), bd=2, width=3, state=DISABLED,
                              textvariable=txtblue)
            blueEntry.grid(row=9, column=1)

            # =============================================== Labels and Entries ===================================================
            # ------------------------------------------------ Entries Variables ---------------------------------------------------
            foodcost = StringVar()
            drinkcost = StringVar()
            cakescost = StringVar()
            subtotal = StringVar()
            tax = StringVar()
            total = StringVar()

            foodcostlbl = Label(costFrame, text='Cost of Food', font=('arial', 16, 'bold'), fg='blue')
            foodcostlbl.grid(row=1, column=0, sticky=W)
            foodcostEntry = Entry(costFrame, font=('arial', 15, 'bold'), bd=5, width=15, state='readonly',
                                  textvariable=foodcost)
            foodcostEntry.grid(row=1, column=1)

            drinkscostlbl = Label(costFrame, text='Cost of Drinks', font=('arial', 16, 'bold'), fg='blue')
            drinkscostlbl.grid(row=2, column=0, sticky=W)
            drinkscostEntry = Entry(costFrame, font=('arial', 15, 'bold'), bd=5, width=15, state='readonly',
                                    textvariable=drinkcost)
            drinkscostEntry.grid(row=2, column=1)

            cakescostlbl = Label(costFrame, text='Cost of Cakes', font=('arial', 16, 'bold'), fg='blue')
            cakescostlbl.grid(row=3, column=0, sticky=W)
            cakescostEntry = Entry(costFrame, font=('arial', 15, 'bold'), bd=5, width=15, state='readonly',
                                   textvariable=cakescost)
            cakescostEntry.grid(row=3, column=1)

            subtotallbl = Label(costFrame, text='Sub Total', font=('arial', 16, 'bold'), fg='blue')
            subtotallbl.grid(row=1, column=3, sticky=W)
            subtotalEntry = Entry(costFrame, font=('arial', 15, 'bold'), bd=5, width=15, state='readonly',
                                  textvariable=subtotal)
            subtotalEntry.grid(row=1, column=4)

            taxlbl = Label(costFrame, text='Services Tax', font=('arial', 16, 'bold'), fg='blue')
            taxlbl.grid(row=2, column=3, sticky=W)
            taxEntry = Entry(costFrame, font=('arial', 15, 'bold'), bd=5, width=15, state='readonly', textvariable=tax)
            taxEntry.grid(row=2, column=4)

            totallbl = Label(costFrame, text='Total', font=('arial', 16, 'bold'), fg='blue')
            totallbl.grid(row=3, column=3, sticky=W)
            totalEntry = Entry(costFrame, font=('arial', 15, 'bold'), bd=5, width=15, state='readonly',
                               textvariable=total)
            totalEntry.grid(row=3, column=4)

            # ====================================== Buttons =======================================================================
            btnTotal = Button(costFrame, text='Total', font=('arial', 14, 'bold'), bd=2, width=10, command=total_cost)
            btnTotal.grid(row=0, column=0, columnspan=5, pady=10)

            btnSave = Button(BtnFrame, text='Save', font=('arial', 14, 'bold'), bd=3, width=7, command=save)
            btnSave.grid(row=0, column=2)

            # from KFC import *
            btnSend = Button(BtnFrame, text='Send', font=('arial', 14, 'bold'), bd=3, width=7, command=send)
            btnSend.grid(row=0, column=3)

            btnReset = Button(BtnFrame, text='Reset', font=('arial', 14, 'bold'), bd=3, width=7, command=reset)
            btnReset.grid(row=0, column=4)

            # ======================================Text Area ======================================================================
            txtReceipt = Text(receiptFrame, font=('times', 12, 'bold'), bd=3, width=45, height=14)
            txtReceipt.grid(row=0, column=0)

            # ====================================================== Services ======================================================
            Checkbutton(servicesFrame, text='Event Management', font=('tahoma', 8, 'bold'), bd=1, onvalue=1,
                        offvalue=0).grid(row=0, column=0, sticky=W)
            Checkbutton(servicesFrame, text='Hampers', font=('tahoma', 8, 'bold'), bd=1, onvalue=1, offvalue=0).grid(
                row=1, column=0, sticky=W)
            Checkbutton(servicesFrame, text='Training in:\nCakes Descoration &\nPractical Cookery',
                        font=('tahoma', 8, 'bold'), bd=1, onvalue=1, offvalue=0).grid(row=2, column=0, sticky=W)

            petascolbl = Label(servicesFrame, text='By Petasco 0547736844', font=('algeria', 9, 'bold italic'),
                               fg='blue')
            petascolbl.grid(row=6, column=0, sticky=W, pady=12)
            # ======================================================= Orders =======================================================
            Checkbutton(ordersFrame, text='Local Dishes', font=('tahoma', 8, 'bold'), bd=1, onvalue=1, offvalue=0).grid(
                row=0, column=0, sticky=W)
            Checkbutton(ordersFrame, text='Continetal Dishes', font=('tahoma', 8, 'bold'), bd=1, onvalue=1,
                        offvalue=0).grid(row=1, column=0, sticky=W)
            Checkbutton(ordersFrame, text='Lunch', font=('tahoma', 8, 'bold'), bd=1, onvalue=1, offvalue=0).grid(row=2,
                                                                                                                 column=0,
                                                                                                                 sticky=W)
            Checkbutton(ordersFrame, text='Dinner', font=('tahoma', 8, 'bold'), bd=1, onvalue=1, offvalue=0).grid(row=3,
                                                                                                                  column=0,
                                                                                                                  sticky=W)
            Checkbutton(ordersFrame, text='Wedding', font=('tahoma', 8, 'bold'), bd=1, onvalue=1, offvalue=0).grid(
                row=4, column=0, sticky=W)
            Checkbutton(ordersFrame, text='Funneral', font=('tahoma', 8, 'bold'), bd=1, onvalue=1, offvalue=0).grid(
                row=5, column=0, sticky=W)
            Checkbutton(ordersFrame, text='Office Delivery', font=('tahoma', 8, 'bold'), bd=1, onvalue=1,
                        offvalue=0).grid(row=6, column=0, sticky=W)

            # ==================================================== Calculator ======================================================
            operator = ''

            def buttonClick(numbers):
                global operator
                operator = operator + numbers
                calculatorFeild.delete(0, END)
                calculatorFeild.insert(END, operator)

            def clear():
                global operator
                operator = ''
                calculatorFeild.delete(0, END)

            def answer():
                global operator
                result = str(eval(operator))
                calculatorFeild.delete(0, END)
                calculatorFeild.insert(0, result)
                operator = ''

            calculatorFeild = Entry(calFrame, font=('arial', 15, 'bold'), width=30, bd=5)
            calculatorFeild.grid(row=0, column=0, columnspan=5)
            # ------------------------------- Calculator Buttons -------------------------------------------------------------------
            btn7 = Button(calFrame, text='7', font=('arial', 16, 'bold'), bd=6, width=5,
                          command=lambda: buttonClick('7'))
            btn7.grid(row=1, column=0)
            btn8 = Button(calFrame, text='8', font=('arial', 16, 'bold'), bd=6, width=5,
                          command=lambda: buttonClick('8'))
            btn8.grid(row=1, column=1)
            btn9 = Button(calFrame, text='9', font=('arial', 16, 'bold'), bd=6, width=5,
                          command=lambda: buttonClick('9'))
            btn9.grid(row=1, column=2)
            btnplus = Button(calFrame, text='+', font=('arial', 16, 'bold'), bd=6, width=5,
                             command=lambda: buttonClick('+'))
            btnplus.grid(row=1, column=3)
            # -------------------------------- Row 2 ----------------------------------
            btn4 = Button(calFrame, text='4', font=('arial', 16, 'bold'), bd=6, width=5,
                          command=lambda: buttonClick('4'))
            btn4.grid(row=2, column=0)
            btn5 = Button(calFrame, text='5', font=('arial', 16, 'bold'), bd=6, width=5,
                          command=lambda: buttonClick('5'))
            btn5.grid(row=2, column=1)
            btn6 = Button(calFrame, text='6', font=('arial', 16, 'bold'), bd=6, width=5,
                          command=lambda: buttonClick('6'))
            btn6.grid(row=2, column=2)
            btnminus = Button(calFrame, text='-', font=('arial', 16, 'bold'), bd=6, width=5,
                              command=lambda: buttonClick('-'))
            btnminus.grid(row=2, column=3)
            # -------------------------------- Row 3 -------------------------------------
            btn1 = Button(calFrame, text='1', font=('arial', 16, 'bold'), bd=6, width=5,
                          command=lambda: buttonClick('1'))
            btn1.grid(row=3, column=0)
            btn2 = Button(calFrame, text='2', font=('arial', 16, 'bold'), bd=6, width=5,
                          command=lambda: buttonClick('2'))
            btn2.grid(row=3, column=1)
            btn3 = Button(calFrame, text='3', font=('arial', 16, 'bold'), bd=6, width=5,
                          command=lambda: buttonClick('3'))
            btn3.grid(row=3, column=2)
            btntimes = Button(calFrame, text='x', font=('arial', 16, 'bold'), bd=6, width=5,
                              command=lambda: buttonClick('*'))
            btntimes.grid(row=3, column=3)
            # --------------------------------- Row 4 --------------------------------------
            btn0 = Button(calFrame, text='0', font=('arial', 16, 'bold'), bd=6, width=5,
                          command=lambda: buttonClick('0'))
            btn0.grid(row=4, column=0)
            btnClear = Button(calFrame, text='Clear', font=('arial', 16, 'bold'), bd=6, width=5, command=clear)
            btnClear.grid(row=4, column=1)
            btnEqual = Button(calFrame, text='=', font=('arial', 16, 'bold'), bd=6, width=5, command=answer)
            btnEqual.grid(row=4, column=2)
            btnDivide = Button(calFrame, text='/', font=('arial', 16, 'bold'), bd=6, width=5,
                               command=lambda: buttonClick('/'))
            btnDivide.grid(row=4, column=3)



        except EXCEPTION as es:
            messagebox.showerror('Error',f'Error due to {str(es)}')

root = Tk()
ob = Login(root)
root.mainloop()
