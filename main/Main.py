from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import mysql.connector,datetime,os

from Admin_1 import admin__1
from Admin_2 import admin__2

'''
main - Main Menu has options of mystocks or allstocks
       mystocks 
              mystocks_login - For user to login

                     insert_into_mystocks - Accepts a stock's details
                            insert_enter - Inserts stock details into database

                     view_stock - View stocks in the user's table

                     viewstock - View all stocks that the program can use

                     plot_one - Accepts details of one specific stock to be plotted
                            st_comp_one - Plots the graph using accepted details

                     plot_compare - Accepts details of one specific stock to be plotted
                            plot_compare_1 - Plots the graph using accepted details

                     delete_record - Displays buttons of all recorded stocks
                            delete_stock - Deletes the clicked stock

              mystocks_signup

                     insert_into_mystocks - Accepts a stock's details
                            insert_enter - Inserts stock details into database

                     view_stock - View stocks in the user's table

                     viewstock - View all stocks that the program can use

                     plot_one - Accepts details of one specific stock to be plotted
                            st_comp_one - Plots the graph using accepted details

                     plot_compare - Accepts details of one specific stock to be plotted
                            plot_compare_1 - Plots the graph using accepted details

                     delete_record - Displays buttons of all recorded stocks
                            delete_stock - Deletes the clicked stock     
       allstocks

              viewstock - View all stocks available to program

              
              plot_one - Accepts details of one specific stock to be plotted
                     st_comp_one - Plots the graph using accepted details

              plot_compare - Accepts details of one specific stock to be plotted
                     plot_compare_1 - Plots the graph using accepted details 
       
       misc

              insert_into_stock_checklist - Creates keyword table

              create_table - Program to create tables that do not exist

              check_entry_in_db - Checks whether input stock is available to program

       main
              main_menu - Main program
'''                  
#------------------------------------------------------------------------------------------------------

def mystocks():

       global mystocks_level

       mystocks_level=Toplevel()
       mystocks_level.title('LOGIN')
       mystocks_level.configure(background='#318f4a')

       Label(mystocks_level, text='\n'+"_"*150+'\n',bg='#318f4a').grid(row=0, column=0,columnspan=4)       

       Label(mystocks_level, text='LOGIN',font=('Times New Roman',13),
              bg='black',fg='white',relief='raised',width = 20).grid(row=1, column=1)
       Label(mystocks_level, text='Username:',font=('Times New Roman',11),
              bg='#318f4a',fg='white',width = 20).grid(row=2, column=0)
       Label(mystocks_level, text='Password:',font=('Times New Roman',11),
              bg='#318f4a',fg=F'white',width = 20).grid(row=3, column=0)

       e_un=Entry(mystocks_level, width=30)
       e_un.grid(row=2, column=2)
       e_pwd=Entry(mystocks_level, width=30)
       e_pwd.grid(row=3, column=2)

       Label(mystocks_level, text='\n'+"_"*150+'\n',bg='#318f4a').grid(row=4, column=0,columnspan=4)
       
       Label(mystocks_level, text='SIGN UP',font=('Times New Roman',13),
              bg='black',fg='white',relief='raised',width = 20).grid(row=5, column=1)
       Label(mystocks_level, text='Username:',font=('Times New Roman',11),
              bg='#318f4a',fg='white',width = 20).grid(row=6, column=0)
       Label(mystocks_level, text='Password:',font=('Times New Roman',11),
              bg='#318f4a',fg='white',width = 20).grid(row=7, column=0)

       e_un_s=Entry(mystocks_level, width=30)
       e_un_s.grid(row=6, column=2)
       e_pwd_s=Entry(mystocks_level, width=30)
       e_pwd_s.grid(row=7, column=2)
       
       Button(mystocks_level, text='Login', font=('Times New Roman',11),bg='dark green',fg='white',
              command= lambda:mystocks_login(e_un.get(),e_pwd.get())).grid(row=2, column=3)
       Button(mystocks_level, text='Sign Up', font=('Times New Roman',11),bg='dark green',fg='white',
              command= lambda:mystocks_signup(e_un_s.get(),e_pwd_s.get())).grid(row=6, column=3)

       Label(mystocks_level, text='\n'+"_"*150+'\n',bg='#318f4a').grid(row=8, column=0,columnspan=4)

#------------------------------------------------------------------------------------------------------

def mystocks_login(username,passwd):

       cursor=cnx.cursor()
       create_table('users','Create table users(Username Varchar(50),Password Varchar(50))')
       insert_into_stock_checklist()      
       
       query2="select * from users where Username= '{}' and Password='{}'".format(username,passwd)
       cursor.execute(query2)
       x=cursor.fetchall()
       y=cursor.rowcount
       
       if y > 0: 
              tablename = username+'stocks'

              mystocks_menu_level=Toplevel()
              mystocks_menu_level.title('MY MENU')
              mystocks_menu_level.geometry('250x180')
              mystocks_menu_level.configure(background='#318f4a')
              mystocks_level.destroy()

              Button(mystocks_menu_level,text='Insert New Record',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: insert_into_mystocks(tablename)).pack()
              Button(mystocks_menu_level,text='View All Recorded Stocks',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: view_stock(tablename)).pack()
              Button(mystocks_menu_level,text='View All Available Stocks',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: viewstock()).pack()
              Button(mystocks_menu_level,text='Graph One Stock',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: plot_one(tablename)).pack()
              Button(mystocks_menu_level,text='Compare Many Stocks',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: plot_compare(tablename)).pack()
              Button(mystocks_menu_level,text='Delete a record',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: delete_record(tablename)).pack()
              
       else:
              Label(mystocks_level, text='Incorrect password or username.',
                     relief='ridge',bg='red').grid(row=9, column=0,columnspan=3)
              

def mystocks_signup(username,passwd):
                    
       cursor=cnx.cursor()                   
       tablename=username+'stocks'

       query2="show tables"
       cursor.execute(query2)
       x=cursor.fetchall()
       
       ch = 1
       for i in range(len(x)):
              if tablename== x[i][0]:
                     ch=0
                     break
       
       if ch == 1:
              mystocks_menu_level=Toplevel()
              mystocks_menu_level.title('MY MENU')
              mystocks_menu_level.geometry('250x180')
              mystocks_menu_level.configure(background='#318f4a')
              mystocks_level.destroy()

              insert_into_stock_checklist()

              create_table('users','Create table users(Username Varchar(50),Password Varchar(50))')
              query='insert into users values("{}","{}")'.format(username,passwd)
              cursor.execute(query)
              query2="create table {} (Stock Varchar(30), Date_of_Purchase Date, Num Decimal)".format(username+'stocks')
              cursor.execute(query2)
              
              Button(mystocks_menu_level,text='Insert New Record',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: insert_into_mystocks(tablename)).pack()
              Button(mystocks_menu_level,text='View All Recorded Stocks',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: view_stock(tablename)).pack()
              Button(mystocks_menu_level,text='View All Available Stocks',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: viewstock()).pack()
              Button(mystocks_menu_level,text='Graph One Stock',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: plot_one(tablename)).pack()
              Button(mystocks_menu_level,text='Compare Many Stocks',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: plot_compare(tablename)).pack()
              Button(mystocks_menu_level,text='Delete a record',font=('Times New Roman',11),
                     bg='dark green',fg='white',command= lambda: delete_record(tablename)).pack()

              cnx.commit()
       else:
              Label(mystocks_level,text="Username Already Exists, Please Retry",bg='red').grid(row=10,column=1,columnspan=4)

#------------------------------------------------------------------------------------------------------

def insert_into_mystocks(tablename):
       global insert_into_mystocks_level

       cursor = cnx.cursor()
       insert_into_mystocks_level=Toplevel()
       insert_into_mystocks_level.title('INSERT STOCKS')
       insert_into_mystocks_level.configure(background='#318f4a')

       Label(insert_into_mystocks_level, text='Enter Stock name:',
              font=('Times New Roman',11),bg='#318f4a',fg='white').grid(row=0, column=0)

       e_stock=Entry(insert_into_mystocks_level, width=30)
       e_stock.grid(row=0, column=1)

       Label(insert_into_mystocks_level, text='Enter date of purchase(yyyy-mm-dd):',
              font=('Times New Roman',11),bg='#318f4a',fg='white').grid(row=1, column=0)

       e_date=Entry(insert_into_mystocks_level, width=30)
       e_date.grid(row=1, column=1)

       Label(insert_into_mystocks_level, text='Enter Number of Shares:',
              font=('Times New Roman',11),bg='#318f4a',fg='white').grid(row=2, column=0)

       e_num=Entry(insert_into_mystocks_level, width=30)
       e_num.grid(row=2, column=1)

       Enter = Button(insert_into_mystocks_level, text='Enter', font=('Times New Roman',11),bg='dark green',fg='white',
       command= lambda: insert_enter(tablename,e_stock.get(),e_date.get(),e_num.get()))
       Enter.grid(row=2, column=3)    

       def insert_enter(tablename,stock,date,num):
       
              if  check_entry_in_db(stock)==True:
                     query="insert into {} values ('{}','{}',{})".format(tablename,stock,date,num)
                     e_num.delete(0, 'end')
                     e_stock.delete(0, 'end')
                     e_date.delete(0,'end')
                     Label(insert_into_mystocks_level,text='New Stock Inserted.',bg='dark green').grid(row=3,column=0,columnspan=3)
                     cursor.execute(query)
                     cnx.commit()
              else:
                     e_num.delete(0, 'end')
                     e_date.delete(0,'end')
                     Label(insert_into_mystocks_level,
                            text='Specified Stock '+stock+' is not supported by the application.',
                            bg='red').grid(row=3,column=0,columnspan=3)
       
                   

def view_stock(tablename):    
       view_stock_level=Toplevel()
       view_stock_level.title('VIEW YOUR PORTFOLIO')
       view_stock_level.configure(background='#318f4a')
       cursor = cnx.cursor()
       query = "select * from {}".format(tablename)
       cursor.execute(query)
       x = cursor.fetchall()       
       y=[]
       
       Label(view_stock_level,text='Stock',relief='ridge',font=('Times New Roman',11),bg='dark green',fg='white').grid(row=0,column=0)
       Label(view_stock_level,text='Date of Purchase',relief='ridge',font=('Times New Roman',11),bg='dark green',fg='white').grid(row=0,column=1)
       Label(view_stock_level,text='Shares Purchased',relief='ridge',font=('Times New Roman',11),bg='dark green',fg='white').grid(row=0,column=2)
       Label(view_stock_level,text='Profit/Loss',relief='ridge',font=('Times New Roman',11),bg='dark green',fg='white').grid(row=0,column=3)
       Label(view_stock_level,text='|',font=('Times New Roman',11),bg='#318f4a',fg='black').grid(row=0,column=4)

       for i in x :
              
              z=list(i)
              date=z[1]
              num = float(z[2])
              cursor.execute('Select Dop,Average from {}'.format(z[0]))
              l=cursor.fetchall()
              
              for dop,ave in l:
                     if ave is not None:
                            
                            price_standby=ave
                            
                                                 
                     if date == dop:
                            if ave == None:
                                  
                                   price = price_standby
                            else:
                                   
                                   price=ave
                            
              if ave is None:
                     ave = price_standby
              profit=round(ave-price,2)
              profitperc = round((profit*100)/price,2)
              z+=[profit*num,profitperc]
              
              y.append(z)
       
       n=1
       
       if len(y) == 0:
              Label(view_stock_level,text='No Stocks Available',font=('Times New Roman',11),
                     bg='dark green',fg='white').grid(row=1,column=0,columnspan=3)
       else:
              for j in y:
                     col=(n//30)*5
                     Label(view_stock_level,text=j[0],font=('Times New Roman',11),bg='#318f4a',fg='white').grid(row=n%30,column=col+0)
                     Label(view_stock_level,text=j[1],font=('Times New Roman',11),bg='#318f4a',fg='white').grid(row=n%30,column=col+1)
                     Label(view_stock_level,text=j[2],font=('Times New Roman',11),bg='#318f4a',fg='white').grid(row=n%30,column=col+2)
                     if j[3]>0:
                            Label(view_stock_level,text='$'+str(round(j[3],2))+' ('+str(j[4])+')%',
                            font=('Times New Roman',11),bg='green',fg='white').grid(row=n%30,column=col+3)
                     else:
                            Label(view_stock_level,text='$'+str(j[3])+' ('+str(j[4])+')%',
                            font=('Times New Roman',11),bg='red',fg='white').grid(row=n%30,column=col+3)
                     Label(view_stock_level,text='|',font=('Times New Roman',11),bg='#318f4a',fg='black').grid(row=n%30,column=col+4)
                     n+=1

              
              

def plot_one(tbname=''):
       plot_one_level=Toplevel()
       plot_one_level.title('GRAPH OF ONE STOCK')
       plot_one_level.configure(background='#318f4a')
       Label(plot_one_level, text='Open, High, Low, Close, Average',font=('Times New Roman',11),bg='#318f4a',fg='white').grid(row=0, column=0)       
       e = Entry(plot_one_level, width=30)
       e.grid(row=0,column=1)
       Label(plot_one_level, text='Enter Stock Name:',font=('Times New Roman',11),bg='#318f4a',fg='white',width = 20).grid(row=1, column=0)
       e_stock=Entry(plot_one_level, width=30)
       e_stock.grid(row=1, column=1)
       Enter = Button(plot_one_level, text='Enter', font=('Times New Roman',11),bg='dark green',fg='white',
              command= lambda: st_comp_one(e.get(),e_stock.get()))
       Enter.grid(row=1, column=2)

       def st_comp_one(ch,stock):

              if ch == '' or stock=='':
                     Label(plot_one_level, text='Incorrect Input. Try Again!',font=('Times New Roman',11),
                            bg='Red',fg='black',width = 20).grid(row=2, column=0, columnspan=3) 
                     e.delete(0,'end')
                     e_stock.delete(0,'end')  
                     return None 
              names_list = []

              name_dict = {'1': 'Open', '2': 'High','3': 'Low', '4': 'Close', '5': 'Average'}

              if ',' not in ch:
                     names_list += [ch]
              else:
                     names_list = ch.split(',')
              names_list_fin=[]

              for i in names_list:
                     if i in name_dict.values():
                            names_list_fin += [i]
                     else:
                            e.delete(0,'end')
                            Label(plot_one_level, text='Incorrect Classes. Try Again!',font=('Times New Roman',11),
                            bg='Red',fg='black',width = 20).grid(row=2, column=0, columnspan=3)
                            return(None)
              for i in names_list_fin:
                     x_price = []
                     y_days = []

                     try:
                            query = 'select dop,{} from {}'.format(i, stock)
                            cursor.execute(query)
                     except:
                            Label(plot_one_level, text='Incorrect Input. Try Again!',font=('Times New Roman',11),
                            bg='Red',fg='black',width = 20).grid(row=2, column=0, columnspan=3) 
                            e.delete(0,'end')
                            e_stock.delete(0,'end')  
                            return None    

                     Label(plot_one_level, text='Success!',font=('Times New Roman',11),
                            bg='Green',fg='black',width = 20).grid(row=2, column=0, columnspan=3) 
                     e.delete(0,'end')
                     e_stock.delete(0,'end')  
                     
                     for row in cursor.fetchall():
                            if row[1] == None:
                                   continue
                            else:
                                   dayinchk = row[0]
                                   x_price += [dayinchk.day]
                                   y_days += [row[1]]
                     plt.plot(x_price, y_days)

              plt.title('Share Prices of Stocks from August 2020')
              plt.xlabel('Date')
              plt.ylabel('Share Price in USD')
              plt.legend(names_list_fin)
              plt.show()


def plot_compare(tbname=''):
       global plot_compare_level
       
       plot_compare_level=Toplevel()
       plot_compare_level.title('COMPARE STOCKS')
       plot_compare_level.configure(background='#318f4a')
       Label(plot_compare_level, text='Enter Names of Stocks:',
              font=('Times New Roman',11),bg='#318f4a',fg='white').grid(row=0, column=0)

       e_stocks=Entry(plot_compare_level, width=30)
       e_stocks.grid(row=0, column=1)

       Enter_1 = Button(plot_compare_level, text='Enter', font=('Times New Roman',11),bg='dark green',fg='white',
       command= lambda: plot_compare_1((e_stocks.get()).split(',')))                     
       Enter_1.grid(row=0, column=2)                     
       
       def plot_compare_1(l=[]): 
              
              chk=0  
              for i in l:
                     #['amazon','apple']
                     if check_entry_in_db(i)== False:
                            chk=1
                            break

              if chk==1:
                     Label(plot_compare_level,text='Recheck Stock Names',font=('Times New Roman',11),
                           bg='red',fg='white',relief='raised',width=30).grid(row=2,column=0,columnspan=3)
              else:     
                     Label(plot_compare_level,text='Success',font=('Times New Roman',11),
                           bg='green',fg='white',relief='raised',width=30).grid(row=2,column=0,columnspan=3)                       
                     n= len(l)
                     names=[]
                     for i in range(n):
                            x_price=[]
                            y_days=[]
                            stock=l[i]
                            names+=stock
                            stock=stock.lower()
                            query='select * from {}'.format(stock)
                            cursor.execute(query)
                            for row in cursor.fetchall():
                                   if row[1]==None:
                                          continue
                                   else:
                                          dayinchk = row[0]
                                          x_price+=[dayinchk.day]
                                          y_days+=[row[1]]
                            plt.plot(x_price,y_days)    
              
                     plt.title('Share Prices of Stocks from August 2020')
                     plt.xlabel('Date')
                     plt.ylabel('Share Price in USD')
                     plt.legend(l)
                     plt.show()

def delete_record(tablename):
       delete_record_level=Toplevel()
       delete_record_level.title('DELETE A RECORD')
       delete_record_level.configure(background='#318f4a')
       cursor = cnx.cursor()
       
       query = "select * from {}".format(tablename)
       cursor.execute(query)
       x = cursor.fetchall()       
       
       
       if len(x) == 0:
              Label(delete_record_level,text='No Stocks Available',font=('Times New Roman',11),bg='dark green',fg='white').pack()
       else:
              n=len(x)
              Label(delete_record_level,text='Click Button to Delete',font=('Times New Roman',11),bg='black',fg='white').grid(column=0,row=0)
              delete_record_level.geometry(str(200*(n//30 + 1))+'x'+str(30*(n%30 +1)))
              m=1

              for i in x:
                     if len(i[0])>10:
                            name=i[0][0:7]+'...'
                     else: name=i[0]
                     Button(delete_record_level,text='{},{},{}'.format(name,i[1],i[2]),font=('Times New Roman',11),bg='dark green',
                            fg='white', command=lambda:delete_stock(tablename,i)).grid(row=m,column=0)
                     m+=1
                     
       def delete_stock(tn,a):
              cursor.execute(
                     "delete from {} where stock= '{}' and Date_of_Purchase ='{}' and Num ='{}'".format(tn,a[0],a[1],a[2]))
              cnx.commit()
              delete_record_level.destroy()
              delete_record(tn)
       
#------------------------------------------------------------------------------------------------------

def check_entry_in_db(user_entry):   

    cursor.execute("select * from keyword")
    data=cursor.fetchall()
    
    for i in data:
        if user_entry.lower() in (i[0].lower(),):
            return True
        else:
            continue
    return False

def create_table(name,query):    
       query2="show tables"
       cursor.execute(query2)
       x=cursor.fetchall()
       if (name,) not in x: 
              cursor.execute(query)

def insert_into_stock_checklist():
       L=[]    
       files=os.listdir()
       for i in files:
              if i[-4:]=='.csv':
                     L.append(i[0:len(i)-4])

       cursor.execute('DROP TABLE IF EXISTS keyword')
       cursor.execute("Create table keyword(Name varchar(40))")

       for i in L:
              query="insert into keyword values('{}')".format(i)
              cursor.execute(query)
       cnx.commit()      

#-------------------------------------------------------------------------------------------------

def allstocks():                  

       allstocks_menu_level=Toplevel()
       insert_into_stock_checklist()
       allstocks_menu_level.title('ALL STOCKS')
       allstocks_menu_level.geometry('250x100')
       allstocks_menu_level.configure(background='#318f4a')
       Button(allstocks_menu_level,text='View All Available Stocks',
              font=('Times New Roman',11),bg='dark green',fg='white',command= viewstock).pack()
       Button(allstocks_menu_level,text='Graph One Stock',
              font=('Times New Roman',11),bg='dark green',fg='white',command= lambda: plot_one()).pack()
       Button(allstocks_menu_level,text='Compare Many Stocks',
              font=('Times New Roman',11),bg='dark green',fg='white',command= lambda: plot_compare()).pack()
       cnx.commit()
#-------------------------------------------------------------------------------------------------  
  
def viewstock():
       
       viewstock_level=Toplevel()
       viewstock_level.title('AVAILABLE STOCKS')
       viewstock_level.configure(background='#318f4a')
       query='select * from keyword'
       cursor.execute(query)
       x=cursor.fetchall()
       Label(viewstock_level,text='NAME OF STOCK',relief='raised',font=('Times New Roman',11),bg='black',fg='white').grid(row=0,column=0)
       n=1
       for j in x:
              
              Label(viewstock_level,text=j[0],font=('Times New Roman',11),bg='#318f4a',fg='white').grid(row=n%30,column=n//30)
              n+=1
              
#-------------------------------------------------------------------------------------------------
       
def main():
       global mystocks_image,stocks_compare_image, root
       root = Tk()
       root.title('MAIN')  
       root.configure(background='black')
       Label(root, text='Enter Password to SQL Database:',font=('Times New Roman',11),
       bg='black',fg='white').grid(row=0, column=0)
       
       e_pwd=Entry(root, width=30)
       e_pwd.grid(row=0, column=1)
       
       Button(root, text='Enter' ,font=('Times New Roman',11),bg='Dark Green',fg='white',
       command= lambda: main_menu(e_pwd.get())).grid(row=0, column=2)
       
       img = Image.open("stockportfolio.png")
       img = img.resize((250,250),Image.ANTIALIAS)
       mystocks_image=ImageTk.PhotoImage(img)

       img1 = Image.open("market1.jpg")
       img1 = img1.resize((250,250),Image.ANTIALIAS)
       stocks_compare_image = ImageTk.PhotoImage(img1)


def main_menu(pwd):

       global cursor,cnx,mystocks_image,stocks_compare_image,main_dir
       
       try:
              print(main_dir)
       except:
              main_dir=os.getcwd()
       
       admin__2(pwd,main_dir)
       admin__1(pwd,main_dir)       

       try:
              cnx=mysql.connector.connect(host='localhost',
                            user='root',
                            password='{}'.format(pwd))
              cursor=cnx.cursor()
              cursor.execute('CREATE DATABASE IF NOT EXISTS Project')
              cursor.execute('Use Project')
              mystocks_button = Button(root,text='',
                            command=mystocks,
                            image=mystocks_image,                        
                            bg='black')
              mystocks_button.grid(row=1,column=0,padx=10,pady=10)
              root.title('MAIN MENU')
              mystocks_label=Label(root,text='<--MY STOCKS',font=('Times New Roman',11),bg='black',fg='white')
              mystocks_label.grid(row=1,column=1,padx=10,pady=10)

              
              
              allstocks_button = Button(root,text='',
                                   command=allstocks,
                                   image=stocks_compare_image,
                                   bg='black')
              allstocks_button.grid(row=2,column=0,padx=10,pady=10)
              allstocks_label=Label(root,text='<--ALL STOCKS',font=('Times New Roman',11),bg='black',fg='white')
              allstocks_label.grid(row=2,column=1,padx=10,pady=10)

       except: 

              root.destroy()
              main()     
       
#------------------------------------------------------------------------------------------------------

main()


