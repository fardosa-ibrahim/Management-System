from cProfile import label
from logging import root
from tkinter import*
from tkinter import ttk
from tkinter import font
from turtle import width
from PIL import Image,ImageTk
from matplotlib.pyplot import text
from phonenumbers import PhoneNumber


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1430x790+0+0")
        self.root.title("Employee Management System")

        self.var_dep=StringVar()

        hd_title=Label(self.root,text='EMPLOYEEE MANAGEMENT SYSTEM',font=('times new roman',30,'bold'),fg='darkgreen',bg='white')
        hd_title.place(x=0,y=0,width=1430,height=50)

        image_logo=Image.open('Images/logoGreen-removebg-preview.png')
        image_logo=image_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_images=ImageTk.PhotoImage(image_logo)

        self.logo=Label(self.root,image=self.photo_images)
        self.logo.place(x=280,y=0,width=50,height=50)

        img_frame=Frame(self.root,bd=3,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1430,height=160)

        image1=Image.open('Images/undraw_In_the_office_re_jtgc.png')
        image1=image1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(image1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        image2=Image.open('Images/undraw_Working_re_ddwy.png')
        image2=image2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(image2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        image3=Image.open('Images/undraw_design_tools_42tf.png')
        image3=image3.resize((500,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(image3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1290,y=0,width=540,height=160)
        #   main frame
        main_frame=Frame(self.root,bd=3,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=210,width=1275,height=460)

        inner_frame=LabelFrame(main_frame,bd=3,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',11,'bold'),fg='red')
        inner_frame.place(x=10,y=10,width=1380,height=230)


        label_name=Label(inner_frame,font=('arial',12,'bold'),text='Name',bg='white')
        label_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(inner_frame,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)


        label_designition=Label(inner_frame,font=('arial',12,'bold'),text='Designition',bg='white')
        label_designition.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_designition=ttk.Entry(inner_frame,width=22,font=('arial',11,'bold'))
        txt_designition.grid(row=1,column=1,padx=2,pady=7)


        label_email=Label(inner_frame,font=('arial',12,'bold'),text='Email',bg='white')
        label_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(inner_frame,width=22,font=('arial',11,'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=7)


        label_marital_status=Label(inner_frame,font=('arial',12,'bold'),text='Status',bg='white')
        label_marital_status.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        combo_maried=ttk.Combobox(inner_frame,font=('arial',12,'bold'),width=18,state='readonly')
        combo_maried['value']=('Married','Unmarried')
        combo_maried.current(0)
        combo_maried.grid(row=2,column=1,padx=10,pady=10,sticky=W)


        label_bithdate=Label(inner_frame,font=('arial',12,'bold'),text='DateOfBirth',bg='white')
        label_bithdate.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        txt_bithdate=ttk.Entry(inner_frame,width=22,font=('arial',11,'bold'))
        txt_bithdate.grid(row=2,column=3,padx=2,pady=7)


        label_Joiningdate=Label(inner_frame,font=('arial',12,'bold'),text='JoiningDate',bg='white')
        label_Joiningdate.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_joiningdate=ttk.Entry(inner_frame,width=22,font=('arial',11,'bold'))
        txt_joiningdate.grid(row=3,column=1,padx=2,pady=7)


        combo_proof=ttk.Combobox(inner_frame,font=('arial',12,'bold'),width=18,state='readonly')
        combo_proof['value']=("select id proof","Other cards","Driving licence")
        combo_proof.current(0)
        combo_proof.grid(row=4,column=0,padx=10,pady=10,sticky=W)

        txt_proof=ttk.Entry(inner_frame,width=22,font=('arial',11,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)


        txt_name=ttk.Entry(inner_frame,width=22,font=('arial',11,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        combo_dep=ttk.Combobox(inner_frame,textvariable=self.var_dep,font=('arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('select department','Sofware Engineering','HR','Reserch','UI/UX Design','Managerial')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=10,pady=10,sticky=W)


        label_gender=Label(inner_frame,font=('arial',12,'bold'),text='Gender',bg='white')
        label_gender.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        combo_gender=ttk.Combobox(inner_frame,font=('arial',12,'bold'),width=17,state='readonly')
        combo_gender['value']=("Female","Male","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=3,padx=10,pady=10,sticky=W)


        label_MobileNumber=Label(inner_frame,font=('arial',12,'bold'),text='PhoneNumber',bg='white')
        label_MobileNumber.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_mobileNumber=ttk.Entry(inner_frame,width=22,font=('arial',11,'bold'))
        txt_mobileNumber.grid(row=3,column=1,padx=2,pady=7)

        
        image3=Image.open('Images/offices.jpeg')
        image3=image3.resize((200,200),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(image3)

        self.img_3=Label(inner_frame,image=self.photo3)
        self.img_3.place(x=800,y=0,width=200,height=200)

        #  Button
        Button_frame=Frame(inner_frame,bd=3,relief=RIDGE,bg='white')
        Button_frame.place(x=1070,y=10,width=160,height=190)



        btn_add=Button(Button_frame,text='Save',font=('arial',15,'bold'),width=13,bg='green',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(Button_frame,text='Update',font=('arial',15,'bold'),width=13,bg='green',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(Button_frame,text='Delete',font=('arial',15,'bold'),width=13,bg='green',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_reset=Button(Button_frame,text='Reset',font=('arial',15,'bold'),width=13,bg='green',fg='white')
        btn_reset.grid(row=3,column=0,padx=1,pady=5)

  



        label_name=Label(inner_frame,text='Department',font=('arial',11,'bold'),bg='white')
        label_name.grid(row=0,column=0,padx=2,sticky=W)

        inner2_frame=LabelFrame(main_frame,bd=3,relief=RIDGE,bg='white',text='Employee Information Table',font=('times new roman',8,'bold'),fg='red')
        inner2_frame.place(x=10,y=250,width=1380,height=230)


        search_frame=LabelFrame(inner2_frame,bd=3,relief=RIDGE,bg='white',text='Search Employees Information',font=('times new roman',8,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1400,height=50)


        search_by=Label(search_frame,font=('arial',12,'bold'),text='search_by',bg='green',fg="white")
        search_by.grid(row=0,column=1,padx=2,pady=7,sticky=W)

        com_search=ttk.Combobox(search_frame,state='readonly',font=('arial',11,'bold'),width=20)
        com_search['value']=("Select Option","Phone","id_proof")
        com_search.current(0)
        com_search.grid(row=0,column=2,padx=1,sticky=W)


        txt_search=ttk.Entry(search_frame,width=20,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=3,padx=5)

        btn_search=Button(search_frame,text='Search',width=20,font=('arial',11,'bold'),bg='green')
        btn_search.grid(row=0,column=4,padx=5)

        btn_search=Button(search_frame,text='Show All',width=20,font=('arial',11,'bold'),bg='green')
        btn_search.grid(row=0,column=5,padx=5)


        table_frame=Frame(inner2_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=50,width=1250,height=135)

        scrol_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrol_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,column=('depertment','Decignition','Status','phoneNumber','Name','Email','DateOfBirth','Gender','select id proof'),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)

        scrol_x.config(command=self.employee_table.xview)
        scrol_y.config(command=self.employee_table.yview)

        self.employee_table.heading('depertment',text='Department')
        self.employee_table.heading('Decignition',text='Decignition')
        self.employee_table.heading('Status',text='status')
        self.employee_table.heading('phoneNumber',text='PhoneNumber')
        self.employee_table.heading('Name',text='Name')
        self.employee_table.heading('Email',text='Email')
        self.employee_table.heading('DateOfBirth',text='DateOfBirth')
        self.employee_table.heading('Gender',text='Gender')
        self.employee_table.heading('select id proof',text='select id proof')

        self.employee_table['show']='headings'
        self.employee_table.column('depertment',width=100)
        self.employee_table.column('Decignition',width=100)
        self.employee_table.column('Status',width=100)
        self.employee_table.column('phoneNumber',width=100)
        self.employee_table.column('Name',width=100)
        self.employee_table.column('Email',width=100)
        self.employee_table.column('DateOfBirth',width=100)
        self.employee_table.column('Gender',width=100)
        self.employee_table.column('select id proof',width=100)

        self.employee_table.pack(fill=BOTH,expand=1)
        
        # serch_frame=Frame(inner2_frame,bd=3,relief=RIDGE,bg='white')
        # serch_frame.place(x=1070,y=10,width=160,height=180)


if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()