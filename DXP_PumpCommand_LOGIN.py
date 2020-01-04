import sqlite3 as sq3
import datetime, time, random
from Tkinter import *
import tkFileDialog
import tkcalendar
import collections as clc
import tkMessageBox
import textwrap
import calendar
import PIL
from PIL import Image, ImageTk
from tkColorChooser import askcolor
import DXP_PumpCommand_db_projects as pcprojects
import DXP_PumpCommand_db_todo as pctodo
import DXP_PC_contacts_accounts_2ND as acccon2
import DXP_tkcalendar as tkc



"""
USER LOGIN:

- Add to database users prefered colors, fonts...etc

- Each entry addition of users, needs a folder container to house all the folders
like I have used them.
        - This way each user has a unique set of folders to keep
        clean and organized.

"""



############################################
class Login(object):

    backg = '#0C1021'
    foreg = 'white'
    
    def __init__(self,master):
        self.master = master
        self.master.title('DXP - Pump Commander - PLEASE LOGIN to continue'.format(datetime.date.today()))

        self.user_database()

        #MENUBAR CREATION--------------------------------------------------------------------------------------------------
        self.menubar = Menu(self.master,
                            bg = Login.backg, fg = Login.foreg,
                            activebackground='dark goldenrod', activeforeground='white')
        
        self.filemenu = Menu(self.menubar,
                             tearoff=0,
                             bg = Login.backg, fg = Login.foreg,
                             activebackground='dark goldenrod', activeforeground='white')
        
        self.filemenu.add_command(label="Log-in",
                                  command = lambda: self.log_in_window())
        self.filemenu.add_command(label="New User",
                                  command = lambda: self.new_user_register())
        
        self.menubar.add_cascade(label="Account",
                                 menu = self.filemenu)
        

        #STATE CHOICE--------------------------------------------------------------------------------------------------------
        self.statemenu = Menu(self.menubar,
                              tearoff = 0,
                              bg = Login.backg, fg = Login.foreg,
                              activebackground='dark goldenrod', activeforeground='white')
        
        self.statemenu.add_command(label = "Pick Colors",
                                   command = lambda: self.ask_user_colors(self.master, 'no'))
        
        self.statemenu.add_command(label = "Default Colors",
                                   command = lambda: self.ask_user_colors(self.master, 'yes'))
        
        self.menubar.add_cascade(label = "Change Colors",
                                 menu = self.statemenu)

        self.master.config(bg= Login.backg,
                           menu = self.menubar)
        

        #MAIN FRAME TO HOUSE WIDGETS-----------------------------------------------------------------------------------
        self.mainframe = Frame(self.master, bg = Login.backg)
        self.mainframe.grid(row = 0, column = 0, columnspan = 4)

        self.imglf = LabelFrame(self.mainframe,
                                text = 'Pump Commander Main:',
                                bg = Login.backg, fg = Login.foreg, font = ('Verdana',8))
        self.imglf.grid(row = 0, columnspan = 4,
                        padx = 5, pady = 5,
                        sticky = NSEW)

        #Image resizing
        width = 600
        height = 250
        
        self.ima = Image.open(r"C:\Users\Mechkro\Desktop\DXPU Logo\DXPU_5.png")
        self.ima = self.ima.resize((width,height), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.ima)
        
        self.logolabel = Label(self.imglf,
                               image = self.photo,
                               cursor = 'hand2')
        self.logolabel.image = self.photo
        self.logolabel.grid(row = 0, columnspan = 4,
                            padx = 5, pady = 4,
                            sticky = NSEW)

        self.logoinstruct = Label(self.imglf,
                                  text = '(Image Clickable)',
                                  bg = Login.backg, fg = Login.foreg, font = ('Verdana',6))
        self.logoinstruct.grid(row = 1, columnspan = 4,
                               padx = 5, pady = 2,
                               sticky = E+W)

        self.see_database()
        self.logolabel.bind('<Button-1>', self.change_photo)

        
    ############################################
    def see_database(self):
        '''
        '''
        c = self.currlog.cursor()
        c.execute('SELECT * FROM users')
        res = c.fetchall()
        
        for r in res:
            
            print r[0]
            print r[1]
            print r[2]
            print r[3]
            print r[4]
            print r[5]
            print r[6]
            
        return


    ############################################
    def change_photo(self, event = None):
        '''Will use this as a sneak peek view of each of the sections....

                -We can do like - ToDo (total entries, etc)
                                       - Projects (first few entries)
                                       - etc...
        '''
        choices = (r"C:\Users\Mechkro\Desktop\DXPU Logo\dxp-enterprises_owler_20160226_174230_original.jpg",
                       r"C:\Users\Mechkro\Desktop\DXPU Logo\PumpPic.png",
                       r"C:\Users\Mechkro\Desktop\DXPU Logo\39de2be6-2110-4825-a72d-26b231663167_small.jpg",
                       r"C:\Users\Mechkro\Desktop\DXPU Logo\DXPU_13.png",
                       r"C:\Users\Mechkro\Desktop\DXPU Logo\DXPU_5.png")
        
        self.path2 = Image.open(random.choice(choices))
        self.path2 = self.path2.resize((600,250), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(self.path2)
        self.logolabel.config(image = self.photo2)
        self.logolabel.image = self.photo2
        self.master.update()

        return
        


    ############################################
    def user_database(self):
        ''' '''
        self.currlog = sq3.connect(r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\User Info\dxp_pc_users.db")
        self.user_db_table()
        

    ############################################
    def user_db_table(self):
        ''' '''
        self.currlog.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY  AUTOINCREMENT,
             datestamp           TEXT,
             fname            TEXT,
             lname           TEXT,
             email            TEXT,
             username      TEXT,
             password       TEXT,
             backg            TEXT,
             foreg             TEXT);''')
        self.currlog.commit()

        return
    
    

    ############################################
    def new_user_register(self):
        ''' '''
        self.newuser = Toplevel(bg =  Login.backg)
        self.newuser.title('Registration')

        #First name
        self.fname = Label(self.newuser,
                            text  = 'First Name',
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8))
        self.fname.grid(row = 0, column = 0,
                            padx = 5, pady = 5)
        
        self.fnameent = Entry(self.newuser,
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8),
                            cursor = 'xterm',
                            selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.fnameent.grid(row = 0, column = 1,
                            padx = 5, pady = 5)

        #Last name
        self.lname = Label(self.newuser,
                            text  = 'Last Name',
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8))
        self.lname.grid(row = 1, column = 0,
                            padx = 5, pady = 5)
        
        self.lnameent = Entry(self.newuser,
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8),
                            cursor = 'xterm',
                            selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.lnameent.grid(row = 1, column = 1,
                            padx = 5, pady = 5)

        #-------------------------------------EMAIL--------------------------------------
        self.uemail = Label(self.newuser,
                            text  = 'Email',
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8))
        self.uemail.grid(row = 2, column = 0,
                            padx = 5, pady = 5)
        
        self.emailent = Entry(self.newuser,
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8),
                            cursor = 'xterm',
                            selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.emailent.grid(row = 2, column = 1,
                            padx = 5, pady = 5)

        #---------------------------------------USERNAME-----------------------------------------
        self.uname = Label(self.newuser,
                            text  = 'Choose Username',
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8))
        self.uname.grid(row = 3, column = 0,
                            padx = 5, pady = 5)
        
        self.unameent = Entry(self.newuser,
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8),
                            cursor = 'xterm',
                            selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.unameent.grid(row = 3, column = 1,
                            padx = 5, pady = 5)

        #-------------------------------------PASSWORD-----------------------------------
        self.pwrd1 = Label(self.newuser,
                            text  = 'Pick Password',
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8))
        self.pwrd1.grid(row = 4, column = 0,
                            padx = 5, pady = 5)
        
        self.p1ent = Entry(self.newuser,
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8),
                            show = '*',
                            cursor = 'xterm',
                            selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.p1ent.grid(row = 4, column = 1,
                            padx = 5, pady = 5)

        self.pwrd2 = Label(self.newuser,
                            text  = 'Enter Password Again',
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8))
        self.pwrd2.grid(row = 5, column = 0,
                            padx = 5, pady = 5)
        
        self.p2ent = Entry(self.newuser,
                            bg = Login.backg, fg = Login.foreg, font = ('Verdana',8),
                            show = '*', cursor = 'xterm',
                            selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.p2ent.grid(row = 5, column = 1,
                            padx = 5, pady = 5)

        self.checkuser = Button(self.newuser,
                            text = 'Submit', bg = Login.backg, fg = Login.foreg,
                            font = ('Verdana',8), bd = 3,
                            command = lambda: self.check_user_and_pwrd())
        self.checkuser.grid(row = 6, columnspan = 2,
                            padx = 5, pady = 5,
                            sticky = E+W)
        
        self.newuser.protocol("WM_DELETE_WINDOW",  lambda: self.newuser.destroy())
        self.newuser.mainloop()


    ############################################
    def check_user_and_pwrd(self):
        '''To check database and make sure username is not taken and both passwords match '''

        fn = self.fnameent.get()
        ln = self.lnameent.get()
        em = self.emailent.get()
        un = self.unameent.get()
        p1 = self.p1ent.get()
        p2 = self.p2ent.get()

        entcheck = [fn,ln,em,un,p1,p2]
        
        result = [i for i in entcheck if len(i) > 0]
        
        if len(entcheck) == len(result):            
            pass
        
        else:
            
            tkMessageBox.showerror(title = 'Insufficient Entries', message = 'Please fill out all fields!')
            self.fnameent.delete(0,END)
            self.lnameent.delete(0,END)
            self.emailent.delete(0,END)
            self.unameent.delete(0,END)
            self.p1ent.delete(0,END)
            self.p2ent.delete(0,END)
            self.newuser.lift()
            self.fnameent.focus_set()
            
            return        
        
        if p1 != p2:
            tkMessageBox.showerror(title = 'Password Error', message = 'Passwords do not match!')
            return

        #uname = self.unameent.get()
        self.c = self.currlog.cursor()
        self.c.execute('SELECT COUNT(*) FROM users WHERE username = ?',(un,))

        testr =  self.c.fetchall()[0][0]
        print testr
        
        if int(testr) > 1:
            tkMessageBox.showerror(title = 'Username Error', message = 'Username already taken!')
            return

        else:
            self.account_create_success()


    ############################################
    def account_create_success(self):
        ''' '''
        unix = time.time()
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d  %H: %M: %S'))
        
        v = (date, self.fnameent.get(),
               self.lnameent.get(),
               self.emailent.get(),
               self.unameent.get(),
               self.p1ent.get())
        
        try:
            
            self.c = self.currlog.cursor()
            self.c.execute("""INSERT INTO users(datestamp, fname,  lname,  email,  username,  password, backg, foreg)  VALUES (?,?,?,?,?,?,?,?)""",(v[0], v[1], v[2], v[3], v[4], v[5], None, None))
            self.currlog.commit()
            tkMessageBox.showinfo(title = 'User Account Created', message = 'Succesful User Account Created!')
            
        except Exception as e:
            
            print e

        self.newuser.destroy()
        
        return


    ############################################
    def log_in_window(self):
        '''A Toplevel widget utilized to provide a login screen with widgets for inputting te user name and pswrd.

            - Password entry is viewing blocked with *'s
            - Passed to check credentials function to verify input is correct -or- bring back
            
        '''
        
        self.login = Toplevel(bg =  Login.backg)
        self.login.title('Login')

        self.uname_lab = Label(self.login,
                               text  = 'Enter UserName',
                               bg = Login.backg, fg = Login.foreg, font = ('Verdana',11,'bold'))
        self.uname_lab.grid(row = 0,
                            padx = 10, pady = 5)
        
        self.user_ent = Entry(self.login,
                              bg = Login.backg, fg = Login.foreg, font = ('Verdana',8),
                              cursor = 'xterm',
                              selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.user_ent.grid(row = 1,
                           padx = 10, pady = 5)
        
        self.user_ent.focus_set()
        
        self.pass_lab = Label(self.login,
                              text  = 'Enter Password',
                              bg = Login.backg, fg = Login.foreg, font = ('Verdana',11, 'bold'))
        self.pass_lab.grid(row = 2,
                           padx = 10, pady = 5)
        
        self.pass_ent = Entry(self.login,
                              bg = Login.backg, fg = Login.foreg, font = ('Verdana',8),
                              show = '*', cursor = 'xterm',
                               selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white' )
        self.pass_ent.grid(row = 3,
                           padx = 10, pady = 5)

        self.checkcredit = Button(self.login,
                                  text = 'Log In',
                                  bg = Login.backg, fg = Login.foreg, font = ('Verdana',10),
                                  bd = 3,
                                  command = lambda: self.check_credentials(),
                                  cursor = 'hand2')
        self.checkcredit.grid(row = 4,
                              padx = 10, pady = 8,
                              sticky = E+W)

        self.checkcredit.bind('<Return>', self.check_credentials_enter)
        self.login.protocol("WM_DELETE_WINDOW",  lambda: self.login_oncancel())
        self.login.mainloop()


    ############################################
    def login_oncancel(self):
        '''
        Func to kill window if canceled
        '''
        self.login.destroy()
        return


    ############################################
    def check_credentials_enter(self,event = None):
        ''' '''
        self.check_credentials()


    ############################################
    def check_credentials(self):
        '''
        Take user submitted entry's and check db if we have match

        '''
        temp1 = self.user_ent.get()
        temp2 = self.pass_ent.get()
        self.c = self.currlog.cursor()
        self.c.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (temp1, temp2))
        
        exist = self.c.fetchall()
        
        if not exist:
            
            self.user_ent.delete(0,END)
            self.pass_ent.delete(0,END)
            tkMessageBox.showerror(title = 'Invalid Entry', message = 'Username or Password Incorrect!\nTry Again.')
            self.uname_lab.config(fg = '#ac1f0f')
            self.pass_lab.config(fg = '#ac1f0f')
            self.login.lift()
            self.checkcredit.flash()
            
            return
        
        else:
            
            self.login.destroy()
            self.credits_passed(temp1)


    ############################################
    def credits_passed(self, usr):
        ''' '''

        self.master.title('DXP - Pump Commander - Logged User: -{}'.format(usr))
        
        self.upass_ok = Label(self.mainframe,
                              text  = 'Succesfully Logged in!\nWelcome back, {}!'.format(usr),
                              bg =  Login.backg, fg = Login.foreg, font = ('Verdana',12, 'bold'),
                              cursor = 'hand2')
        self.upass_ok.grid(row = 1, columnspan = 4,
                           padx = 5, pady = 5)
        
        self.lframe = LabelFrame(self.mainframe,
                                 text = 'Navigation Pane',
                                 bg =  Login.backg, fg = Login.foreg, font = ('Verdana',12, 'bold'))
        self.lframe.grid(row = 2, columnspan = 4,
                         padx = 5, pady = 10)
        
        self.accnts = Button(self.lframe,
                             text = 'Accounts',
                             bg =  Login.backg, fg = Login.foreg, font = ('Verdana',8),
                             bd = 2, width = 16, height = 5,
                             cursor = 'hand2',
                             command = lambda: self.start_acccon())
        self.accnts.grid(row = 0, column = 0,
                         padx = 8, pady = 5)

        self.clog = Button(self.lframe,
                           text = 'Call Log',
                           bg =  Login.backg, fg = Login.foreg, font = ('Verdana',8),
                           bd = 2, width = 16, height = 5,
                           cursor = 'hand2',
                           command = lambda: None)
        self.clog.grid(row = 0, column = 1,
                       padx = 8, pady = 5)

        self.todo = Button(self.lframe,
                           text = 'To Do',
                           bg =  Login.backg, fg = Login.foreg, font = ('Verdana',8),
                           bd = 2, width = 16, height = 5,
                           cursor = 'hand2',
                           command = lambda: self.start_todos())
        self.todo.grid(row = 0, column = 2,
                       padx = 8, pady = 5)

        self.proj = Button(self.lframe,
                           text = 'Projects',
                           bg =  Login.backg, fg = Login.foreg, font = ('Verdana',8),
                           bd = 2, width = 16, height = 5,
                           cursor = 'hand2',
                           command = lambda:  self.start_projects())
        self.proj.grid(row = 0, column = 3, padx = 8, pady = 5)

        self.wscrape = Button(self.lframe,
                              text = 'Webscrape: Bid Solicits',
                              bg =  Login.backg, fg = Login.foreg, font = ('Verdana',8),
                              bd = 2,
                              cursor = 'hand2',
                              command = lambda: None)
        self.wscrape.grid(row = 1, columnspan = 4,
                          padx = 8, pady = 5,
                          sticky = E+W)

        self.upass_ok.bind('<Button-1>', self.destroy_success_label)
        
        return


    ############################################
    def start_todos(self):
        ''' '''
        self.todo.flash()
        pctodo.start()
        return

    ############################################
    def start_projects(self):
        ''' '''
        self.proj.flash()
        pcprojects.start()
        return

    ############################################
    def start_acccon(self):
        ''' '''
        self.accnts.flash()
        acccon2.start()
        return


    ############################################
    def destroy_success_label(self, event = None):
        ''' '''
        self.upass_ok.destroy()
        return


    
    ############################################
    def ask_user_colors(self,win, inq):
        '''Take the bg and fg colors picked by user and config all widgets to match.
            - Need to figure how to call all widgets
        '''

        if inq == 'no':
            
            #Asking user twice for color choice (Background and Foreground selection)
            BG = askcolor(title = 'Choose Background Color', parent  = win)
            FG =  askcolor(title = 'Choose Foreground Color', parent  = win)

        if inq == 'yes':
            
            BG = ('1', '#0C1021')
            FG = ('1', 'white')

        Login.backg = BG[-1]
        Login.foreg = FG[-1]
        
        win.config(bg = BG[-1])
        self.menubar.config(bg = BG[-1], fg = FG[-1])
        self.filemenu.config(bg = BG[-1], fg = FG[-1])
        self.statemenu.config(bg = BG[-1], fg = FG[-1])
            
        arghold = []
        
        try:
            if win.winfo_exists():
                arghold.append(win.winfo_children())
                
        except:
            pass

        try:
            if self.mainframe.winfo_exists():
                arghold.append(self.mainframe.winfo_children())
                
        except:
            pass

        try:
            if self.lframe.winfo_exists():
                arghold.append(self.lframe.winfo_children())
                
        except:
            pass

        try:
            if self.logoinstruct.winfo_exists():
                self.logoinstruct.config(bg = BG[-1], fg = FG[-1])
                
        except:
            pass
        
        #Assigning the color choices to the available widgets
        for w in arghold:
            for wids in w:
                
                try:
                    
                    if isinstance(wids, Menu):
                        wids.config(bg = BG[-1], fg = FG[-1])
                        
                    if isinstance(wids, Frame):
                        wids.config(bg = BG[-1])
                        
                    if isinstance(wids, Label):
                        wids.config(bg = BG[-1], fg = FG[-1])
                        
                    if isinstance(wids, Button):
                        wids.config(bg = BG[-1], fg = FG[-1])
                        
                    if isinstance(wids, Entry):
                        wids.config(bg = BG[-1], fg = FG[-1])
                        
                    if isinstance(wids, LabelFrame):
                        wids.config(bg = BG[-1], fg = FG[-1])
                        
                except AttributeError:
                    
                    pass

        return

   



def startup():
    '''
    Initilize the database before
    '''
    root = Tk()
    Login(root)
    root.mainloop()

        
####################################
#MAIN CALL
####################################            
if __name__ == '__main__':
    startup()

























        
