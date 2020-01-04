import sqlite3 as lite
from sqlite3 import Error
import datetime, time, random
from Tkinter import *
import datetime
import ttk
import os
import webbrowser as wb
import tkFileDialog
import tkcalendar
import collections as clc
import tkMessageBox
import textwrap
import calendar


#READ ME --------------------------------------------------------------------------------------------------------------------------------------------------------
'''
Each state will have an accounts database and a contacts database

'''
############################################################################################


##START OF THE MAIN DATABASE
##conn = sq3.connect(':memory:')
##c = conn.cursor()


conn = lite.connect(':memory:')




file_contain =  {
                        'AZA': r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\AZ Accounts",
                        'AZC': r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\AZ Accounts\AZ Contacts",
                        'NVA': r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\NV Accounts",
                        'NVC': r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\NV Accounts\NV Contacts",
                        'NMA': r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\NM Accounts",
                        'NMC': r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\NM Accounts\NM Contacts",
                      }



#THIS IS FIRST RUN ONLY --------- AFTER IT HAS BEEN CREATED WILL RAISE ERROR
def create_table_accounts():
    '''
    Func to initiate a table within the given database specified.
    - STATE (AZ,NV,NM)
        - INDUSTRY
            - Industrial
            - Commercial
            - Food and Beverage
            - Pulp and Paper
            - Municipal
            - Chemical
            - Agro
            - Engineering/Consulting
            - Other
            - All (*)

    Each company will fall under one of these filters. Each contact will have the following characteristics:
    '''
    
    #ARIZONA----------------------------------------------------------------------------------------------------
    #CREATE - ACCOUNTS DB
    #azacc = lite.connect(':memory:')
    conn.execute('''CREATE TABLE IF NOT EXISTS azaccounts
         (id INTEGER PRIMARY KEY AUTOINCREMENT,                     
         companyname   TEXT,
         industry            TEXT,
         overviewfile       TEXT,
         contactsfile        TEXT,
         note                  TEXT);''')
    conn.commit()
    #azacc.close()

    #azcon = lite.connect(':memory:')
    #CREATE - CONTACTS for EACH ACCOUNT
    conn.execute('''CREATE TABLE IF NOT EXISTS azcontacts
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         companyname  TEXT,
         contactfirst     TEXT,
         contactlast     TEXT,         
         position          TEXT,
         phonenumb    TEXT,
         numbalt         TEXT,
         email             TEXT,
         note              TEXT,
         datelast         TEXT);''')
    conn.commit()
    #azcon.close()

    #NEVADA -----------------------------------------------------------------------------------------------------
    #CREATE - ACCOUNTS DB
    #nvacc = lite.connect(':memory:')
    conn.execute('''CREATE TABLE IF NOT EXISTS nvaccounts
         (id INTEGER PRIMARY KEY AUTOINCREMENT,                     
         companyname   TEXT,
         industry             TEXT,
         overviewfile       TEXT,
         contactsfile        TEXT,
         note                  TEXT);''')
    conn.commit()
    #nvacc.close()

    #nvcon = lite.connect(':memory:')    
    #CREATE - CONTACTS for EACH ACCOUNT
    conn.execute('''CREATE TABLE IF NOT EXISTS nvcontacts
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         companyname  TEXT,
         contactfirst     TEXT,
         contactlast     TEXT,         
         position          TEXT,
         phonenumb    TEXT,
         numbalt         TEXT,
         email             TEXT,
         note              TEXT,
         datelast         TEXT);''')
    conn.commit()
    #nvcon.close()

    #NEW MEXICO------------------------------------------------------------------------------------------------
    #CREATE - ACCOUNTS DB
    #nmacc = lite.connect(':memory:')
    conn.execute('''CREATE TABLE IF NOT EXISTS nmaccounts
         (id INTEGER PRIMARY KEY AUTOINCREMENT,                     
         companyname   TEXT,
         industry             TEXT,
         overviewfile       TEXT,
         contactsfile        TEXT,
         note                 TEXT);''')
    conn.commit()
    #nmacc.close()
    
    #CREATE - CONTACTS for EACH ACCOUNT
    #nmcon = lite.connect(':memory:')
    conn.execute('''CREATE TABLE IF NOT EXISTS nmcontacts
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         companyname  TEXT,
         contactfirst       TEXT,
         contactlast       TEXT,         
         position            TEXT,
         phonenumb      TEXT,
         numbalt           TEXT,
         email               TEXT,
         note                TEXT,
         datelast           TEXT);''')
    conn.commit()
    #nmcon.close()
    return






#################################################################
#ACCOUNTS DATABASE ---------------------------------------------------------------------------------------

def accounts_commited(state, **kwargs):
    ''' COLUMN ------ companyname , industry,  overviewfile, contactsfile, note'''

    vcname  = kwargs['companyname']
    vind  = kwargs['industry']
    vovrfile  = kwargs['overviewfile']
    vcontfile  = kwargs['contactsfile']
    vnote  = kwargs['note']

    varcont = (vcname, vind, vovrfile, vcontfile, vnote) 

    if state == 'ARIZONA':
        az_account_add(*varcont)

    if state == 'NEVADA':
        nv_account_add(*varcont)

    if state == 'NEW MEXICO':
        nm_account_add(*varcont)

    else:
        pass        #pop_up_warning()



def az_account_add(*args):
    '''

    '''    
    #conn = lite.connect(':memory:')                        #cname + '\\{}.db'.format(cfile))    
    conn.execute('INSERT INTO azaccounts (companyname , industry,  overviewfile, contactsfile, note) VALUES (?, ?, ?, ?, ?)',
              (args))
    conn.commit()
    #conn.close()
    print 'succesful entry of az contact'
    return



def nv_account_add(*args):
    '''

    '''    
    #conn = lite.connect(':memory:')                        #cname + '\\{}.db'.format(cfile))   
    conn.execute('INSERT INTO nvaccounts (companyname , industry,  overviewfile, contactsfile, note) VALUES (?, ?, ?, ?, ?)',
              (args))
    conn.commit()
    #conn.close()
    print 'succesful entry of nv contact'
    return



def nm_account_add(*args):
    '''

    '''
    #conn = lite.connect(':memory:')                        #cname + '\\{}.db'.format(cfile))   
    conn.execute('INSERT INTO nmaccounts (companyname , industry,  overviewfile, contactsfile, note) VALUES (?, ?, ?, ?, ?)',
              (args))
    conn.commit()
    #conn.close()
    print 'succesful entry of nm contact'
    return





#################################################################
#CONTACTS DATABASE ---------------------------------------------------------------------------------------

def contacts_commited(state, cname, cfile, **kwargs):
    '''
    Func to add a row to a DB in the contacts
    state - will distribute these additions to the correct lfunctions
    cname - company name (company to be added to)
    cfile - location or name of the accounts contacts file

    COLUMNS ----- id, companyname, contactfirst, contactlast, position, phonenumb,  numbalt,  email, note, datelast
    '''

    vcname = kwargs['companyname']
    vfname = kwargs['contactfirst']
    flname = kwargs['contactlast']
    vpos = kwargs['position']
    vnumb = kwargs['phonenumb']
    vnumbalt = kwargs['numbalt']
    vemail = kwargs['email']
    vnote = kwargs['note']
    vdlast = kwargs['datelast']

    varcont = (vcname, vfname, flname, vpos, vnumb, vnumbalt, vemail, vnote, vdlast)
    
    if state == 'ARIZONA':
        az_contact_add(cname, cfile, *varcont)

    if state == 'NEVADA':
        nv_contact_add(cname, cfile, *varcont)

    if state == 'NEW MEXICO':
        nm_contact_add(cname, cfile, *varcont)

    else:
        pass        #pop_up_warning()


    
def az_contact_add(cname, cfile, *args):
    '''

    '''    
    #conn = lite.connect(cname + '\\{}.db'.format(cfile))    
    conn.execute('INSERT INTO azcontacts (companyname, contactfirst, contactlast, position, phonenumb,  numbalt,  email, note, datelast) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
              (args))
    conn.commit()
    #conn.close()
    print 'succesful entry of az contact'
    return



def nv_contact_add(cname, cfile, *args):
    '''

    '''    
    #conn = lite.connect(cname + '\\{}.db'.format(cfile))
    conn.execute('INSERT INTO nvcontacts (companyname, contactfirst, contactlast, position, phonenumb,  numbalt,  email, note, datelast) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
              (args))
    conn.commit()
    #conn.close()
    print 'succesful entry of nv contact'
    return



def nm_contact_add(cname, cfile, *args):
    '''

    '''
    #conn = lite.connect(cname + '\\{}.db'.format(cfile))
    conn.execute('INSERT INTO nmcontacts (companyname, contactfirst, contactlast, position, phonenumb,  numbalt,  email, note, datelast) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
              (args))
    conn.commit()
    #conn.close()
    print 'succesful entry of nm contact'
    return






def return_db():
    '''
    Func which calls to the DB and retrieves all entries that are present

    VARS : companyname , industry,  overviewfile, contactsfile, note
    '''
    azacc = conn.cursor()
    azcon = conn.cursor()
    az = conn.execute('SELECT * FROM azaccounts')
    for row in az.fetchall():
        r1 = textwrap.fill(str(row[0]), width = 80)
        r2 = textwrap.fill(str(row[1]), width = 80)
        r3 = textwrap.fill(row[2], width = 80)
        r4 = textwrap.fill(row[3], width = 80)
        r5 = textwrap.fill(row[4], width = 80)
        r6 = textwrap.fill(row[5], width = 80)

        print '\n---------------------------------------\n'
        print 'ID:                       {}'.format(r1)
        print 'COMPNAME:          {}'.format(r2)
        print 'INDUSTRY:           {}'.format(r3)
        print 'OVERVIEW FILE:    {}'.format(r4)
        print 'CONTACT FILE:     {}'.format(r5)
        print 'NOTES:                {}'.format(r6)
        print '\n--- CONTACTS ---------------------\n'

        #companyname, contactfirst, contactlast, position, phonenumb,  numbalt,  email, note, datelast
    azcon = conn.cursor()
    azresults = azcon.execute('SELECT * FROM azcontacts')
    for rows in azresults.fetchall():
        c1 = textwrap.fill(str(row[0]), width = 80)
        c2 = textwrap.fill(str(row[1]), width = 80)
        c3 = textwrap.fill(str(row[2]), width = 80)
        c4 = textwrap.fill(str(row[3]), width = 80)
        c5 = textwrap.fill(str(row[4]), width = 80)
        c6 = textwrap.fill(str(row[5]), width = 80)
##        c7 = textwrap.fill(str(row[6]), width = 80)
##        c8 = textwrap.fill(str(row[7]), width = 80)
##        c9 = textwrap.fill(str(row[8]), width = 80)
##        c10 = textwrap.fill(str(row[9]), width = 80)

        print 'ID:                   {}'.format(c1)
        print 'COMPNAME:      {}'.format(c2)
        print 'FIRST NAME:     {}'.format(c3)
        print 'LAST NAME:      {}'.format(c4)
        print 'POSITION:        {}'.format(c5)
        print 'PHONE #:          {}'.format(c6)
##        print 'PHONE # ALT:   {}'.format(c7)
##        print 'EMAIL:              {}'.format(c8)
##        print 'NOTE:               {}'.format(c9)
##        print 'DATE LAST:       {}'.format(c10)
        print '\n---------------------------------------\n'

    time.sleep(.1)

    nv = conn.execute('SELECT * FROM nvaccounts')
    for row in nv.fetchall():
        print row
    time.sleep(.25)

    nm = conn.execute('SELECT * FROM nmaccounts')
    for row in nm.fetchall():
        print row
    time.sleep(.25)

    return







class App(object):

    def __init__(self,parent):
        '''
        WIDGETS:
        state - Spinbox or Checkboxes
        companyname - Entry or Spinbox,
        industry - Spinbox,
        overviewfile - Choose directory?,
        contactsfile - Choose directory or just pick name (entry),
        note = TEXT box
        '''
        #column = 0,columnspan = 2,
        
        self.parent = parent
        self.parent.config(bg =  '#0C1021')
        self.parent.title('New Account Creation')

        #STATE INPUT---------------------------------------------------------------------------------------------------------------
        self.state_lf = LabelFrame(self.parent, text = 'STATE', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.state_lf.grid(row = 0, padx = 3, pady = 3, sticky = E+W)
        self.s_lab = Label(self.state_lf, text = 'Choose State to assign Account', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.s_lab.grid(row = 0, padx = 3, pady = 3, sticky = E+W)
        self.s_sbox = Spinbox(self.state_lf, values = ('ARIZONA','NEVADA','NEW MEXICO'), bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.s_sbox.grid(row = 1, padx = 3, pady = 3, sticky = E+W)


        #SEARCH INPUT--------------------------------------------------------------------------------------------------------------
        self.searchlab = Label(self.state_lf, text = 'Search for Entry', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.searchlab.grid(row = 0, column = 1, padx = 3, pady = 3, sticky = E)
        self.searchent = Entry(self.state_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.searchent.grid(row = 1, column = 1,padx = 3, pady = 3, sticky = E)
        self.searchbutt = Button(self.state_lf, text = 'Search', command = lambda: self.search_window(), bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.searchbutt.grid(row = 2 , column = 1, padx = 3, pady = 3, sticky = E)


        #COMPANY NAME INPUT -------------------------------------------------------------------------------------------------------------
        self.cname_lf = LabelFrame(self.parent, text = 'COMP NAME', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.cname_lf.grid(row = 1, column = 2, columnspan = 2,padx = 3, pady = 3, sticky = E+W)
        self.cname_ent = Entry(self.cname_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.cname_ent.grid(padx = 3, pady = 3, sticky = E+W)
        
        self.indust_lf = LabelFrame(self.parent, text = 'INDUSTRY', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.indust_lf.grid(row = 2, padx = 3, pady = 3, sticky = E+W)
        self.ind_sbox = Spinbox(self.indust_lf, values = ('INDUSTRIAL', 'COMMERCIAL' , 'FOOD_AND_BEVERAGE',
                                                          'PULP_AND_PAPER', 'MUNICIPAL',  'CHEMICAL', 'AGRICULTURE',
                                                          'ENGINEERING/CONSULTING','MINING', 'OTHER'),
                                                          bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.ind_sbox.grid(padx = 3, pady = 3, sticky = E+W)
        
        self.ofile_lf = LabelFrame(self.parent, text = 'COMPANY OVERVIEW', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.ofile_lf.grid(row = 3, padx = 3, pady = 3, sticky = E+W)
        self.ofile_ent = Entry(self.ofile_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.ofile_ent.grid(padx = 3, pady = 3, sticky = E+W)
        
        self.cfile_lf = LabelFrame(self.parent, text = 'COMPANY CONTACTS', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.cfile_lf.grid(row = 4, padx = 3, pady = 3, sticky = E+W)
        self.cfile_ent = Entry(self.cfile_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.cfile_ent.grid(padx = 3, pady = 3, sticky = E+W)
        
        self.note_lf = LabelFrame(self.parent, text = 'ACC. NOTES', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.note_lf.grid(row = 5, padx = 3, pady = 3, sticky = E+W)
        self.note_text = Text(self.note_lf, height = 5, bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.note_text.grid(padx = 3, pady = 3, sticky = E+W)

        self.submit_butt = Button(self.parent, text = 'submit', command = lambda: self.gather_vars(), bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.submit_butt.grid(row = 6, padx = 3, pady = 3, sticky = E+W)



    def search_window(self):
        '''
        Func - to be called after search button clicked. Will pull the entry widgets contents to use as search for DB.
                - Will probably need a "Category" spinbox to be set to correct DB column search (i.e. limit search to "INDUSTRY")
                - 
        '''
        searchterm = self.searchent.get()
        load_search = conn.execute('SELECT * FROM azaccounts WHERE industry = ?',(searchterm.upper(),))
        for row in load_search:
            print row
        return

    

    def gather_vars(self):
        '''
        Func - called by submit button. Will gather all of the entered information in the called from window.
                - along with gathering the inputted info, we need to format it for DB use before passing it on
                - passed to outside class function
                - then call to clear fields to delete all entry widgets in prep for next use
        '''
        
        loc_cname = self.cname_ent.get().upper()
        rev_cname = loc_cname.replace(' ', '_')
        
        other_columns = {'companyname': rev_cname,
                                   'industry': self.ind_sbox.get().upper(),
                                   'overviewfile': self.ofile_ent.get().upper(),
                                   'contactsfile': self.cfile_ent.get().upper(),
                                   'note': self.note_text.get(1.0, END)}
        try:
            accounts_commited(self.s_sbox.get(), **other_columns)
            
        except Error as e:         #Previously used ---> Exceptions as e:
            print 'Error occured:  {}'.format(e)
            
        self.clear_fields()
        


    def clear_fields(self):
        '''
        Func - called after data has been gathered, formatted, and passed on by previous function
                - Clears or deletes all entry fields -- "Refreshes" window widgets for next use
        '''
        self.cname_ent.delete(0, END)
        self.ofile_ent.delete(0, END)
        self.cfile_ent.delete(0, END)
        self.note_text.delete(1.0, END)

        self.display_db_entries()


    def display_db_entries(self):
        '''

        '''
        self.parent.iconify()
        self.displaywin = Toplevel()
        self.displaywin.title('Observe Window')
        self.displaywin.config(bg =  '#0C1021')
        
        self.disp_lf = LabelFrame(self.displaywin, bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.disp_lf.grid(row = 0, padx = 5, pady = 5)

        self.disp_text = Text(self.disp_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.disp_text.grid(row = 0, padx = 5, pady = 5)

        self.done_butt = Button(self.displaywin, text = 'Ok', bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                command = lambda: self.destroy_and_raise())
        self.done_butt.grid(row = 1, padx = 5, pady = 5)

        load_ents = conn.execute('SELECT * FROM azaccounts')
        
        for row in load_ents.fetchall():
            self.disp_text.insert(END, )
            
        self.displaywin.protocol("WM_DELETE_WINDOW", lambda: self.destroy_and_raise())
        self.displaywin.mainloop()



    def destroy_and_raise(self):
        '''

        '''
        self.parent.deiconify()
        self.displaywin.destroy()
        return
        




class MainView(object):
    #REF - C:\Anaconda2\Scripts\DXP_PumpCommand_db_contacts.py
    
    def __init__(self,parent):
        self.parent = parent

        #Functionality - single click on list entity brings up there contacts sheet in right window
        #Functionality - double click on list entity brings up there overview sheet info in pop-up window
        self.left_labelframe = LabelFrame(self.parent, text = 'Accounts View', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.left_labelframe.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.left_labelframe = LabelFrame(self.parent, text = 'Contacts View', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.left_labelframe.grid(row = 0, column = 1, padx = 5, pady = 5)



    def populate_accounts(self, state):
        '''
        Func -  to pull account names from DB depending on state provided
                - Need to clear list first upon each call as it may not be the first and already populated
        '''
        pass
    


    def pull_overview_info(self, event):
        '''
        Func -  to be BINDED to a "double Click" event on account list item
                - Need to accuretely select clicked item and pull OVERVIEW fileloc from DB
                - Make call to overview window creator for temperory pop up window display of given info
                - 
        '''
        pass


    def display_overview_info(self, floc):
        '''
        Func -  to inherit file loc of double clicked item in listbox
                - Need to read file and display contents in TEXT box in window
                - Ability to ADD, EDIT, DELETE as seen fit.
                - When updated or changed - call to file and write over existing info to fill with new

        Overview File: Will contain all the pertinent notes and info one would want to maintain on customer
                - TEXT widgets allow creation of hyperlinks (If bid solicit window doesnt pan out - allow user to simply visit webpage)
        '''
        pass
        
        
                                          
        
        





####################################
#Eventually needs to be moved to seperate File or simply
#Account info needs to be added 1 by 1

acclist  = ['AZ_Canning', 'Abrams_Airborne', 'Air_Liquide_Bagdad', 'Air_Products_and_Chemicals', 'Apache_Nitrogen', 'Arizona_Electric_Power', 'Arizona_LNG_Applied_LNG',
            'Arizona_Mining_Company', 'Arizona_Pacific_Wood', 'Asarco_Mission', 'Avondale', 'BE_Aerospace', 'Biosphere', 'Black_&_Veatch', 'Botanicare', 'Brown_and_Caldwell',
            'Bull_Moose', 'Bullhead_City', 'CCA', 'Camp_Dresser_McGhee', 'Carefree', 'Casa_Grande', 'Casa_Grande_Area', 'Cave_Creek', 'Chandler', 'Chino_Valley_',
            'City_of_Casa_Grande_WWTP', 'City_of_Henderson', 'City_of_Las_Vegas', 'Clark_County_Water_Reclamation_District', 'Clarkdale_Metals', 'Coolidge_Land_Acquition_Wes_Emulsions',
            'Cottonwood', 'Daisy_Sour_Cream', 'Davis_Monthan_AFB', 'Drake_Materials_Paulden', 'Ehrmanns_Dairy', 'Envirogen', 'Environmental_Biomass', 'Epcor_Bullhead_City',
            'Euclid_Chemical', 'FMI_Ajo', 'FMI_Bagdad', 'FMI_Bisbee', 'FMI_Sieritta', 'Fann_Environmental', 'Florence', 'Fluid_Solutions', 'Fountain_Hills', 'Franklin_Foods_Cream_Cheese',
            'Frito_Lay', 'Ft_Huachuca', 'Ft_Mohave', 'GCW', 'Glendale', 'Goodyear', 'Greeley_and_Hansen', 'Green_Valley_Pecans', 'Griffith_Energy_New_Star_Energy', 'Henderson_Electric',
            'Hexcel', 'Honeywell', 'Hydro_Geo_Chem', 'IBM', 'IDG', 'JDS_Engineering', 'Jones_Lang_LaSalle', 'Kinder_Morgan', 'Kingman', 'Kingman_all_Accounts', 'LPC_Contstruction',
            'Las_Vegas_Valley_Water_District', 'Laughlin', 'Lhoist_North_America', 'MGC', 'Mesa_NOT_Riverview', 'Mingus_Associates_Construction', 'Mohave_Valley', 'Morrison_Maierle',
            'Needles', 'Neltec', 'Nexus_Energy_calpine', 'Nord_Copper', 'Nucor', 'Oceanspray', 'Olin_Chlor', 'Paragon', 'Peoria', 'Phoenix_', 'Pima_County_WW', 'Poggemeyer_Engineers',
            'Praxair_Electronics', 'Prescott', 'Pro_Petroleum', 'Queen_Creek', 'Rain_Bird', 'Raytheon_Hagemeyer', 'Renewable_Algal_Energy', 'Sasol_Inc', 'Scottsdale', 'Severn_Trent_Environmental_Services',
            'Sierra_Vista_Regional_Health_Center', 'Slater_Hannifan_Group', 'Sletten', 'Southern_Nevada_Water_Authority', 'Sun_Mechanical', 'Sundt_', 'Surprise', 'Swissport_Fueling_',
            'TEP_Irvington', 'Timet_HOLD_OFF', 'Tolin_Mechanical', 'Tolleson', 'Topock', 'Trans_Canada_Power_Plant_Coolidge', 'United_Metals', 'Wilson_Engineers']


industries = ['INDUSTRIAL', 'COMMERCIAL' , 'FOOD_AND_BEVERAGE', 'PULP_AND_PAPER', 'MUNICIPAL',  'CHEMICAL', 'AGRICULTURE',
                   'ENGINEERING/CONSULTING','MINING', 'OTHER']


firstnames = ['Tony', 'John', 'Jim', 'Ken', 'Mary', 'Ashley', 'Gavin', 'Rich', 'Wesley', 'Sean', 'Shelly', 'Candi']
lastnames = ['smith', 'rogers', 'kinsey', 'jones', 'focker', 'white', 'johnson', 'harris', 'burnes', 'harrington', 'li', 'wang']
pos = ['Manager', 'Supervisor', 'Plant Mng', 'Buyer', 'Purchaser', 'Tech', 'Mechanic', 'Engineer', 'Lead']



####################################
#MAIN CALL
####################################            
if __name__ == '__main__':
    create_table_accounts()
    print 'succesful  table creations in memory'

    for acc in acclist:
        acc_columns = {'companyname': acc.upper(),
                                   'industry': random.choice(industries),
                                   'overviewfile': 'NONE',
                                   'contactsfile': 'NONE',
                                   'note': 'NONE'}

        statechoice = random.choice(['ARIZONA','NEVADA','NEW MEXICO'])
        accounts_commited(statechoice, **acc_columns)

        #companyname, contactfirst, contactlast, position, phonenumb,  numbalt,  email, note, datelast
        for i in range(3):
            fn = random.choice(firstnames)
            ln = random.choice(lastnames)
            con_columns =   {'companyname': acc.upper(),
                                       'contactfirst': fn,
                                       'contactlast': ln,
                                       'position': random.choice(pos),
                                       'phonenumb': '{}-{}-{}'.format(random.randint(200,880),random.randint(200,880),random.randint(200,880)),
                                       'numbalt': '{}-{}-{}'.format(random.randint(200,880),random.randint(200,880),random.randint(200,880)),
                                       'email': '{}.{}@{}.com'.format(fn,ln,acc),
                                       'note': 'NONE',
                                       'datelast': 'NONE'}

            #state, cname, cfile, **kwargs
            contacts_commited(statechoice, acc.upper(), 'None', **con_columns)

        
    print 'Completed!\n\n'
    print 'Start of Database retrieval......'
    return_db()
    
    root = Tk()
    App(root)
    root.mainloop()
    
    conn.close()
    

    
