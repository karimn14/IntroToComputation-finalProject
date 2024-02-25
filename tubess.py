from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.config(bg='white')
root.title('MCMC DRIVE')
root.geometry('740x570')
root.iconbitmap(r'c:\Users\Moscha\Downloads\mcdrive.ico')


# SECOND SCREEN
def secWin():
    global sec, sp_secdic1, sp_secdic2
    sec = Toplevel()
    sec.config(bg='yellow',bd=3)
    sec.iconbitmap(r'c:\Users\Moscha\Downloads\mcdrive.ico')
    #sec.geometry('740x590')

    # Adding Menu
    myMenu = Menu(sec)
    sec.config(menu=myMenu)

    myMenu.add_command(label='Food',command=food_menu)
    myMenu.add_command(label='Drinks',command=drinks_menu)
    myMenu.add_command(label='Payment',command=payment_menu)

    sp_secdic1={
        'product1':0,
        'product2':0,
        'product3':0,
        'product4':0,
        'product5':0,
        'product6':0,
        }

    sp_secdic2={
            'product7':0,
            'product8':0,
            'product9':0,
            'product10':0,
            'product11':0,
            'product12':0,
        }

    global sp_sec7, sp_sec8, sp_sec9, sp_sec10, sp_sec11, sp_sec12
    sp_sec7 = Spinbox(sec, values=0)
    sp_sec8= Spinbox(sec, values=0)
    sp_sec9 = Spinbox(sec, values=0)
    sp_sec10 = Spinbox(sec, values=0)
    sp_sec11 = Spinbox(sec, values=0)
    sp_sec12 = Spinbox(sec, values=0)

    global sec7, sec8,sec9,sec10,sec11,sec12
    sec7=Frame(sec)
    sec7.grid(row=0,column=0)
    sec8=Frame(sec)
    sec8.grid(row=0,column=0)
    sec9=Frame(sec)
    sec9.grid(row=0,column=0)
    sec10=Frame(sec)
    sec10.grid(row=0,column=0)
    sec11=Frame(sec)
    sec11.grid(row=0,column=0)
    sec12=Frame(sec)
    sec12.grid(row=0,column=0)

    global third1,third2,third3,thirdsuper
    thirdsuper=Frame(sec)
    thirdsuper.grid(row=0,column=0)
    third1=Frame(sec)
    third1.grid(row=0,column=0)
    third2=Frame(sec)
    third2.grid(row=0,column=0)
    third3=Frame(sec)
    third3.grid(row=0,column=0)

    food_menu()
    
def hideFrame1():
    sec1.grid_forget()
    sec2.grid_forget()
    sec3.grid_forget()
    sec4.grid_forget()    
    sec5.grid_forget()
    sec6.grid_forget()
   
def hideFrame2():
    sec7.grid_forget()
    sec8.grid_forget()
    sec9.grid_forget()
    sec10.grid_forget()
    sec11.grid_forget()
    sec12.grid_forget()

def hideFrame3():
    third1.grid_forget()
    thirdsuper.grid_forget()

global b,sp_secdic1
b = 0
sp_secdic1={
            'product1':0,
            'product2':0,
            'product3':0,
            'product4':0,
            'product5':0,
            'product6':0,}
global sp1,sp2,sp3,sp4,sp5,sp6
sp1=StringVar()
sp2=StringVar()
sp3=StringVar()
sp4=StringVar()
sp5=StringVar()
sp6=StringVar()
def food_menu():
    def food():
        global sec1,sec2,sec3,sec4,sec5,sec6
        sec1 = Frame(sec, width=310,height=310,bg='orange',bd=1)
        sec1.grid(row=0,column=0,padx=3,pady=3)

        sec2 = Frame(sec, width=310,height=310,bg='pink',bd=1)
        sec2.grid(row=0,column=1,padx=3,pady=3)

        sec3 = Frame(sec, width=310,height=310,bg='black',bd=1)
        sec3.grid(row=0,column=2,padx=3,pady=3)

        sec4 = Frame(sec, width=310,height=310,bg='blue',bd=1)
        sec4.grid(row=1,column=0,padx=3,pady=3)

        sec5 = Frame(sec, width=310,height=310,bg='purple',bd=1)
        sec5.grid(row=1,column=1,padx=3,pady=3)

        sec6 = Frame(sec, width=310,height=310,bg='cyan',bd=1)
        sec6.grid(row=1,column=2,padx=3,pady=3)

        ## -IMAGE
        sec1_img = Image.open(r'c:\Users\Moscha\Pictures\display.png').resize((230,230))
        sec1_image = ImageTk.PhotoImage(sec1_img)

        sec2_img = Image.open(r'c:\Users\Moscha\Pictures\topban.jpg').resize((230,230))
        sec2_image = ImageTk.PhotoImage(sec2_img)

        sec3_img = Image.open(r'c:\Users\Moscha\Pictures\topban.jpg').resize((230,230))
        sec3_image = ImageTk.PhotoImage(sec3_img)

        sec4_img = Image.open(r'c:\Users\Moscha\Pictures\topban.jpg').resize((230,230))
        sec4_image = ImageTk.PhotoImage(sec4_img)

        sec5_img = Image.open(r'c:\Users\Moscha\Pictures\topban.jpg').resize((230,230))
        sec5_image = ImageTk.PhotoImage(sec5_img)

        sec6_img = Image.open(r'c:\Users\Moscha\Pictures\topban.jpg').resize((230,230))
        sec6_image = ImageTk.PhotoImage(sec6_img)

        ## -LABEL
        img_lab1 = Label(sec1,image=sec1_image,text='Product #1',compound='bottom')
        img_lab1.image = sec1_image
        img_lab1.grid(row=0,column=0,columnspan=2)

        amount_sec1 = Label(sec1, text='Amount: ')
        amount_sec1.grid(row=1,column=0,sticky=EW)

        img_lab2 = Label(sec2,image=sec2_image,text='Product #2',compound='bottom')
        img_lab2.image = sec2_image
        img_lab2.grid(row=0,column=0,columnspan=2)
    
        amount_sec2 = Label(sec2, text='Amount: ')
        amount_sec2.grid(row=1,column=0,sticky=EW)

        img_lab3 = Label(sec3,image=sec3_image,text='Product #3',compound='bottom')
        img_lab3.image = sec3_image
        img_lab3.grid(row=0,column=0,columnspan=2)

        amount_sec3 = Label(sec3, text='Amount: ')
        amount_sec3.grid(row=1,column=0,sticky=EW)

        img_lab4 = Label(sec4,image=sec4_image,text='Product #4',compound='bottom')
        img_lab4.image = sec4_image
        img_lab4.grid(row=0,column=0,columnspan=2)

        amount_sec4 = Label(sec4, text='Amount: ')
        amount_sec4.grid(row=1,column=0,sticky=EW)

        img_lab5 = Label(sec5,image=sec5_image,text='Product #5',compound='bottom')
        img_lab5.image = sec5_image
        img_lab5.grid(row=0,column=0,columnspan=2)

        amount_sec5 = Label(sec5, text='Amount: ')
        amount_sec5.grid(row=1,column=0,sticky=EW)

        img_lab6 = Label(sec6,image=sec6_image,text='Product #6',compound='bottom')
        img_lab6.image = sec6_image
        img_lab6.grid(row=0,column=0,columnspan=2)

        amount_sec6 = Label(sec6, text='Amount: ')
        amount_sec6.grid(row=1,column=0,sticky=EW)

        
        ## -SPINBOX
        global sp_sec1, sp_sec2, sp_sec3, sp_sec4, sp_sec5, sp_sec6,sp_secdic1,b
        if b == 0:
            sp_sec1 = Spinbox(sec1, from_=0,to=10,)
            sp_sec1.grid(row=1,column=1,sticky=EW)

            sp_sec2 = Spinbox(sec2, from_=0,to=10,)
            sp_sec2.grid(row=1,column=1,sticky=EW)

            sp_sec3 = Spinbox(sec3, from_=0,to=10,)
            sp_sec3.grid(row=1,column=1,sticky=EW)    

            sp_sec4 = Spinbox(sec4, from_=0,to=10,)
            sp_sec4.grid(row=1,column=1,sticky=EW)

            sp_sec5 = Spinbox(sec5, from_=0,to=10,)
            sp_sec5.grid(row=1,column=1,sticky=EW)    

            sp_sec6 = Spinbox(sec6, from_=0,to=10,)
            sp_sec6.grid(row=1,column=1,sticky=EW)   

            sp_secdic1['product1'] = sp_sec1.get()
            sp_secdic1['product2'] = sp_sec2.get()
            sp_secdic1['product3'] = sp_sec3.get()
            sp_secdic1['product4'] = sp_sec4.get()
            sp_secdic1['product5'] = sp_sec5.get()
            sp_secdic1['product6'] = sp_sec6.get()
            b += 1
        else:
            sp_sec1 = Spinbox(sec1, from_=0,to=10,textvariable=sp1)
            sp1.set(sp_secdic1['product1'])
            sp_sec1.grid(row=1,column=1,sticky=EW)

            sp_sec2 = Spinbox(sec2, from_=0,to=10,textvariable=sp2)
            sp2.set(sp_secdic1['product2'])
            sp_sec2.grid(row=1,column=1,sticky=EW)

            sp_sec3 = Spinbox(sec3, from_=0,to=10,textvariable=sp3)
            sp3.set(sp_secdic1['product3'])
            sp_sec3.grid(row=1,column=1,sticky=EW)    

            sp_sec4 = Spinbox(sec4, from_=0,to=10,textvariable=sp4)
            sp4.set(sp_secdic1['product4'])
            sp_sec4.grid(row=1,column=1,sticky=EW)

            sp_sec5 = Spinbox(sec5, from_=0,to=10,textvariable=sp5)
            sp5.set(sp_secdic1['product5'])
            sp_sec5.grid(row=1,column=1,sticky=EW)    

            sp_sec6 = Spinbox(sec6, from_=0,to=10,textvariable=sp6)
            sp6.set(sp_secdic1['product6'])
            sp_sec6.grid(row=1,column=1,sticky=EW)
        
    hideFrame2()
    hideFrame3()
    food()

global c,sp_secdic2
c = 0
sp_secdic2={
    'product7':0,
    'product8':0,
    'product9':0,
    'product10':0,
    'product11':0,
    'product12':0,}
global sp7,sp8,sp9,sp10,sp11,sp12
sp7=StringVar()
sp8=StringVar()
sp9=StringVar()
sp10=StringVar()
sp11=StringVar()
sp12=StringVar()
def drinks_menu():
    def drinks():
        global sec7, sec8, sec9,sec10,sec11, sec12
        sec7 = Frame(sec, width=310,height=310,bg='orange',bd=1)
        sec7.grid(row=0,column=0,padx=3,pady=3)

        sec8 = Frame(sec, width=310,height=310,bg='pink',bd=1)
        sec8.grid(row=0,column=1,padx=3,pady=3)

        sec9 = Frame(sec, width=310,height=310,bg='black',bd=1)
        sec9.grid(row=0,column=2,padx=3,pady=3)

        sec10 = Frame(sec, width=310,height=310,bg='blue',bd=1)
        sec10.grid(row=1,column=0,padx=3,pady=3)

        sec11 = Frame(sec, width=310,height=310,bg='purple',bd=1)
        sec11.grid(row=1,column=1,padx=3,pady=3)

        sec12 = Frame(sec, width=310,height=310,bg='cyan',bd=1)
        sec12.grid(row=1,column=2,padx=3,pady=3)

        ## -IMAGE
        sec7_img = Image.open(r'c:\Users\Moscha\Pictures\display.png').resize((230,230))
        sec7_image = ImageTk.PhotoImage(sec7_img)

        sec8_img = Image.open(r'c:\Users\Moscha\Pictures\topban.jpg').resize((230,230))
        sec8_image = ImageTk.PhotoImage(sec8_img)

        sec9_img = Image.open(r'c:\Users\Moscha\Pictures\display.png').resize((230,230))
        sec9_image = ImageTk.PhotoImage(sec9_img)

        sec10_img = Image.open(r'c:\Users\Moscha\Pictures\topban.jpg').resize((230,230))
        sec10_image = ImageTk.PhotoImage(sec10_img)

        sec11_img = Image.open(r'c:\Users\Moscha\Pictures\topban.jpg').resize((230,230))
        sec11_image = ImageTk.PhotoImage(sec11_img)

        sec12_img = Image.open(r'c:\Users\Moscha\Pictures\topban.jpg').resize((230,230))
        sec12_image = ImageTk.PhotoImage(sec12_img)

        ## -LABEL
        img_lab7 = Label(sec7,image=sec7_image,text='Product #7',compound='bottom')
        img_lab7.image = sec7_image
        img_lab7.grid(row=0,column=0,columnspan=2)

        amount_sec7 = Label(sec7, text='Amount: ')
        amount_sec7.grid(row=1,column=0,sticky=EW)

        img_lab8 = Label(sec8,image=sec8_image,text='Product #8',compound='bottom')
        img_lab8.image = sec8_image
        img_lab8.grid(row=0,column=0,columnspan=2)

        amount_sec8 = Label(sec8, text='Amount: ')
        amount_sec8.grid(row=1,column=0,sticky=EW)

        img_lab9 = Label(sec9,image=sec9_image,text='Product #9',compound='bottom')
        img_lab9.image = sec9_image
        img_lab9.grid(row=0,column=0,columnspan=2)

        amount_sec9 = Label(sec9, text='Amount: ')
        amount_sec9.grid(row=1,column=0,sticky=EW)

        img_lab10 = Label(sec10,image=sec10_image,text='Product #10',compound='bottom')
        img_lab10.image = sec10_image
        img_lab10.grid(row=0,column=0,columnspan=2)

        amount_sec10 = Label(sec10, text='Amount: ')
        amount_sec10.grid(row=1,column=0,sticky=EW)

        img_lab11 = Label(sec11,image=sec11_image,text='Product #11',compound='bottom')
        img_lab11.image = sec11_image
        img_lab11.grid(row=0,column=0,columnspan=2)

        amount_sec11 = Label(sec11, text='Amount: ')
        amount_sec11.grid(row=1,column=0,sticky=EW)

        img_lab12 = Label(sec12,image=sec12_image,text='Product #12',compound='bottom')
        img_lab12.image = sec12_image
        img_lab12.grid(row=0,column=0,columnspan=2)

        amount_sec12 = Label(sec12, text='Amount: ')
        amount_sec12.grid(row=1,column=0,sticky=EW)

        
        ## -SLIDER
        global sp_sec7, sp_sec8, sp_sec9, sp_sec10, sp_sec11, sp_sec12,sp_secdic2,c
        if c == 0:
            sp_sec7 = Spinbox(sec7, from_=0,to=10,)
            sp_sec7.grid(row=1,column=1,sticky=EW)

            sp_sec8 = Spinbox(sec8, from_=0,to=10,)
            sp_sec8.grid(row=1,column=1,sticky=EW)

            sp_sec9 = Spinbox(sec9, from_=0,to=10,)
            sp_sec9.grid(row=1,column=1,sticky=EW)    

            sp_sec10 = Spinbox(sec10, from_=0,to=10,)
            sp_sec10.grid(row=1,column=1,sticky=EW)

            sp_sec11 = Spinbox(sec11, from_=0,to=10,)
            sp_sec11.grid(row=1,column=1,sticky=EW)    

            sp_sec12 = Spinbox(sec12, from_=0,to=10,)
            sp_sec12.grid(row=1,column=1,sticky=EW)   

            sp_secdic2['product7'] = sp_sec7.get()
            sp_secdic2['product8'] = sp_sec8.get()
            sp_secdic2['product9'] = sp_sec9.get()
            sp_secdic2['product10'] = sp_sec10.get()
            sp_secdic2['product11'] = sp_sec11.get()
            sp_secdic2['product12'] = sp_sec12.get()
            c += 1
        else:
            sp_sec7 = Spinbox(sec7, from_=0,to=10,textvariable=sp7)
            sp7.set(sp_secdic2['product7'])
            sp_sec7.grid(row=1,column=1,sticky=EW)

            sp_sec8 = Spinbox(sec8, from_=0,to=10,textvariable=sp8)
            sp8.set(sp_secdic2['product8'])
            sp_sec8.grid(row=1,column=1,sticky=EW)

            sp_sec9 = Spinbox(sec9, from_=0,to=10,textvariable=sp9)
            sp9.set(sp_secdic2['product9'])
            sp_sec9.grid(row=1,column=1,sticky=EW)    

            sp_sec10 = Spinbox(sec10, from_=0,to=10,textvariable=sp10)
            sp10.set(sp_secdic2['product10'])
            sp_sec10.grid(row=1,column=1,sticky=EW)

            sp_sec11 = Spinbox(sec11, from_=0,to=10,textvariable=sp11)
            sp11.set(sp_secdic2['product11'])
            sp_sec11.grid(row=1,column=1,sticky=EW)    

            sp_sec12 = Spinbox(sec12, from_=0,to=10,textvariable=sp12)
            sp12.set(sp_secdic2['product12'])
            sp_sec12.grid(row=1,column=1,sticky=EW)

    hideFrame1()
    hideFrame3()
    drinks()
    
def payment_menu():
    global sp_secdic1,sp_secdic2
    sp_secdic1['product1'] = sp_sec1.get()
    sp_secdic1['product2'] = sp_sec2.get()
    sp_secdic1['product3'] = sp_sec3.get()
    sp_secdic1['product4'] = sp_sec4.get()
    sp_secdic1['product5'] = sp_sec5.get()
    sp_secdic1['product6'] = sp_sec6.get()
    sp_secdic2['product7'] = sp_sec7.get()
    sp_secdic2['product8'] = sp_sec8.get()
    sp_secdic2['product9'] = sp_sec9.get()
    sp_secdic2['product10'] = sp_sec10.get()
    sp_secdic2['product11'] = sp_sec11.get()
    sp_secdic2['product12'] = sp_sec12.get()

    print(sp_secdic1)
    print('')
    print(sp_secdic2)

    def pay():
        prices = {
            'product1':24,
            'product2':21,
            'product3':23,
            'product4':24,
            'product5':5,
            'product6':14,
            'product7':24,
            'product8':21,
            'product9':23,
            'product10':24,
            'product11':5,
            'product12':14,
        }
        ## - FRAMES
        global third1,third2,third3,thirdsuper
        third1 = Frame(sec, bg='orange',width=430,height=900)
        third1.grid(row=0,column=0, rowspan=2,padx=2,pady=4,sticky=NW)
        third1.grid_propagate(True)

        # -----
        third11 = Frame(third1, bg='red',width=420,height=258,relief=RIDGE)
        third11.grid(row=1,column=0,padx=4,pady=2,sticky=EW)
        third11.grid_propagate(True)

        third11_prd = LabelFrame(third11,text='Product Name', bg=third11.cget('bg'),width=303,height=258,labelanchor=NW,font=('Norwester',10))
        third11_prd.grid(row=0,column=0,padx=2,pady=2,sticky=EW)
        third11_prd.grid_propagate(False)

        third11_prc = LabelFrame(third11,text='Price', bg=third11.cget('bg'),width=45,height=258,labelanchor=NW,font=('Norwester',10))
        third11_prc.grid(row=0,column=1,padx=2,pady=2,sticky=NSEW)
        third11_prc.grid_propagate(False)

        third11_amo = LabelFrame(third11,text='Amount',bg=third11.cget('bg'),width=67,height=258,labelanchor=NW,font=('Norwester',10))
        third11_amo.grid(row=0,column=2,padx=2,pady=2,sticky=EW)
        third11_amo.grid_propagate(False)

        # -----
        third12 = Frame(third1, bg='red',width=420,height=258)
        third12.grid(row=2,column=0,padx=4,pady=2)
        third12.grid_propagate(True)

        third12_prd = LabelFrame(third12,text='Product Name',bg=third12.cget('bg'),width=303,height=258,labelanchor=NW,font=('Norwester',10))
        third12_prd.grid(row=0,column=0,padx=2,pady=2,sticky=EW)
        third12_prd.grid_propagate(False)

        third12_prc = LabelFrame(third12,text='Price', bg=third12.cget('bg'),width=45,height=258,labelanchor=NW,font=('Norwester',10))
        third12_prc.grid(row=0,column=1,padx=2,pady=2,sticky=EW)
        third12_prc.grid_propagate(False)

        third12_amo =LabelFrame(third12,text='Amount', bg=third12.cget('bg'),width=67,height=258,labelanchor=NW,font=('Norwester',10))
        third12_amo.grid(row=0,column=2,padx=2,pady=2,sticky=EW)
        third12_amo.grid_propagate(False)

        # ------
        thirdsuper = Frame(sec, bg='red',width=290,height=630)
        thirdsuper.grid(row=0,column=1,padx=3,pady=2,sticky=N)

        third2 = Frame(thirdsuper, bg='orange',width=290,height=310)
        third2.grid(row=0,column=0,padx=3,pady=2,sticky=NW)
        third3 = Frame(thirdsuper, bg='orange',width=290,height=230)
        third3.grid(row=1,column=0,padx=3,pady=3,sticky=NW)


        cc_frame1=Frame(third3,bg=third3.cget('bg'),width=140,height=43)
        cc_frame1.grid(row=5,column=0, sticky=NSEW,padx=3)
        cc_frame1.grid_propagate(False)
        cc_frame2=Frame(third3,bg=third3.cget('bg'),width=140,height=43)
        cc_frame2.grid(row=5,column=1, sticky=NSEW,padx=3)
        cc_frame2.grid_propagate(False)

        cc_frame1.columnconfigure(0, weight=1)   
        cc_frame1.rowconfigure(0, weight=1)
        cc_frame2.columnconfigure(0, weight=1)
        cc_frame2.rowconfigure(0, weight=1)   

        ## = LABELS
        orderlist_lab = Label(third1, text='ORDER LIST',bg=third1.cget('bg'),font=("Norwester",16))
        orderlist_lab.grid(row=0,column=0,padx=5, pady=3 ,sticky=NW)

        sp1_list=['product1','product2','product3','product4','product5','product6']
        sp1_lis2=['product7','product8','product9','product10','product11','product12']

        global total_int
        total_int = 0
        for idx,i in enumerate(sp1_list[:]):
            if int(sp_secdic1[i]) > 0 :
                x = Label(third11_prd,text=i,justify=LEFT,font=('Comic Sans Ms',14),bg=third11.cget('bg'))
                x.grid(row=idx,column=0,padx=2,pady=2)
                y = Label(third11_prc,text=prices[i],justify=RIGHT,font=('Comic Sans Ms',14),bg=third11.cget('bg'))
                y.grid(row=idx,column=0,padx=2,pady=2,sticky=E)
                z = Label(third11_amo,text=sp_secdic1[i],justify=RIGHT,font=('Comic Sans Ms',14),bg=third11.cget('bg'))
                z.grid(row=idx,column=0,padx=2,pady=2,sticky=E)

                total_int += int(z.cget('text'))*int(y.cget('text'))

        for idx,i in enumerate(sp1_lis2[:]):
            if int(sp_secdic2[i]) > 0 :
                p = Label(third12_prd,text=i,justify=LEFT,font=('Comic Sans Ms',14),bg=third11.cget('bg'))
                p.grid(row=idx,column=0,sticky=W,padx=2,pady=2)
                q = Label(third12_prc,text=prices[i],justify=CENTER,font=('Comic Sans Ms',14),bg=third11.cget('bg'))
                q.grid(row=idx,column=0,sticky=EW,padx=2,pady=2)
                r = Label(third12_amo,text=sp_secdic2[i],justify=CENTER,font=('Comic Sans Ms',14),bg=third11.cget('bg'))
                r.grid(row=idx,column=0,sticky=EW,padx=2,pady=2)

                total_int += int(r.cget('text'))*int(q.cget('text'))

        ### DISCOUNT SECTION ###
        disc_list=['123','456','789']
        disc_lab = Label(third2, text="DISCOUNT CODE:",bg=third2.cget('bg'))
        disc_lab.grid(row=0,column=0,padx=3,pady=3,sticky=W)
        disc_entry = Entry(third2, bd=3)
        disc_entry.grid(row=0,column=1,padx=3,pady=3,sticky=W)

        def check_discount():
            if(disc_entry.get())in disc_list:
                total_int_afdisc = round(total_int*0.7, 2)
                total_afdisc_lab = Label(third3,text='TOTAL : ',justify=LEFT,bg=third3.cget('bg'),font=('Mandalore', 30, 'bold'))
                total_afdisc_lab.grid(row=1,column=0,padx=3,pady=3,sticky=W)
                total_int_afdisc_lab = Label(third3,text=str(total_int_afdisc)+ '$',justify=RIGHT,bg=third3.cget('bg'),font=('Mandalore', 30, 'bold'))
                total_int_afdisc_lab.grid(row=1,column=1,padx=3,pady=3,sticky=E)
                congrats_lab = Label(third3, text="Congrats, you're having 30% discount",bg=third3.cget('bg'))
                congrats_lab.grid(row=2,column=0, columnspan=2, padx=3,pady=3)
                root.messagebox.showinfo('Congrats!', 'You get 30% discount' )
                root.deiconify()
                root.destroy()

                return disc_list

             #harga barang*discount
            else:
                root.messagebox.showwarning('Error!','Please enter the right discount code' )
                root.deiconify()
                root.destroy()
            
        checkdisc_but = Button(third2, text= "CHECK", command= check_discount)
        checkdisc_but.grid(row=0,column=3, padx=3,pady=3,sticky=EW)
        ########################
        ### TOTAL SECTION ###
        total_lab = Label(third3,text='TOTAL : ',justify=LEFT,bg=third3.cget('bg'),font=('Mandalore', 20, 'bold'))
        total_lab.grid(row=0,column=0,padx=3,pady=3,sticky=W)
        total_int_lab = Label(third3, text=str(total_int)+' $ ',justify=RIGHT,bg=third3.cget('bg'),font=('Mandalore', 20, 'bold'))
        total_int_lab.grid(row=0,column=1,padx=3,pady=3,sticky=E)

        skip = Label(third3, text='',bg=third3.cget('bg')).grid(row=3,column=0,columnspan=2,)
        ### PAYMENT SECTION ###
        slcpay_lab = Label(third3, text='SELECT PAYMENT',font=('Mandalore', 20, 'bold'),bg=third3.cget('bg'))
        slcpay_lab.grid(row=4,column=0,columnspan=2,padx=2,pady=3,sticky=W)        

        ## - BUTTON
        pay_but = Button(third3, text="PAY",command=lambda:sec.quit(),bg='red')
        pay_but.grid(row=7,column=0,padx=3,pady=3,columnspan=2,rowspan=2,sticky=EW)

        global a
        a=0
        def cashout():
            global cb_lab1,a
            if a == 0:
                cb_lab1 = Label(third3,text="Please pay the bills at cashier",bg=third3.cget('bg'))
                a += 1
                return cb_lab1.grid(row=6,column=0,padx=3,pady=3,columnspan=2)
            else:
                credit_box.deselect()
                cb_lab1 = Label(third3,text="Please pay the bills at cashier",bg=third3.cget('bg'))
                return cb_lab1.grid(row=6,column=0,padx=3,pady=3,columnspan=2,sticky=W),cb_entry.destroy(),cb_lab2.destroy()

        def creditnum():
            global cb_entry,cb_lab2,a
            if a == 0:
                cb_lab2 = Label(third3, text='CREDIT CARD NUMBER',bg=third3.cget('bg'))
                cb_entry = Entry(third3,bd=3)
                a+=1
                return cb_lab2.grid(row=6,column=0,padx=3,pady=3),cb_entry.grid(row=6,column=1,padx=3,pady=3)
            else:
                cash_box.deselect()
                cb_lab2 = Label(third3,text='CREDIT CARD NUMBER',bg=third3.cget('bg'))
                cb_entry = Entry(third3,bd=3)
                return cb_lab2.grid(row=6,column=0,padx=3,pady=3,sticky=W),cb_entry.grid(row=6,column=1,padx=3,pady=3),cb_lab1.destroy()

        cb1 = BooleanVar()
        cb2 = BooleanVar()
        cash_box = Checkbutton(cc_frame1,variable=cb1,command=cashout,onvalue=True,offvalue=False,text="CASH",font=('Mandalore', 14),bg=third3.cget('bg'),justify=LEFT)
        cash_box.grid(row=0,column=0,padx=3,pady=3,sticky=EW)
        credit_box = Checkbutton(cc_frame2,variable=cb2,command=creditnum,onvalue=True,offvalue=False,text="CREDIT",font=('Mandalore', 14),bg=third3.cget('bg'),justify=LEFT)
        credit_box.grid(row=0,column=0,padx=3,pady=3,sticky=EW)

    hideFrame1()
    hideFrame2()
    pay()


# FIRST SCREEN
## -FRAME
mainFrame1 = Frame(root, bg='white', bd=1)
mainFrame1.place(relx=0.5,rely=0.5,anchor=CENTER)

## -IMAGE
img = Image.open(r'c:\Users\Moscha\Downloads\mcdrive.ico').resize((230,230))
image = ImageTk.PhotoImage(img)
lab_img = Label(mainFrame1,image=image)
lab_img.grid(row=0,column=0,columnspan=2)

## -LABEL 
first = Label(mainFrame1, text='ORDER HERE', bg='white',fg='red', font=('MANDALORE',22))
first.grid(row=1,column=0,columnspan=2,sticky=N)
second = Label(mainFrame1, text='PLEASE CHOOSE', bg='white',fg='red',font=('Againts', 14))
second.grid(row=2,column=0,columnspan=2,sticky=N)

## -BUTTON
dine_but = Button(mainFrame1, text='DINE IN', bg='white',fg='red',font=('Againts',13),command=secWin)
dine_but.grid(row=3,column=0)
take_but = Button(mainFrame1, text='TAKE AWAY', bg='white',fg='red',font=('Againts',13),command=secWin)
take_but.grid(row=3,column=1)

root.mainloop()