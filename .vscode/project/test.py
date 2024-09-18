from tkinter import *
from tkinter import ttk
from beem.blockchain import Blockchain
from datetime import datetime

class BillClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System  |  Developed By Aman Kothari")
        self.root.config(bg="white")

        # Title
        self.icon_title = PhotoImage(file="logo1.png")
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="orange", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # Logout Button
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 20, "bold"), bg="yellow", cursor="hand2")
        btn_logout.place(x=1150, y=10, height=50, width=150)

        #====Clock====
        self.lbl_clock = Label(self.root, text="", font=("times new roman", 15), bg="green", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.tick()

        #====Product Frame====
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE)
        ProductFrame1.place(x=6,y=110,width=410,height=550)

        ptitle= Label(ProductFrame1,text="All Products",font=("goudy old style",20),bg="#262626",fg="white").pack(side=TOP,fill=X)

        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search= Label(ProductFrame2,text="Search Product | By Name ",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_search= Label(ProductFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)
        txt_search= Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=47,width=150,height=22)
        btn_search= Button(ProductFrame2,text="Search",font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=280,y=45,width=100,height=25)
        btn_show_all= Button(ProductFrame2,text="Show All",font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=280,y=10,width=100,height=25)
   
        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=375)
        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set,show="headings")

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)
      
        self.ProductTable.heading("pid",text="PID")
        self.ProductTable.heading("name",text="Name")
        self.ProductTable.heading("price",text="Price")
        self.ProductTable.heading("qty",text="Quantity")
        self.ProductTable.heading("status",text="Status")

        self.ProductTable["show"]="headings"

        self.ProductTable.column("pid",width=90)
        self.ProductTable.column("name",width=100)
        self.ProductTable.column("price",width=100)
        self.ProductTable.column("qty",width=100)
        self.ProductTable.column("status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)

        #self.ProductTable.bind("<ButtonRelease-1>",self.get_data)
        lbl_note= Label(ProductFrame1,text="Note: 'Enter 0 Quantity to remove product from the cart'",font=("goudy old style",13),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)

#========Customer Frame========
        self.var_cname=StringVar()
        self.var_contact=StringVar()

        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE)
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        ctitle= Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)

        lbl_name= Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white").place(x=5,y=35)
        txt_name= Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_contact= Label(CustomerFrame,text="Contact No.",font=("times new roman",15),bg="white").place(x=270,y=35)
        txt_contact= Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)

        #===Cal Cart Frame===#
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE)
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)

        #===Calculator Frame===#
        self.var_cal_input=StringVar()

        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)

        self.txt_cal_input= Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        self.txt_cal_input.grid(row=0,columnspan=4)

        btn_7= Button(Cal_Frame,text='7',font=('arial',15,'bold',),command=lambda:self.get_input(7),cursor="hand2",bd=5,width=4,pady=10).grid(row=1,column=0)
        btn_8= Button(Cal_Frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),cursor="hand2",bd=5,width=4,pady=10).grid(row=1,column=1)
        btn_9= Button(Cal_Frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),cursor="hand2",bd=5,width=4,pady=10).grid(row=1,column=2)
        btn_sum= Button(Cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),cursor="hand2",bd=5,width=4,pady=10).grid(row=1,column=3)

        btn_4= Button(Cal_Frame,text='4',font=('arial',15,'bold',),command=lambda:self.get_input(4),cursor="hand2",bd=5,width=4,pady=10).grid(row=2,column=0)
        btn_5= Button(Cal_Frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),cursor="hand2",bd=5,width=4,pady=10).grid(row=2,column=1)
        btn_6= Button(Cal_Frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),cursor="hand2",bd=5,width=4,pady=10).grid(row=2,column=2)
        btn_sub= Button(Cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),cursor="hand2",bd=5,width=4,pady=10).grid(row=2,column=3)

        btn_1= Button(Cal_Frame,text='1',font=('arial',15,'bold',),command=lambda:self.get_input(1),cursor="hand2",bd=5,width=4,pady=10).grid(row=3,column=0)
        btn_2= Button(Cal_Frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),cursor="hand2",bd=5,width=4,pady=10).grid(row=3,column=1)
        btn_3= Button(Cal_Frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),cursor="hand2",bd=5,width=4,pady=10).grid(row=3,column=2)
        btn_mul= Button(Cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),cursor="hand2",bd=5,width=4,pady=10).grid(row=3,column=3)

        btn_0= Button(Cal_Frame,text='0',font=('arial',15,'bold',),command=lambda:self.get_input(0),cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=0)
        btn_c= Button(Cal_Frame,text='c',font=('arial',15,'bold'),command=self.clear_cal,cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=1)
        btn_eq= Button(Cal_Frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=2)
        btn_div= Button(Cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=3)


        #===Cart Frame===#
        Cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        Cart_Frame.place(x=280,y=8,width=245,height=342)
        cartTitle= Label(Cart_Frame,text="Cart \t Total Product: [0]",font=("goudy old style",15),bg="lightgray").pack(side=TOP,fill=X)

        scrolly=Scrollbar(Cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(Cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(Cart_Frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set, xscrollcommand=scrollx.set,show="headings")

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
      
        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY.")
        self.CartTable.heading("status",text="Status")

        self.CartTable["show"]="headings"

        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=100)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        self.CartTable.column("status",width=90)
        self.CartTable.pack(fill=BOTH,expand=1)

        #self.CartTable.bind("<ButtonRelease-1>",self.get_data)

        #====ADD CART BUTTONS====
        self.var_pid= StringVar()
        self.var_pname= StringVar()
        self.var_price= StringVar()
        self.var_qty= StringVar()
        self.var_status= StringVar()

        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=550,width=530,height=110)

        lbl_p_name= Label(Cal_Cart_Frame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name= Entry(Cal_Cart_Frame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_p_price= Label(Cal_Cart_Frame,text="Price per Qty.",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price= Entry(Cal_Cart_Frame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)

        
        lbl_p_qty= Label(Cal_Cart_Frame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty= Entry(Cal_Cart_Frame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)
    
        self.lbl_inStock= Label(Cal_Cart_Frame,text="InStock [9999]",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)

        btn_clear_cart=Button(Cal_Cart_Frame,text="Clear",font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Cal_Cart_Frame,text="Add | Update Cart",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
    

#==============Billing Area==================
        BillFrame= Frame(self.root,bd=2,relief=RIDGE,bg='white')
        BillFrame.place(x=953,y=110,width=410,height=410)

        Btitle= Label(BillFrame,text="Customer Bill Area",font=("goudy old style",20),bg="red",fg="white").pack(side=TOP,fill=X)
        scrolly= Scrollbar(BillFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.txt_bill_area= Text(BillFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

#=============Biling Area=================
        BillMenuFrame= Frame(self.root,bd=2,relief=RIDGE,bg='white')
        BillMenuFrame.place(x=953,y=520,width=410,height=140)
        
        self.lbl_amnt= Label(BillMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)

        self.lbl_discount= Label(BillMenuFrame,text="Discount\n[%5]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay= Label(BillMenuFrame,text="Net Pay\n[0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)

        btn_print= Button(BillMenuFrame,text="Print",cursor='hand2',font=("goudy old style",15,"bold"),bg="lightgreen",fg="white")
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear= Button(BillMenuFrame,text="Clear All",cursor='hand2',font=("goudy old style",15,"bold"),bg="gray",fg="white")
        btn_clear.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(BillMenuFrame,text="Generate/Save Bill",cursor='hand2',font=("goudy old style",15,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=246,y=80,width=160,height=50)

#================Footer=======================
        Footer = Label(self.root, text="IMS-Inventory Management System\n For any Technical Issue Contact: CodeCrusaders", font=("times new roman", 12), bg="Darkblue", fg="white")
        Footer.place(x=0, y=750, relwidth=1, height=50)  

        Footer2 = Label(self.root, text="IMS-Inventory Management System\n For any Technical Issue Contact: CodeCrusaders", font=("times new roman", 12), bg="Darkblue", fg="white")
        Footer2.place(x=0, y=750, relwidth=1, height=50)

        blockchain = Blockchain()
        latest_block = blockchain.get_current_block_num()

        footer_text = f"Latest Hive Block: {latest_block}"
        Footer2.config(text=footer_text)
#===================All Functions====================
    def get_input(self,num):
        xnum= self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')
    
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
    
    def tick(self):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {date_time}")
        self.lbl_clock.after(1000, self.tick)
    


if __name__=="__main__":
    root = Tk()
    obj = BillClass(root)
    root.mainloop()