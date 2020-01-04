from Tkinter import *
import sqlite3 as lite
import datetime, time
import tkMessageBox



#Datetime manipulation
'''
day_uni = u'11/24/2015'
delta_t = datetime.datetime.strptime('string', '%m/%d/%Y')
delta_time = (datetime.datetime.today() - inputdate*).days

'''


class ToDo(object):
    
    def __init__(self, master):
        '''
        To Add: 
            - REV - Formatting of the window widgets
            - REV - Finalize the database columns
            - ADD - Follow up box --------
            - ADD Feature - Click listbox item and pop-up with text box appears giving full view for hard to read notes
            - SEARCH function on main screen
                - auto scroll to loc of highlights


            - SEE TEXT widget docs for search feature!

        Troubleshoot:
            - EDIT - not showing up
        '''

        #DEFINE COLORS AND FONT ------------------------------------------------------
        self.bG =  '#0C1021'
        self.fG = 'white'
        self.Font = ('Verdana',8)


        #CONFIGURE ROOTS BG COLOR ---------------------------------------------------------- 
        self.master = master
        self.master.config(bg = self.bG)


        #LOAD DB-------------------------------------------------------------
        self.menubar = Menu(self.master, background = '#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white', cursor = 'hand2')
        self.filemenu = Menu(self.menubar, tearoff=0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white', cursor = 'hand2')
        self.filemenu.add_command(label="ToDo", command = lambda: self.load_todo_db())
        #self.filemenu.add_command(label="Tools", command = lambda: None)
        #self.filemenu.add_command(label="Call Log", command = lambda: CallLog(master))
        self.menubar.add_cascade(label="File", menu = self.filemenu)
        

        #####################
        #ADD UNDO BUTTON or MENU OPTION----------------------------
        #####################

        #####################
        #SWITCH OUT TO DO CODE -----------------
        #####################

        self.master.config(bg='#0C1021', menu = self.menubar)


        #DEFINE TWO FRAMES - Top and Bottom Widgets -----------------------------------------
        self.frame = Frame(self.master, bg = self.bG)
        self.frame.grid(row = 0, rowspan = 2, column = 0)

        self.framebot = Frame(self.master, bg = self.bG)
        self.framebot.grid(row = 2, column = 0)

       
        #TOPLEVEL LABELFRAME------------------------------------------------------------------------------------------------------------------------------
        self.lf_todo = LabelFrame(self.frame, text = "TO DO's", bg = self.bG, font = self.Font, fg = self.fG)
        self.lf_todo.grid(columnspan = 2, padx = 3, pady = 3, sticky = NSEW)


        #################################################################################################
        #LABELS and COORESPONDING ENTRY WIDGETS --------------------------------------------------------------------------
        self.ddlab = Label(self.lf_todo, text = 'DATE DUE\n(mm/dd/yyyy)', bg = self.bG, fg = self.fG, font = self.Font)
        self.ddlab.grid(row = 0, column = 0,  padx = 8, pady = 3, sticky = W+E)

        self.desclab = Label(self.lf_todo, text = 'DESCRIPTION', bg = self.bG, fg = self.fG, font = self.Font)
        self.desclab.grid(row = 1, column = 0, padx = 8, pady = 3, sticky = W+E)

        self.conlab = Label(self.lf_todo,  text = 'WHO/WHAT?', bg = self.bG, fg = self.fG, font = self.Font)
        self.conlab.grid(row = 2, column = 0, padx = 8, pady = 3, sticky = W+E)

        self.statelab = Label(self.lf_todo,  text = 'STATE', bg = self.bG, fg = self.fG, font = self.Font)
        self.statelab.grid(row = 3, column = 0, padx = 8, pady = 3, sticky = W+E)


        #Due date       
        self.dd_ent = Entry(self.lf_todo, width = 65, bg = self.bG, fg = self.fG, font = self.Font, 
                             insertbackground = 'white', cursor = 'xterm')
        self.dd_ent.grid(row = 0, column = 1,  columnspan = 2,  padx = 8, pady = 3, sticky = W+E)

        #Description of the entry
        self.desc_ent = Text(self.lf_todo, width = 65, height = 3, bg = self.bG, fg = self.fG, font = self.Font,
                             insertbackground = 'white', cursor = 'xterm', wrap = WORD)
        self.desc_ent.grid(row = 1, column = 1, padx = 8, pady = 3, sticky = W+E)

        #Contact or whom we have been dealing with
        self.con_ent = Entry(self.lf_todo, width = 65, bg = self.bG, fg = self.fG, font = self.Font,
                             insertbackground = 'white', cursor = 'xterm')
        self.con_ent.grid(row = 2, column = 1, padx = 8, pady = 3, sticky = W+E)

        #State of the to do
        self.sta_ent = Entry(self.lf_todo, width = 65, bg = self.bG, fg = self.fG, font = self.Font,
                             insertbackground = 'white', cursor = 'xterm')
        self.sta_ent.grid(row = 3, column = 1, padx = 8, pady = 3, sticky = W+E)


        ####################################################################################################
        #BUTTON WIDGET ----------------------------------------------------------------------------------------------------
        self.close_button = Button(self.lf_todo, text = 'EXIT TO-DO', bg = self.bG, fg = self.fG, font = self.Font,
                                   cursor ='hand2', command = lambda: self.master.destroy())
        self.close_button.grid(row = 4, column = 0, padx = 5, pady = 3)
        
        self.submitbutton = Button(self.lf_todo, width = 20, bg = self.bG, fg = self.fG, font = self.Font,
                                   text = 'SUBMIT', cursor = 'hand2', command = self.db_entry)
        self.submitbutton.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = E+W)


        #BOTLEVEL LABELFRAME------------------------------------------------------------------------------------------------------------------------------
        self.ents_todo = LabelFrame(self.framebot, text = "ENTRY DETAILS", bg = self.bG, fg = self.fG, font = self.Font)
        self.ents_todo.grid(padx = 5, pady = 20, sticky = NSEW)
        

        #SCROLLBAR and LISTBOX ----------------------------------------------------------------------------------
        self.lb1_horiz_scroll = Scrollbar(self.ents_todo, orient = HORIZONTAL, bg = self.bG, cursor = 'hand2')
        self.lb1_vert_scroll = Scrollbar(self.ents_todo, orient = VERTICAL, bg = self.bG, cursor = 'hand2')
        
        self.lbox = Listbox(self.ents_todo, width = 80, height = 15, bg = self.bG, fg = self.fG, font = self.Font,
                            xscrollcommand = self.lb1_horiz_scroll, yscrollcommand =self.lb1_vert_scroll.set,
                            cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black')
        self.lbox.grid(row = 0, columnspan = 2, padx = 5, pady = 5, sticky = NSEW)
        
        self.lb1_horiz_scroll.config(command = self.lbox.xview)
        self.lb1_horiz_scroll.grid(row = 1, columnspan = 2, padx = 5, pady = 3, sticky = E+W)
        self.lb1_vert_scroll.config(command = self.lbox.yview)
        self.lb1_vert_scroll.grid(row = 0, column = 2, padx = 5, pady= 3, sticky = N+S)


        #Functionality widgets
        self.idlab = Label(self.ents_todo, text = 'ID TO DELETE\n(Manual Insertion)', bg = self.bG, fg = self.fG, font = self.Font)
        self.idlab.grid(row = 2, column = 0,  padx = 5, pady = 20)

        self.id_ent = Entry(self.ents_todo, width = 40, bg = self.bG, fg = self.fG, font = self.Font,
                            insertbackground = 'white', cursor = 'xterm')
        self.id_ent.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 20, sticky = W+E)
        
        self.delbutton = Button(self.ents_todo, bg = self.bG, fg = self.fG, font = self.Font,
                                   text = 'DELETE', cursor  = 'hand2', command = lambda: self.delete_row())
        self.delbutton.grid(row = 3, columnspan = 3, padx = 5, pady = 5, sticky = E+W)

        self.editbutton = Button(self.ents_todo, bg = self.bG, fg = self.fG, font = self.Font,
                                   text = 'EDIT', cursor = 'hand2', command = lambda: PopUpEdit(self.master))
        self.editbutton.grid(row = 4, columnspan = 3, padx = 5, pady = 5, sticky = E+W)

        #Turn this into a total entries label - will update upon new entries
        self.lastaction = Label(self.ents_todo, text = 'TOTAL ENTRIES:', bg = self.bG, fg = self.fG, font = ('Verdana',6))
        self.lastaction.grid(row = 5, columnspan = 2, padx = 5, pady = 5, sticky = E+W)

        self.database_init()
        
        #Mainloop
        self.master.protocol("WM_DELETE_WINDOW", self.kill_app)
        self.lbox.bind('<Double-Button-1>', self.magnify_win)
        

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! LOOK INTO USING THESE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##        self.lbox.bind('<Double-Button-1>',self.change_text_color_dblone)
##        self.lbox.bind('<Double-Button-2>',self.change_text_color_dbltwo)


    def load_todo_db(self):
        pass
        #tkMessageBox


    #-------------------------------------------------------------------------------
    def database_init(self):
        '''

        '''
        
        self.dbloc = r'C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\tk_todolist2.db'
        self.dataname = 'tk_todolist2.db'
        self.conn = lite.connect(self.dbloc)         #":memory:")   #(self.dbloc)
        self.c = self.conn.cursor()
        self.create_todo_table()
        self.refresh_listbox()


    #THIS IS FIRST RUN ONLY --------- AFTER IT HAS BEEN CREATED WILL RAISE ERROR
    def create_todo_table(self):
        '''
        Func to create table in the database
        '''
        
        self.c.execute('''CREATE TABLE IF NOT EXISTS todo
         (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
         datestamp           TEXT    NOT NULL,
         datedue            INT     NOT NULL,
         descript        TEXT,
         contact         TEXT,
         state            TEXT);''')
                       
        self.conn.commit()

        
    #-------------------------------------------------------------------------------
    def delete_row(self):
        '''
        Delete row Func - Currently works on the premise that the selection is an ID line. Anyothers would not work for the code.

        *** Is there a way to have any of the entries
        *** clicked that belong to the same entry would still get us the ID
        '''
        
        id_flag = self.lbox.get(ACTIVE).split()                 #Grab ACTIVE element in the listbox

        try:
            self.c.execute("""DELETE FROM todo WHERE id = ? """, (id_flag[-1],))        #Split above creates 2 string list [ID, #Val]
            self.conn.commit()

            #Update the total entries in the list now after deletion
            total_inquire = self.c.execute("""SELECT COUNT(*) FROM todo""")
            total_numb = total_inquire.fetchone()
            self.lastaction.config(text = 'Total DB modifications: {}'.format(total_numb[0]))
            self.conn.commit()

            #Clear the entry widget
            self.id_ent.delete(0,END)   
            self.refresh_listbox()              #Call to refresh the listbox (re-write it)

        except:
            pas


    #-------------------------------------------------------------------------------
    def db_entry(self):
        '''
        Func to enter the user provided information to the Database
        '''

        #For the timestamp
        self.unix = time.time()
        self.date = str(datetime.datetime.fromtimestamp(self.unix).strftime('%d-%m-%Y  %H: %M: %S'))

        #Command to insert into TODO database
        self.c.execute('INSERT INTO todo (datestamp, datedue, descript, contact, state) VALUES (?, ?, ?, ?, ?)',
              (self.date, self.dd_ent.get(), self.desc_ent.get(1.0,END), self.con_ent.get(), self.sta_ent.get()))
        self.conn.commit()

        #Call to refresh the listbox with newly updated info
        self.refresh_listbox()
        self.clear_ents()               #This func clears all of the entrywidgets for a new entry


    #-------------------------------------------------------------------------------
    def db_add_column(self):
        '''
        One time use Func -

                - Confirm no longer needed than DELETE!!!!!
        '''
        
        self.c.execute('ALTER TABLE todo ADD COLUMN state TEXT')
        self.conn.commit()
        
        return
    

    #-------------------------------------------------------------------------------
    def insert_state(self):
        '''
        
        '''
        
        self.c.execute('SELECT * FROM todo')
        itrs = self.c.fetchall()
        
        for rows in itrs:
            self.c.execute('INSERT INTO todo (id, datestamp, datedue, descript, contact, state) VALUES (?, ?, ?, ?, ?, ?)',
              (1, rows[0],rows[1],rows[2],rows[3], "off"))
        self.conn.commit()


    #-------------------------------------------------------------------------------
    def refresh_listbox(self):
        '''
        Func to refresh the listbox. Earlier funcs deleted all the entry widgets then called this. This just
        calls to the dtaatbase and gets most up to date info
        '''
        
        self.lbox.delete(0,END)     #Cleat Listbox

        #Update the total count of entries to display in main window
        total_inquire = self.c.execute("""SELECT COUNT(*) FROM todo""")
        total_numb = total_inquire.fetchone()
        self.lastaction.config(text = 'TOTAL ENTRIES: {}'.format(total_numb[0]))

        itr = 0         #Iteration for the loop below

        self.c.execute('SELECT * FROM todo')
        for row in self.c.fetchall():

            #We break down the row by position in list and print accordingly or add to listbox
            self.lbox.insert(END, 'ID: {}'.format(row[0]))
            self.lbox.insert(END, 'Datestamp: {}'.format(row[1].encode("utf-8")))           #'utf-8' : Required to make the input understandable to widget
            self.lbox.insert(END, 'Due Date: {}'.format(row[2].encode("utf-8")))
            self.lbox.insert(END, 'Description: {}'.format(row[3].encode("utf-8")))
            self.lbox.insert(END, 'Contact: {}'.format(row[4].encode("utf-8")))
            self.lbox.insert(END, 'State: {}'.format(row[5].encode("utf-8")))

            #Linebreak
            self.lbox.insert(END, '--------------------------------------------')

            #Meant to capture the newly added state parameter in DB.
            #Being able to assign an entry this variable allows us to make it triggerable for say.... "All entries past 14 days contact.... 'red' ----> Call all red entries
            
            if row[-1] == 'ON':
                self.lbox.itemconfig(itr, bg = 'red')

            else:
                pass
            
            itr += 1
        return


    #-------------------------------------------------------------------------------
    def clear_ents(self):
        '''
        Func - when called clears all of the entriy widgets
        '''
        
        self.dd_ent.delete(0,END)               #Due date  (Entry Widget)
        self.desc_ent.delete(1.0,END)         #Description (Text Widget)
        self.con_ent.delete(0,END)              #Contact  (Entry Widget)
        self.sta_ent.delete(0,END)              #State (Entry Widget)
        
        return


    #-------------------------------------------------------------------------------
    def change_text_color_dblone(self, event):
        '''
        Func to alter color of n entry item.
        ***Possible DELETION***
        '''
        
        indx = '@{},{}'.format(event.x, event.y)
        self.lbox.itemconfig(indx, bg = 'red')
        line_item = self.lbox.get(ACTIVE)        
        self.update_db_state(self.lbox.index(ACTIVE))
        

    #-------------------------------------------------------------------------------
    def change_text_color_dbltwo(self, event):
        '''
        Func to alter color of n entry item.
        ***Possible DELETION***
        '''
        
        indx = '@{},{}'.format(event.x, event.y)
        self.lbox.itemconfig(indx, bg = 'white')
        return


    #-------------------------------------------------------------------------------
    def update_db_state(self, indx):
        '''
        Func -  Using input index info

        Caller - 
        '''
        
        self.c.execute('''UPDATE todo SET state = 'ON' WHERE ID = ? ''',(indx,))
        self.conn.commit()
        self.refresh_listbox()



    #--------------------------------------------------------------------------------------------
    def kill_app(self):
        '''
        Func - Kills the main window effectivly ending the application

        Caller - 
        '''
        
        self.master.destroy()
        

    #----------------------------------------------------------------------------------------------
    def magnify_win(self,event):
        '''
        Func -

        Caller -
        '''
        
        self.master.iconify()       #This minimizes the main application window while this window is temp 'raised up'
        
        indx = '@{},{}'.format(event.x, event.y)
        sel_line = self.lbox.get(ACTIVE)
        ent_id = sel_line.strip('ID: ')

        self.temp_pop = Toplevel()                              #Creates a new toplevel window
        self.temp_pop.title('Mag View Window')             
        
        self.tempframe = Frame(self.temp_pop, bg = self.bG)         
        self.tempframe.grid()

        #WIDGET CREATION ----------------------------------------------------------------
        self.temptext = Text(self.tempframe, width = 100, height = 15, bg = self.bG, fg = self.fG, font = self.Font,
                             cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white', wrap = WORD)
        self.temptext.grid(row = 0, columnspan = 2, padx = 5, pady = 5, sticky = NSEW)

        #self.temptext.tag_configure("search", background="green")

        self.searchbut = Button(self.tempframe, text = 'Search Key', bg = self.bG, fg = self.fG, font = self.Font,
                                command =  lambda: self.print_search(self.searchent.get()))
        self.searchbut.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.searchent = Entry(self.tempframe, bg = self.bG, fg = self.fG, font = self.Font, insertbackground = 'white')
        self.searchent.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = E+W)

        self.searchlab = Label(self.tempframe, text = '', bg = self.bG, fg = self.fG, font = ('Verdana',12))
        self.searchlab.grid(row = 3, column = 1, padx = 3, pady = 3, sticky = E+W)

        #DATABASE selection of entries based on criteria input
        self.c.execute('''SELECT * FROM todo WHERE ID = ? ''',(ent_id,))
        for row in self.c.fetchall():

            #Format of the row data 
            self.temptext.insert(END, 'Selected Entry:\n')
            self.temptext.insert(END, '-----------------------------------------------------------\n')
            self.temptext.insert(END, 'ID: {}\n'.format(row[0]))
            self.temptext.insert(END, 'Datestamp: {}\n'.format(row[1].encode("utf-8")))
            self.temptext.insert(END, 'Due Date: {}\n'.format(row[2].encode("utf-8")))
            self.temptext.insert(END, 'Description: {}\n'.format(row[3].encode("utf-8")))
            self.temptext.insert(END, 'Contact: {}\n'.format(row[4].encode("utf-8")))
            self.temptext.insert(END, 'State: {}\n'.format(row[5].encode("utf-8")))
            self.temptext.insert(END, '-----------------------------------------------------------\n')

        #PROTOCOL and MAINLOOP ------------------------------------------------------------
        self.temp_pop.protocol("WM_DELETE_WINDOW", self.kill_popup)               
        self.temp_pop.mainloop()



    #----------------------------------------------------------------
    def print_search(self, s):
        '''
        To highlight all matches, just put the search command in a loop, and adjust the
        starting position to be one character past the end of the previous match.
        '''
          
        if s:
            self.searchlab.config(text = '')        #If previous search result produced the "Cant be BLANK" this returns it  none warning
            self.searchent.delete(0,END)          #Remove the search entry
            
            try:
                self.temptext.tag_remove('highlight', 0.0, END)         #Reset all the highlights
                
            except Exception as e:
                pass
            
            pos = self.temptext.search(s, 1.0, stopindex = END, nocase = 1)
            print pos
            
            while pos:                                      #Pos call above seeks first instance of the search result
                print pos                             
                length = len(s)
                row, col = pos.split('.')                #Position is in form X.YYY or Line # = X, index of that line = YYY
                ending = int(col) + length
                endr = row + '.' + str(ending)
                self.temptext.tag_add('highlight', pos, endr)    
                start = endr
                pos = self.temptext.search(s, start, stopindex=END)
                
            self.temptext.tag_config('highlight', background= 'dark goldenrod', foreground= 'black')
            
        else:
            self.temptext.tag_remove('highlight', 0.0, END)                 #Remove highlight of the previous searched result
            self.searchlab.config(text = '**Cannot be BLANK**')         #Change label from blank to "Warning" that must be value entered
            
            return


    #---------------------------------------------------------------------------------
    def kill_popup(self):
        '''
        Func - Kill the popup window and raise back to toplevel status the main (root) window

        Caller - self.temp_pop
        '''
        
        self.temp_pop.destroy()
        self.master.deiconify()
        
        return



#------------------------------------------------------------------------------------------
class PopUpEdit(object):
    
    def __init__(self, parent):
        '''
        Init - This is first window for edit window. It calls windows in succession of the information needed
        to be aquired.

        Caller - 
        '''
        
        self.parent = parent            #Referening the main window   
        self.parent.iconify()             #Minimize the main calling window until this func has run its course
        
        self.editlevel = Toplevel()
        self.editlevel.title('EDIT ToDo Entry')

        #Initilize main used values for widget character
        self.bGg =  '#0C1021'
        self.fGg = 'white'
        self.Fonts = ('Verdana',8)

        #Frame to house widgets
        self.editframe = Frame(self.editlevel, bg = self.bGg)
        self.editframe.grid(row = 0, column = 0, padx = 3, pady = 3, sticky = NSEW)
        
        #WIDGET CREATION ---------------------------------------------------------------
        self.q1_label = Label(self.editframe, text = 'WHICH ID TO EDIT?\n(Enter ID)', bg = self.bGg, fg = self.fGg, font = self.Fonts)
        self.q1_label.grid(row = 0, padx = 5, pady = 5)

        self.q1_ent = Entry(self.editframe, bg = self.bGg, fg = self.fGg, font = self.Fonts,  insertbackground = 'white')
        self.q1_ent.grid(row = 1, padx = 10, pady = 10)

        self.q1_but = Button(self.editframe, bg = self.bGg, fg = self.fGg, font = self.Fonts,
                                   text = 'NEXT', command = lambda: self.quest_two(self.q1_ent.get()))
        self.q1_but.grid(row = 2, padx = 5, pady = 5)

        #PROTOCOL to destroy if closed // Mainloop call
        self.editlevel.protocol("WM_DELETE_WINDOW", lambda: self.edit_on_closing())
        self.editlevel.mainloop()


    #------------------------------------------------------------------------------------------
    def edit_on_closing(self):
        '''
        If user decides to end the app ealry - we destroy it and raise
        back the main window
        '''
        
        self.parent.deiconify()
        self.editlevel.destroy()
        return
    
    
    #------------------------------------------------------------------------------------------
    def quest_two(self, identry):
        '''
        Func -

        Caller - __init__ (self.q1.but)
        '''
        
        self.editframe.destroy()            #Destroy last frame ending all widgets along with it. Create new one
        
        self.eframe = Frame(self.editlevel, bg = self.bGg)
        self.eframe.grid(columnspan = 3, sticky = NSEW)

        #**** !!!!  *****
        #This is currently a static assignment. Will need to be dynamically entered or asked for
        self.dbloc = r'C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Databases\tk_todolist2.db'
        self.dataname = 'tk_todolist2.db'

        #Create a databse connecction and select all that match entry ID
        self.conn = lite.connect(self.dbloc)
        self.c = self.conn.cursor()

        try:
            self.c.execute("""SELECT * FROM todo WHERE ID = ? """,(identry,))
            self.cent = self.c.fetchone()
        
        except Execption as e:
            print e
            return

        #LABELS ---------------------------------------------------------------------------------------------------
        self.q2lab = Label(self.eframe, text = 'Edit fields below then click "SUBMIT" ', bg = self.bGg, fg = self.fGg, font = self.Fonts)
        self.q2lab.grid(row = 0, column = 0,  padx = 8, pady = 3, sticky = W+E)

        self.datelab = Label(self.eframe, text = 'DATE DUE\n(mm/dd/yyyy)', bg = self.bGg, fg = self.fGg, font = self.Fonts)
        self.datelab.grid(row = 1, column = 0,  padx = 8, pady = 3, sticky = W+E)

        self.dsclab = Label(self.eframe, text = 'DESCRIPTION', bg = self.bGg, fg = self.fGg, font = self.Fonts)
        self.dsclab.grid(row = 2, column = 0, padx = 8, pady = 3, sticky = W+E)

        self.contlab = Label(self.eframe,  text = 'WHO/WHAT?', bg = self.bGg,  fg = self.fGg, font = self.Fonts)
        self.contlab.grid(row = 3, column = 0, padx = 8, pady = 3, sticky = W+E)

        self.statlab = Label(self.eframe,  text = 'STATE', bg = self.bGg, fg = self.fGg, font = self.Fonts)
        self.statlab.grid(row = 4, column = 0, padx = 8, pady = 3, sticky = W+E)


        #STRINGVARS and ENTRY WIDGETS -----------------------------------------------------------
        self.v1 = StringVar()       #v2 was originally assigned to TEXT widget but cannot have textvariable as argument
        self.v3 = StringVar()
        self.v4 = StringVar()

        
        self.ddate_ent = Entry(self.eframe, width = 75, bg = self.bGg, fg = self.fGg, font = self.Fonts, textvariable = self.v1, 
                                insertbackground = 'white', cursor = 'xterm')
        self.ddate_ent.grid(row = 1, column = 1, columnspan = 2, padx = 8, pady = 3, sticky = W+E)

        self.dsc_ent = Text(self.eframe, width = 75, height = 3, bg = self.bGg, fg = self.fGg, font = self.Fonts,
                             insertbackground = 'white', cursor = 'xterm')
        self.dsc_ent.grid(row = 2, column = 1, columnspan = 2,  padx = 8, pady = 3, sticky = W+E)

        self.cont_ent = Entry(self.eframe, width = 75, bg = self.bGg, fg = self.fGg, font = self.Fonts, textvariable = self.v3,
                               insertbackground = 'white', cursor = 'xterm')
        self.cont_ent.grid(row = 3, column = 1, columnspan = 2, padx = 8, pady = 3, sticky = W+E)

        self.stat_ent = Entry(self.eframe, width = 75, bg = self.bGg, fg = self.fGg, font = self.Fonts, textvariable = self.v4,
                               insertbackground = 'white', cursor = 'xterm')
        self.stat_ent.grid(row = 4, column = 1,columnspan = 2, padx = 8, pady = 3, sticky = W+E)


        print self.cent         #This is the TEST to see what we are producing for values
                                    #DELETE Later

    
        self.ddate_ent.insert(0, str(self.cent[2]))         #DUE DATE  (Entry)
        self.dsc_ent.insert(1.0, str(self.cent[3]))         #DESCRIPTION  (Text)
        self.cont_ent.insert(0, str(self.cent[4]))           #CONTACT  (entry)
        self.stat_ent.insert(0, str(self.cent[5]))            #STATE  (entry)


        self.v1.set(str(self.ddate_ent.get()))          #Set the variables
        self.v3.set(str(self.cont_ent.get()))
        self.v4.set(str(self.stat_ent.get()))


        #BUTTON WIDGET - Submit what has been entered-----------------------------------------------
        self.q2_but = Button(self.eframe, bg = self.bGg, fg = self.fGg, font = self.Fonts, cursor = 'hand2',
                             text = 'SUBMIT', command = lambda: self.submit_edit(identry))
        self.q2_but.grid(row = 5, columnspan = 3, padx = 5, pady = 5, sticky = E+W)
        

    #----------------------------------------------------------------------------------------------
    def submit_edit(self, identry):
        '''
        Func -

        Caller -
        '''
        
        self.c.execute("UPDATE todo SET datedue == :ddue, descript == :dsc, contact = :cnt, state = :st WHERE ID == :id ",
                          {"ddue" :self.v1.get(),  "dsc":self.dsc_ent.get(1.0,END), "cnt":self.v3.get(), "st":self.v4.get(), "id":identry})
        
        self.conn.commit()
        
        self.c.execute('SELECT * FROM todo')        
        for row in self.c.fetchall():
            print row
            
        self.kill_edit_window()

        
    #------------------------------------------------------------------------------------------------
    def kill_edit_window(self):
        '''
        Func -Kill the edit entry window and raise back to toplevel the main window

        Caller - Func self.Submit_edit when completed
        '''
        
        self.parent.deiconify()
        self.editlevel.destroy()
        return        
    


def start():
    root = Tk()
    root.title('DXP PumpCommander - To-Do')
    root.minsize(620,620)
    root.maxsize(625,650)
    ToDo(root)
    root.mainloop()


#START ------------------------------------------------------------------------
if __name__ ==  '__main__':
    root = Tk()
    root.title('DXP PumpCommander - To-Do')
    root.minsize(620,620)
    root.maxsize(625,650)
    ToDo(root)
    root.mainloop()


