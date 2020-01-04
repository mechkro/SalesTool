from Tkinter import *
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
PROJECTS FILE - CREATE LIST OF ON GOING PROJECTS. EACH PROJECT LINKED TO TEXT FILE FOR NOTES

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



class Projects(object):

    currentfile = None

    #-------------------------------------------------------------------------
    def __init__(self, parent):
        self.parent = parent


        #MENU CREATION -----------------------------------------------------------------------------------------------------------------
        self.menubar = Menu(self.parent, background = '#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.filemenu = Menu(self.menubar, tearoff=0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.filemenu.add_command(label="Load Projects", command = lambda: self.load_projects_db())
        self.filemenu.add_command(label="New Project", command = lambda: self.add_project())
        self.filemenu.add_command(label="Write Projects Report", command = lambda: None)
    
        self.menubar.add_cascade(label="File", menu = self.filemenu)
        self.parent.config(bg='#0C1021', menu = self.menubar)

        #WIDGETS ----------------------------------------------------------------------------------------------------------------------------------
        #PROJECTS LIST TEXTBOX----------------------------------------
        self.entnew_labelframe = LabelFrame(self.parent, text = 'Current Projects', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.entnew_labelframe.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = NSEW)

        self.projectstext = Text(self.entnew_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 80, highlightthickness = 2,
                               cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white', state = 'disabled')
        self.projectstext.grid(row = 0, columnspan = 2, padx = 3, pady = 3)


        #----------------------------------------------------------------------
        self.projectstext.insert(END, '\n\n     ---------------------------------------------------------------------------------\n')
        self.projectstext.insert(END, '\n     REQUIRED ACTION:\n\n     Load projects (file menu) before continuing\n')
        self.projectstext.insert(END, '\n\n     ---------------------------------------------------------------------------------\n')

        #----------------------------------------------------------------------
        self.newdb_butt = Button(self.entnew_labelframe,  bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                   text = 'OK', command = lambda: None)     #CF#9
        self.newdb_butt.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = E+W)

        self.deldb_butt = Button(self.entnew_labelframe,  bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                   text = 'Delete', command = lambda: self.del_secondchance())     #CF#9
        self.deldb_butt.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = E+W)
        

        #PROJECTS OVERVIEW (DETAILED) ----------------------------------------------
        self.notes_labelframe = LabelFrame(self.parent, text = 'Project Notes', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.notes_labelframe.grid(row = 0, column = 2, columnspan = 2, padx = 5, pady = 5, sticky = NSEW)

        self.notestext = Text(self.notes_labelframe, bg =  '#0C1021', fg = 'white', font = ('Verdana',8), width = 70, highlightthickness = 2,
                               cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white',  state = 'disabled')
        self.notestext.grid(row = 0 , column = 2, columnspan = 2, padx = 3, pady = 3)


        #----------------------------------------------------------------------
        self.notestext.insert(END, '\n\n     ---------------------------------------------------------------------------------\n')
        self.notestext.insert(END, '\n     REQUIRED ACTION:\n\n     <<< --- SEE Projects Labeled Section\n')
        self.notestext.insert(END, '\n\n     ---------------------------------------------------------------------------------\n')


        #----------------------------------------------------------------------
        self.notes_butt = Button(self.notes_labelframe,  bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                   text = 'OK', command = lambda: None)     #CF#9
        self.notes_butt.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = E+W)

        self.editnotes_butt = Button(self.notes_labelframe,  bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                   text = 'Edit', command = lambda: self.edit_notes_projfile())     #CF#9
        self.editnotes_butt.grid(row = 1, column = 3, padx = 3, pady = 3, sticky = E+W)
        

        #-----------------------------------------------------------------------
        self.parent.protocol("WM_DELETE_WINDOW", lambda: self.parent.destroy())
        self.projectstext.bind("<Double-Button-1>", self.print_line)



    ##########################################
    def del_secondchance(self):
        '''
        Func - Calls a messagebox widget to confirm you really want to 'DE:ETE' the entry.

        ID Line must be highlighted in order to use.
        '''
        
        inp = self.notestext.selection_get()
        
        if inp.startswith('ID'):            
            idnumb = inp.strip('ID:')

            if tkMessageBox.askyesno(parent = self.parent, title='Are you sure?', message = 'Deleting Entry ID#\n {}'.format(str(idnumb))):
                
                dbfile = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Projects\databases\project_db.db"
                currlog = sq3.connect(dbfile)
                c = currlog.execute("""SELECT notesfile FROM projects WHERE id = ?""", (idnumb,))

                for i in c.fetchall():
                    fileloc = str(i[0])
                    os.remove(fileloc)                
               
                currlog.execute("""DELETE FROM projects WHERE id = ?""", (idnumb,))
                currlog.commit()
                self.load_projects_db()

            else:
                return
            
        else:
            tkMessageBox.showinfo(title = 'Error',
                                  message = 'Wrong line highlighted!\n(highlight the ID line)')
            
            print 'Wrong line highlighted'
            return



    def print_line(self,event):
        '''
        Currently need to select exact line of the floc directory in order to succesfully load file.
        '''
        self.notestext.delete(1.0,END)
        index = event.widget.index("@%d,%d" % (event.x, event.y))
        k = index.split('.')
        j = self.projectstext.get(float(k[0]), END)
        z = str(j).split('\n')
        zz = r'{}'.format(z[0].strip('PROJ FILE NOTES:'))

        Projects.currentfile = zz
        
        try:
            
            with open(zz, 'r+')as F:
                for line in F.readlines():
                    self.notestext.insert(END, line)

        except IOError:
            
            print 'bad selection'

        return



    def edit_notes_projfile(self):
        '''
        Func - provides a textbox to use and edit text. Once completed then submit back to the file to re-write the entry.
        
        '''
        self.editnotes_butt.config(state = DISABLED)    #Dont allow two EDIT button hits
        
        self.edit_topwin = Toplevel()
        self.edit_topwin.title('Edit project File')
        self.edit_topwin.config(bg = '#0C1021')

        self.edit_lab_instruct = Label(self.edit_topwin,
                                       text = 'Edit file then click "Submit" to update',
                                       bg =  '#0C1021', fg = 'white', font = ('Verdana',8, 'bold'))
        self.edit_lab_instruct.grid(row = 0,
                                    padx = 5, pady = 5)
        
        self.edittext = Text(self.edit_topwin,
                             bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                             cursor = 'xterm',
                             selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white',
                             highlightthickness = 2)
        self.edittext.grid(row = 1,
                           padx = 3, pady = 3,
                           sticky = NSEW)

        with open(Projects.currentfile, 'r+')as F:
            for line in F.readlines():
                self.edittext.insert(END, line)

        self.editsubmit = Button(self.edit_topwin,
                                 text = 'Submit Edit',
                                 bg =  '#0C1021', fg = 'white', font = ('Verdana',8),
                                 cursor ='hand2',
                                 command = lambda: self.update_edittext())
        self.editsubmit.grid(row= 2,
                             padx = 3, pady = 3,
                             sticky = E+W)
        
        self.edit_topwin.protocol("WM_DELETE_WINDOW", lambda: self.edit_topwin_onclose())
        self.edit_topwin.mainloop()


    #############################################
    def edit_topwin_onclose(self):
        '''

        '''
        
        self.editnotes_butt.config(state = NORMAL)
        self.edit_topwin.destroy()
        
        return
    

    #############################################
    def update_edittext(self):
        '''

        '''
        
        rewrite = self.edittext.get(1.0,END)
        
        with open(Projects.currentfile, 'w+')as F:
            for i in rewrite:
                F.write(i)

        self.notestext.delete(1.0, END)
        self.editnotes_butt.config(state = NORMAL)
        floc = Projects.currentfile
        
        with open(floc, 'r+')as F:
            for line in F.readlines():
                self.notestext.insert(END, line)

        self.edit_topwin.destroy()
        
        return
    
        

    #############################################
    def load_projects_db(self):
        '''
        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        projname TEXT,
                                        engineerfirm TEXT,
                                        contact TEXT,
                                        datedue TEXT,
                                        notesfile TEXT
        '''
        self.projectstext.delete(1.0, END)

        #----------------------------------------------------------------------
        self.notestext.delete(1.0,END)
        
        self.notestext.insert(END, '\n\n     ---------------------------------------------------------------------------------\n')
        self.notestext.insert(END, '\n     REQUIRED ACTION:\n\n     - CHOOSE project (Click)\n')
        self.notestext.insert(END, '\n\n     ---------------------------------------------------------------------------------\n')

        #----------------------------------------------------------------------
        dbfile = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Projects\databases\project_db.db"
        self.currlog = sq3.connect(dbfile)
        self.c = self.currlog.cursor()
        self.c.execute("""SELECT * FROM sqlite_master WHERE type = 'table' """)

        self.projectstext.insert(END, '\n\n     ---------------------------------------------------------------------------------\n')
        self.projectstext.insert(END, '\n       INSTRUCTIONS:\n\n      - "Double Click" left mouse button on project File Directory to open detailed file.')
        self.projectstext.insert(END, '\n\n     ---------------------------------------------------------------------------------\n')

        self.c.execute("""SELECT * FROM projects""")
        for row in self.c.fetchall():
            
            row_id = row[0]                 #Entry ID Number (unique!)
            row_pname = row[1]          #Project name or title
            row_efirm = row[2]            #Engineering firm or Contractor in possesion
            row_cont = row[3]              #Contact @ Eng firm or Contractor
            row_ddue = row[4]             #Date this is due
            row_nfile = row[5]              #Text file location - will house all pertinent info
            textentry = """\n
ID:  {}
PROJ: NAME:  {}
ENG FIRM:  {}
MAIN CONTACT:\n{}
DATE DUE:  {}
PROJ FILE NOTES:  {}\n
""".format(row_id, row_pname, row_efirm, row_cont, row_ddue, row_nfile)
            
            self.projectstext.insert(END, textentry)
            self.projectstext.insert(END, '\n--------------------------------------------------\n')
        self.currlog.close()
        return
    


    def new_projects_file(self):
        '''

        '''
        fname = tkFileDialog.asksaveasfilename(title = 'Choose Directory and File name',
                                              initialdir= r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Projects\notefiles",
                                              filetypes = (("Text Document", "*.txt"),))
        return fname
        


    def add_project(self):
        """
        Create window with widgets to input for db and notesfile creation

        - Ask projectname, contact, datedue
        - then proceed to get notefile directory by creating text file and saving directory
        - we then have the info to proceed with database creation
        - 
        """
        self.parent.iconify()
        
        self.addproj_win = Toplevel()
        self.addproj_win.title('New Project - Details Setup')
        self.addproj_win.config(bg =  '#0C1021')

        #RFQ/PROJECT NAME -----------------------------------------------------------------------------------------------------------------------
        self.pname_lf = LabelFrame(self.addproj_win, text = 'Project Name', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.pname_lf.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = NSEW)  
        self.pname_ent = Entry(self.pname_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.pname_ent.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = E+W)

        #CONTRACTOR/ENGINEER FIRM---------------------------------------------------------------------------------------------------------------------
        self.engfirm_lf = LabelFrame(self.addproj_win, text = 'Contractor/Eng.Firm', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.engfirm_lf.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = NSEW) 
        self.engfirm_ent = Entry(self.engfirm_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.engfirm_ent.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = E+W)

        #MAIN CONTACT INFO----------------------------------------------------------------------------------------------------------------------
        self.contact_lf = LabelFrame(self.addproj_win, text = 'Main Contact', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.contact_lf.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = NSEW)

        #CONTACT NAME
        self.contact_name  = Label(self.contact_lf, text = 'Contact Name:', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.contact_name.grid(row = 0, column = 0, padx = 3, pady = 3)
        self.contname_ent = Entry(self.contact_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.contname_ent.grid(row = 0, column = 1, padx = 3, pady = 3)

        #CONTACT P#
        self.contact_numb  = Label(self.contact_lf, text = 'Contact Phone#:', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.contact_numb.grid(row = 1, column = 0, padx = 3, pady = 3)
        self.contnumb_ent = Entry(self.contact_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.contnumb_ent.grid(row = 1, column = 1, padx = 3, pady = 3)

        #CONTACT EMAIL
        self.contact_email  = Label(self.contact_lf, text = 'Contact Email:', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.contact_email.grid(row = 2, column = 0, padx = 3, pady = 3)
        self.contemail_ent = Entry(self.contact_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.contemail_ent.grid(row = 2, column = 1, padx = 3, pady = 3)

        #DATE DUE ---------------------------------------------------------------------------------------------------------------------------------
        self.ddue_lf = LabelFrame(self.addproj_win, text = 'Date Due', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.ddue_lf.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = NSEW)

        #YEAR
        self.ddue_year  = Label(self.ddue_lf, text = 'Year (XXXX)', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.ddue_year.grid(row = 0, column = 0, padx = 3, pady = 3)
        self.ddyear_ent = Entry(self.ddue_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.ddyear_ent.grid(row = 0, column = 1, padx = 3, pady = 3)

        #MONTH
        self.ddue_month  = Label(self.ddue_lf, text = 'Month (xx)', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.ddue_month.grid(row = 1, column = 0, padx = 3, pady = 3)
        self.ddmonth_ent = Entry(self.ddue_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.ddmonth_ent.grid(row = 1, column = 1, padx = 3, pady = 3)

        #DAY
        self.ddue_day  = Label(self.ddue_lf, text = 'Day (xx)', bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.ddue_day.grid(row = 2, column = 0, padx = 3, pady = 3)
        self.ddday_ent = Entry(self.ddue_lf, bg =  '#0C1021', fg = 'white', font = ('Verdana',8,'bold'))
        self.ddday_ent.grid(row = 2, column = 1, padx = 3, pady = 3)

        #SUBMIT BUTTON -------------------------------------------------------------------------------------------
        self.proj_add_butt = Button(self.addproj_win,  bg =  '#0C1021', fg = 'white', font = ('Verdana',8), cursor = 'hand2',
                                   text = 'Submit', command = lambda: self.compile_and_upload()) 
        self.proj_add_butt.grid(row = 4, column = 0, columnspan = 2,  padx = 5, pady = 5)

        self.addproj_win.protocol("WM_DELETE_WINDOW", lambda: self.addproj_oncancel())
        self.addproj_win.mainloop()


    def addproj_oncancel(self):
        '''
        Protocol function which directs what to do in case the pop up window is not used (User hit 'X')
        '''
        self.addproj_win.destroy()
        self.parent.deiconify()
        return

        
    def compile_and_upload(self):
        '''

        '''        
        vpname = self.pname_ent.get()
        vfirm = self.engfirm_ent.get()
        
        vc_name = self.contname_ent.get()
        vc_pnumb = self.contnumb_ent.get()
        vc_email = self.contemail_ent.get()
        
        vd_year = self.ddyear_ent.get()
        vd_month = self.ddmonth_ent.get()
        vd_day = self.ddday_ent.get()

        v_contstr = """Contact Name:  {}
Contact Phone #:  {}
Contact Email:  {}
""".format(vc_name,
           vc_pnumb,
           vc_email)
        
        duedate = datetime.date(int(vd_year), int(vd_month), int(vd_day))

        floc = self.new_projects_file()
        if floc.endswith('.txt'):
            pass
        else:
            floc = floc + '.txt'

        vars = (vpname, vfirm, v_contstr, duedate, r'{}'.format(floc))
        
        self.create_proj_textfile(floc, *vars)    
        self.insert_to_table(vars)



    def create_proj_textfile(self,floc, *args):
        '''

        '''
        file_format = """\n
Created: {}  ----  {} days until due
PROJ: NAME:  {}
ENG FIRM:  {}
MAIN CONTACT:\n{}
DATE DUE:  {}
PROJ FILE NOTES:  {}\n
""".format(datetime.date.today(), (args[3]- datetime.date.today()).days, args[0],args[1],args[2], args[3],args[4])
        with open(floc, 'w+')as F:
            F.write(file_format)
        return
        


    def insert_to_table(self, vars):
        '''

        '''
        v1,v2,v3,v4,v5 = vars[0],vars[1],vars[2],vars[3],vars[4]
        dbfile = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Projects\databases\project_db.db"
        self.currlog = sq3.connect(dbfile)
        self.c = self.currlog.cursor()
        self.c.execute("""INSERT INTO projects (projname, engineerfirm, contact, datedue, notesfile) VALUES (?,?,?,?,?)""",(v1,v2,v3,v4,v5))
        self.currlog.commit()
        self.addproj_oncancel()
        self.load_projects_db()
        return

    ###END OF CLASS -----------------------------------------------------------------------------------------------
        



#DATABASE INIITIAL ---------------------------------------------------------------------------------------------
def connect_proj_db():
    '''
    
    '''
    dbfile = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Projects\databases\project_db.db"
    currlog = sq3.connect(dbfile)
    currlog.row_factory = sq3.Row

    create_table(currlog)
    currlog.close()
 

def create_table(clog):
        '''
        '''        
        clog.execute("""CREATE TABLE IF NOT EXISTS projects
                                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        projname TEXT,
                                        engineerfirm TEXT,
                                        contact TEXT,
                                        datedue TEXT,
                                        notesfile TEXT);""")
        clog.commit()
        return


def start():
    connect_proj_db()
    root = Tk()
    root.title('Pump Commander: Projects Info')
    Projects(root)
    root.mainloop()


if __name__ == '__main__':
    start()





