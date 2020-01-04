from Tkinter import *
import ttk
import sqlite3 as sq3
import datetime, time, random
import tkFileDialog
import tkcalendar
import collections as clc
import tkMessageBox
import textwrap
import calendar
import os



"""
ACCOUNTS AND CONTACTS DIRECTORY - MODELED AFTER  PROJECTS FILE.
LIKE THE PROJECTS FILE:

        - LEFT WINDOW - Will have list of all the accounts
        - RIGHT WINDOW - Will display all asociated contacts when assoc.
                                    account is clicked.
                                    
        - Since there is not a conclusive list // EITHER
                    - Create a formatted list
                    - Just utilize one at a time entry

- NEED TO ADD:

        - Edit ability
        - Delete ability
        - search function
        -
        
- ADD:
All projects written to file function

- ADD:
an image viewer for any images that have been put in project folder.

"""




###########################################
class AccountsContacts(object):

    currentaccount = None               #Holder variable to maintain what current account company name is loaded

    #------------------------------------------------------------------------
    def __init__(self, master):
        
        self.master = master

        #CONTACTS MENU CREATION -----------------------------------------------------------------------------------------------------------------
        self.menubar = Menu(self.master,
                            background = '#0C1021', foreground='white',
                            activebackground='dark goldenrod', activeforeground='white')

        self.filemenu = Menu(self.menubar, tearoff=0,
                             background='#0C1021', foreground='white',
                             activebackground='dark goldenrod', activeforeground='white')
        
        self.filemenu.add_command(label="Add Account",
                            command = lambda: self.add_account())
        
        self.filemenu.add_command(label="Add Contact",
                            command = lambda: self.check_current_account())
        
        self.filemenu.add_command(label="Write Contacts Report",
                            command = lambda: None)
    
        self.menubar.add_cascade(label="Accounts/Contacts",
                            menu = self.filemenu)

        #FILTER MENU CREATION -----------------------------------------------------------------------------------------------------------------
        self.filter_menu = Menu(self.menubar, tearoff=0,
                            background='#0C1021', foreground='white',
                            activebackground='dark goldenrod', activeforeground='white')
        
        self.filter_menu.add_command(label="Filter Accounts",
                            command = lambda: None)
        
        self.filter_menu.add_command(label="Filter Contacts",
                            command = lambda: None)

        self.menubar.add_cascade(label="Filter",
                            menu = self.filter_menu)
        
        self.master.config(bg='#0C1021',
                            menu = self.menubar)

        #WIDGETS ----------------------------------------------------------------------------------------------------------------------------------
        #ACCOUNTS LIST TEXTBOX----------------------------------------
        self.accounts_labelframe = LabelFrame(self.master,
                                              text = 'ACCOUNTS',
                                              bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'),
                                              labelanchor = N)        
        self.accounts_labelframe.grid(row = 0, column = 0, columnspan = 2,
                                      padx = 5, pady = 5,
                                      sticky = NSEW)

        self.acctext = Text(self.accounts_labelframe,
                            bg =  '#0C1021', fg = 'white', font = ('Verdana',7),
                            width = 80, highlightthickness = 2,
                            cursor = 'xterm',
                            selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')        
        self.acctext.grid(row = 0, columnspan = 2,
                          padx = 5, pady = 5)
        
        self.newdb_butt = Button(self.accounts_labelframe,
                                 bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                 cursor = 'hand2',
                                 text = 'OK',
                                 command = lambda: None)        
        self.newdb_butt.grid(row = 1, column = 0,
                             padx = 3, pady = 5,
                             sticky = E+W)
        
        self.deldb_butt = Button(self.accounts_labelframe,
                                 bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                 cursor = 'hand2',
                                 text = 'Delete',
                                 command = lambda: self.del_secondchance())
        self.deldb_butt.grid(row = 1, column = 1,
                             padx = 3, pady = 5,
                             sticky = E+W)

        #SEARCH INPUT--------------------------------------------------------------------------------------------------------------
        self.searchacc = Label(self.accounts_labelframe,
                               text = 'Search Accounts',
                               bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.searchacc.grid(row = 2, column = 0,
                            padx = 3, pady = 3)
        
        self.saccent = Entry(self.accounts_labelframe,
                             bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                             cursor = 'xterm',
                             insertbackground = 'white')
        self.saccent.grid(row = 2, column = 1,
                          padx = 3, pady = 3,
                          sticky = E+W)
        
        self.saccbutt = Button(self.accounts_labelframe,
                               text = 'Search',
                               command = lambda: None,
                               bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                               cursor = 'hand2')
        self.saccbutt.grid(row = 3 , column = 0, columnspan = 2,
                           padx = 3, pady = 3,
                           sticky = E+W)


        #CONTACTS OVERVIEW (DETAILED) ------------------------------------------------------------------------------------
        self.notes_labelframe = LabelFrame(self.master,
                                           text = 'CONTACTS',
                                           bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'),
                                           labelanchor = N)        
        self.notes_labelframe.grid(row = 0, column = 2, columnspan = 2,
                                   padx = 5, pady = 5,
                                   sticky = NSEW)

        self.constext = Text(self.notes_labelframe,
                             bg =  '#0C1021', fg = 'white', font = ('Verdana',7),
                             width = 50,
                             highlightthickness = 2,
                             cursor = 'xterm',
                             selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')        
        self.constext.grid(row = 0 , column = 2, columnspan = 2,
                           padx = 5, pady = 5)


        #------------------------------------------------------------------------------------------------------------------------------
        self.constext.insert(END, '\n     ----------------------------------------------------')        
        self.constext.insert(END, '\n      INSTRUCTIONS:\n\n      - must click on account companyname in textbox\n      to the left in order to spawn contacts -')
        self.constext.insert(END, '\n     ----------------------------------------------------')      
        #------------------------------------------------------------------------------------------------------------------------------
        
        self.notes_butt = Button(self.notes_labelframe,
                                 bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                 cursor = 'hand2',
                                 text = 'OK',
                                 command = lambda: None)        
        self.notes_butt.grid(row = 1, column = 2,
                             padx = 3, pady = 5,
                             sticky = E+W)

        self.editnotes_butt = Button(self.notes_labelframe,
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     cursor = 'hand2',
                                     text = 'Edit',
                                     command = lambda: self.edit_notes_projfile())        
        self.editnotes_butt.grid(row = 1, column = 3,
                                 padx = 3, pady = 5,
                                 sticky = E+W)

        #SEARCH INPUT--------------------------------------------------------------------------------------------------------------
        self.searchcon = Label(self.notes_labelframe,
                               text = 'Search Contacts',
                               bg =  '#0C1021', fg = 'white', font = ('Verdana',8))        
        self.searchcon.grid(row = 2, column = 2,
                             padx = 3, pady = 3)
        
        self.sconent = Entry(self.notes_labelframe,
                             bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                             cursor = 'xterm', insertbackground = 'white')        
        self.sconent.grid(row = 2, column = 3,
                          padx = 3, pady = 3,
                          sticky = E+W)
        
        self.sconbutt = Button(self.notes_labelframe,
                               text = 'Search',
                               command = lambda: None,
                               bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                               cursor = 'hand2')        
        self.sconbutt.grid(row = 3, column = 2, columnspan = 2,
                           padx = 3, pady = 3,
                           sticky = E+W)

        #LOAD ACCOUNTS
        self.load_accounts()
        #self.Treeview_widge()

        #BINDINGS and EVENTS
        self.master.protocol("WM_DELETE_WINDOW", lambda: self.master.destroy())
        self.acctext.bind("<Double-Button-1>", self.pull_text_event)




    ##########################################################
    #------------------------------------------------------
    def load_accounts(self):
        '''
         Func - to be called and load all the accounts that are in the database at time
         of calling.

         - Clear the textbox and re-insert the newly called up inquiry data
        '''

        self.acctext.delete(1.0,END)
        
        accounts_dbfile = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\accounts\accountsdb.db"
        acon = sq3.connect(accounts_dbfile)
        alog = acon.cursor()

        #Display the total count ----- Update the labelframe to include qty
        numbents = alog.execute('''SELECT COUNT(*) FROM accounts''')
        ents = numbents.fetchall()[0]
        self.accounts_labelframe.config(text = 'ACCOUNTS: Total Entries {}'.format(ents[0]))

        #Pull all the accounts and format print them to text widget
        results = alog.execute("""SELECT * FROM accounts""")

        #Writing instructions to the textbox
        self.acctext.insert(END, '''\n''')
        self.acctext.insert(END, '''            -----------------------------------------------------------------------\n''')
        self.acctext.insert(END, '''            INSTRUCTIONS: To view contacts, left-mouse\n            click the company name....\n''')
        self.acctext.insert(END, '''            -----------------------------------------------------------------------\n\n''')


        treehold = clc.OrderedDict()
        #Pull column data
        for cnt,row in enumerate(results.fetchall()):

            treehold[str(cnt)] = clc.OrderedDict()
            id_row = row[0]
            treehold[str(cnt)]['ID'] = row[0]
            cname_row = row[1]
            treehold[str(cnt)]['CNAME'] = row[1]
            state_row = row[2]
            treehold[str(cnt)]['STATE'] = row[2]
            indust_row = row[3]
            treehold[str(cnt)]['IND'] = row[3]
            ofile_row = row[4]
            treehold[str(cnt)]['OFILE'] = row[4]
            note_row = row[5]
            treehold[str(cnt)]['NOTE'] = row[5]

            forminsert = """

---------------------------------------------------------------
---------------------------------------------------------------

'COMPNAME':              {}

---------------------------------------------------------------
---------------------------------------------------------------

'STATE':                        {}
'INDUSTRY':                 {}
'OVERVIEW FILE':       {}

'NOTES':                     {}
'ENTRY ID':                {}

- - - - - - - - - - -


    """.format(cname_row.upper(),
               state_row,
               indust_row,
               ofile_row.upper(),
               note_row.upper(),
               id_row)

            self.acctext.insert(END, forminsert)
        self.Treeview_widge(treehold)
        return
                                           


    ############################################
    def pull_text_event(self, event):
        '''Func will be called upon Button (mouse) click on textbox. This will
        pull the string contents of that line.
        '''
        
        index = event.widget.index("@%d,%d" % (event.x, event.y))   #Get the index in Textbox of the selected line
        line_index = index.split('.')

        line_content =  self.acctext.get(float(line_index[0]),
                                         END)

        column_title = str(line_content).split()
        if "'COMPNAME':" not in column_title[0]:
            
            self.constext.delete(1.0, END)            
            self.constext.insert(END, 'RESULT:  ---- DIDNT WORK!\n\n'.format(line_index))

        else:
            
            self.constext.delete(1.0, END)
            self.constext.insert(END, 'RESULT:  ---- DB Call Succesful!\n\n'.format(line_index))
            AccountsContacts.currentaccount = column_title[1]
   
            self.pull_contacts_click(AccountsContacts.currentaccount)

        return


    ############################################
    def pull_contacts_click(self, index_str):
        '''
  
        '''

        #DATABASE -------------------------------------------------
        contacts_dbfile = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\contacts\contactsdb.db"
        ccon = sq3.connect(contacts_dbfile)
        clog = ccon.cursor()

        results = clog.execute("""SELECT * FROM contacts WHERE companyname = ? COLLATE NOCASE""", (index_str,))
        
        for row in results.fetchall():
            r2 = row[2]
            r3 = row[3]
            r9 = row[9]
            r1 = row[1]
            r4 = row[4]
            r5 = row[5]
            r6 = row[6]
            r7 = row[7]
            r8 = row[8]
            r9 = row[9]
            r0 = row[0]
            rvar = (r2,r3,r9,r1,r4,r5,r6,r7,r8,r9,r0)
            self.format_pulled_data(rvar)

        return



    ###########################################
    def pull_contacts(self, comp):
        '''
  
        '''

        #DATABASE ----------------------------------------------------------------------
        contacts_dbfile = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\contacts\contactsdb.db"
        ccon = sq3.connect(contacts_dbfile)
        clog = ccon.cursor()

        results = clog.execute("""SELECT * FROM contacts WHERE companyname = ? COLLATE NOCASE""", (comp,))
        
        for row in results.fetchall():
            
            r2 = row[2]
            r3 = row[3]
            r9 = row[9]
            r1 = row[1]
            r4 = row[4]
            r5 = row[5]
            r6 = row[6]
            r7 = row[7]
            r8 = row[8]
            r9 = row[9]
            r0 = row[0]
            
            rvar = (r2,r3,r9,r1,r4,r5,r6,r7,r8,r9,r0)
            self.format_pulled_data(rvar)

        return


    ################################################################3
    def format_pulled_data(self, rvar):
        '''

        '''

        date_format = str(rvar[2]).split(',')
        print date_format
        y,m,d = date_format[0], date_format[1], date_format[2]
        duedate = datetime.date(int(y), int(m), int(d))
        delta = (datetime.date.today() - duedate).days

        if delta >= 14:
            delta = str(delta) + ' days ***F/U*** '

        else:
            delta = str(delta) + ' days'

        
        forminsert = """

###########################################

FIRST NAME:     {}
LASTNAME:        {}

DATE OF LAST CONTACT:     {}
DAYS SINCE:     {}
---------------------------------------------------------------
'COMPNAME':              {}
'POSITION':                {}
'PHONE #':                 {}
'ALT #':                      {}
'EMAIL':                      {}
'NOTES':                     {}
'ENTRY ID':                {}

###########################################
""".format(rvar[0],
           rvar[1],
           rvar[2],
           delta,
           rvar[3],
           rvar[4],
           rvar[5],
           rvar[6],
           rvar[7],
           rvar[8],
           rvar[9])           

        self.constext.insert(END, forminsert)
        return



    #ADD CONTACT
    ##############################################################################
    #------------------------------------------------------------------------------------------------------------------------------------------
    def check_current_account(self):
        ''' '''
        
        if AccountsContacts.currentaccount == None:
            self.constext.delete(1.0, END)
            self.constext.insert(END, '\n     ACCOUNT HAS NOT BEEN SELECTED!')
            return
        
        else:
            self.add_contact(AccountsContacts.currentaccount)


    #############################################################3
    def add_contact(self, comp):
        """
        Create window with widgets to input for db and notesfile creation
        comp - Company Name inherited when clicked
        """
        
        self.master.iconify()   #Minimize inherited parent window

        #NEW TOPLEVEL-----------------------------------------
        self.addcontact_win = Toplevel()
        self.addcontact_win.title('New Contact Setup -- Company: {}'.format(comp))
        self.addcontact_win.config(bg =  '#0C1021')


        #LABELFRAME WIDGET--------------------------------------------------------------------------------------
        self.new_con_name_lf = LabelFrame(self.addcontact_win,
                                          text = 'Enter Details for -- {} contact:'.format(comp),
                                          bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        
        self.new_con_name_lf.grid(row = 0, column = 0, columnspan = 2,
                                  padx = 5, pady = 5,
                                  sticky = NSEW)

        #ENTRY AND LABEL WIDGETS -----------------------------------------------------------------------------
        
        #--------------------------------FIRSTNAME        
        self.fnamelab = Label(self.new_con_name_lf,
                                    text = 'FIRST NAME :',
                                    bg =  '#0C1021', fg = 'white', font = ('Verdana',8))        
        self.fnamelab.grid(row = 0, column = 0,
                                    padx = 5, pady = 5)
        
        self.firstname_acc = Entry(self.new_con_name_lf,
                                bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                width = 50,cursor = 'xterm', insertbackground = 'white')
        self.firstname_acc.grid(row = 0, column = 1,
                                padx = 5, pady = 5,
                                sticky = E+W)

        #-------------------------------LASTNAME
        self.lnamelab = Label(self.new_con_name_lf,
                                    text = 'LAST NAME :',
                                    bg =  '#0C1021', fg = 'white', font = ('Verdana',8))        
        self.lnamelab.grid(row = 1, column = 0,
                                    padx = 5, pady = 5)
        
        self.lastname_acc = Entry(self.new_con_name_lf,
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     width = 50, cursor = 'xterm', insertbackground = 'white')
        self.lastname_acc.grid(row = 1, column = 1,
                               padx = 5, pady = 5,
                               sticky = E+W)

        #-------------------------------POSITION
        self.poslab = Label(self.new_con_name_lf,
                                    text = 'POSITION :',
                                    bg =  '#0C1021', fg = 'white', font = ('Verdana',8))        
        self.poslab.grid(row = 2, column = 0,
                                    padx = 5, pady = 5)
        
        self.position_acc = Entry(self.new_con_name_lf,
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     width = 50, cursor = 'xterm', insertbackground = 'white')
        self.position_acc.grid(row = 2, column = 1,
                               padx = 5, pady = 5,
                               sticky = E+W)

        #-------------------------------PHONE NUMB
        self.pnumblab = Label(self.new_con_name_lf,
                                    text = 'PHONE # :',
                                    bg =  '#0C1021', fg = 'white', font = ('Verdana',8))        
        self.pnumblab.grid(row = 3, column = 0,
                                    padx = 5, pady = 5)
        
        self.phonenumb_acc = Entry(self.new_con_name_lf,
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     width = 50, cursor = 'xterm', insertbackground = 'white')
        self.phonenumb_acc.grid(row = 3, column = 1,
                                padx = 5, pady = 5,
                                sticky = E+W)

        #-------------------------------ALT PHONE
        self.anumblab = Label(self.new_con_name_lf,
                                    text = 'ALT PHONE # :',
                                    bg =  '#0C1021', fg = 'white', font = ('Verdana',8))        
        self.anumblab.grid(row = 4, column = 0,
                                    padx = 5, pady = 5)

        self.altnumb_acc = Entry(self.new_con_name_lf,
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     width = 50, cursor = 'xterm', insertbackground = 'white')        
        self.altnumb_acc.grid(row = 4, column = 1,
                              padx = 5, pady = 5,
                              sticky = E+W)

        #-------------------------------EMAIL
        self.emaillab = Label(self.new_con_name_lf,
                                    text = 'EMAIL :',
                                    bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        self.emaillab.grid(row = 5, column = 0,
                                    padx = 5, pady = 5)

        self.email_acc = Entry(self.new_con_name_lf,
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     width = 50, cursor = 'xterm', insertbackground = 'white')
        self.email_acc.grid(row = 5, column = 1,
                           padx = 5, pady = 5,
                           sticky = E+W)

        #-------------------------------NOTE
        self.notelab = Label(self.new_con_name_lf,
                                    text = 'NOTE :',
                                    bg =  '#0C1021', fg = 'white', font = ('Verdana',8))        
        self.notelab.grid(row = 6, column = 0,
                                    padx = 5, pady = 5)

        self.note_acc = Entry(self.new_con_name_lf,
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     width = 50, cursor = 'xterm', insertbackground = 'white')
        self.note_acc.grid(row = 6, column = 1,
                          padx = 5, pady = 5,
                          sticky = E+W)

        #-------------------------------DATE LAST CALL
        self.datelab = Label(self.new_con_name_lf,
                                    text = 'DATE\n(yyyy,mm,dd) :',
                                    bg =  '#0C1021', fg = 'white', font = ('Verdana',8))        
        self.datelab.grid(row = 7, column = 0,
                                    padx = 5, pady = 5)

        self.date_acc = Entry(self.new_con_name_lf,
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     width = 50, cursor = 'xterm', insertbackground = 'white')
        self.date_acc.grid(row = 7, column = 1,
                          padx = 5, pady = 5,
                          sticky = E+W)


        #SUBMIT BUTTON -------------------------------------------------------------------------------------------
        self.con_add_butt = Button(self.new_con_name_lf,
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     cursor = 'hand2',
                                     text = '- ADD CONTACT -',
                                     command = lambda: self.add_contact_compile(comp))

        self.con_add_butt.grid(row = 8, column = 0, columnspan = 2,
                                 padx = 5, pady = 5,
                                 sticky = E+W)


        #BINDINGS AND PROTOCOLS------------------------------------------------
        self.addcontact_win.protocol("WM_DELETE_WINDOW",  lambda: self.addcon_oncancel())        
        self.addcontact_win.mainloop()



    ################################################
    def addcon_oncancel(self):
        ''' '''
        self.addcontact_win.destroy()
        self.master.deiconify()
        
        return


    ################################################
    def add_contact_compile(self,comp):
        '''
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         companyname  TEXT NOT NULL,
         contactfirst     TEXT,
         contactlast     TEXT,         
         position          TEXT,
         phonenumb    TEXT,
         numbalt         TEXT,
         email             TEXT,
         note              TEXT,
         datelast         TEXT);
        '''
        vals = (comp, self.firstname_acc.get(), self.lastname_acc.get(),
                self.position_acc.get(), self.phonenumb_acc.get(),
                self.altnumb_acc.get(), self.email_acc.get(),
                self.note_acc.get(), self.date_acc.get())
        
        #DATABASE -----------------------------------------------------------------------------
        contacts_db = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\contacts\contactsdb.db"
        ccon = sq3.connect(contacts_db)
        ccur = ccon.cursor()
        ccur.execute('''INSERT INTO contacts (companyname, contactfirst, contactlast, position, phonenumb, numbalt, email, note, datelast) VALUES (?,?,?,?,?,?,?,?,?)''', (vals))
        ccon.commit()

        #GUI WINDOW LEVELS -----------------------------------------------------
        self.addcontact_win.destroy()
        self.master.deiconify()

        self.pull_contacts(str(comp))     


   

    #ADD ACOUNT
    ##############################################################################
    #------------------------------------------------------------------------------------------------------------------------------------------
    def add_account(self):
        """
        Create window with widgets to input for db and notesfile creation
        """
        
        self.master.iconify()   #Minimize inherited parent window

        #NEW TOPLEVEL-----------------------------------------
        self.addcon_win = Toplevel()
        self.addcon_win.title('New Account Setup')
        self.addcon_win.config(bg =  '#0C1021')

        #COMPANY NAME (Labelframe and Entry Widget)----------------------------------------------------------
        self.new_acc_name_lf = LabelFrame(self.addcon_win,
                                          text = 'Company Name',
                                          bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))        
        self.new_acc_name_lf.grid(row = 0, column = 0, columnspan = 2,
                                  padx = 5, pady = 5,
                                  sticky = NSEW)
        
        self.accname_ent = Entry(self.new_acc_name_lf,
                                 bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                 width = 50)        
        self.accname_ent.grid(columnspan = 2,
                              padx = 5, pady = 5,
                              sticky = E+W)

        #SUBMIT BUTTON -------------------------------------------------------------------------------------------
        self.acc_add_butt_1 = Button(self.addcon_win,
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                     cursor = 'hand2',
                                     text = 'Next',
                                     command = lambda: self.add_account_next())        
        self.acc_add_butt_1.grid(row = 1, column = 0, columnspan = 2,
                                 padx = 5, pady = 5,
                                 sticky = E+W)

        #PROTOCOLS AND BINDINGS --------------------------------------
        self.addcon_win.protocol("WM_DELETE_WINDOW",
                                 lambda: self.addwin_oncancel())
        
        self.addcon_win.mainloop()


    ###########################################
    def addwin_oncancel(self):
        ''' '''
        self.addcon_win.destroy()
        self.master.deiconify()
        return


    ###########################################
    def add_account_next(self):
        """
        Create window with widgets to input for db and notesfile creation

        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         companyname   TEXT NOT NULL,
         state                 TEXT,
         industry            TEXT,
         overviewfile       TEXT,
         note                  TEXT) 
        """

        #SPINBOX VALUES ---------------------------------------------------
        statechoice = ('ARIZONA','NEVADA','NEWMEXICO')
        
        industrychoice = ('INDUSTRIAL', 'COMMERCIAL' , 'FOOD_AND_BEVERAGE',
                                  'PULP_AND_PAPER', 'MUNICIPAL',  'CHEMICAL', 'AGRICULTURE',
                                  'ENGINEERING/CONSULTING','MINING', 'POWER/ENERGY', 'OTHER')

       #DATABASE-----------------------------------------------------------------
        cname = self.accname_ent .get()
        cname_formatted = cname.replace(' ', '_')
        fileloc =  "C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Accounts\Overview_Files\{}.txt".format(cname_formatted)

        self.acc_add_butt_1.destroy()
        self.addcon_win.update()

        
        #STATE---------------------------------------------------------------------------------------------------------------------
        self.con_state_lf = LabelFrame(self.addcon_win,
                                       text = 'State',
                                       bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.con_state_lf.grid(row = 1, column = 0, columnspan = 2,
                               padx = 5, pady = 5,
                               sticky = NSEW)
        
        self.con_state_sbox = Spinbox(self.con_state_lf,
                                      values = statechoice,
                                      bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                      width =50, justify = CENTER)
        self.con_state_sbox.grid(columnspan = 2,
                                 padx = 5, pady = 5,
                                 sticky = E+W)

        #INDUSTRY----------------------------------------------------------------------------------------------------------------------
        self.con_ind_lf = LabelFrame(self.addcon_win,
                                     text = 'Industry',
                                     bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.con_ind_lf.grid(row = 2, column = 0, columnspan = 2,
                             padx = 5, pady = 5,
                             sticky = NSEW)

        self.con_indust_sbox = Spinbox(self.con_ind_lf,
                                       values = industrychoice,
                                       bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                       width =50, justify = CENTER)
        self.con_indust_sbox.grid(columnspan = 2,
                                  padx = 5, pady = 5,
                                  sticky = E+W)

        #OVERVIEW FILE ----------------------------------------------------------------------------------------
        self.over_file_lf  = LabelFrame(self.addcon_win,
                                        text = 'Directory File Location:',
                                        bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.over_file_lf.grid(row = 3, column = 0, columnspan = 2,
                               padx = 5, pady = 5,
                               sticky = NSEW)

        self.overfile_lab  = Label(self.over_file_lf,
                                   text = fileloc,
                                   bg =  '#0C1021', fg = 'white', font = ('Verdana',7))
        self.overfile_lab.grid(columnspan = 2,
                               padx = 5, pady = 5,
                               sticky = E+W)

        #BRIEF NOTE---------------------------------------------------------------------------------------------
        self.bnote_lf  = LabelFrame(self.addcon_win,
                                    text = 'Add Brief Description',
                                    bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.bnote_lf.grid(row = 4, column = 0, columnspan = 2,
                           padx = 5, pady = 5, sticky = NSEW)
        
        self.bnote_ent = Entry(self.bnote_lf,
                               bg = '#0C1021', fg = 'white', font = ('Verdana',8),
                               width = 55)
        self.bnote_ent.grid(columnspan = 2,
                            padx = 5, pady = 5,
                            sticky = E+W)

        #SUBMIT BUTTON -------------------------------------------------------------------------------------------
        self.proj_add_butt_2 = Button(self.addcon_win,
                                      bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                      cursor = 'hand2',
                                      text = 'Submit Rest',
                                      command = lambda: self.compile_and_enter(fileloc)) 
        self.proj_add_butt_2.grid(row = 5, column = 0, columnspan = 2,
                                  padx = 5, pady = 5,
                                  sticky = E+W)

        self.addcon_win.update()


    ###########################################
    def compile_and_enter(self, fileloc):
        ''' '''
        vals = (self.accname_ent.get(), self.con_state_sbox.get(), self.con_indust_sbox.get(), fileloc, self.bnote_ent.get())
        
        accounts_db = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\accounts\accountsdb.db"
        alog = sq3.connect(accounts_db)
        acon = alog.cursor()
        
        acon.execute('''INSERT INTO accounts (companyname, state, industry, overviewfile, note) VALUES (?,?,?,?,?)''', (vals))
        alog.commit()
        
        self.print_accounts()


    ###########################################
    def print_accounts(self):
        ''' '''
        self.addwin_oncancel()
        accounts_db = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\accounts\accountsdb.db"
        alog = sq3.connect(accounts_db)
        acon = alog.cursor()
        
        results = acon.execute('''SELECT * FROM accounts''')
        
        for row in results.fetchall():
            print row

        self.load_accounts()
        return



    def Treeview_widge(self, dicts):
        '''id INTEGER PRIMARY KEY AUTOINCREMENT,
         companyname   TEXT NOT NULL,
         state                 TEXT,
         industry            TEXT,
         overviewfile       TEXT,
         note                  TEXT '''
        #self.master.iconify()   #Minimize inherited parent window

        #NEW TOPLEVEL-----------------------------------------
        self.tree_win = Toplevel()
        self.tree_win.title('Treeview')

        self.tree = ttk.Treeview(self.tree_win)
        self.tree["columns"]=("P1","P2","P3", "P4", "P5", "P6")
##        self.tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
##        self.tree.column("one", width=150, minwidth=150, stretch=tk.NO)
##        self.tree.column("two", width=400, minwidth=200)
##        self.tree.column("three", width=80, minwidth=50, stretch=tk.NO)

        self.tree.heading("P1",text="ID",anchor=W)
        self.tree.heading("P2", text="COMP NAME",anchor=W)
        self.tree.heading("P3", text="STATE",anchor=W)
        self.tree.heading("P4", text="INDUSTRY",anchor=W)
        self.tree.heading("P5", text="OVERFILE",anchor=W)
        self.tree.heading("P6", text="NOTE",anchor=W)

        itr = 0
        for k,v in dicts.items():
            self.tree.insert("", 'end', '{}'.format(dicts[str(itr)]['CNAME']), values = (v.values()))
            itr += 1
            #self.tree_cont(dicts[str(itr)]['CNAME'])

        
        self.tree.grid(row = 0, column = 0, sticky = NSEW)
        self.tree_win.mainloop()

##    def tree_cont(self,cname):
##        contacts_dbfile = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\contacts\contactsdb.db"
##        ccon = sq3.connect(contacts_dbfile)
##        clog = ccon.cursor()
##
##        results = clog.execute("""SELECT * FROM contacts WHERE companyname = ? COLLATE NOCASE""", (cname,))
##        
##        for row in results.fetchall():
##            
##            r2 = row[2]
##            r3 = row[3]
##            r9 = row[9]
##            r1 = row[1]
##            r4 = row[4]
##            r5 = row[5]
##            r6 = row[6]
##            r7 = row[7]
##            r8 = row[8]
##            r9 = row[9]
##            r0 = row[0]
##            
##            rvar = (r2,r3,r9,r1,r4,r5,r6,r7,r8,r9,r0)
##            self.tree.insert('','end','{}'.format(cname),values = (rvar))



###########################################
#DATABASE INIITIAL ---------------------------------------------------------------------------------------------
def connect_contacts_accounts_db():
    '''
    
    '''
    accounts_db = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\accounts\accountsdb.db"
    contacts_db = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\contacts\contactsdb.db"

    alog = sq3.connect(accounts_db)
    clog = sq3.connect(contacts_db)

    alog.row_factory = sq3.Row
    clog.row_factory = sq3.Row

    create_table_accounts_contacts(alog, clog)

    alog.close()
    clog.close()



###########################################
#THIS IS FIRST RUN ONLY --------- AFTER IT HAS BEEN CREATED WILL RAISE ERROR
def create_table_accounts_contacts(alog, clog):
    '''
    Func to initiate a table within the given database specified.
    Each company will fall under one of these filters. Each contact will have the following characteristics:
    '''
    
    #CREATE - ACCOUNTS TABLE------------------------------------------------------------------
    alog.execute('''CREATE TABLE IF NOT EXISTS accounts
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         companyname   TEXT NOT NULL,
         state                 TEXT,
         industry            TEXT,
         overviewfile       TEXT,
         note                  TEXT);''')
    alog.commit()


    #CREATE - CONTACTS for ACCOUNTS--------------------------------------------------------
    clog.execute('''CREATE TABLE IF NOT EXISTS contacts
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
         companyname  TEXT NOT NULL,
         contactfirst     TEXT,
         contactlast     TEXT,         
         position          TEXT,
         phonenumb    TEXT,
         numbalt         TEXT,
         email             TEXT,
         note              TEXT,
         datelast         TEXT);''')
    clog.commit()

    return



##########################################################
#START of the ACCOUNTS AND CONTACTS WINDOW
def start():
    connect_contacts_accounts_db()
    root = Tk()
    root.title('Accounts and Contacts')
    AccountsContacts(root)
    root.mainloop()


##################################
#--------------------------------------
if __name__ == '__main__':
    start()
