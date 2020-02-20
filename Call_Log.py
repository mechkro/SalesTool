import tkinter as tk
from tkinter import filedialog as fd
import os



#class CallLog(tk.Tk):
    #'''
    #- Need to be able to add entries to call log and be able to click and update them instead  of having to add a new line
    #- Have a submit button -
            #- Compile and format the file for presentation
            #- Ask to save the database file to a directory
            #- New DB creation required
    #'''
    
    #def __init__(self, parent):
        #'''
        #Init Func to build out the root master iwndow
        #'''
        
        #self.parent = parent
        #self.parent.iconify()
        ##self.Database()

        #self.clog_level = Toplevel()
        #self.clog_level.title('CALL-LOG - TODAYS DATE: {}'.format(datetime.date.today()))
        #self.set_clog_level_size()


        ##MENUBAR CREATION--------------------------------------------------------------------------------------------------
        #self.clogmenu = Menu(self.clog_level, background = '#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')

        #self.writemenu = Menu(self.clogmenu, tearoff=0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        #self.writemenu.add_command(label="Write Log to File", command = lambda: self.name_text_file())

        #self.clogmenu.add_cascade(label="Write Log", menu = self.writemenu)

        
        ##STATE CHOICE --------------------------------------------------------------------------------------------------------
        #self.resetmenu = Menu(self.clogmenu, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        #self.resetmenu.add_command(label = "Reset Call File", command = lambda: self.reset_log_protocol())

        #self.clogmenu.add_cascade(label = "Reset", menu = self.resetmenu)


        ##LOAD DATABASE ------------------------------------------------------------------------------------------------------
        #self.loadmenu = Menu(self.clogmenu, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        #self.loadmenu.add_command(label = "New DB", command = lambda:  self.ask_db_filename())      #self.new_database())
        #self.loadmenu.add_command(label = "Load Database", command = lambda: self.open_db_file())           #self.Database('START'))
        #self.loadmenu.add_command(label = "Add Note", command = lambda: self.check_if_db_open())       #add_note_to_db())

        #self.clogmenu.add_cascade(label = "Load", menu = self.loadmenu)


        ##LOAD TO WINDOW
        #self.clog_level.config(bg='#0C1021', menu = self.clogmenu)


        ##TEXT WIDGET CREATION-----------------------------------------------------------------------------
        #self.clog_frame = Frame(self.clog_level, bg =  '#0C1021')
        #self.clog_frame.grid(row = 0, column = 0)

        #self.mon_labelframe = LabelFrame(self.clog_frame, text = 'MONDAY', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        #self.mon_labelframe.grid(row = 0, padx = 3, pady = 3, sticky = N+E+W)
        #self.tue_labelframe = LabelFrame(self.clog_frame, text = 'TUESDAY', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        #self.tue_labelframe.grid(row = 1, padx = 3, pady = 3, sticky = N+E+W)
        #self.wed_labelframe = LabelFrame(self.clog_frame, text = 'WED', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        #self.wed_labelframe.grid(row = 2, padx = 3, pady = 3, sticky = N+E+W)
        #self.thur_labelframe = LabelFrame(self.clog_frame, text = 'THURSDAY', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        #self.thur_labelframe.grid(row = 3, padx = 3, pady = 3, sticky = N+E+W)
        #self.fri_labelframe = LabelFrame(self.clog_frame, text = 'FRIDAY', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        #self.fri_labelframe.grid(row = 4, padx = 3, pady = 3, sticky = N+E+W)

        
        ##TEXT BOX CREATION----------------------------------------------------------------------------------
        #self.mon_text = Text(self.mon_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            #cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', height = 5)
        #self.mon_text.grid(padx = 3, pady = 3, sticky = NSEW)
        #self.tue_text = Text(self.tue_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            #cursor = 'xterm', selectbackground = 'dark goldenrod' ,selectforeground = 'black', height = 5)
        #self.tue_text.grid(padx = 3, pady = 3, sticky = NSEW)
        #self.wed_text = Text(self.wed_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            #cursor = 'xterm', selectbackground = 'dark goldenrod',selectforeground = 'black', height = 5)
        #self.wed_text.grid(padx = 3, pady = 3, sticky = NSEW)
        #self.thur_text = Text(self.thur_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            #cursor = 'xterm', selectbackground = 'dark goldenrod' ,selectforeground = 'black', height = 5)
        #self.thur_text.grid(padx = 3, pady = 3, sticky = NSEW)
        #self.fri_text = Text(self.fri_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            #cursor = 'xterm', selectbackground = 'dark goldenrod' ,selectforeground = 'black', height = 5)
        #self.fri_text.grid(padx = 3, pady = 3, sticky = NSEW)

        ##Initial instructions -------------------------------------------------------------------
        #self.mon_text.insert(END, "\n--- MUST LOAD  '*.db' FILE ---")
        #self.tue_text.insert(END, "\n--- MUST LOAD  '*.db' FILE ---")
        #self.wed_text.insert(END, "\n--- MUST LOAD  '*.db' FILE ---")
        #self.thur_text.insert(END, "\n--- MUST LOAD  '*.db' FILE ---")
        #self.fri_text.insert(END, "\n--- MUST LOAD  '*.db' FILE ---")

        ##LOAD WHAT DATA IS THERE-------------------------------------------------------
        ##self.PreloadData('MONDAY', 'TUESDAY', 'WED', 'THURSDAY', 'FRIDAY')
        

        ##BOTTOM----------------------------------------------------------------------------------------
        #self.widge_labelframe = LabelFrame(self.clog_frame, text = 'CALL LOG - OPS',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        #self.widge_labelframe.grid(row = 5, padx = 5, pady = 5, sticky = E+W)

        #self.spinlab = Label(self.widge_labelframe, text = 'CHOOSE WHICH DAY\nTO "SUBMIT" ENTRY', bg =  '#0C1021', fg = 'white', font = ('Verdana', 7))
        #self.spinlab.grid(row = 0 , column = 0, padx = 5, pady = 3, sticky = NSEW)


        ##SPINBOX TO SELECT DAY OF WEEK TO LOAD--------------------------------------------
        ########################################################################################
        #"""THINK ABOUT CHANGING TO A POP UP WINDOW TO CHOOSE DAY ---- I HAVE FORGOTTEN MULTIPLE TIMES NOW TO CORRECT IT"""
        ########################################################################################
        
        #self.choices = ('MONDAY', 'TUESDAY', 'WED', 'THURSDAY', 'FRIDAY')
        #self.spinbox = Spinbox(self.widge_labelframe, values = self.choices, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2')
        #self.spinbox.grid(row = 2, column = 0, padx = 3, pady = 3, sticky = S)


        ##LABELS FOR THE ENTRIES-------------------------------------------------------------------------------------------------------------
        #self.complab = Label(self.widge_labelframe, text = 'Company Name', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))         #some type of auto populate
        #self.complab.grid(row = 0 , column = 1, padx = 3, pady = 3, sticky = W)
        
        #self.contlab = Label(self.widge_labelframe, text = 'Contact Name', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        #self.contlab.grid(row = 1 , column = 1, padx = 3, pady = 3, sticky = W)
        
        #self.medlab = Label(self.widge_labelframe, text = 'Medium Used', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))           #Think about using a spinbox
        #self.medlab.grid(row = 2 , column = 1, padx = 3, pady = 3, sticky = W)
        
        #self.desclab = Label(self.widge_labelframe, text = 'Description', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        #self.desclab.grid(row = 3 , column = 1, padx = 3, pady = 3, sticky = W)
        
        #self.fwdlab = Label(self.widge_labelframe, text = 'Forward', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        #self.fwdlab.grid(row = 4, column = 1, padx = 3, pady = 3, sticky = W)


        ###### !!!! Think about adding colorcode maping to the text
        

        ##ENTRY WIDGETS---------------------------------------------------------------------------------------------------------------
        #self.comp_ent =  Entry(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                               #cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white')
        #self.comp_ent.grid(row = 0 , column = 2, padx = 3, pady = 3, sticky = E)
        
        #self.cont_ent =  Entry(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                               #cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white' )
        #self.cont_ent.grid(row = 1 , column = 2, padx = 3, pady = 3, sticky = E)
        
        #self.med_ent =  Entry(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                              #cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white' )
        #self.med_ent.grid(row = 2 , column = 2, padx = 3, pady = 3, sticky = E)
        
        #self.desc_ent =  Entry(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                               #cursor = 'xterm', selectbackground = 'dark goldenrod' , insertbackground = 'white')
        #self.desc_ent.grid(row = 3 , column = 2, padx = 3, pady = 3, sticky = E)
        
        #self.fwd_ent =  Entry(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                              #cursor = 'xterm', selectbackground = 'dark goldenrod' , insertbackground = 'white')
        #self.fwd_ent.grid(row = 4 , column = 2, columnspan = 2, padx = 3, pady = 3, sticky = E)
        

        ##BUTTON WIDGET -----------------------------------------------------------------------------------------------------
        #self.submitbutton = Button(self.widge_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                   #text = 'SUBMIT', command = lambda: self.enter_new_entry())     
        #self.submitbutton.grid(row = 5, columnspan = 4, padx = 3, pady = 3, sticky = E+W)
    
        ##LOOP --------------------------------
        #self.clog_level.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())
        #self.clog_level.mainloop()


    #def set_clog_level_size(self):
        #'''
        #CLASS FUNC #1-------------------------------------------------
        #Func to set the min and max adjustable size of the window.
        #Will maintain its size to minimize adjustments required.
        #'''
        
        #self.clog_level.minsize(575,800)
        #self.clog_level.maxsize(580,900)
        
        #print 'Succesful Pass of set call log window size parameters'
        #return


    #def open_db_file(self):
        #floc = tkFileDialog.askopenfilename(title = 'Chose database directory',
                                              #initialdir= r"C:\Anaconda2\Scripts\databases",
                                              #filetypes = (("database file", "*.db"),))
        #self.database_load(floc)


    #def ask_db_filename(self):
        #'''

        #'''
        #fname = tkFileDialog.asksaveasfilename(title = 'Chose database directory',
                                              #initialdir= r"C:\Anaconda2\Scripts\databases",
                                              #filetypes = (("database file", "*.db"),))
        #self.database_load(fname)

        

    #def database_load(self, dbfile):
        #'''

        #'''
        #self.db_loc = dbfile

        #if self.db_loc != None:
            #self.currlog = sq3.connect(self.db_loc)
            #self.currlog.row_factory = sq3.Row
            #self.cur = self.currlog.cursor()

        #self.create_table()
        #self.reset_ent_widgets()
        
        #days = {'MONDAY': self.mon_text,
                    #'TUESDAY': self.tue_text,
                    #'WED': self.wed_text,
                    #'THURSDAY': self.thur_text,
                    #'FRIDAY': self.fri_text}
        
        #for k,v in days.items():
            #self.cur.execute('''SELECT COUNT(*) FROM call_log WHERE day = ?''', (k,))
            #days_ents = self.cur.fetchone()

            #v.delete(1.0, END)
            #itr = 1
            #v.insert(END, '--Entry 1 of {}--------------------------\n'.format(days_ents[0]+1))


            #self.cur.execute('''SELECT * FROM call_log WHERE day = ?''', (k,))            #OUTPUT - ['datestamp', 'compname', 'contact', 'medium', 'desc', 'forward', 'day']
            #for row in self.cur.fetchall():

                #insrt = '''\nCompany Name: {}
    #Contact: {}
    #Medium: {}
    #Description: {}
    #Forward: {}
    #Day of Week: {}
    #Timestamp: {}\n\n'''.format(row['compname'].encode('utf-8'), row['contact'].encode('utf-8'), row['medium'].encode('utf-8'),
                                #row['desc'].encode('utf-8'), row['forward'].encode('utf-8'), row['day'].encode('utf-8'), row['datestamp'].encode('utf-8')) 

                #v.insert(END, insrt)
                #itr+=1
                #v.insert(END, '--Entry {} of {}--------------------------\n'.format(itr,days_ents[0]+1))
                
        #self.reset_ent_widgets()


    #def check_if_db_open(self):
        #'''
        #Func to check if NOTE can and should be added. If no DB active then watrning is provided.
        #Else - func will move forward with request
        #'''

        #try:
            #if self.currlog:
                #self.add_note_to_db()
        #except AttributeError:
            #tkMessageBox.showerror(title = 'ERROR', message = 'No DB has been connected!\nPlease, try again')



    #def add_note_to_db(self):

        #self.notewin = Toplevel()
        #self.notelf = LabelFrame(self.notewin, text = 'ADD note then press SUBMIT', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        #self.notelf.grid(padx = 5, pady = 5, sticky = NSEW)

        #self.notetext = Text(self.notelf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), insertbackground = 'white',
                            #cursor = 'xterm', selectbackground = 'dark goldenrod' ,selectforeground = 'black')
        #self.notetext.grid(row = 0, padx = 5, pady = 5, sticky = NSEW)

        #self.notebutt = Button(self.notelf, text = 'SUBMIT', command = lambda: self.enter_note(),
                               #bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2')
        #self.notebutt.grid(row = 1, padx = 5, pady = 5, sticky = E+W)

        #self.notewin.protocol("WM_DELETE_WINDOW", lambda: self.note_close())
        #self.notewin.mainloop()


    #def note_close(self):
        #'''
        #Func - user clicking 'X' will close window
        #'''
        #self.notewin.destroy()
        #return
    

    #def enter_note(self):

        #self.unix = time.time()
        #self.notedate = str(datetime.datetime.fromtimestamp(self.unix).strftime('%Y-%m-%d  %H: %M: %S'))
        #n = self.notetext.get(1.0, END)
        #self.cur.execute("""INSERT INTO log_notes (datestamp, note) VALUES (?, ?)""", (self.notedate,n))
        #self.currlog.commit()

        #selects = self.cur.execute('''SELECT * FROM log_notes''')
        #for row in selects.fetchall():
            #print 'Timestamp: {}'.format(row[0])
            #print 'NOTE:  {}'.format(row[1])

        #self.notewin.destroy()
        #return
    

    #def reset_ent_widgets(self):

        #'''
        #CLASS FUNC #7-------------------------------------------
        #Func - Reset the entriy widgets to blank for next entry
        #'''
        
        #self.comp_ent.delete(0,END)   #Company name
        #self.cont_ent.delete(0,END)    #Contact Name
        #self.med_ent.delete(0,END)    #Medium 
        #self.desc_ent.delete(0,END)    #Description
        #self.fwd_ent.delete(0,END)    #Forward

        #return


    ##THIS IS FIRST RUN ONLY --------- AFTER IT HAS BEEN CREATED WILL RAISE ERROR
    #def create_table(self):
        #'''
        #CLASS FUNC #4----------------------
        #Func to create table in the database
        #'''
        
        #self.currlog.execute('CREATE TABLE IF NOT EXISTS call_log (datestamp TEXT, compname TEXT, contact TEXT, medium TEXT,  desc TEXT, forward TEXT, day TEXT)')
        #self.currlog.commit()

        #self.currlog.execute('CREATE TABLE IF NOT EXISTS log_notes (datestamp TEXT, note TEXT)')
        #self.currlog.commit()
        
        #return

        ##This will be a database that contains and tracks all the notes needed to add for overall message of the call log for any particular week
        ##Each entry will be datestamped.
        ##self.cur.execute('CREATE TABLE IF NOT EXISTS call_log_notes (datestamp TEXT, note TEXT)')
        ##self.currlog.commit()
    

    #def enter_new_entry(self):      #Normally had d as argument
        #'''
        #CLASS FUNC #5------------------------------------------------------------------------------------------
        #Func that recieves the day of the week from inser of database and then refreshing the text box
       
        #CLASS FUNC #12 -------------------------------------------------

        #CALLED from submit button for  new entries
        #datestamp, compname, contact,  medium, desc, forward, day

        #*FUTURE - Think about swapping out spinbox with a popup toplevel window asking for the day to enter.
        #'''
        
        #self.unix = time.time()
        #self.date = str(datetime.datetime.fromtimestamp(self.unix).strftime('%Y-%m-%d  %H: %M: %S'))
        
        #e1 = self.comp_ent.get()    #Company name
        #e2 = self.cont_ent.get()      #Contact Name
        #e3 = self.med_ent.get()     #Medium 
        #e4 = self.desc_ent.get()     #Description
        #e5 = self.fwd_ent.get()      #Forward
        #s1 = self.spinbox.get()       #Day - M/T/W/TH/F

        #self.cur.execute('INSERT INTO call_log (datestamp, compname, contact,  medium, desc, forward, day) VALUES (?, ?, ?, ?, ?, ?, ?)', (self.date, e1, e2, e3, e4, e5, s1))
        #self.currlog.commit()
        
        #days = {'MONDAY': self.mon_text,
                    #'TUESDAY': self.tue_text,
                    #'WED': self.wed_text,
                    #'THURSDAY': self.thur_text,
                    #'FRIDAY': self.fri_text}
        
        #for k,v in days.items():
            #self.cur.execute('''SELECT COUNT(*) FROM call_log WHERE day = ?''', (k,))
            #days_ents = self.cur.fetchone()

            #v.delete(1.0, END)
            #itr = 1
            #v.insert(END, '--Entry 1 of {}--------------------------\n'.format(days_ents[0]+1))


            #self.cur.execute('''SELECT * FROM call_log WHERE day = ?''', (k,))            #OUTPUT - ['datestamp', 'compname', 'contact', 'medium', 'desc', 'forward', 'day']
            #for row in self.cur.fetchall():

                #insrt = '''\nCompany Name: {}
#Contact: {}
#Medium: {}
#Description: {}
#Forward: {}
#Day of Week: {}
#Timestamp: {}\n\n'''.format(row['compname'].encode('utf-8'), row['contact'].encode('utf-8'), row['medium'].encode('utf-8'),
                                #row['desc'].encode('utf-8'), row['forward'].encode('utf-8'), row['day'].encode('utf-8'), row['datestamp'].encode('utf-8')) 

                #v.insert(END, insrt)
                #itr+=1
                #v.insert(END, '--Entry {} of {}--------------------------\n'.format(itr,days_ents[0]+1))
                
        #self.reset_ent_widgets()



    #def new_database(self):
        #'''
        #CLASS FUNC #8 ------------------------------------------
        #Func called from Call log window menubar

        #Will allow users to enter new db name and start new file
        #'''

        #self.ResetEntries()     #CF#7
        #self.ask_new = Toplevel()
        #self.ask_new.title('New DB Creation')
        #self.ask_new.config(bg =  '#0C1021')

        #self.entnew_labelframe = LabelFrame(self.ask_new, text = 'Please enter a new DB file name', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        #self.entnew_labelframe.grid(padx = 5, pady = 5, sticky = NSEW)

        #self.newdb_ent = Entry(self.entnew_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 40,
                               #cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white')
        #self.newdb_ent.grid(row = 0 , padx = 3, pady = 3)

        #self.newdb_butt = Button(self.entnew_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                   #text = 'OK', command = lambda: self.ask_newdb_dir())     #CF#9
        #self.newdb_butt.grid(row = 1, padx = 3, pady = 3)

        #self.ask_new.protocol("WM_DELETE_WINDOW", lambda: self.ask_new.destroy())
        #self.ask_new.mainloop()
        

       

    #def on_closing(self):
        #'''
        #CLASS FUNC #10 -----------------------------------------------------------------
        
        #Func called from Call log window when the 'X' button is pressed to close win
        #Note: If this is called before connection to database is established, need
        #to catch attribute error and pass it
        #'''

        #try:
            #self.currlog.close()
            #print "Current connection to DB Succesfully closed"

        #except AttributeError as e:
            #print e
        
        #self.parent.deiconify()
        #self.clog_level.destroy()
        #return




    ###########################################################################################
    ##CREATION OF TEXT FILE -----------------------------------------------------------------------------------------------------------------------------------
    #def name_text_file(self):
        #'''
        #A Toplevel window that allows users to enter all the info required to properly compile and file all
        #of the entries for the call log.

        #Makes call to compiler func that writes to file row for row in the database
        #'''
        
        #calen = self.pull_month_calendar()          #Call to return current calendar month in str format to display

        #self.name_text = Toplevel()
        #self.name_text.title('Choose File Dir')
        #self.name_text.minsize(565,545)
        #self.name_text.maxsize(580,550)
                             
        #self.name_frame = Frame(self.name_text, bg =  '#0C1021')
        #self.name_frame.grid()

        ##WIDGET CREATION
        #self.name_lab = Label(self.name_frame, text = 'Please Enter a File name and\nchoose a directory!',
                               #bg =  '#0C1021', fg = 'white', font = ('Verdana',12,'bold'))
        #self.name_lab.grid(row = 0, columnspan = 2, padx = 5, pady = 5)

        #self.ent_lab = Label(self.name_frame, text = 'Enter File name:',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        #self.ent_lab.grid(row = 1,columnspan = 2,  padx = 5, pady = 5)

        #self.lab_ent = Entry(self.name_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 25,
                               #cursor = 'xterm', selectbackground = 'dark goldenrod',insertbackground = 'white' )
        #self.lab_ent.grid(row = 2,columnspan = 2,  padx = 15, pady = 5, sticky = E+W)

        #self.cal_display = Label(self.name_frame, text = calen, bg =  '#0C1021', fg = 'white', font = ('Verdana',13), cursor = 'plus')
        #self.cal_display.grid(row = 3, columnspan = 2, padx = 5, pady = 5, sticky = NSEW)

        #self.week_lab = Label(self.name_frame, text = 'Enter what week this is for:',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        #self.week_lab.grid(row = 4, columnspan = 2, padx = 5, pady = 5)

        #self.week_ent = Entry(self.name_frame, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 25,
                               #cursor = 'xterm', selectbackground = 'dark goldenrod' ,insertbackground = 'white')
        #self.week_ent.grid(row = 5, columnspan = 2, padx = 15,  pady = 5, sticky = E+W)

        #self.log_notes = Label(self.name_frame, text = 'Do you have any comments to\nadd to the call log?',  bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        #self.log_notes.grid(row = 6, columnspan = 2, padx = 5, pady = 5)

        #self.dir_textframe = LabelFrame(self.name_frame, text = 'Add Note to Call Log:', bg =  '#0C1021', fg = 'white', font = ('Verdana',8))
        #self.dir_textframe.grid(row = 7, columnspan = 2,  padx = 5, pady = 5)
                                                
        #self.notes_txt = Text(self.dir_textframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), 
                            #cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white', height = 5)
        #self.notes_txt.grid(columnspan = 2, padx = 5, pady = 5, sticky = NSEW)

        #self.dir_button = Button(self.dir_textframe, text = 'Choose File Directory', bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                 #command = lambda: self.ask_dir(self.lab_ent.get(), self.notes_txt.get(1.0, END), self.week_ent.get()))
        #self.dir_button.grid(row = 1, columnspan = 2, padx = 5, pady = 5, sticky = E+W)

        ##self.name_text.protocol("WM_DELETE_WINDOW", lambda: self.on_closing())
        #self.name_text.mainloop()



    #def pull_month_calendar(self):
        #'''
        #Func - to pull current month calendar to display on call log to help aid define which week.
        
        #'''
        #today = datetime.date.today()
        #today_str = today.strftime("%d/%m/%Y").split('/')
        #mm = int(today_str[1])
        #yyyy = int(today_str[-1])
        #return calendar.month(yyyy,mm)


    #def ask_dir(self, fname, lognotes, wk):
        #'''
        
        #'''
        #fdir = tkFileDialog.askdirectory()
        #self.write_to_text_file(fdir, fname.replace(' ', '_'), lognotes, wk)
        #self.name_text.destroy()


    #def write_to_text_file(self, fdir, fname, lognotes, wk):
        #'''
        #- Ask where they want file saved to:
        #- need to add option for continually applying general comments
        #- Keep write to file and reset log seperate.... -or- until we know all the bugs have been removed
        #'''

        #wrapper = textwrap.TextWrapper(width = 100)
        ##EX: txtt = wrapper.wrap(text = txt)

        #fdir_alter = fdir.replace('/','\\')
        #fname_alter = fname + '.txt'
                                  
        #full_dir = r'{}\{}'.format(fdir_alter, fname_alter)

        ##This will be standard format for top of all Call Logs
        #Intro_L1 = 'CALL LOG:  DXP Enterprises, Phoenix AZ'
        #Intro_L2 = 'SALESMAN :  Tony Kinsey_Engineered Sales_#480-294-1294'
        #Intro_L3 = 'WEEK OF {}\n'.format(wk)
        #Intro_L4 = 'OVERVIEW NOTES:\n'
        

        #introlines = (Intro_L1, Intro_L2, Intro_L3)
        #breakline = '''\n------------------------------------------------------------------------------------------------------------------------\n'''
        #endline = '''\n\n---------------------------------------------END OF FILE----------------------------------------------------------------\n\n'''

        #try:
            #with open(full_dir, 'w')as F:
                
                #for line in introlines:
                    #F.write(line.center(100))
                    #F.write('\n')

                #F.write(Intro_L4)
                #selects = self.cur.execute('''SELECT * FROM log_notes''')
                #for row in selects.fetchall():
                    #F.write('Timestamp: {}'.format(row[0]))
                    #F.write('NOTE:  {}'.format(row[1]))
                    
                #F.write(breakline)

            #days = ('MONDAY', 'TUESDAY', 'WED', 'THURSDAY', 'FRIDAY')
            #for d in days:
                #self.cur.execute('SELECT COUNT(*) FROM call_log WHERE day = ?''', (d,))
                #cnt = int(self.cur.fetchone()[0])
                #itr = 1
                #with open(full_dir, 'a')as F:
                    #F.write('**************   {} Entries:  ***************\n'.format(d.center(5)))        #Added '*'s to the entry make it pop when
                    #F.write('''\n----Entry {} of {}---------------------------------------------------------------------------------------------------------\n\n'''.format(itr, cnt))

                    #self.cur.execute('''SELECT * FROM call_log WHERE day = ?''', (d,))
                    ##Wrap all of the rows ---- Dont want print out to have long uneven lines. (FOR Format purpous)
                    #for row in self.cur.fetchall():
                        #row0 =  textwrap.fill(row[0].encode('utf-8'), width = 100)             #wrapper.wrap(text = (row[0]).encode('utf-8'))
                        #row1 =  textwrap.fill(row[1].encode('utf-8'), width = 100)            #wrapper.wrap(text = (row[1]).encode('utf-8'))
                        #row2 =  textwrap.fill(row[2].encode('utf-8'), width = 100)            #wrapper.wrap(text = (row[2]).encode('utf-8'))
                        #row3 =  textwrap.fill(row[3].encode('utf-8'), width = 100)            #wrapper.wrap(text = (row[3]).encode('utf-8'))
                        #row4 =  textwrap.fill(row[4].encode('utf-8'), width = 100)            #wrapper.fill(text = (row[4]).encode('utf-8'))
                        #row5 =  textwrap.fill(row[5].encode('utf-8'), width = 100)            #wrapper.fill(text = (row[5]).encode('utf-8'))
                        #row6 =  textwrap.fill(row[6].encode('utf-8'), width = 100)            #wrapper.wrap(text = (row[6]).encode('utf-8'))

                        #rows = clc.OrderedDict()
                        #rows['Account Name'] = row1
                        #rows['Contact Name'] = row2
                        #rows['Contact Method'] = row3
                        #rows['Description'] = row4
                        #rows['Follow UP'] = row5
                        #rows['Timestamp'] = row0
                        #rows['Day of Entry'] = row6

                        #itr += 1
                        #for k,v in rows.items():
                            #F.write('{}:{}\n'.format(k,v))
                        #if itr <= cnt:
                            #F.write('''\n----Entry {} of {}---------------------------------------------------------------------------------------------------------\n\n'''.format(itr, cnt))
                        #else:
                            #pass
                    #F.write('''\n-----------------------------------------END OF {} ENTRIES-----------------------------------------------------------\n'''.format(d))

            #with open(full_dir, 'a')as F:
                #F.write(endline)

###            with open(r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\banner.txt", 'a')as A:
###                lines = A.readlines()
###                for line in lines:
###                    A.write(line)
                    
            #print 'Succesful Upload of Call Log to Designated Folder'
            #self.ask_if_reset()

        #except Exception as e:
            #print e
            #print '''An Error has occured, please check data has not been comprimised'''



    #def ask_if_reset(self):
        #'''

        #'''
        #tkMessageBox.askyesno("Success!","It appears your call log entries have\nbeen succesfully exported.\nWould you like to reset log now?")
        #if 'yes':
            #pass        
            ##self.reset_procedure()
        #else:
            #tkMessageBox.OK('Sys Response', 'Ok no problem')
            
        #return



    #def reset_log_protocol(self):
        #'''
        #Func to call and reset the call log. Will delete all entries and enter new database directory.
        #Saves it to the designated Database file
        #'''
        #pass
    


BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'
SFG = 'black'


class CallLogWindow:
    
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent 
        
        #Menu Creation 
        #----------------------------------------------------------------------------------------------------------
        self.calllog_menu = tk.Menu(self.parent, background = '#0C1021', foreground='white', activebackground= DGR, activeforeground='white')

        self.writemenu = tk.Menu(self.calllog_menu, tearoff=0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.writemenu.add_command(label="Write Log to File", command = lambda: self.write_to_file()) 

        self.calllog_menu.add_cascade(label="Write Log", menu = self.writemenu)

        
        #STATE CHOICE --------------------------------------------------------------------------------------------------------
        self.resetmenu = tk.Menu(self.calllog_menu, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.resetmenu.add_command(label = "Reset Call File", command = lambda: None) #self.reset_log_protocol())

        self.calllog_menu.add_cascade(label = "Reset", menu = self.resetmenu)


        #LOAD DATABASE ------------------------------------------------------------------------------------------------------
        self.loadmenu = tk.Menu(self.calllog_menu, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.loadmenu.add_command(label = "New DB", command = lambda:  None)  #self.ask_db_filename())      #self.new_database())
        self.loadmenu.add_command(label = "Load Database", command = lambda: None)  #self.open_db_file())           #self.Database('START'))
        self.loadmenu.add_command(label = "Add Note", command = lambda: None) #self.check_if_db_open())       #add_note_to_db())

        self.calllog_menu.add_cascade(label = "Load", menu = self.loadmenu)


        #LOAD TO WINDOW
        # ----------------------------------------------------------------------------------------------------------
        self.parent.config(bg='#0C1021', menu = self.calllog_menu)
        
       
       #Widget Frames
       # ----------------------------------------------------------------------------------------------------------
        self.display_frame = tk.Frame(self.parent,  bg = BG)
        self.display_frame.grid(row = 0, column = 0, sticky = tk.NS)
        
        self.selection_frame = tk.Frame(self.parent,  bg =  BG)
        self.selection_frame.grid(row = 0, column = 1, columnspan = 2,  sticky = tk.NS)        
                
        
       #Label Creation
       # ----------------------------------------------------------------------------------------------------------
        self.lab_accounts = tk.Label(self.display_frame, text = 'Accounts',  bg = BG, fg = FG, 
                              font = ('terminal', 20, 'bold'))
        self.lab_accounts.grid(row = 0, column = 0 , padx = 5, pady = 5, sticky = tk.EW)
        
        self.lab_selection= tk.Label(self.selection_frame, text = 'Selection',  bg = BG, fg = FG,
                               font = ('terminal', 20, 'bold'))        
        self.lab_selection.grid(row = 0, column = 0 , columnspan = 2,  padx = 5, pady = 5, sticky = tk.EW) 
        
        
        ### Automate labelframe creation w/ widget
        #-----------------------------------------------------------------------------------------------------------
        self.mon_labelframe = tk.LabelFrame(self.display_frame, text = 'MONDAY', 
                                            bg =  BG,  fg =  FG, font = ('Verdana',8,'bold'))
        self.mon_labelframe.grid(row = 1, padx = 3, pady = 3, sticky = tk.NS)
        self.mon_lbox = tk.Listbox(self.mon_labelframe, height = 4, bg = BG, fg = FG)
        self.mon_lbox.grid(padx = 5, pady = 5)
        
        self.tue_labelframe = tk.LabelFrame(self.display_frame, text = 'TUESDAY', 
                                            bg =  BG,  fg =  FG, font = ('Verdana',8,'bold'))
        self.tue_labelframe.grid(row = 2 ,padx = 3, pady = 3, sticky =  tk.NS)
        self.tue_lbox = tk.Listbox(self.tue_labelframe, height = 4, bg = BG, fg = FG)
        self.tue_lbox.grid(padx = 5, pady = 5)        
        
        self.wed_labelframe = tk.LabelFrame(self.display_frame, text = 'WED', 
                                            bg =  BG,  fg =  FG,  font = ('Verdana',8,'bold'))
        self.wed_labelframe.grid(row = 3, padx = 3, pady = 3, sticky =  tk.NS)
        self.wed_lbox = tk.Listbox(self.wed_labelframe, height = 4, bg = BG, fg = FG)
        self.wed_lbox.grid(padx = 5, pady = 5)        
        
        self.thur_labelframe = tk.LabelFrame(self.display_frame, text = 'THURSDAY', 
                                             bg =  BG,  fg =  FG,  font = ('Verdana',8,'bold'))
        self.thur_labelframe.grid(row = 4, padx = 3, pady = 3, sticky =  tk.NS)
        self.th_lbox = tk.Listbox(self.thur_labelframe, height = 4, bg = BG, fg = FG)
        self.th_lbox.grid(padx = 5, pady = 5)        
        
        self.fri_labelframe = tk.LabelFrame(self.display_frame, text = 'FRIDAY', 
                                            bg =  BG,  fg =  FG,  font = ('Verdana',8,'bold'))
        self.fri_labelframe.grid(row = 5, padx = 3, pady = 3, sticky =  tk.NS)        
        self.f_lbox = tk.Listbox(self.fri_labelframe, height = 4, bg = BG, fg = FG)
        self.f_lbox.grid(padx = 5, pady = 5) 
        
        self.unitholdr = [(self.mon_labelframe, 'a', self.mon_lbox),
                                   (self.tue_labelframe, 'a', self.tue_lbox),
                                   (self.wed_labelframe, 'a', self.wed_lbox),
                                   (self.thur_labelframe, 'a', self.th_lbox),
                                   (self.fri_labelframe, 'a', self.f_lbox),
                                   (self.selection_frame, 's', None)]
        
        for i in self.unitholdr:
            
            self.bind_enter_leave(i[1],i[0])
            if i[0] == self.selection_frame:
                pass
            
            else:
                    self.bind_clicking_widge(i[-1])
                    
                    
        #Selection Frame Side
        #------------------------------------------------------------------------------------------------------------------
        #Top Section------------------
        self.det_labelframe_1 = tk.LabelFrame(self.selection_frame, text = 'Enter Info', 
                                            bg =  BG,  fg =  FG,  font = ('Verdana',8,'bold'))
        self.det_labelframe_1.grid(row = 1, padx = 3, pady = 5, sticky =  tk.NS) 
        
        #Spinbox to assign and send data to correct field for viewing
        self.choices = ('MONDAY', 'TUESDAY', 'WED', 'THURSDAY', 'FRIDAY')
        self.spinbox = tk.Spinbox(self.det_labelframe_1, values = self.choices, bg =  '#0C1021', fg = DGR,  font = ('Verdana',8), cursor = 'hand2')
        self.spinbox.grid(row = 0, column =1, columnspan = 2, padx = 3, pady = 3, sticky = tk.EW)        
        
        #Company name
        self.complab = tk.Label(self.det_labelframe_1, text = 'Company Name', bg = BG, fg = FG, font = ('Verdana',8))         #some type of auto populate
        self.complab.grid(row = 1 , column = 1, padx = 3, pady = 3, sticky = tk.W)
        self.comp_ent =  tk.Entry(self.det_labelframe_1, bg = BG, fg = FG, font = ('Verdana',8), width = 40,
                               cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white')
        self.comp_ent.grid(row = 1 , column = 2, padx = 3, pady = 3, sticky = tk.E)        
        
        #Contact Info
        self.contlab = tk.Label(self.det_labelframe_1, text = 'Contact Name', bg = BG, fg = FG, font = ('Verdana',8))
        self.contlab.grid(row = 2 , column = 1, padx = 3, pady = 3, sticky = tk.W)
        self.cont_ent =  tk.Entry(self.det_labelframe_1, bg = BG, fg = FG,  font = ('Verdana',8), width = 40,
                               cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white' )
        self.cont_ent.grid(row = 2 , column = 2, padx = 3, pady = 3, sticky = tk.E) 
        
        #Medium used i.e. email, phone call, meeting , etc.
        self.medlab = tk.Label(self.det_labelframe_1, text = 'Medium Used', bg = BG, fg = FG, font = ('Verdana',8))           #Think about using a spinbox
        self.medlab.grid(row = 3 , column = 1, padx = 3, pady = 3, sticky = tk.W)
        self.med_ent =  tk.Entry(self.det_labelframe_1, bg = BG, fg = FG, font = ('Verdana',8), width = 40,
                              cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white' )
        self.med_ent.grid(row = 3 , column = 2, padx = 3, pady = 3, sticky = tk.E)        
        
        #Description of transaction
        self.desclab = tk.Label(self.det_labelframe_1, text = 'Description', bg = BG, fg = FG, font = ('Verdana',8))
        self.desclab.grid(row = 4 , column = 1, padx = 3, pady = 3, sticky = tk.W)
        self.desc_text = tk.Text(self.det_labelframe_1, bg = BG, fg = FG, font = ('Verdana',8), height = 5, width = 40,
                                 cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.desc_text.grid(row = 4, column = 2, padx = 3, pady = 3, sticky = tk.E)           

        #Going forward what to do
        self.fwdlab = tk.Label(self.det_labelframe_1, text = 'Forward', bg = BG, fg = FG, font = ('Verdana',8))
        self.fwdlab.grid(row = 5, column = 1, padx = 3, pady = 3, sticky = tk.W) 
        self.fwd_text = tk.Text(self.det_labelframe_1, bg = BG, fg = FG, font = ('Verdana',8), height = 5, width = 40,
                                cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.fwd_text.grid(row = 5, column = 2, padx = 3, pady = 3, sticky = tk.E)     
        
        #BUTTON WIDGET -----------------------------------------------------------------------------------------------------
        self.submitbutton = tk.Button(self.det_labelframe_1, bg = BG, fg = FG, font = ('Verdana',8), cursor = 'hand2',
                                   text = 'SUBMIT', command = lambda: self.pull_entry_data())   #self.enter_new_entry())     
        self.submitbutton.grid(row = 6, column = 1, columnspan = 2,  padx = 3, pady = 3, sticky = tk.EW)             
        
        
        #Bottom Section--------------
        self.det_labelframe_2 = tk.LabelFrame(self.selection_frame, text = 'Detail Window 2', 
                                            bg =  BG,  fg =  FG,  font = ('Verdana',8,'bold'))
        self.det_labelframe_2.grid(row = 2, padx = 3, pady = 5, sticky =  tk.NS) 
        
        self.det_text = tk.Text(self.det_labelframe_2, bg = BG, fg = FG, font = ('Verdana',8), height = 12, width = 55,
                                cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.det_text.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tk.NS)         
          

    
    
    #----------------------------------------------------------------------------------------------
    def create_labels(self, w):
        """

        """
        
        pass
    
    #----------------------------------------------------------------------------------------------
    def create_entries(self, w):
        """

        """
        
        pass
    
    #----------------------------------------------------------------------------------------------
    def create_labframe(self, w):
        """

        """
        
        pass


    #Functions for GUI Functionality --------------------------------------------------------------
    ##################################################################
    def pull_entry_data(self):
        """
        Func - called by submit button. Pull all the data from the widgets and send to perspective day of the week storage 
        and viewing  on left side of screen widgets
        """
        
        sbox = self.spinbox.get()
        comp_E = self.comp_ent.get()
        cont_E = self.cont_ent.get()
        med_E = self.med_ent.get()
        desc_T = self.desc_text.get(1.0, tk.END)
        fwd_T = self.fwd_text.get(1.0, tk.END)
        
        pulled_data_array = (sbox, comp_E, cont_E, med_E, desc_T, fwd_T)
        for i in pulled_data_array:
            print(i)

        self.add_entry_data_to_field(*pulled_data_array)
        self.clear_entry_widgets()


    #---------------------------------------------------------------------
    def add_entry_data_to_field(self, *args):
        """
        Func - to take pulled data from entry fields and input to appropriate
        """
        
        fields = {'MONDAY': self.mon_lbox,
                  'TUESDAY': self.tue_lbox,
                  'WED': self.wed_lbox,
                  'THURSDAY': self.th_lbox,
                  'FRIDAY':self.f_lbox}

        fields[args[0]].insert(tk.END, '{} Entry:'.format(args[0]))
        for i in args[1::]:
            j = str(i).strip('\n')
            fields[args[0]].insert(tk.END, j)

        return
        
        
    #------------------------------------------------------------------------------------------------    
    def clear_entry_widgets(self):
        """

        """
        
        self.comp_ent.delete(0, tk.END)
        self.cont_ent.delete(0, tk.END)
        self.med_ent.delete(0, tk.END)
        self.desc_text.delete(1.0, tk.END)
        self.fwd_text.delete(1.0, tk.END)
    
        return
      
    
    #----------------------------------------------------------------------------------------------
    def bind_enter_leave(self, c, widge):
        """
         c - catagory, either 'a' for account or 's' for selection_frames
         widge - widget being passed to get assigned a binding action
        """
        
        if c == 'a':
            widge.bind('<Enter>', self.change_acc_color)
            widge.bind('<Leave>', self.change_acc_def_color)
        if c == 's':
            widge.bind('<Enter>', self.change_select_color)
            widge.bind('<Leave>', self.change_select_def_color)
        
        return      
    
    #----------------------------------------------------------------------------------------------
    def bind_clicking_widge(self, widge):
        """ 
        widge is given bind method to call resizing function when it is clicked
        """
        
        widge.bind('<Button-1>', self.widge_enlarge_shrink)
        return
    
    
    
    #----------------------------------------------------------------------------------------------
    def widge_enlarge_shrink(self, event):
        """
        Func to resize the clicked listbox (enlarge) as well as the other 4 listboxes (shrink)
        """
        
        filtered = [self.mon_lbox,
                             self.tue_lbox,
                             self.wed_lbox,
                             self.th_lbox,
                             self.f_lbox]
        
        for i in filtered:
            if i == event.widget:
                event.widget.config(height = 8)
                event.widget.master.config(fg = DGR)        #Change FG color of labelframe so we know who has focus
            else:
                i.config(height = 3)
                i.master.config(fg = 'white')                           #All other labelframes changed back to white default
        return
    
    
    #----------------------------------------------------------------------------------------------
    def change_acc_color(self, event):
        """ 
        
        """
        
        self.lab_accounts.config(fg = DGR)
        self.lab_selection.config(fg = 'white')
        
        return
    
    
    #----------------------------------------------------------------------------------------------
    def change_select_color(self, event):
        """ 
        
        """
        
        self.lab_accounts.config(fg = 'white')
        self.lab_selection.config(fg = DGR)
        
        return  
    
    
    #----------------------------------------------------------------------------------------------
    def change_acc_def_color(self, event):
        """ 
        
        """
        
        self.lab_selection.config(fg = 'white')
        
        return
    
    
    #----------------------------------------------------------------------------------------------
    def change_select_def_color(self, event):
        """ """
        self.lab_selection.config(fg = 'white')
        
        return
    
    
    #----------------------------------------------------------------------------------------------
    def write_to_file(self):
        """ 
        Source: https://automatetheboringstuff.com/chapter8/
        """
        
        self.parent.iconify()
        
        self.writefile_window = tk.Toplevel()
        self.wfile = tk.Frame(self.writefile_window, bg = BG)
        self.wfile.grid()
        
        current_dir = os.getcwd()
        tstr = 'Testing.txt'
        self.wfile_lab = tk.Label(self.wfile,  bg = BG, fg = FG, font = ('Verdana', 14, 'bold'),
                                  text = 'Current Directory:\n{}'.format(os.path.join(current_dir, tstr)))
        self.wfile_lab.grid(padx = 5, pady = 5)
        
        self.writefile_window.protocol('WM_DELETE_WINDOW', self.wfile_win_destroy)
        self.writefile_window.mainloop()
    
    
    #----------------------------------------------------------------------------------------------
    def wfile_win_destroy(self):
        """ 
        Destroy the write file window and bring back to view the parent window so user 
        can continue with workflow
        """
        
        self.writefile_window.destroy()
        self.parent.deiconify()
        
        
        
#----------------------------------------------------------------------------------------------    
if __name__ == '__main__':
    
    root = tk.Tk()
    CallLogWindow(root)
    root.mainloop()
