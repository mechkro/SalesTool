import sqlite3 as sq3
import datetime, time, random
from Tkinter import *
import datetime
import ttk
import os
import webbrowser as wb
import tkFileDialog
#import tkcalendar
import collections as clc
import tkMessageBox
import textwrap
import calendar



'''
FILE CHECKLIST:     -----      CURRENT : ALPHA

- Make widget classes - clean up code
- Seperate Files into sections
- Format the project folder for Beta release

INIT:
    - When the program is initiated - start with check of "Delta time between contact"
    - Any TODO's that are due today/tommorow
    

MAIN SCREEN:
    - format the output display
    - load all accounts w/ associated contacts
        - dbl click account - auto populates contacts
    - keep database same just make X amount of tables
    - Popup box warning - pulls all the contacts that have not been contacted
    - Move start of all databases to a function


CALL LOG:
    - format the output better. (Hard to read)
    - Add comment table to the database
        - This will allow comments and thoughts to be added real time instead of at compiling
            - EX: - Discuss with Ken expenses needed

    - askfilename or directory for saving
    - prompt when new DB is created for user to name it
    - 


TO DO:
    - clean up the grid and the look
    - F/U reqd functionality needs added
    - Better options or less options keep it simple......

'''

accnts = """
COMPANY NAME, 
*Desert Star Energy,
*Nevada Solar One ,
Abbott Nutrition        ,
Abrams Airborne M,
Air Liquide - Bagda,
Air Products and Ch,
AMEC Engineering ,
Ames Construction ,
Apache Nitrogen     ,
Applied LNG            ,
Arcadis -  W&WW   ,
Archer-Western - C,
Argus Consulting     ,
Arizona Mining Com,
Arizona Pacific Wo,
AZ CoOP                 ,
Black & Veatch - NV,
Black & Veatch - Ph,
Boulder City             ,
Brown & Caldwell    ,
Brown & Caldwell (T,
Bull Moose Tube Co,
Calpine                     ,
Camp Dresser McG,
Carollo                      ,
Carollo - Phx            ,
Carollo - Tucson      ,
Casa Grande (exce,
CCA (Central Arizo,
CCWRD                   ,
Chino Valley             ,
City of Avondale      ,
City of Bullhead       ,
City of Casa Grand,
City of Chandler       ,
City of Chandler - P,
City of Flagstaff       ,
City of Henderson   ,
City of Las Vegas   ,
City of Mesa             ,
City of NORTH LV   ,
City of Phoenix        ,
Clark County Dept. ,
Clark County Water ,
ClearWater paper   ,
Daisy Sour Cream  ,
Davis Monthan AFB,
Drake Materials       ,
Ehrmann's Dairy (La,
Envirogen                 ,
Enviromental Bioma,
Epcor - Bullhed City,
Euclid Chemical = E,
Evoqua - Chandler  ,
Evoqua - Mesa        ,
Evoqua - Parker      ,
Fairibault Foods      ,
Fann Environmental,
Fann Environmental,
Felix Construction   ,
Fluid Solutions         ,
FMI - Ajo                   ,
FMI - Bisbee            ,
FMI - Corp                ,
FMI- Bagdad            ,
FMI- Sierrita             ,
Franklin Foods Cre,
Frito Lay                   ,
Ft. Huachuca            ,
Ft. Mojave                ,
Garver USA             ,
GCW Engineering   ,
Greeley & Hansen   ,
Green Valley Pecan,
Griffith Energy/New ,
Hazen & Sawyer      ,
HDR (Tucson)          ,
Henderson Electric ,
Hexcel                       ,
Honeywell - Jones L,
Hunter Contracting  ,
Hydro Geo Chem    ,
IBM                            ,
IDG (Ind. Dist. Grou,
Jacobs (CH2MHill)?,
Kinder Morgan (Bull,
Kinder Morgan (Pho,
Kinder Morgan (Top,
Kingman - ****** Put,
Laughlin Water Rec,
Lhoist North Americ,
LPC Construction    ,
LPC Contstruction   ,
LVVWD                    ,
McCarthy Building C,
MGC Contractors, In,
Mingus Constructor,
Morrison Maierle     ,
Neltec                       ,
Nevada Cogen        ,
Nevada Resellers - ,
Nexus Energy (form,
Nord Copper            ,
Nucor                        ,
NV Energy                ,
NV Energy (Chuck L,
NV Energy (Harry A,
NV Energy (Silverha,
Oceanspray             ,
Olin Chlor                 ,
Paragon Services, ,
PCL Contruction      ,
Pima County WW    ,
Poggemeyer Engin,
Praxair Electronics  ,
Pro Petroleum - Phx,
Pro Petroleum - Ve,
Rain Bird (Tucson)  ,
Raytheon (Hageme,
Renewable Algal En,
Romtec Utilities       ,
Sasol Inc                   ,
Severn Trent Enviro,
Sierra Vista Region,
Slater Hannifan Gro,
Sletten Companies ,
Sletten Construction,
Southern Nevada W,
SRP - Desert Basin,
Stantec - (W&WW) ,
Stantec Consulting  ,
Sun Mechanical - Te,
Sun Mechanical - Tu,
Sundt (W&WW)       ,
Sundt Construction  ,
Swissport Fueling   ,
TEP (Tucson Electri,
TEP Irvington           ,
Timet - HOLD OFF ,
Tolin Mechanical - P,
Tolin Mechanical - T,
Town of Casa Gran,
Town of Kingman    ,
Town of Wickenburg,
Town of Queen Cre,
Trans-Canada Pow,
Walsh Group - Arch,
Western Emulsions ,
Western Emulsions ,
Wilson Engineering ,
WW Engineers        ,
X - DXP Corp          ,
X - DXP Internal       ,
X - Other                   ,
X - Vendor                ,
"""

accnt_dict = clc.OrderedDict()
itr_acc = 0
acc_sep = accnts.split(',')
for i in acc_sep:
    accnt_dict[itr_acc] = i.strip('\n')
    itr_acc += 1

for k,v in accnt_dict.items():
    print('Key is {}, and account is {}'.format(k,v))


#START OF THE MAIN DATABASE
conn = sq3.connect('tonyk_dxp.db')
c = conn.cursor()



def attempt_dbconnect_again():
    '''
    ## D1 ##    
    Func - to allow user a second chance on there .db file directory selection.
    '''
    
    tkMessageBox.askyesno("Re-Connect Inquiry", "Try choosing .db directory, again?")
    if True:
        second_dbloc = tkFileDialog.askopenfilename(title = 'Chose database directory',
                                          initialdir= r"C:\Anaconda2\Scripts\databases",
                                          filetypes = (("database file", "*.db"),))
        return second_dbloc
    
    else:
        pass
    
    return



def connect_to_db():
    '''
    ## D2 ## - called by Class Call Log ---> Func - Databse
    
    When accessing a database - we need to prompt user to select which database file to load and communicate with
        - This has added benefit of allowing users to switch between databases
        
        - BUG::::(happened after deliberate attempt to pick wrong file first run)
        Exception in Tkinter callback
        Traceback (most recent call last):
          File "C:\Anaconda2\lib\lib-tk\Tkinter.py", line 1542, in __call__
            return self.func(*args)
          File "C:\Anaconda2\Scripts\DXP_PumpCommand.py", line 284, in <lambda>
            self.filemenu.add_command(label="Call Log", command = lambda: CallLog(master))
          File "C:\Anaconda2\Scripts\DXP_PumpCommand.py", line 564, in __init__
            self.Database()
          File "C:\Anaconda2\Scripts\DXP_PumpCommand.py", line 778, in Database
            self.currlog = sq3.connect(self.clog_db)
        ValueError: database parameter must be string or APSW Connection object
    '''
    
    db_loc = tkFileDialog.askopenfilename(title = 'Chose database directory',
                                          initialdir= r"C:\Anaconda2\Scripts\databases",
                                          filetypes = (("database file", "*.db"),))

    #Test to help alleviaate user selection errror
    if not db_loc:
        pass

    elif not db_loc.endswith('.db'):
        #del(db_loc)
        tkMessageBox.showwarning("Warning", "Filetype must be .db, try your request again")
        newfile = attempt_dbconnect_again()
        return newfile
    
    else:
        return db_loc




#THIS IS FIRST RUN ONLY --------- AFTER IT HAS BEEN CREATED WILL RAISE ERROR
def create_table_accounts():

    c.execute('CREATE TABLE IF NOT EXISTS azaccounts (compname TEXT, industry TEXT, website TEXT, address TEXT, note TEXT, datestamp TEXT)')




def create_table_contacts():
    
    c.execute('CREATE TABLE IF NOT EXISTS azcontacts (compname TEXT, contname TEXT, position TEXT, phonenumb TEXT, email TEXT, note TEXT, datestamp TEXT, datelast TEXT)')




def static_date_entry():
    '''

    '''
    c.execute('INSERT INTO azaccounts VALUES()')
    comm.commit()
    return



def dynamic_data_entry_accounts(name, ind, url, addr, note):
    '''

    '''
    
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d  %H: %M: %S'))
    c.execute('INSERT INTO azaccounts (compname, industry, website, address, note, datestamp) VALUES (?, ?, ?, ?, ?, ?)',
              (name, ind, url, addr, note, date))
    conn.commit()




def dynamic_data_entry_contacts(cname, contn, pos, pnum, email, note, dlast):
    '''

    '''
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d  %H: %M: %S'))
    c.execute('INSERT INTO azcontacts (compname, contname , position , phonenumb , email , note , datestamp , datelast) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
              (cname, contn, pos, pnum, email, note, date, dlast))
    conn.commit()

    


def read_from_db(db, *args):
    '''
    Func to read from a DB
    '''
    
    print('\n\n--------------------------\n\n')
    print('AZ Contacts ----------------------')
    c.execute('SELECT rowid,  compname, contname FROM azcontacts ORDER BY compname')#             * FROM azcontacts WHERE rowid = 6')
    for row in c.fetchall():
        print row



def  delete_and_update(db):
    '''
    Func to select database entries
    '''
    
    c.execute('SELECT * FROM {}'.format(db))
    for row in c.fetchall():
        print row

    return



def update_accounts(db,old,new):

    '''
    Func - will need to provide an interface to input updatd account data.
        - Need to be able to pull the correct clicked index and associated database location
        - Populate the entry boxes with the existing information allowing user to edit.
        - Once "submit" button is pushed new info to replace the old.
        - Make call to update the listbox that is being displayed.
    '''
    
    old_info = 'compname = {}, industry = {}, website {}, address {}, note {}, datestamp {}'.format(old[0],old[1],old[2],old[3],old[4],old[5])
    old_info = 'compname = {}, industry = {}, website {}, address {}, note {}, datestamp {}'.format(new[0],new[1],new[2],new[3],new[4],new[5])
    
    instruct = 'UPDATE {} SET'
    c.execute('UPDATE {} SET ()')
    comm.commit()
        


def get_account_contacts(company, widge):

    widge.delete(0,END)         #Contacts List
    widge.insert(END, '{} Contacts:\n')

    c.execute('SELECT * FROM')   
    



def read_from_accounts(widge):

    '''
    There are 6 columns in database entry
    '''

    widge.delete(0,END)    
    c.execute('SELECT * FROM azaccounts')
    data = c.fetchall()

    for row in data:
        ent = (','.join(row))
        widge.insert(END, ent)

    return


        
def read_from_contacts(widge):

    '''
    There are 8 columns in database entry
    Poss other opts:

        #ent = (','.join(row))
        #widge.insert(END, row[0])        
    '''

    widge.delete(0,END)
    c.execute('SELECT * FROM azcontacts')
    data = c.fetchall()
    
    for i, row in enumerate(data):
        entry = '{} of {}:\nCompany: {}\nName: {}\nPos: {}\nP#: {}\nEmail: {}\nNote: {}\nDateEntered: {}\nLastSpoke: {}\n\n'.format(i+1,len(data),row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        entrys = entry.split('\n')
        
        for i in entrys:
            widge.insert(END, i)

    return



def write_to_file(floc, *args, **kwargs):
    '''

    '''
    with open(floc, 'w+')as F:
        
        for i in args:
            F.write(i + '\n')
        
        for k,v in kwargs.items():
            F.write(k + '\n')
            
            for ents in v:
                F.write(ents)
            F.write('\n')
            
        
        


class App(object):

    '''
    Each Account to have:
        - Web URL
        - Descript of what they do
        - Potential equipment to pitch
    '''
    current_state = 'AZ'
    state_choices = {'AZ': ('AZ ACCOUNTS', 'AZ CONTACTS'),
                             'NV': ('NV ACCOUNTS', 'NV CONTACTS'),
                             'NM': ('NM ACCOUNTS', 'NM CONTACTS')
                             }
    
    def __init__(self,master):
        self.master = master
        self.master.title('DXP PUMP COMMANDER  -  TODAYS DATE: {}'.format(datetime.date.today()))

        #MENUBAR CREATION--------------------------------------------------------------------------------------------------
        self.menubar = Menu(self.master, background = '#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.filemenu = Menu(self.menubar, tearoff=0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.filemenu.add_command(label="ToDo", command = lambda: ToDo(master))
        self.filemenu.add_command(label="Tools", command = lambda: None)
        self.filemenu.add_command(label="Call Log", command = lambda: CallLog(master))
        self.menubar.add_cascade(label="File", menu = self.filemenu)
        

        #STATE CHOICE--------------------------------------------------------------------------------------------------------
        self.statemenu = Menu(self.menubar, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.statemenu.add_command(label = "AZ", command = lambda: self.revise_labeling('AZ'))
        self.statemenu.add_command(label = "NV", command = lambda: self.revise_labeling('NV'))
        self.statemenu.add_command(label = "NM", command = lambda: self.revise_labeling('NM'))
        self.menubar.add_cascade(label = "Change State", menu = self.statemenu)

        #####################
        #ADD UNDO BUTTON or MENU OPTION----------------------------
        #####################

        #####################
        #SWITCH OUT TO DO CODE -----------------
        #####################

        self.master.config(bg='#0C1021', menu = self.menubar)
        

        #MAIN FRAME TO HOUSE WIDGETS-----------------------------------------------------------------------------------
        self.mainframe = Frame(self.master,bg =  '#0C1021')
        self.mainframe.grid(row = 0, column = 0)
        

        #LABELFRAME CREATION ---------------------------------------------------------------------------------------------
        self.lf1 = LabelFrame(self.mainframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'), text = App.state_choices[App.current_state][0])
        self.lf1.grid(row = 0, column = 0, sticky = NSEW)
        self.lf2 = LabelFrame(self.mainframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'), text = App.state_choices[App.current_state][1])
        self.lf2.grid(row = 0, column = 1, sticky = NSEW)
        

        #WIDGETS IN LABELFRAMES -----------------------------------------------------------------------------------------
        self.lb1_horiz_scroll = Scrollbar(self.lf1, orient = HORIZONTAL)
        self.lb1_vert_scroll = Scrollbar(self.lf1, orient = VERTICAL, bg =  '#0C1021')
        self.lb1 = Listbox(self.lf1, bg =  '#0C1021', fg = 'white', font = ('Verdana',7), height = 15, width = 80, cursor = 'hand2',
                           xscrollcommand = self.lb1_horiz_scroll, yscrollcommand =self.lb1_vert_scroll.set,
                           selectbackground = 'dark goldenrod', selectforeground = 'black', activestyle = 'dotbox')
        self.lb1.grid(row = 0, column = 0, padx = 3, pady = 3)
        self.lb1_horiz_scroll.config(command = self.lb1.xview)
        self.lb1_horiz_scroll.grid(row = 1, sticky = E+W)
        self.lb1_vert_scroll.config(command = self.lb1.yview)
        self.lb1_vert_scroll.grid(row = 0, column = 1, sticky = N+S)

        lb1start = '''
        This will be the accounts window display. Each of my acccounts will be listed.
        - Functionality to add:
            - Double Click will bring up each accounts profile page
            - All pertinent info added to profile
        '''
        lb1lines = lb1start.split('\n')
        for i in lb1lines:
            self.lb1.insert(END,i)

        for v in accnt_dict.values():
            temp = v.replace(' ','_',3)
            self.lb1.insert(END, temp.strip(' '))
            

        #WIDGETS IN LABELFRAMES -----------------------------------------------------------------------------------------
        self.lb2_horiz_scroll = Scrollbar(self.lf2, orient = HORIZONTAL)
        self.lb2_vert_scroll = Scrollbar(self.lf2, orient = VERTICAL)
        self.lb2 = Listbox(self.lf2, bg =  '#0C1021', fg = 'white', font = ('Verdana',7), height = 15, width = 80,
                           cursor = 'hand2', xscrollcommand =self.lb2_horiz_scroll.set, yscrollcommand =self.lb2_vert_scroll.set,
                           selectbackground = 'dark goldenrod', selectforeground = 'black', activestyle = 'dotbox')
        self.lb2.grid(row = 0, column = 0, padx = 3, pady = 3)
        self.lb2_horiz_scroll.config(command = self.lb2.xview)
        self.lb2_horiz_scroll.grid(row = 1, sticky = E+W)
        self.lb2_vert_scroll.config(command = self.lb2.yview)
        self.lb2_vert_scroll.grid(row = 0, column = 1, sticky = N+S)


        lb2start = '''
        This will be the contacts window display. 
        - Functionality to add:
            - This will autopopulate on ACTIVE member of the Accounts
        '''
        lb2lines = lb2start.split('\n')
        for i in lb1lines:
            self.lb2.insert(END,i)
            

        
        #LISTBOX TOOLS------------------------------------------------------------------------------------------------------
        self.lb1_button = Button(self.lf1, text = ' Load Database',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'),
                                 command = lambda: read_from_accounts(self.lb1))
        self.lb1_button.grid(row = 2, padx = 3, pady = 3, sticky = E+W)
        self.lb2_button = Button(self.lf2, text = ' Load Database',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'),
                                 command = lambda: read_from_contacts(self.lb2))
        self.lb2_button.grid(row = 2, padx = 3, pady = 3, sticky = E+W)
        
        self.lf_filter = LabelFrame(self.mainframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'), text = 'FILTER')
        self.lf_filter.grid(row = 3, column = 1, sticky = E+W)
        self.lf_filter.grid_columnconfigure(1,weight =2)        
        self.filt_label = Label(self.lf_filter, text = 'Enter Filter\nElement:', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.filt_label.grid(row = 0, column = 0, sticky = W, padx = 3, pady = 3)
        self.filtvar = StringVar()
        self.filt_entry = Entry(self.lf_filter, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), textvariable = self.filtvar, width = 50)
        self.filt_entry.grid(row = 0, column = 1, sticky = E+W, padx = 5, pady = 3)
        self.filt_button = Button(self.lf_filter, text = 'F I L T E R',  bg =  '#0C1021', fg = 'white', font = ('Verdana',10,'bold'),
                                 command = lambda: None)
        self.filt_button.grid(row = 1, column = 0, columnspan =3, sticky = E+W, padx = 5, pady = 3)



        #LEFT SIDE ADDITION---------------------------------------------------------------------------------------------------
        self.lf_filter2 = LabelFrame(self.mainframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'), text = 'FILTER')
        self.lf_filter2.grid(row = 3, column = 0, sticky = E+W)
        self.lf_filter2.grid_columnconfigure(1,weight =2)        
        self.filt_label2 = Label(self.lf_filter2, text = 'Enter Filter\nElement:', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.filt_label2.grid(row = 0, column = 0, sticky = W, padx = 3, pady = 3)
        self.filtvar2 = StringVar()
        self.filt_entry2 = Entry(self.lf_filter2, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), textvariable = self.filtvar2, width = 50)
        self.filt_entry2.grid(row = 0, column = 1, sticky = E+W, padx = 5, pady = 3)
        self.filt_button2 = Button(self.lf_filter2, text = 'F I L T E R',  bg =  '#0C1021', fg = 'white', font = ('Verdana',10,'bold'),
                                 command = lambda: None)
        self.filt_button2.grid(row = 1, column = 0, columnspan =3, sticky = E+W, padx = 5, pady = 3)

        self.lb1.bind('<<Button-1>>', self.fill_account_contacts())

        #CREATE REMINDER and GAMEPLAN POP UP --------------------------------------------------------------------------
        self.reminder_gameplan_win()



    def reminder_gameplan_win(self):
        '''

        '''

        self.master.iconify()
        
        self.remind_gplan = Toplevel(bg =  '#0C1021')
        self.remind_gplan.title('Reminder & Gameplan Inquiry')
        self.remind_gplan.minsize(270,240)
        self.remind_gplan.maxsize(280,250)
        
        self.rgplan_frame = Frame(self.remind_gplan, bg =  '#0C1021')
        self.rgplan_frame.grid()

        #LABELFRAMES ---------------------------------------------------
        self.remind_lframe = LabelFrame(self.rgplan_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'), text = 'REMINDERS')
        self.remind_lframe.grid(row = 0, padx = 5, pady = 5)

        self.gplan_lframe = LabelFrame(self.rgplan_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'), text = 'GAMEPLAN')
        self.gplan_lframe.grid(row = 1, padx = 5, pady = 5, sticky = E+W)


        #WIDGETS--------------------------------------------------------
        #REMINDERS -------------------
        self.remind_lab = Label(self.remind_lframe, text = 'You have REMINDERS waiting for you,\nWould you like to view them?',
                                 bg =  '#0C1021', fg = 'white', font = ('Verdana',10))
        self.remind_lab.grid(row=0, columnspan = 2, padx = 5, pady = 5)

        self.ry_var = IntVar()                             
        self.remind_yes = Checkbutton(self.remind_lframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), text = 'YES',
                                    onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = CENTER, variable = self.ry_var,
                                    command = lambda: self.remind_no.deselect())
        self.remind_yes.grid(row = 1, column = 0, padx = 2, pady = 5)

        self.rn_var = IntVar()                             
        self.remind_no = Checkbutton(self.remind_lframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), text = 'NO',
                                    onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = CENTER, variable = self.rn_var,
                                    command = lambda:  self.remind_yes.deselect())
        self.remind_no.grid(row = 1, column = 1, padx = 2, pady = 5)

        #GAMEPLAN---------------------        
        self.gplan_lab = Label( self.gplan_lframe, text = 'Look at the GAMEPLAN?',
                                 bg =  '#0C1021', fg = 'white', font = ('Verdana',10))
        self.gplan_lab.grid(row=0, columnspan = 2, padx = 5, pady = 5)

        self.gy_var = IntVar()                             
        self.gplan_yes = Checkbutton( self.gplan_lframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), text = 'YES',
                                    onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = CENTER, variable = self.gy_var,
                                    command = lambda:  self.gplan_no.deselect())
        self.gplan_yes.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.gn_var = IntVar()                             
        self.gplan_no = Checkbutton( self.gplan_lframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), text = 'NO',
                                    onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = CENTER, variable = self.gn_var,
                                    command = lambda: self.gplan_yes.deselect())
        self.gplan_no.grid(row = 1, column = 1, padx = 5, pady = 5)

        #SUBMIT ANS TO INQUIRY -----------------------------------------------------------
        self.rgplan_button = Button(self.rgplan_frame, text = ' Submit',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'),
                                 command = lambda: self.evaluate_remind_gplan())
        self.rgplan_button.grid(row = 2, columnspan = 2, padx = 3, pady = 3, sticky = E+W)

        self.remind_gplan.protocol("WM_DELETE_WINDOW",  lambda: self.kill_rgplan_win())
        self.remind_gplan.mainloop()


    def evaluate_remind_gplan(self):
        '''
        
        '''
        if self.gy_var:
            print 'gameplan yes'
        else:
            print 'gameplan no'

        if self.ry_var:
            print 'remind yes'
        else:
            print 'remind no'

        self.kill_rgplan_win()



    def kill_rgplan_win(self):
        '''

        '''
        self.remind_gplan.destroy()
        return self.master.deiconify()




    def revise_labeling(self, state):
        '''

        '''
        App.current_state = state
        self.lf1.config( text = App.state_choices[App.current_state][0])
        self.lf2.config( text = App.state_choices[App.current_state][1])
        self.refresh_listbox(state)




    def refresh_listbox(self, state):
        '''

        '''        
        self.lb1.delete(0,END)
        self.lb2.delete(0,END)

        try:
            state_dir = {'AZ': r'c:\azfile',
                               'NV': r'c:\nvfile',
                              'NM': r'c:\nmfile'}

            with open(state_dir[state], 'r')as F:
                lines = F.readlines()
                for line in lines:
                    self.lb1.insert(END, line)
        except:
            pass
                


    def fill_account_contacts(self):
        '''

        '''                                   
        try:
            current_account = self.lb1.get(ACTIVE)
            #SEEK DIR - MATCHES or is defined to be associated with ACCOUNT
        except:
            pass
                
                


class CallLog(object):
    '''
    - Need to be able to add entries to call log and be able to click and update them instead  of having to add a new line
    - Have a submit button -
            - Compile and format the file for presentation
            - Ask to save the database file to a directory
            - New DB creation required
    '''
    
    def __init__(self, parent):
        '''
        Init Func to build out the root master iwndow
        '''
        
        self.parent = parent
        self.parent.iconify()
        #self.Database()

        self.clog_level = Toplevel()
        self.clog_level.title('CALL-LOG - TODAYS DATE: {}'.format(datetime.date.today()))
        self.set_clog_level_size()


        #MENUBAR CREATION--------------------------------------------------------------------------------------------------
        self.clogmenu = Menu(self.clog_level, background = '#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')

        self.writemenu = Menu(self.clogmenu, tearoff=0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.writemenu.add_command(label="Write Log to File", command = lambda: self.name_text_file())

        self.clogmenu.add_cascade(label="Write Log", menu = self.writemenu)

        
        #STATE CHOICE --------------------------------------------------------------------------------------------------------
        self.resetmenu = Menu(self.clogmenu, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.resetmenu.add_command(label = "Reset Call File", command = lambda: self.reset_log_protocol())

        self.clogmenu.add_cascade(label = "Reset", menu = self.resetmenu)


        #LOAD DATABASE ------------------------------------------------------------------------------------------------------
        self.loadmenu = Menu(self.clogmenu, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.loadmenu.add_command(label = "New DB", command = lambda:  self.ask_db_filename())      #self.new_database())
        self.loadmenu.add_command(label = "Load Database", command = lambda: self.open_db_file())           #self.Database('START'))
        self.loadmenu.add_command(label = "Add Note", command = lambda: self.check_if_db_open())       #add_note_to_db())

        self.clogmenu.add_cascade(label = "Load", menu = self.loadmenu)


        #LOAD TO WINDOW
        self.clog_level.config(bg='#0C1021', menu = self.clogmenu)


        #TEXT WIDGET CREATION-----------------------------------------------------------------------------
        self.clog_frame = Frame(self.clog_level, bg =  '#0C1021')
        self.clog_frame.grid(row = 0, column = 0)

        self.mon_labelframe = LabelFrame(self.clog_frame, text = 'MONDAY', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.mon_labelframe.grid(row = 0, padx = 3, pady = 3, sticky = N+E+W)
        self.tue_labelframe = LabelFrame(self.clog_frame, text = 'TUESDAY', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.tue_labelframe.grid(row = 1, padx = 3, pady = 3, sticky = N+E+W)
        self.wed_labelframe = LabelFrame(self.clog_frame, text = 'WED', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.wed_labelframe.grid(row = 2, padx = 3, pady = 3, sticky = N+E+W)
        self.thur_labelframe = LabelFrame(self.clog_frame, text = 'THURSDAY', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.thur_labelframe.grid(row = 3, padx = 3, pady = 3, sticky = N+E+W)
        self.fri_labelframe = LabelFrame(self.clog_frame, text = 'FRIDAY', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.fri_labelframe.grid(row = 4, padx = 3, pady = 3, sticky = N+E+W)

        
        #TEXT BOX CREATION----------------------------------------------------------------------------------
        self.mon_text = Text(self.mon_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', height = 5)
        self.mon_text.grid(padx = 3, pady = 3, sticky = NSEW)
        self.tue_text = Text(self.tue_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            cursor = 'xterm', selectbackground = 'dark goldenrod' ,selectforeground = 'black', height = 5)
        self.tue_text.grid(padx = 3, pady = 3, sticky = NSEW)
        self.wed_text = Text(self.wed_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            cursor = 'xterm', selectbackground = 'dark goldenrod',selectforeground = 'black', height = 5)
        self.wed_text.grid(padx = 3, pady = 3, sticky = NSEW)
        self.thur_text = Text(self.thur_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            cursor = 'xterm', selectbackground = 'dark goldenrod' ,selectforeground = 'black', height = 5)
        self.thur_text.grid(padx = 3, pady = 3, sticky = NSEW)
        self.fri_text = Text(self.fri_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            cursor = 'xterm', selectbackground = 'dark goldenrod' ,selectforeground = 'black', height = 5)
        self.fri_text.grid(padx = 3, pady = 3, sticky = NSEW)

        #Initial instructions -------------------------------------------------------------------
        self.mon_text.insert(END, "\n--- MUST LOAD  '*.db' FILE ---")
        self.tue_text.insert(END, "\n--- MUST LOAD  '*.db' FILE ---")
        self.wed_text.insert(END, "\n--- MUST LOAD  '*.db' FILE ---")
        self.thur_text.insert(END, "\n--- MUST LOAD  '*.db' FILE ---")
        self.fri_text.insert(END, "\n--- MUST LOAD  '*.db' FILE ---")

        #LOAD WHAT DATA IS THERE-------------------------------------------------------
        #self.PreloadData('MONDAY', 'TUESDAY', 'WED', 'THURSDAY', 'FRIDAY')
        

        #BOTTOM----------------------------------------------------------------------------------------
        self.widge_labelframe = LabelFrame(self.clog_frame, text = 'CALL LOG - OPS',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.widge_labelframe.grid(row = 5, padx = 5, pady = 5, sticky = E+W)

        self.spinlab = Label(self.widge_labelframe, text = 'CHOOSE WHICH DAY\nTO "SUBMIT" ENTRY', bg =  '#0C1021', fg = 'white', font = ('Verdana', 7))
        self.spinlab.grid(row = 0 , column = 0, padx = 5, pady = 3, sticky = NSEW)


        #SPINBOX TO SELECT DAY OF WEEK TO LOAD--------------------------------------------
        #######################################################################################
        """THINK ABOUT CHANGING TO A POP UP WINDOW TO CHOOSE DAY ---- I HAVE FORGOTTEN MULTIPLE TIMES NOW TO CORRECT IT"""
        #######################################################################################
        
        self.choices = ('MONDAY', 'TUESDAY', 'WED', 'THURSDAY', 'FRIDAY')
        self.spinbox = Spinbox(self.widge_labelframe, values = self.choices, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2')
        self.spinbox.grid(row = 2, column = 0, padx = 3, pady = 3, sticky = S)


        #LABELS FOR THE ENTRIES-------------------------------------------------------------------------------------------------------------
        self.complab = Label(self.widge_labelframe, text = 'Company Name', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))         #some type of auto populate
        self.complab.grid(row = 0 , column = 1, padx = 3, pady = 3, sticky = W)
        
        self.contlab = Label(self.widge_labelframe, text = 'Contact Name', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.contlab.grid(row = 1 , column = 1, padx = 3, pady = 3, sticky = W)
        
        self.medlab = Label(self.widge_labelframe, text = 'Medium Used', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))           #Think about using a spinbox
        self.medlab.grid(row = 2 , column = 1, padx = 3, pady = 3, sticky = W)
        
        self.desclab = Label(self.widge_labelframe, text = 'Description', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.desclab.grid(row = 3 , column = 1, padx = 3, pady = 3, sticky = W)
        
        self.fwdlab = Label(self.widge_labelframe, text = 'Forward', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.fwdlab.grid(row = 4, column = 1, padx = 3, pady = 3, sticky = W)


        ##### !!!! Think about adding colorcode maping to the text
        

        #ENTRY WIDGETS---------------------------------------------------------------------------------------------------------------
        self.comp_ent =  Entry(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                               cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white')
        self.comp_ent.grid(row = 0 , column = 2, padx = 3, pady = 3, sticky = E)
        
        self.cont_ent =  Entry(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                               cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white' )
        self.cont_ent.grid(row = 1 , column = 2, padx = 3, pady = 3, sticky = E)
        
        self.med_ent =  Entry(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                              cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white' )
        self.med_ent.grid(row = 2 , column = 2, padx = 3, pady = 3, sticky = E)
        
        self.desc_ent =  Entry(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                               cursor = 'xterm', selectbackground = 'dark goldenrod' , insertbackground = 'white')
        self.desc_ent.grid(row = 3 , column = 2, padx = 3, pady = 3, sticky = E)
        
        self.fwd_ent =  Entry(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                              cursor = 'xterm', selectbackground = 'dark goldenrod' , insertbackground = 'white')
        self.fwd_ent.grid(row = 4 , column = 2, columnspan = 2, padx = 3, pady = 3, sticky = E)
        

        #BUTTON WIDGET -----------------------------------------------------------------------------------------------------
        self.submitbutton = Button(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                   text = 'SUBMIT', command = lambda: self.enter_new_entry())     
        self.submitbutton.grid(row = 5, columnspan = 4, padx = 3, pady = 3, sticky = E+W)
    
        #LOOP --------------------------------
        self.clog_level.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())
        self.clog_level.mainloop()


    def set_clog_level_size(self):
        '''
        CLASS FUNC #1-------------------------------------------------
        Func to set the min and max adjustable size of the window.
        Will maintain its size to minimize adjustments required.
        '''
        
        self.clog_level.minsize(575,800)
        self.clog_level.maxsize(580,900)
        
        print 'Succesful Pass of set call log window size parameters'
        return


    def open_db_file(self):
        floc = tkFileDialog.askopenfilename(title = 'Chose database directory',
                                              initialdir= r"C:\Anaconda2\Scripts\databases",
                                              filetypes = (("database file", "*.db"),))
        self.database_load(floc)


    def ask_db_filename(self):
        '''

        '''
        fname = tkFileDialog.asksaveasfilename(title = 'Chose database directory',
                                              initialdir= r"C:\Anaconda2\Scripts\databases",
                                              filetypes = (("database file", "*.db"),))
        self.database_load(fname)

        

    def database_load(self, dbfile):
        '''

        '''
        self.db_loc = dbfile

        if self.db_loc != None:
            self.currlog = sq3.connect(self.db_loc)
            self.currlog.row_factory = sq3.Row
            self.cur = self.currlog.cursor()

        self.create_table()
        self.reset_ent_widgets()
        
        days = {'MONDAY': self.mon_text,
                    'TUESDAY': self.tue_text,
                    'WED': self.wed_text,
                    'THURSDAY': self.thur_text,
                    'FRIDAY': self.fri_text}
        
        for k,v in days.items():
            self.cur.execute('''SELECT COUNT(*) FROM call_log WHERE day = ?''', (k,))
            days_ents = self.cur.fetchone()

            v.delete(1.0, END)
            itr = 1
            v.insert(END, '--Entry 1 of {}--------------------------\n'.format(days_ents[0]+1))


            self.cur.execute('''SELECT * FROM call_log WHERE day = ?''', (k,))            #OUTPUT - ['datestamp', 'compname', 'contact', 'medium', 'desc', 'forward', 'day']
            for row in self.cur.fetchall():

                insrt = '''\nCompany Name: {}
    Contact: {}
    Medium: {}
    Description: {}
    Forward: {}
    Day of Week: {}
    Timestamp: {}\n\n'''.format(row['compname'].encode('utf-8'), row['contact'].encode('utf-8'), row['medium'].encode('utf-8'),
                                row['desc'].encode('utf-8'), row['forward'].encode('utf-8'), row['day'].encode('utf-8'), row['datestamp'].encode('utf-8')) 

                v.insert(END, insrt)
                itr+=1
                v.insert(END, '--Entry {} of {}--------------------------\n'.format(itr,days_ents[0]+1))
                
        self.reset_ent_widgets()


    def check_if_db_open(self):
        '''
        Func to check if NOTE can and should be added. If no DB active then watrning is provided.
        Else - func will move forward with request
        '''

        try:
            if self.currlog:
                self.add_note_to_db()
        except AttributeError:
            tkMessageBox.showerror(title = 'ERROR', message = 'No DB has been connected!\nPlease, try again')



    def add_note_to_db(self):

        self.notewin = Toplevel()
        self.notelf = LabelFrame(self.notewin, text = 'ADD note then press SUBMIT', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.notelf.grid(padx = 5, pady = 5, sticky = NSEW)

        self.notetext = Text(self.notelf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            cursor = 'xterm', selectbackground = 'dark goldenrod' ,selectforeground = 'black')
        self.notetext.grid(row = 0, padx = 5, pady = 5, sticky = NSEW)

        self.notebutt = Button(self.notelf, text = 'SUBMIT', command = lambda: self.enter_note(),
                               bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2')
        self.notebutt.grid(row = 1, padx = 5, pady = 5, sticky = E+W)

        self.notewin.protocol("WM_DELETE_WINDOW", lambda: self.note_close())
        self.notewin.mainloop()


    def note_close(self):
        '''
        Func - user clicking 'X' will close window
        '''
        self.notewin.destroy()
        return
    

    def enter_note(self):

        self.unix = time.time()
        self.notedate = str(datetime.datetime.fromtimestamp(self.unix).strftime('%Y-%m-%d  %H: %M: %S'))
        n = self.notetext.get(1.0, END)
        self.cur.execute("""INSERT INTO log_notes (datestamp, note) VALUES (?, ?)""", (self.notedate,n))
        self.currlog.commit()

        selects = self.cur.execute('''SELECT * FROM log_notes''')
        for row in selects.fetchall():
            print 'Timestamp: {}'.format(row[0])
            print 'NOTE:  {}'.format(row[1])

        self.notewin.destroy()
        return
    

    def reset_ent_widgets(self):

        '''
        CLASS FUNC #7-------------------------------------------
        Func - Reset the entriy widgets to blank for next entry
        '''
        
        self.comp_ent.delete(0,END)   #Company name
        self.cont_ent.delete(0,END)    #Contact Name
        self.med_ent.delete(0,END)    #Medium 
        self.desc_ent.delete(0,END)    #Description
        self.fwd_ent.delete(0,END)    #Forward

        return


    #THIS IS FIRST RUN ONLY --------- AFTER IT HAS BEEN CREATED WILL RAISE ERROR
    def create_table(self):
        '''
        CLASS FUNC #4----------------------
        Func to create table in the database
        '''
        
        self.currlog.execute('CREATE TABLE IF NOT EXISTS call_log (datestamp TEXT, compname TEXT, contact TEXT, medium TEXT,  desc TEXT, forward TEXT, day TEXT)')
        self.currlog.commit()

        self.currlog.execute('CREATE TABLE IF NOT EXISTS log_notes (datestamp TEXT, note TEXT)')
        self.currlog.commit()
        
        return

        #This will be a database that contains and tracks all the notes needed to add for overall message of the call log for any particular week
        #Each entry will be datestamped.
        #self.cur.execute('CREATE TABLE IF NOT EXISTS call_log_notes (datestamp TEXT, note TEXT)')
        #self.currlog.commit()
    

    def enter_new_entry(self):      #Normally had d as argument
        '''
        CLASS FUNC #5------------------------------------------------------------------------------------------
        Func that recieves the day of the week from inser of database and then refreshing the text box
       
        CLASS FUNC #12 -------------------------------------------------

        CALLED from submit button for  new entries
        datestamp, compname, contact,  medium, desc, forward, day

        *FUTURE - Think about swapping out spinbox with a popup toplevel window asking for the day to enter.
        '''
        
        self.unix = time.time()
        self.date = str(datetime.datetime.fromtimestamp(self.unix).strftime('%Y-%m-%d  %H: %M: %S'))
        
        e1 = self.comp_ent.get()    #Company name
        e2 = self.cont_ent.get()      #Contact Name
        e3 = self.med_ent.get()     #Medium 
        e4 = self.desc_ent.get()     #Description
        e5 = self.fwd_ent.get()      #Forward
        s1 = self.spinbox.get()       #Day - M/T/W/TH/F

        self.cur.execute('INSERT INTO call_log (datestamp, compname, contact,  medium, desc, forward, day) VALUES (?, ?, ?, ?, ?, ?, ?)', (self.date, e1, e2, e3, e4, e5, s1))
        self.currlog.commit()
        
        days = {'MONDAY': self.mon_text,
                    'TUESDAY': self.tue_text,
                    'WED': self.wed_text,
                    'THURSDAY': self.thur_text,
                    'FRIDAY': self.fri_text}
        
        for k,v in days.items():
            self.cur.execute('''SELECT COUNT(*) FROM call_log WHERE day = ?''', (k,))
            days_ents = self.cur.fetchone()

            v.delete(1.0, END)
            itr = 1
            v.insert(END, '--Entry 1 of {}--------------------------\n'.format(days_ents[0]+1))


            self.cur.execute('''SELECT * FROM call_log WHERE day = ?''', (k,))            #OUTPUT - ['datestamp', 'compname', 'contact', 'medium', 'desc', 'forward', 'day']
            for row in self.cur.fetchall():

                insrt = '''\nCompany Name: {}
Contact: {}
Medium: {}
Description: {}
Forward: {}
Day of Week: {}
Timestamp: {}\n\n'''.format(row['compname'].encode('utf-8'), row['contact'].encode('utf-8'), row['medium'].encode('utf-8'),
                                row['desc'].encode('utf-8'), row['forward'].encode('utf-8'), row['day'].encode('utf-8'), row['datestamp'].encode('utf-8')) 

                v.insert(END, insrt)
                itr+=1
                v.insert(END, '--Entry {} of {}--------------------------\n'.format(itr,days_ents[0]+1))
                
        self.reset_ent_widgets()



    def new_database(self):
        '''
        CLASS FUNC #8 ------------------------------------------
        Func called from Call log window menubar

        Will allow users to enter new db name and start new file
        '''

        self.ResetEntries()     #CF#7
        self.ask_new = Toplevel()
        self.ask_new.title('New DB Creation')
        self.ask_new.config(bg =  '#0C1021')

        self.entnew_labelframe = LabelFrame(self.ask_new, text = 'Please enter a new DB file name', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.entnew_labelframe.grid(padx = 5, pady = 5, sticky = NSEW)

        self.newdb_ent = Entry(self.entnew_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                               cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white')
        self.newdb_ent.grid(row = 0 , padx = 3, pady = 3)

        self.newdb_butt = Button(self.entnew_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                   text = 'OK', command = lambda: self.ask_newdb_dir())     #CF#9
        self.newdb_butt.grid(row = 1, padx = 3, pady = 3)

        self.ask_new.protocol("WM_DELETE_WINDOW", lambda: self.ask_new.destroy())
        self.ask_new.mainloop()
        

       

    def on_closing(self):
        '''
        CLASS FUNC #10 -----------------------------------------------------------------
        
        Func called from Call log window when the 'X' button is pressed to close win
        Note: If this is called before connection to database is established, need
        to catch attribute error and pass it
        '''

        try:
            self.currlog.close()
            print "Current connection to DB Succesfully closed"

        except AttributeError as e:
            print e
        
        self.parent.deiconify()
        self.clog_level.destroy()
        return




    ##########################################################################################
    #CREATION OF TEXT FILE -----------------------------------------------------------------------------------------------------------------------------------
    def name_text_file(self):
        '''
        A Toplevel window that allows users to enter all the info required to properly compile and file all
        of the entries for the call log.

        Makes call to compiler func that writes to file row for row in the database
        '''
        
        calen = self.pull_month_calendar()          #Call to return current calendar month in str format to display

        self.name_text = Toplevel()
        self.name_text.title('Choose File Dir')
        self.name_text.minsize(565,545)
        self.name_text.maxsize(580,550)
                             
        self.name_frame = Frame(self.name_text, bg =  '#0C1021')
        self.name_frame.grid()

        #WIDGET CREATION
        self.name_lab = Label(self.name_frame, text = 'Please Enter a File name and\nchoose a directory!',
                               bg =  '#0C1021', fg = 'white', font = ('Verdana',12,'bold'))
        self.name_lab.grid(row = 0, columnspan = 2, padx = 5, pady = 5)

        self.ent_lab = Label(self.name_frame, text = 'Enter File name:',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.ent_lab.grid(row = 1,columnspan = 2,  padx = 5, pady = 5)

        self.lab_ent = Entry(self.name_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 25,
                               cursor = 'xterm', selectbackground = 'dark goldenrod',insertbackground = 'white' )
        self.lab_ent.grid(row = 2,columnspan = 2,  padx = 15, pady = 5, sticky = E+W)

        self.cal_display = Label(self.name_frame, text = calen, bg =  '#0C1021', fg = 'white', font = ('Verdana',13), cursor = 'plus')
        self.cal_display.grid(row = 3, columnspan = 2, padx = 5, pady = 5, sticky = NSEW)

        self.week_lab = Label(self.name_frame, text = 'Enter what week this is for:',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.week_lab.grid(row = 4, columnspan = 2, padx = 5, pady = 5)

        self.week_ent = Entry(self.name_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 25,
                               cursor = 'xterm', selectbackground = 'dark goldenrod' ,insertbackground = 'white')
        self.week_ent.grid(row = 5, columnspan = 2, padx = 15,  pady = 5, sticky = E+W)

        self.log_notes = Label(self.name_frame, text = 'Do you have any comments to\nadd to the call log?',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.log_notes.grid(row = 6, columnspan = 2, padx = 5, pady = 5)

        self.dir_textframe = LabelFrame(self.name_frame, text = 'Add Note to Call Log:', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.dir_textframe.grid(row = 7, columnspan = 2,  padx = 5, pady = 5)
                                                
        self.notes_txt = Text(self.dir_textframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), 
                            cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white', height = 5)
        self.notes_txt.grid(columnspan = 2, padx = 5, pady = 5, sticky = NSEW)

        self.dir_button = Button(self.dir_textframe, text = 'Choose File Directory', bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                 command = lambda: self.ask_dir(self.lab_ent.get(), self.notes_txt.get(1.0, END), self.week_ent.get()))
        self.dir_button.grid(row = 1, columnspan = 2, padx = 5, pady = 5, sticky = E+W)

        #self.name_text.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())
        self.name_text.mainloop()



    def pull_month_calendar(self):
        '''
        Func - to pull current month calendar to display on call log to help aid define which week.
        
        '''
        today = datetime.date.today()
        today_str = today.strftime("%d/%m/%Y").split('/')
        mm = int(today_str[1])
        yyyy = int(today_str[-1])
        return calendar.month(yyyy,mm)


    def ask_dir(self, fname, lognotes, wk):
        '''
        
        '''
        fdir = tkFileDialog.askdirectory()
        self.write_to_text_file(fdir, fname.replace(' ', '_'), lognotes, wk)
        self.name_text.destroy()


    def write_to_text_file(self, fdir, fname, lognotes, wk):
        '''
        - Ask where they want file saved to:
        - need to add option for continually applying general comments
        - Keep write to file and reset log seperate.... -or- until we know all the bugs have been removed
        '''

        wrapper = textwrap.TextWrapper(width = 100)
        #EX: txtt = wrapper.wrap(text = txt)

        fdir_alter = fdir.replace('/','\\')
        fname_alter = fname + '.txt'
                                  
        full_dir = r'{}\{}'.format(fdir_alter, fname_alter)

        #This will be standard format for top of all Call Logs
        Intro_L1 = 'CALL LOG:  DXP Enterprises, Phoenix AZ'
        Intro_L2 = 'SALESMAN :  Tony Kinsey_Engineered Sales_#480-294-1294'
        Intro_L3 = 'WEEK OF {}\n'.format(wk)
        Intro_L4 = 'OVERVIEW NOTES:\n'
        

        introlines = (Intro_L1, Intro_L2, Intro_L3)
        breakline = '''\n------------------------------------------------------------------------------------------------------------------------\n'''
        endline = '''\n\n---------------------------------------------END OF FILE----------------------------------------------------------------\n\n'''

        try:
            with open(full_dir, 'w')as F:
                
                for line in introlines:
                    F.write(line.center(100))
                    F.write('\n')

                F.write(Intro_L4)
                selects = self.cur.execute('''SELECT * FROM log_notes''')
                for row in selects.fetchall():
                    F.write('Timestamp: {}'.format(row[0]))
                    F.write('NOTE:  {}'.format(row[1]))
                    
                F.write(breakline)

            days = ('MONDAY', 'TUESDAY', 'WED', 'THURSDAY', 'FRIDAY')
            for d in days:
                self.cur.execute('SELECT COUNT(*) FROM call_log WHERE day = ?''', (d,))
                cnt = int(self.cur.fetchone()[0])
                itr = 1
                with open(full_dir, 'a')as F:
                    F.write('**************   {} Entries:  ***************\n'.format(d.center(5)))        #Added '*'s to the entry make it pop when
                    F.write('''\n----Entry {} of {}---------------------------------------------------------------------------------------------------------\n\n'''.format(itr, cnt))

                    self.cur.execute('''SELECT * FROM call_log WHERE day = ?''', (d,))
                    #Wrap all of the rows ---- Dont want print out to have long uneven lines. (FOR Format purpous)
                    for row in self.cur.fetchall():
                        row0 =  textwrap.fill(row[0].encode('utf-8'), width = 100)             #wrapper.wrap(text = (row[0]).encode('utf-8'))
                        row1 =  textwrap.fill(row[1].encode('utf-8'), width = 100)            #wrapper.wrap(text = (row[1]).encode('utf-8'))
                        row2 =  textwrap.fill(row[2].encode('utf-8'), width = 100)            #wrapper.wrap(text = (row[2]).encode('utf-8'))
                        row3 =  textwrap.fill(row[3].encode('utf-8'), width = 100)            #wrapper.wrap(text = (row[3]).encode('utf-8'))
                        row4 =  textwrap.fill(row[4].encode('utf-8'), width = 100)            #wrapper.fill(text = (row[4]).encode('utf-8'))
                        row5 =  textwrap.fill(row[5].encode('utf-8'), width = 100)            #wrapper.fill(text = (row[5]).encode('utf-8'))
                        row6 =  textwrap.fill(row[6].encode('utf-8'), width = 100)            #wrapper.wrap(text = (row[6]).encode('utf-8'))

                        rows = clc.OrderedDict()
                        rows['Account Name'] = row1
                        rows['Contact Name'] = row2
                        rows['Contact Method'] = row3
                        rows['Description'] = row4
                        rows['Follow UP'] = row5
                        rows['Timestamp'] = row0
                        rows['Day of Entry'] = row6

                        itr += 1
                        for k,v in rows.items():
                            F.write('{}:{}\n'.format(k,v))
                        if itr <= cnt:
                            F.write('''\n----Entry {} of {}---------------------------------------------------------------------------------------------------------\n\n'''.format(itr, cnt))
                        else:
                            pass
                    F.write('''\n-----------------------------------------END OF {} ENTRIES-----------------------------------------------------------\n'''.format(d))

            with open(full_dir, 'a')as F:
                F.write(endline)

##            with open(r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\banner.txt", 'a')as A:
##                lines = A.readlines()
##                for line in lines:
##                    A.write(line)
                    
            print 'Succesful Upload of Call Log to Designated Folder'
            self.ask_if_reset()

        except Exception as e:
            print e
            print '''An Error has occured, please check data has not been comprimised'''



    def ask_if_reset(self):
        '''

        '''
        tkMessageBox.askyesno("Success!","It appears your call log entries have\nbeen succesfully exported.\nWould you like to reset log now?")
        if 'yes':
            pass        
            #self.reset_procedure()
        else:
            tkMessageBox.OK('Sys Response', 'Ok no problem')
            
        return



    def reset_log_protocol(self):
        '''
        Func to call and reset the call log. Will delete all entries and enter new database directory.
        Saves it to the designated Database file
        '''
        pass
    


######################################################################################################
#TO DO WINDOW ------------------------------------------------------------------------------------------------------------------------------------------------------------------
class ToDo(object):
    
    def __init__(self, parent):
        '''
        To Add:
            - With the list we have how many contacts show with it
            - 
        '''
        
        self.parent = parent         #Roots frame 
        self.parent.iconify()          #Iconify or 'Minimize' the main frame to make toplevel have focus

        self.Todo_Database()        #Initiate todo Database

        self.todo_level = Toplevel()
        self.todo_level.title('TO DO WINDOW')
        self.todo_level.minsize(800,800)
        self.set_todo_level_size()
       
                
        ########################################################################################################
        #MENUBAR CREATION--------------------------------------------------------------------------------------------------
        self.menubar = Menu(self.todo_level, background = '#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.filemenu = Menu(self.menubar, tearoff=0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.filemenu.add_command(label="ToDo", command = None)
        self.filemenu.add_command(label="Tools", command = None)
        self.filemenu.add_command(label="Ref. Files", command = None)
        self.menubar.add_cascade(label="File", menu = self.filemenu)

        #STATE CHOICE-----------------------------------------------------------------------------------------------------------------------------
        self.statemenu = Menu(self.menubar, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.statemenu.add_command(label = "AZ", command = lambda: None)
        self.statemenu.add_command(label = "NV", command = lambda: None)
        self.statemenu.add_command(label = "NM", command = lambda: None)
        self.menubar.add_cascade(label = "State Mode", menu = self.statemenu)

        self.todo_level.config(bg='#0C1021', menu = self.menubar)


        ########################################################################################################
        #TOPLEVEL FRAME--------------------------------------------------------------
        self.todo_frame = Frame(self.todo_level, bg =  '#0C1021')
        self.todo_frame.grid(row = 0, column = 0, columnspan = 2)

        #TOPLEVEL LABELFRAME------------------------------------------------------------------------------------------------------------------------------
        self.lf_todo = LabelFrame(self.todo_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'), text = "TO DO's")
        self.lf_todo.grid(row = 0, columnspan = 2, padx = 3, pady = 3, sticky = N+E+W)

        self.redlf = LabelFrame(self.lf_todo, bg =  '#0C1021', fg = 'red', font = ('Verdana',7), text = 'RED LEVEL (URGENT)')
        self.redlf.grid(row = 0, columnspan = 2, padx = 3, pady = 3, sticky = N+E+W)
                                  
        self.yellf = LabelFrame(self.lf_todo, bg =  '#0C1021', fg = 'yellow', font = ('Verdana',7), text = 'YELLOW LEVEL (INTERMED)')
        self.yellf.grid(row = 1, columnspan = 2, padx = 3, pady = 3, sticky = N+E+W)
                                  
        self.whilf = LabelFrame(self.lf_todo, bg =  '#0C1021', fg = 'white', font = ('Verdana',7), text = 'WHITE LEVEL (NORMAL)')
        self.whilf.grid(row = 2, columnspan = 2, padx = 3, pady = 3, sticky = N+E+W)




       #########################################################################################################
        #LISTBOXES TO HOUSE EACH CATEGORY OF TO DO LIST - RED, YELLOW, GREEN------------------------------
        #RED CREATION
        self.lboxred = Listbox(self.redlf, bg =  '#0C1021', fg = 'red', font = ('Verdana',8), relief = GROOVE,
                            cursor = 'xterm', selectbackground = 'white', selectforeground = 'black',  width = 100, height = 5)
        self.lboxred.grid(row = 0, rowspan = 2, columnspan = 2, padx =5, pady = 3, sticky = E+W)
        
        self.r_to_yellow = Checkbutton(self.redlf, bg =  '#0C1021', fg = 'red', font = ('Verdana',6), text = '*',
                                         onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = RIGHT,
                                         command = lambda: self.DeleteAndMove('RED','YELLOW'))
        self.r_to_yellow.grid(row = 0, column = 3)        

        self.r_to_white = Checkbutton(self.redlf, bg =  '#0C1021', fg = 'white', font = ('Verdana',6), text = '*',
                                         onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = RIGHT,
                                         command = lambda: self.DeleteAndMove('RED','WHITE'))
        self.r_to_white.grid(row = 1, column = 3)
         
        
        #YELLOW 
        self.lboxyellow = Listbox(self.yellf, bg =  '#0C1021', fg = 'yellow', font = ('Verdana',8),
                            cursor = 'xterm', selectbackground = 'white', selectforeground = 'black', width = 100, height = 5)
        self.lboxyellow.grid(row = 0, rowspan = 2,  columnspan = 2, padx =5, pady = 3, sticky = E+W)

        self.y_to_red = Checkbutton(self.yellf, bg =  '#0C1021', fg = 'yellow', font = ('Verdana',6), text = '*',
                                         onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = RIGHT,
                                         command = lambda: self.DeleteAndMove('YELLOW', 'RED'))
        self.y_to_red.grid(row = 0, column = 3)        

        self.y_to_white = Checkbutton(self.yellf, bg =  '#0C1021', fg = 'white', font = ('Verdana',6), text = '*',
                                         onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = RIGHT,
                                         command = lambda: self.DeleteAndMove('YELLOW','WHITE'))
        self.y_to_white.grid(row = 1, column = 3)


        #GREEN
        self.lboxgreen = Listbox(self.whilf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                            cursor = 'xterm', selectbackground = 'white', selectforeground = 'black', width = 100, height = 5)
        self.lboxgreen.grid(row = 0, rowspan = 2, columnspan = 2, padx =5, pady = 3, sticky = E+W)

        self.w_to_yellow = Checkbutton(self.whilf, bg =  '#0C1021', fg = 'yellow', font = ('Verdana',6), text = '*',
                                         onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = RIGHT,
                                         command = lambda: self.DeleteAndMove('WHITE','YELLOW'))
        self.w_to_yellow.grid(row = 0, column = 3)        

        self.w_to_red = Checkbutton(self.whilf, bg =  '#0C1021', fg = 'red', font = ('Verdana',6), text = '*',
                                         onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = RIGHT,
                                         command = lambda: self.DeleteAndMove('WHITE','RED'))
        self.w_to_red.grid(row = 1, column = 3)
        


        #################################################################################################
        #BUTTON TO KILL WINDOW AND BRING BACK MAIN------------------------------------------------------------------
        self.close_button = Button(self.lf_todo, text = 'CLOSE TO DO WINDOW!', font = ('Verdana',8,'bold'),
                                   command = lambda: self.KillWindow(parent), bg =  '#0C1021', fg = 'white')
        self.close_button.grid(row = 3, columnspan = 2, padx = 5, pady = 3, sticky = E+W)


        #LABELS FOR THE ENTRIES-------------------------------------------------------------------------------------------------------------
        self.dslab = Label(self.todo_frame, text = 'Date Entered: {}'.format(self.DateReturn()), bg =  '#0C1021', fg = 'white', font = ('Verdana',8))         #some type of auto populate
        self.dslab.grid(row = 3, padx = 5, pady = 3)  #columnspan = 2, sticky = E+W
        
        self.ddlab = Label(self.todo_frame, text = 'Date Due', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.ddlab.grid(row = 4 , padx = 5, pady = 3)

        self.cclab = Label(self.todo_frame, text = 'ToDo Flag', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))           #Think about using a spinbox
        self.cclab.grid(row = 5 , padx = 5, pady = 3)

        self.sslab = Label(self.todo_frame, text = 'Status', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.sslab.grid(row = 6 , padx = 5, pady = 3)

        self.desclab = Label(self.todo_frame, text = 'Description', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.desclab.grid(row = 7, padx = 5, pady = 3)

        self.conlab = Label(self.todo_frame,  text = 'Who/What?', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.conlab.grid(row = 8, padx = 5, pady = 3)
        
        
        #Datedue - Lets do a calendar pick widge
        self.date_ent =  Entry(self.todo_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     cursor = 'xterm', selectbackground = 'dark goldenrod' )
        self.date_ent.grid(row = 4, column = 1, padx = 5, pady = 3, sticky = E+W)
        
        #Color Code - Spinbox
        self.clrvar = StringVar()
        self.choices = ('RED','YELLOW','WHITE' )
        
        self.clrcode = Spinbox(self.todo_frame, values = self.choices, bg =  '#0C1021', fg = 'red', font = ('Verdana',8),
                               textvariable = self.clrvar, command = lambda: self.SpinTextColor(self.clrvar.get()))
        self.clrcode.grid(row = 5, column = 1, padx = 5, pady = 3, sticky = E+W)

        #Status - Spinbox - WAIT, HOLD, LATE, URGENT, NORUSH
        self.statvar = StringVar()
        self.statusvals = ('WAIT', 'HOLD', 'LATE', 'URGENT', 'NORUSH')
        
        self.status_ent = Spinbox(self.todo_frame, values = self.statusvals, bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                               textvariable = self.statvar, command = lambda: None)
        self.status_ent.grid(row = 6, column = 1, padx = 5, pady = 3, sticky = E+W)
        
        #Description - TEXT WIDGE
        self.desc_ent = Text(self.todo_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                            cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', height = 3, relief = SUNKEN)
        self.desc_ent.grid(row = 7, column = 1, padx = 5, pady = 3, sticky = E+W)

        #Contact Entry - Who is involved?
        self.con_ent =  Entry(self.todo_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     cursor = 'xterm', selectbackground = 'dark goldenrod' )
        self.con_ent.grid(row = 8, column = 1, padx = 5, pady = 3, sticky = E+W)


        ####################################################################################################
        #CHECKBOX - FOLLOWUP REQUIRED (or Reminder)
        self.followupreqd = Label(self.todo_frame, text = "Follow UP Req'D?", bg =  '#0C1021', fg = 'white', font = ('Verdana',12, 'bold'))
        self.followupreqd.grid(row = 9, columnspan = 2, padx = 5, pady = 3, sticky = E+W)

        self.chkyes_var = IntVar()
        self.chkno_var = IntVar()                             
        self.checkyes = Checkbutton(self.todo_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), text = 'YES',
                                    onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = CENTER, variable = self.chkyes_var,
                                    command = lambda: self.DisableNoButton())
        self.checkyes.grid(row = 10, columnspan = 2, padx = 2, pady = 5, sticky = E+W)

        self.checkno = Checkbutton(self.todo_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), text = 'NO',
                                   onvalue = 1, offvalue = 0, selectcolor = '#0C1021', justify = CENTER, variable = self.chkno_var,
                                   command = lambda: self.DisableYesButton())
        self.checkno.grid(row = 11, columnspan = 2, padx = 2, pady = 5, sticky = E+W)


        ####################################################################################################
        #BUTTON WIDGET ----------------------------------------------------------------------------------------------------
        self.submitbutton = Button(self.todo_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8, 'bold'), cursor = 'hand2',
                                   text = 'SUBMIT', command = lambda: self.SubmitEntry())
        self.submitbutton.grid(row = 12, columnspan = 2, padx = 5, pady = 5, sticky = E+W)

        #Mainloop
        self.todo_level.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())
        self.StartUpLoadList()
        
        self.todo_level.mainloop()




    def set_todo_level_size(self):
        '''

        '''
        
        self.todo_level.maxsize(1000,1000)
        self.todo_level.update()
        print 'Succesful Pass of size func'
        return



    def DeleteAndMove(self, currlist, newlist):
        '''
        Func to move one to do list to the other
        **** May be getting to cute with code. KISS Principles!
        '''
        
        pass
    


    def DisableNoButton(self):
        '''
        Func to check the checkbutton state - so both cannot be on the same time
        '''
        self.checkno.deselect()
        return
    


    def DisableYesButton(self):
        '''

        '''
        
        self.checkyes.deselect()
        return
              



    def Todo_Database(self):
        '''

        '''
        
        self.dbloc = r'C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\tk_todolist.db'
        self.dataname = 'tk_todolist.db'
        self.conn = sq3.connect(self.dbloc)
        self.c = self.conn.cursor()

        try:
            self.create_todo_table()
        except:
            pass

        return



    #THIS IS FIRST RUN ONLY --------- AFTER IT HAS BEEN CREATED WILL RAISE ERROR
    def create_todo_table(self):
        '''
        Func to create table in the database
        '''
        
        self.c.execute('CREATE TABLE IF NOT EXISTS todo (datestamp TEXT, datedue TEXT, colorcode TEXT NOT NULL, status TEXT, descript TEXT, cont_comp TEXT)')
        self.conn.commit()
        
        return



    def SubmitEntry(self):
        '''

        '''
        
        self.c.execute("INSERT INTO todo VALUES (:dstamp, :ddue, :clrcode, :sts, :desc, :concomp)",
                       {
                           'dstamp': self.DateReturn(),
                           'ddue': self.date_ent.get(),
                           'clrcode': self.clrvar.get(),
                           'sts': self.statvar.get(),
                           'desc': self.desc_ent.get(1.0, END),
                           'concomp': self.con_ent.get(),
                        }
                          )
        self.conn.commit()
        
        #self.c.execute('INSERT INTO todo (datestamp, datedue , colorcode , status, descript, cont_comp) VALUES (?, ?, ?, ?, ?, ?)',(a1,a2,a3,a4,a5,a6))#datestamp, datedue , colorcode , status, descript, cont_comp 
        #self.conn.commit()
        self.WidgetClear()
        



    def WidgetClear(self):
        '''

        '''
        
        #Disable Checkbuttons
        self.checkno.deselect()
        self.checkyes.deselect()

        #Entry Clear
        self.date_ent.delete(0,END)
        self.desc_ent.delete(1.0,END)
        self.con_ent.delete(0,END)
        return



    def on_closing(self):
        '''
        Func if the window is closed... close the db and raise back the main window
        '''
        
        self.conn.close()
        self.parent.deiconify()
        self.todo_level.destroy()

        return




    def SpinTextColor(self, clr):
        '''
        Each time spinbox up and down arrows pressed. It checks the current item.
        We change the FG color to match what the text states
        '''
        
        colorcodes = {'RED':'red',
                              'YELLOW':'yellow',
                              'WHITE':'white'}
        
        return self.clrcode.config(fg = colorcodes[clr])
        
        


    def KillWindow(self, parent):
        '''
        Func to kill the current window and raise the main
        .'''
        
        parent.deiconify()
        self.todo_level.destroy()
        return
    


    def load_list(self):
        '''
        Functo load the list to be added to the textbox widget
        '''
        
        with open(r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Sales Accounts.txt",'r')as F:
            lines = F.readlines()
            for i in lines:
                self.textbox.insert(END, i)

        return
    


    def DateReturn(self):
        '''
        Func to return the date in string form
        '''
        
        self.unix = time.time()
        self.date = str(datetime.datetime.fromtimestamp(self.unix).strftime('%d-%m-%Y  %H: %M: %S'))
        return self.date
    



    def StartUpLoadList(self):
        '''
        widge = Listbox from todo frame

        Since Tkinter cant keep have individual lines we will track all of them and update the colors in one swoop
        '''

        colorcodes = {'RED':'red',
                              'YELLOW':'yellow',
                              'GREEN':'white'}

        clr_check = "SELECT * FROM todo WHERE colorcode = ?"
        for k,v in colorcodes.items():
            self.c.execute(clr_check , (k,))
            pulled = self.c.fetchall()
            
            for thngs in pulled:
                if k == 'RED':
                    self.lboxred.insert(END, thngs)
                if k == 'YELLOW':
                    self.lboxyellow.insert(END, thngs)
                if k == 'GREEN':
                    self.lboxgreen.insert(END, thngs)
        return



    def ConfigColors(self, widge, qty, widge2):
        '''

        '''
        
        for i,j in widge2.items():
            widge.itemconfig(int(i), fg = j)
    


    def todo_db_entry(self, a1, a2, a3, a4, a5, a6):
        
        '''
        datestamp, datedue , colorcode , status, descript, cont_comp 

        datestamp = When was to do entered
        datedue =  When is this to do by entry needed?
        colorcode = RED, YELLOW, GREEN
                - RED - immediate attention, YELLOW - needs to get done, GREEN - can wait until other things get done
        status = Whats Status? WAIT, HOLD, LATE, URGENT, NORUSH
        descript = Description of the TO DO
        cont_comp = Enter a Company name or Contacts - Something Identifiable

        self.contodo = sq3.connect(self.dataname)
        self.curtodo = self.contodo.cursor()
        '''

        #datestamp, datedue , colorcode , status, descript, cont_comp 
        self.c.execute('INSERT INTO todo (datestamp, datedue , colorcode , status, descript, cont_comp) VALUES (?, ?, ?, ?, ?, ?)',(a1,a2,a3,a4,a5,a6))
        self.conn.commit()
        
        self.StartUpLoadList(a3)



    def TimeElapsedWarning(self):
        
        '''
        Func to check days between today and when the entry was made
        - If too many days have passed a message will pop up
        '''
        
        check = datetime.datetime.today()
        self.c.execute('SELECT * FROM todo')
        entries = self.c.fetchall()
        
        for i in entries[0]:
            tdelta = (check - i).days
            if tdelta <= 7:
                pass
            else:
                pass
        



def startup():
    '''
    Initilize the database before
    '''
    root = Tk()
    App(root)
    root.mainloop()
    c.close()
    conn.close()




        
####################################
#MAIN CALL
####################################            
if __name__ == '__main__':
    startup()
    
##    root = Tk()
##    App(root)
##    root.mainloop()
##    c.close()
##    conn.close()




