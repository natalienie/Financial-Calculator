import tkinter as tk
from tkinter import ttk, Checkbutton, IntVar
import pandas as pd
import numpy as np
import math
#from scipy.optimize import brentq

large_font = ('Verdana', 14)


def popupmsg(msg):

    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=norm_font)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()


class Financial_calculator(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Natalie's Financial calculator")

        container = tk.Frame(self)

        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)


        self.frames = {}
        for F in (StartPage, RegularPage, BondPage, PensionPage):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="""Thanks for using Natalie's calculator!
        Please choose what kind of problem you want to solve""", font=large_font)
        self.grid(column=0, row=0, columnspan=1, rowspan=4)
        label.grid(row=1, column=1)
        B1 = ttk.Button(self, text='Regular Financial Calculation', command=lambda:controller.show_frame(RegularPage))
        B2 = ttk.Button(self, text='Bonds Calculation', command=lambda:controller.show_frame(BondPage))
        B3 = ttk.Button(self, text='Save for Pension Calculation', command=lambda:controller.show_frame(PensionPage))
        B1.grid(row=2, column=1)
        B2.grid(row=3, column=1)
        B3.grid(row=4, column=1)




class RegularPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ttk.Label(self, text="PV").grid(row=1)
        ttk.Label(self, text='FV').grid(row=2)
        ttk.Label(self, text='Rate').grid(row=3)
        ttk.Label(self, text='Period').grid(row=4)
        ttk.Label(self, text='PMT').grid(row=5)

        e1 = ttk.Entry(self)
        e2 = ttk.Entry(self)
        e3 = ttk.Entry(self)
        e4 = ttk.Entry(self)
        e5 = ttk.Entry(self)
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        C1 = Checkbutton(self, variable=var1)
        C2 = Checkbutton(self, variable=var2)
        C3 = Checkbutton(self, variable=var3)
        C4 = Checkbutton(self, variable=var4)
        C5 = Checkbutton(self, variable=var5)
        C6 = Checkbutton(self, text='ordinary', variable=var6)

        Button1 = ttk.Button(self, text='Calculate', command=lambda:calculate())
        Button3 = ttk.Button(self, text='Submit', command=lambda:save_input())
        Button2 = ttk.Button(self, text='Home', command=lambda:controller.show_frame(StartPage))
        self.grid(column=0, row=0, columnspan=2, rowspan=8)
        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=3, column=1)
        e4.grid(row=4, column=1)
        e5.grid(row=5, column=1)

        C1.grid(row=1, column=2)
        C2.grid(row=2, column=2)
        C3.grid(row=3, column=2)
        C4.grid(row=4, column=2)
        C5.grid(row=5, column=2)
        C6.grid(row=6, column=2)

        Button1.grid(row=7, column=1)
        Button2.grid(row=7, column=2)
        Button3.grid(row=7, column=0)


        def save_input():
            """
            PV = float(e1.get())
            FV = float(e2.get())
            Rate = float(e3.get())
            Period = int(e4.get())
            pmt = float(e5.get())
            """
            global entry1
            global entry2
            global entry3
            global entry4
            global entry5
            global entry6

            entry1 = var1.get()
            entry2 = var2.get()
            entry3 = var3.get()
            entry4 = var4.get()
            entry5 = var5.get()
            entry6 = var6.get()


        def calculate():

            if entry1 == True:

                FV = float(e2.get())
                Rate = float(e3.get())
                Period = int(e4.get())
                pmt = float(e5.get())
                print(FV)
                print(Rate)
                print(Period)
                print(pmt)
                sum1 = 0
                if entry6 == True:
                    for i in range(1, Period+1):
                        sum1 += pmt / ((1+Rate)**i)
                    sum2 = FV / ((1+Rate) ** Period)
                    Sum = sum1+sum2
                else:
                    for i in range(0, Period):
                        sum1 += pmt / ((1+Rate)**i)
                    sum2 = FV / ((1+Rate) ** Period)
                    Sum = sum1+sum2
                window = tk.Tk()
                window.wm_title('Result')
                label = ttk.Label(window, text='PV = {}'.format(Sum))
                label.pack(side='top', fill='x', pady=10)
                window.mainloop()

            elif entry2 == True:
                PV = float(e1.get())
                Rate = float(e3.get())
                Period = int(e4.get())
                pmt = float(e5.get())
                sum1 = 0
                if entry6 == True:
                    for i in range(0, Period):
                        sum1 += pmt * ((1+Rate)**i)
                    sum2 = PV * (1+Rate)**Period
                    Sum = sum1 + sum2

                else:
                    for i in range(1, Period+1):
                        sum1 += pmt * ((1+Rate)**i)
                    sum2 = PV * (1+Rate)**Period
                    Sum = sum1 + sum2
                window = tk.Tk()
                window.wm_title('Result')
                label = ttk.Label(window, text='FV = {}'.format(Sum))
                label.pack(side='top', fill='x', pady=10)
                window.mainloop()

            elif entry3 == True:

                PV = float(e1.get())
                FV = float(e2.get())

                Period = int(e4.get())
                pmt = float(e5.get())

                def f(R):
                    return pmt*(1+R)**Period - pmt + FV*R - PV*R*(1+R)**Period
                def f1(R):
                    return pmt*(1+R)**(Period+1) - pmt*(1+R) + FV*R - PV*R*(1+R)**Period


                """
                #if var1.get() == True:
                    #Sum = brentq(f, 0.0, 0.2)
                #else:
                    #Sum = brentq(f1, 0.0, 0.2)
                """


                def simpleton_walk(func):
                    A0 = 0.05
                    current_A = A0
                    step_size = 0.005
                    decay = 0.95
                    threshold = 0.1
                    loc = []
                    for i in range(50):
                        step_left = current_A - step_size
                        step_right = current_A + step_size

                        if (f(step_left))**2 > (f(step_right))**2:
                            best_step = step_right
                        else:
                            best_step = step_left
                        if (f(best_step))**2 < (f(current_A))**2:
                            current_A = best_step
                            loc.append(best_step)
                            step_size *= decay
                    return loc[-1]



                if entry6 == True:
                    root = simpleton_walk(f)
                else:
                    root = simpleton_walk(f1)



                window = tk.Tk()
                window.wm_title('Result')
                label = ttk.Label(window, text='Rate = {}'.format(root))
                label.pack(side='top', fill='x', pady=10)
                window.mainloop()

            elif entry4 == True:

                def f(Period):
                    return pmt*(1+Rate)**Period - pmt + FV*Rate - PV*Rate*(1+Rate)**Period
                def f1(Period):
                    return pmt*(1+Rate)**(Period+1) - pmt*(1+Rate) + FV*Rate - PV*Rate*(1+Rate)**Period
                PV = float(e1.get())
                FV = float(e2.get())

                Rate = float(e3.get())
                pmt = float(e5.get())

                def simpleton_walk(func):
                    A0 = 2
                    current_A = A0
                    step_size = 1


                    loc = []
                    for i in range(30):
                        step_left = current_A - step_size
                        step_right = current_A + step_size

                        if (f(step_left))**2 > (f(step_right))**2:
                            best_step = step_right
                        else:
                            best_step = step_left
                        if (f(best_step))**2 < (f(current_A))**2:
                            current_A = best_step
                            loc.append(best_step)

                    return loc[-1]

                """
                Sum1 = 0
                for i in range(2, 50):
                    for ii in range(1, i):
                        Sum1 += pmt / ((1+Rate)**ii)
                    Sum2 = FV / (1+Rate)**i
                    Sum = Sum1 + Sum2
                    if Sum < PV:
                        continue
                    else:
                        Period = i
                        break
                """

                if entry6 == True:
                    Period = simpleton_walk(f)
                else:
                    Period = simpleton_walk(f1)
                window = tk.Tk()
                window.wm_title('Result')
                label = ttk.Label(window, text='Period = {}'.format(Period))
                label.pack(side='top', fill='x', pady=10)
                window.mainloop()

            else:

                PV = float(e1.get())
                FV = float(e2.get())

                R = float(e3.get())

                Period = int(e4.get())
                if entry6 == True:
                    pmt = (PV*R*(1+R)**Period - FV*R) / ((1+R)**Period - 1)
                else:
                    pmt = (PV*R*(1+R)**Period - FV*R) / ((1+R)**(Period+1) - (1+R))
                window = tk.Tk()
                window.wm_title('Result')
                label = ttk.Label(window, text='PMT = {}'.format(pmt))
                label.pack(side='top', fill='x', pady=10)
                window.mainloop()





class BondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        ttk.Label(self, text="Issue Price").grid(row=1)
        ttk.Label(self, text='Par Value').grid(row=2)
        ttk.Label(self, text='Yield Rate').grid(row=3)
        ttk.Label(self, text='Period').grid(row=4)
        ttk.Label(self, text='Coupon Rate').grid(row=5)
        e1 = ttk.Entry(self)
        e2 = ttk.Entry(self)
        e3 = ttk.Entry(self)
        e4 = ttk.Entry(self)
        e5 = ttk.Entry(self)
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()

        C1 = Checkbutton(self, variable=var1)
        C2 = Checkbutton(self, variable=var2)
        C3 = Checkbutton(self, variable=var3)
        C4 = Checkbutton(self, variable=var4)
        C5 = Checkbutton(self, variable=var5)


        Button1 = ttk.Button(self, text='Calculate', command=lambda:calculate())
        Button3 = ttk.Button(self, text='Submit', command=lambda:save_input())
        Button2 = ttk.Button(self, text='Home', command=lambda:controller.show_frame(StartPage))
        self.grid(column=0, row=0, columnspan=2, rowspan=7)
        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=3, column=1)
        e4.grid(row=4, column=1)
        e5.grid(row=5, column=1)

        C1.grid(row=1, column=2)
        C2.grid(row=2, column=2)
        C3.grid(row=3, column=2)
        C4.grid(row=4, column=2)
        C5.grid(row=5, column=2)


        Button1.grid(row=6, column=1)
        Button2.grid(row=6, column=2)
        Button3.grid(row=6, column=0)

        def save_input():

            global ent1
            global ent2
            global ent3
            global ent4
            global ent5

            ent1 = var1.get()
            ent2 = var2.get()
            ent3 = var3.get()
            ent4 = var4.get()
            ent5 = var5.get()

        def calculate():

            if ent1 == True:

                FV = float(e2.get())
                Rate = float(e3.get())
                Period = int(e4.get())
                CouponR = float(e5.get())
                pmt = FV*CouponR

                sum1 = 0

                for i in range(1, Period+1):
                    sum1 += pmt / ((1+Rate)**i)
                sum2 = FV / ((1+Rate) ** Period)
                Sum = sum1+sum2

                window = tk.Tk()
                window.wm_title('Result')
                label = ttk.Label(window, text='Issue Price = {}'.format(Sum))
                label.pack(side='top', fill='x', pady=10)
                window.mainloop()
            elif ent3 == True:
                PV = float(e1.get())
                FV = float(e2.get())
                Period = int(e4.get())
                CouponR = float(e5.get())
                pmt = FV * CouponR

                def f(R):
                    return pmt*(1+R)**Period - pmt + FV*R - PV*R*(1+R)**Period
                def simpleton_walk(func):
                    A0 = 0.05
                    current_A = A0
                    step_size = 0.005
                    decay = 0.95

                    loc = []
                    for i in range(50):
                        step_left = current_A - step_size
                        step_right = current_A + step_size

                        if (f(step_left))**2 > (f(step_right))**2:
                            best_step = step_right
                        else:
                            best_step = step_left
                        if (f(best_step))**2 < (f(current_A))**2:
                            current_A = best_step
                            loc.append(best_step)
                            step_size *= decay
                    return loc[-1]
                Rate = simpleton_walk(f)
                window = tk.Tk()
                window.wm_title('Result')
                label = ttk.Label(window, text='Yield Rate(Interest Rate) = {}'.format(Rate))
                label.pack(side='top', fill='x', pady=10)
                window.mainloop()

class PensionPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        ttk.Label(self, text="Savings you have now").grid(row=1)
        ttk.Label(self, text="How much pension u want per period?\n in terms of today's purchasing ability").grid(row=2)
        ttk.Label(self, text='How many years u anticipate to draw pension?').grid(row=3)
        ttk.Label(self, text='How many years left before you retire?').grid(row=4)
        ttk.Label(self, text='What is the interest rate?').grid(row=5)
        ttk.Label(self, text='What is the inflation rate?').grid(row=6)
        ttk.Label(self, text='The amount you need to save per year now').grid(row=7)
        ttk.Label(self, text='Would u consider inflation after retire?').grid(row=8)

        e1 = ttk.Entry(self)
        e2 = ttk.Entry(self)
        e3 = ttk.Entry(self)
        e4 = ttk.Entry(self)
        e5 = ttk.Entry(self)
        e6 = ttk.Entry(self)



        var1 = IntVar()
        var2 = IntVar()

        C1 = Checkbutton(self, variable=var1)
        C2 = Checkbutton(self, variable=var2)

        Button1 = ttk.Button(self, text='Calculate', command=lambda:calculate())
        Button3 = ttk.Button(self, text='Submit', command=lambda:save_input())
        Button2 = ttk.Button(self, text='Home', command=lambda:controller.show_frame(StartPage))

        self.grid(column=0, row=0, columnspan=2, rowspan=9)
        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=3, column=1)
        e4.grid(row=4, column=1)
        e5.grid(row=5, column=1)
        e6.grid(row=6, column=1)



        C1.grid(row=7, column=1)
        C2.grid(row=8, column=1)

        Button1.grid(row=9, column=1)
        Button2.grid(row=9, column=2)
        Button3.grid(row=9, column=0)

        def save_input():

            global entr1
            global entr2

            entr1 = var1.get()
            entr2 = var2.get()

        def calculate():
            print('start calculation')
            if entr1 == True:
                PV = float(e1.get())
                pmt1 = float(e2.get())
                n_a = int(e3.get())
                n_b = int(e4.get())
                IR = float(e5.get())
                FR = float(e6.get())

                if entr2 == False:
                    pmt2 = pmt1 * (1+FR)**n_b
                    print(pmt2)
                    Sum1 = 0
                    for i in range(0, n_a):
                        Sum1 += pmt2/(1+IR)**i
                    print(Sum1)
                    FV = Sum1
                    pmt3 = (PV*IR*(1+IR)**n_b - FV*IR) / ((1+IR)**n_b - 1)

                else:
                    Sum1 = 0
                    for ii in range(0, n_a):
                        pmtii = pmt1 * (1+FR)**(n_b+ii)
                        Sum1 += pmtii/(1+IR)**ii
                    FV2 = Sum1
                    pmt3 = (PV*IR*(1+IR)**n_b - FV2*IR) / ((1+IR)**n_b - 1)
            print('get to the end of calculate')
            window = tk.Tk()
            window.wm_title('Result')
            label = ttk.Label(window, text='amount needs to save per year = {}'.format(pmt3))
            label.pack(side='top', fill='x', pady=10)
            window.mainloop()


app = Financial_calculator()
app.mainloop()
