from Tkinter import *
import tkMessageBox
import os
from datetime import date


'''
Approach w/ text file:

Each day of the week will have a tempory file that will have the data appended to it. When the week is complete
each of the days temps files will be written to a master copy. Then the temp files will be truncated back to
original form for the next week.

ADD - menu option to take current content of each file and write to master, then truncate the temps.


MENU:
    - Compile report and truncate temp docs.
    - 
'''



def WriteToMaster():
    '''
    Docstring - This will require us to compile all the temp file's data.
    Once complete truncate teh temp files to  be used on the next week's

    ********** FIXES NEEDED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    - Need to implemeent an ordereddict as we are not getting
    consistant output.    
    '''

    mstdir = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Master_Log.txt"

    #Start the file with the proper components to generate business
    with open(mstdir, 'w+')as md:
        md.write('Call LOG REPORT ---------- WEEK OF {}\n'.format(date.today()))
        md.write('Salesrep: Tony Kinsey\n')
        md.write('Cell: #480-294-1294\n')
        md.write('Email: Tony.Kinsey@DXPE.com\n')
        md.write('----------------- START OF REPORT -----------------\n\n')

    #The file dir locs for sampe vechain
    Mon = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Monday_Temp.txt"
    Tue = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Tuesday_Temp.txt"
    Wed = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Wed_Temp.txt"
    Thu = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Thursday_Temp.txt"
    Fri = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Friday_Temp.txt"

    #Each day will have a container to store each line of the file
    days = {'Monday':[],
            'Tuesday': [],
            'Wed': [],
            'Thursday': [],
            'Friday': []}

    #Pull Mondays 
    with open(Mon, 'r+')as M:
        lines = M.readlines()
        for line in lines:
            days['Monday'].append(line.strip('\n'))

    #Pull Tuesdays 
    with open(Tue, 'r+')as T:
        lines = T.readlines()
        for line in lines:
            days['Tuesday'].append(line.strip('\n'))

    #Pull Wed 
    with open(Wed, 'r+')as W:
        lines = W.readlines()
        for line in lines:
            days['Wed'].append(line.strip('\n'))

    #Pull Thursday
    with open(Thu, 'r+')as TH:
        lines = TH.readlines()
        for line in lines:
            days['Thursday'].append(line.strip('\n'))

    #Pull Friday
    with open(Fri, 'r+')as F:
        lines = F.readlines()
        for line in lines:
            days['Friday'].append(line.strip('\n'))

    #Writing all the compiled reports to the master file,
    #which will be printable for review
            
    with open(mstdir, 'a+')as mda:
        for i,j in days.items():
            mda.write('{} Entries ----------------\n'.format(i))
            for ents in j:
                mda.write('{}\n'.format(ents))

    #Open file to check if it worked
    os.startfile(mstdir)

    return                    
                 
                 


def ToDoTest():
    ''' 
    Docstring -
    
    '''
    
    testwin = Toplevel(bg = 'slate gray')
    testwin.title('ToDo test callback')
    testwin.geometry('300x300')
        
    testl = Label(testwin,
                  bg = 'slate gray',
                  fg = 'white',
                  text = 'NICE',
                  font = 20)
    
    testl.grid(sticky = NSEW)
    
    testwin.mainloop()


def WriteData(fileloc,kwargs, widge):
    '''
    Docstring -

    fileloc = file directory in 'string' form
    kwargs = dictionary woth the inputed data from newentry
    widget = parent window that called this func
    '''

    strdata = str(kwargs)
    with open(fileloc, 'a+')as F:                       #Appned to file mode - Dont want to overwrite our data        
        F.write(strdata)
        #for i,j in kwargs.items():
        #    F.write('{} : {}\n'.format(i,j))
        #Add breakpoint line for readability 
        F.write('\n ----------------------------------------------\n')

    os.startfile(fileloc)                                                       #Excutes r'run
    todo_inquiry = tkMessageBox.askyesno("Reminder!","Is To-Do Entry Req'd?")   #Outputs "True" if
    
    if todo_inquiry:
        widge.iconify()
        ToDoTest()
    else:
        return
    

def NewEntry(widge,day):
    '''
    Docstring --

    widge = window which housed the widget to make this callback (makes less cluttered)
    '''

    widge.iconify()  #Minimizes the window

    #Dictionary housing the file loc's of the temporary files
    days = {'Monday': r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Monday_Temp.txt",
            'Tuesday' : r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Tuesday_Temp.txt"
            }

    ne_win = Toplevel(bg = 'slate gray')

    #lABEL WIDGET for DIRECTIONS
    instruct = Label(ne_win,
                     text = 'Fill In:',
                     font = ("terminal", "14", "bold italic"),
                     bg = 'slate gray',
                     fg = 'white')
    
    instruct.grid(row = 0,
                  padx = 5,
                  pady = 5,
                  sticky = N+W)

    #WIDGET CREATIONS OF LABELS AND ENTRIES TO FILL BE FILLED IN BY USER
    compname = Label(ne_win,
                     text = 'Company Name:',
                     font = ("terminal", "8"),
                     bg = 'slate gray',
                     fg = 'white')
    
    compname.grid(row = 1,
                  column = 0,
                  padx = 3,
                  pady = 3,
                  sticky = W)

    #Entry Widget - Comp Name
    cvar = StringVar()
    comp_e = Entry(ne_win,
                   bg = 'slate gray',
                   fg = 'white',
                   textvariable = cvar,
                   width = 50)
    
    comp_e.grid(row = 1,
                column = 1,
                columnspan = 2,
                padx = 3,
                pady = 3,
                sticky = W+E)

    #LAbel Widget - Comp Name
    lastcont = Label(ne_win,
                     text = 'Date (last Contact):',
                     font = ("terminal", "8"),
                     bg = 'slate gray',
                     fg = 'white')
    
    lastcont.grid(row = 2,
                  column = 0,
                  padx = 3,
                  pady = 3,
                  sticky = W)

    #Entry Widget - Name of Contacts
    lvar = StringVar()
    last_e = Entry(ne_win,
                   bg = 'slate gray',
                   fg = 'white',
                   textvariable = lvar)
    
    last_e.grid(row = 2,
                column = 1,
                columnspan = 2,
                padx = 3,
                pady = 3,
                sticky = W+E)

    #Label Widget - Name of Contacts
    contname = Label(ne_win,
                     text = 'Name of Contact:',
                     font = ("terminal", "8"),
                     bg = 'slate gray',
                     fg = 'white')
    
    contname.grid(row = 3,
                  column = 0,
                  padx = 5,
                  pady = 5,
                  sticky = W)

    ##Entry Widget - Name of Contacts
    nvar = StringVar()
    name_e = Entry(ne_win,
                   bg = 'slate gray',
                   fg = 'white',
                   textvariable = nvar)

    name_e.grid(row = 3,
                column = 1,
                columnspan = 2,
                padx = 3,
                pady = 3,
                sticky = W+E)

    #Label Widget - Position of Contacts
    contpos = Label(ne_win,
                    text = 'Contacts Role/POS:',
                    font = ("terminal", "8"),
                     bg = 'slate gray',
                    fg = 'white')
    
    contpos.grid(row = 4,
                 column = 0,
                 padx = 5,
                 pady = 5,
                 sticky = W)

    #Entry Widget - Position of Contacts
    pvar = StringVar()
    pos_e = Entry(ne_win,
                  bg = 'slate gray',
                  fg = 'white',
                  textvariable = pvar)
    
    pos_e.grid(row = 4,
               column = 1,
               columnspan = 2,
               padx = 3,
               pady = 3,
               sticky = W+E)

    #Note adder using a Text widget. Housed in labelframe
    notelf = LabelFrame(ne_win,
                        text = 'Descriptive note of events:',
                        font = ("terminal", "10"),
                        padx = 3,
                        pady = 3,
                        bg = 'slate gray',
                        fg = 'white')
    
    notelf.grid(row = 5,
                column = 0,
                columnspan = 3,
                padx = 3,
                pady = 3)
    
    notebox = Text(notelf,
                   height = 2,
                   bg = 'slate gray',
                   fg = 'white',
                   cursor = 'pencil')
    
    notebox.grid(row = 0,
                 column = 0,
                 columnspan = 3,
                 padx = 3,
                 pady = 3)

    #Button allowing user to trigger next event
    submit_but = Button(ne_win,
                        text = 'Write to File',
                        bg = 'slate gray',
                        fg = 'white',
                        cursor = 'pencil',
                        command = lambda: GatherData(cvar.get(),lvar.get(),nvar.get(),pvar.get(),notebox.get(1.0,END)))
                        
    submit_but.grid(row = 6,
                    columnspan = 3,
                    padx = 3,
                    pady = 5,
                    sticky = E+W)

    #Nested Func
    def GatherData(c,l,n,p,note):
        '''
        Docstring -

        - delete all the entry widgets contents for the next potential entry
        - create dict to house keyword and value items to pass to writedata
        '''
        comp_e.delete(0,END)
        last_e.delete(0,END)
        name_e.delete(0,END)
        pos_e.delete(0,END)
        notebox.delete(1.0,END)
        
        entrydata = dict()
        entrydata['Company'] = c
        entrydata['Data'] = l
        entrydata['Name'] = n
        entrydata['Position'] = p
        entrydata['Note'] = note
        WriteData(day, entrydata, ne_win)        

    ne_win.mainloop()
    
    ##################################### END OF NEW ENTRY ############################




def EditEntry(widge):
    '''
    Docstring -

    widge = the listbox from which day was chosen
    '''

    widge.config(selectbackground = 'red4')                 #Font color to red to indicate "editing"
    indx = widge.curselection()                             #Current Index of selected item
    txt = widge.get(indx)                                   #Pull the text assigned to indx

    edit_win = Toplevel(bg = 'slate gray')
    edit_win.title('Edit Entry Win')
    
    edit_lab = Label(edit_win,
                     text = 'Edit Selected Entry',
                     font = ("terminal", "10", "italic"),
                     bg = 'slate gray',
                     fg = 'white')
    
    edit_lab.grid(row = 0,
                  padx = 5,
                  pady = 5,
                  sticky = E+W)

    instruct_lab = Label(edit_win, text = 'Instructions: Edit the selected entry.\
                         Once satisfied with the results please click "submit"',
                         font = ("terminal", "8", "italic"),
                         bg = 'slate gray',
                         fg = 'white')
    
    instruct_lab.grid(row = 1,
                      padx = 3,
                      pady = 3,
                      sticky = W)

    edit_txt = Text(edit_win,
                    height = 4,
                    width = 50,
                    bg = 'slate gray',
                    fg = 'white',
                    cursor = 'pencil',
                    font = ('terminal','10'))
    
    edit_txt.grid(row = 2,
                  padx = 3,
                  pady = 3,
                  sticky = E+W)
    
    edit_txt.insert(END, txt)                   #Load the listbox text from given index

    edit_but = Button(edit_win,
                      text = 'Submit Rev',
                      bg = 'slate gray',
                      fg = 'white',
                      cursor = 'pencil',
                      command = lambda: PutBack(widge))
    
    edit_but.grid(row = 3,
                  padx = 3,
                  pady = 5,
                  sticky = E+W)
    

    def PutBack(widge):
        '''
        Docstring -

        widge = same listbox inherited from parent
        '''

        widge.delete(indx[0])                               #Delete the old listbox line item
        widge.insert(indx[0], edit_txt.get(1.0, END))       #Take the text from Text widget and put in place of old listbox index
        chkindex = widge.index(indx[0])                     
        widge.selection_clear(0,END)                        #Clear listbox active selection
        widge.selection_set(indx[0])                        #Reasign the active selection
        widge.activate(indx[0])                             #Highlight the reloaded data
        
        return
    
    edit_win.mainloop()

    ##################################### END OF EDIT ENTRY ############################




def UpdateFile(fileloc,rmvitem):
    '''
    Docstring -

    First, open the file and get all your lines from the file. Then reopen the
    file in write mode and write your lines back, except for the line you want to delete:

    You need to strip("\n") the newline character in the comparison because
    if your file doesn't end with a newline character the very last line won't either.
    '''

    #First pull all the lines in the file
    with open(fileloc, "r") as f:
        lines = f.readlines()

    #Now we rewrite the file line by line skipping or changing what we removed
    with open(fileloc, "w") as f:
        for line in lines:
            if line.strip("\n") != rmvitem:
                f.write(line)
                

def DeleteEntry(widge):
    '''
    Docstring -

    widge = the listbox for the day which the button call was made

        - Delete line element from the widget
        - Delete the line from the file
    
    '''

    try:
        line = widge.curselection()
        widge.delete(line[0])
    except IndexError:
        pass
    return

    ##################################### END OF DELETE ENTRY ############################




def PullDataFile(wday):
    '''
    Docstring -

    wday = weekday that cooresponds to which temp file to pull from.
    to a file loc call Designed to read designated
    '''

    #Directory locations for the temperary files
    Mon = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Monday_Temp.txt"
    Tue = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Tuesday_Temp.txt"
    Wed = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Wed_Temp.txt"
    Thu = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Thursday_Temp.txt"
    Fri = r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Friday_Temp.txt"

    #Checking which day of the week called this func. Then opening associated
    #Data from txt file which matches what day called
    
    if wday == 'MON':                       #MONDAY
        with open(Mon, 'r+')as M:
            lines = M.readlines()
            return lines

    if wday == 'TUE':                       #TUESDAY
        with open(Tue, 'r+')as T:
            lines = T.readlines()
            return lines

    if wday == 'WED':                       #WED
        with open(Wed, 'r+')as W:
            lines = W.readlines()
            return lines

    if wday == 'THU':                       #THURSDAY
        with open(Thu, 'r+')as TH:
            lines = TH.readlines()
            return lines

    if wday == 'FRI':                       #FRIDAY 
        with open(Fri, 'r+')as F:
            lines = F.readlines()
            return lines
        
    else:
        return

    ##################################### END OF DATA PULL ############################
    




def MainWin(frame):
    '''

    Docstring - recieves root window as the input to be "Master" for widgets

    This is the main window for the Call Logging - functionality of the pump
    commander GUI.

        - Display each of the text file entries with listboxes for each of
        the days of the week.
        - Add Buttons to perform actions on the listboxes
        - Major notes can be added with the Textbox widget at the bottom
        
    '''

    #Call to read all lines from text files and pull them to
    #Insert in the perspective listboxes
    
    MON = PullDataFile('MON')           
    TUE = PullDataFile('TUE')           
    WED = PullDataFile('WED')
    THU = PullDataFile('THU')
    FRI = PullDataFile('FRI')

    #Main frame to contain all of the widgets
    main_screen = Frame(frame,
                        bg = 'slate gray')

    #Main label - utilized to display current date
    displaydate = Label(main_screen,
                        text = 'TK - Call Log -{}'.format(date.today()),
                        bg = 'slate gray',
                        fg = 'white',
                        font = ("terminal", "12", "bold italic"))
    
    displaydate.grid(row = 0,
                     column = 0,
                     sticky = W,
                     padx = 15,
                     pady = 2)    


    #########################################################################################
    #MONDAY WIDGETS -------------------------------------------------------------------------
    
    #Label frame creation - will provide nice container for monday inputs
    mlabf = LabelFrame(main_screen,
                       text = 'Monday',
                       font = ("terminal", "10", "bold italic"),
                       padx = 3,
                       pady = 3,
                       bg = 'slate gray',
                       fg = 'white')
    
    mlabf.grid(row = 1,
               column = 0,
               columnspan = 2,
               padx = 5)
    
    #Scrollbar amd listbox creation ---- LEFT side of the frame 
    mscroll = Scrollbar(mlabf,
                        orient = VERTICAL)
    
    m_lbox = Listbox(mlabf,
                     height = 4,
                     width = 75,
                     cursor = 'pencil',
                     bg = 'slate gray',
                     fg = 'white',
                     yscrollcommand = mscroll.set,
                     activestyle = 'dotbox',
                     selectbackground = 'dark goldenrod')
    
    m_lbox.grid(row = 1,
                column = 2,
                pady = 5,
                padx = 5,
                sticky = NSEW)

    #Load pulled data
    for i in MON:
        m_lbox.insert(END,i)
    
    mscroll.config(command = m_lbox.yview)
    mscroll.grid(row=1,
                 column=3,
                 sticky = N+S)
    

    #Labelframe and widgets to control listbox ---- RIGHT side
    mlabfc = LabelFrame(main_screen,
                        text = 'Monday Options',
                        font = ("terminal", "10", "bold italic"),
                        padx = 3,
                        pady = 3,
                        bg = 'slate gray',
                        fg = 'white')
    
    mlabfc.grid(row = 1,
                column = 2,
                columnspan = 3,
                padx = 3,
                sticky = NSEW)
    

    #Button widgets to provide functional interaction with listbox
    add_bm = Button(mlabfc,
                    text = 'ADD',
                    bg = 'slate gray',
                    fg = 'white',
                    command = lambda: NewEntry(frame, r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Monday_Temp.txt"),
                    width = 25)
    
    del_bm = Button(mlabfc,
                    text = 'DELETE',
                    bg = 'slate gray',
                    fg = 'white',
                    command = lambda: DeleteEntry(m_lbox),
                    width = 25)
    
    edit_bm = Button(mlabfc,
                     text = 'EDIT',
                     bg = 'slate gray',
                     fg = 'white',
                     command = lambda: EditEntry(m_lbox),
                     width = 25)
    
    add_bm.grid(row = 1, stick = E+W, padx = 3, pady = 1)
    del_bm.grid(row = 2, sticky = E+W, padx = 3, pady = 1)
    edit_bm.grid(row = 3, sticky = E+W, padx = 3, pady = 1)
    

    #########################################################################################
    #TUESDAY WIDGETS -------------------
    tlabf = LabelFrame(main_screen,
                       text = 'Tuesday',
                       font = ("terminal","10", "bold italic"),
                       padx = 3,
                       pady = 3,
                       bg = 'slate gray',
                       fg = 'white')
                        
    tlabf.grid(row = 2,
               column = 0,
               columnspan = 2,
               padx = 5)


    #Scrollbar amd listbox creation ---- LEFT side of the frame 
    tscroll = Scrollbar(tlabf,
                        orient = VERTICAL)
    
    t_lbox = Listbox(tlabf,
                     height = 4,
                     width = 75,
                     cursor = 'pencil',
                     bg = 'slate gray',
                     fg = 'white',
                     yscrollcommand = tscroll.set,
                     activestyle = 'dotbox',
                     selectbackground = 'dark goldenrod')
                        
    t_lbox.grid(row=2,
                column= 2,
                pady = 5,
                padx = 5)
                        
    #Load pulled data
    for i in TUE:
        t_lbox.insert(END,i)
    
    tscroll.config(command = t_lbox.yview)
    tscroll.grid(row=2,
                 column=3,
                 sticky = N+S)


    #Labelframe and widgets to control listbox ---- RIGHT side
    tlabfc = LabelFrame(main_screen,
                        text = 'Tuesday Options',
                        font = ("terminal", "10", "bold italic"),
                        padx = 3,
                        pady = 3,
                        bg = 'slate gray',
                        fg = 'white')
                        
    tlabfc.grid(row = 2,
                column = 2,
                columnspan = 3,
                padx = 3,
                sticky = NSEW)


    #Button widgets to provide functional interaction with listbox
    add_bt = Button(tlabfc,
                    text = 'ADD',
                    bg = 'slate gray',
                    fg = 'white',
                    command = lambda: NewEntry(frame,r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Tuesday_Temp.txt"),
                    width = 25)
                        
    del_bt = Button(tlabfc,
                    text = 'DELETE',
                    bg = 'slate gray',
                    fg = 'white',
                    command = lambda: DeleteEntry(t_lbox),
                    width = 25)
                        
    edit_bt = Button(tlabfc,
                     text = 'EDIT',
                     bg = 'slate gray',
                     fg = 'white',
                     command = lambda: EditEntry(t_lbox),
                     width = 25)

    add_bt.grid(row = 1, sticky = W+E, padx = 3, pady = 1)
    del_bt.grid(row = 2, sticky = W+E, padx = 3, pady = 1)
    edit_bt.grid(row = 3, sticky = W+E, padx = 3, pady = 1)


    #########################################################################################
    #WEDNESDAYWIDGETS -------------------
    wlabf = LabelFrame(main_screen,
                       text = 'Hump Date',
                       font = ("terminal", "10", "bold italic"),
                       padx = 3,
                       pady = 3,
                       bg = 'slate gray',
                       fg = 'white')
                        
    wlabf.grid(row = 3,
               column = 0,
               columnspan = 2,
               padx = 5)

    #Scrollbar amd listbox creation ---- LEFT side of the frame 
    wscroll = Scrollbar(wlabf,
                        orient = VERTICAL)
    
    w_lbox = Listbox(wlabf,
                     height = 4,
                     width = 75,
                     cursor = 'pencil',
                     bg = 'slate gray',
                     fg = 'white',
                     yscrollcommand = wscroll.set,
                     activestyle = 'dotbox',
                     selectbackground = 'dark goldenrod')
                        
    w_lbox.grid(row=3,
                column= 2,
                pady = 5,
                padx = 5)
                        
    #Load pulled data
    for i in WED:
        w_lbox.insert(END,i)
    
    wscroll.config(command = w_lbox.yview)
    wscroll.grid(row = 3,
                 column = 3,
                 sticky = N+S)

    #Labelframe and widgets to control listbox ---- RIGHT side
    wlabfc = LabelFrame(main_screen,
                        text = 'Humpday Options',
                        font = ("terminal", "10", "bold italic"),
                        padx = 3,
                        pady = 3,
                        bg = 'slate gray',
                        fg = 'white')
                        
    wlabfc.grid(row = 3,
                column = 2,
                columnspan = 3,
                padx = 3,
                sticky = NSEW)

    #Button widgets to provide functional interaction with listbox
    add_bw = Button(wlabfc,
                    text = 'ADD',
                    bg = 'slate gray',
                    fg = 'white',
                    command = lambda: NewEntry(frame,r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Wed_Temp.txt"),
                    width = 25)
                        
    del_bw = Button(wlabfc,
                    text = 'DELETE',
                    bg = 'slate gray',
                    fg = 'white',
                    command = lambda: DeleteEntry(w_lbox),
                    width = 25)
                        
    edit_bw = Button(wlabfc,
                     text = 'EDIT',
                     bg = 'slate gray',
                     fg = 'white',
                     command = lambda: EditEntry(w_lbox),
                     width = 25)

    add_bw.grid(row = 1, sticky = W+E, padx = 3, pady = 1)
    del_bw.grid(row = 2, sticky = W+E, padx = 3, pady = 1)
    edit_bw.grid(row = 3, sticky = W+E, padx = 3, pady = 1)


    #########################################################################################
    #THURSDAY WIDGETS -----------------------------------------------------------------------
    thlabf = LabelFrame(main_screen,
                        text = 'Thursday',
                        font = ("terminal", "10", "bold italic"),
                        padx = 3,
                        pady = 3,
                        bg = 'slate gray',
                        fg = 'white')
                        
    thlabf.grid(row = 4,
                column = 0,
                columnspan = 2,
                padx = 5)

    #Scrollbar amd listbox creation ---- LEFT side of the frame 
    thscroll = Scrollbar(thlabf,
                         orient = VERTICAL)
    
    th_lbox = Listbox(thlabf,
                      height = 4,
                      width = 75,
                      cursor = 'pencil',
                      bg = 'slate gray',
                      fg = 'white',
                      yscrollcommand = thscroll.set,
                      activestyle = 'dotbox',
                      selectbackground = 'dark goldenrod')
                        
    th_lbox.grid(row=4,
                 column= 2,
                 pady = 5,
                 padx = 5)
                        
    #Load pulled data
    for i in THU:
        th_lbox.insert(END,i)
    
    thscroll.config(command = th_lbox.yview)
    thscroll.grid(row=4,
                  column=3,
                  sticky = N+S)

    #Labelframe and widgets to control listbox ---- RIGHT side
    thlabfc = LabelFrame(main_screen,
                         text = 'Thursday Options',
                         font = ("terminal", "10", "bold italic"),
                         padx = 3,
                         pady = 3,
                         bg = 'slate gray',
                         fg = 'white')
                        
    thlabfc.grid(row = 4,
                 column = 2,
                 columnspan = 3,
                 padx = 3,
                 sticky = NSEW)

    #Button widgets to provide functional interaction with listbox
    add_bth = Button(thlabfc,
                     text = 'ADD',
                     bg = 'slate gray',
                     fg = 'white',
                     command = lambda: NewEntry(frame,r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\Thursday_Temp.txt"),
                     width = 25)
                        
    del_bth = Button(thlabfc,
                     text = 'DELETE',
                     bg = 'slate gray',
                     fg = 'white',
                     command = lambda: DeleteEntry(th_lbox),
                     width = 25)
                        
    edit_bth = Button(thlabfc,
                      text = 'EDIT',
                      bg = 'slate gray',
                      fg = 'white',
                      command = lambda: EditEntry(th_lbox),
                      width = 25)

    add_bth.grid(row = 1, sticky = W+E, padx = 3, pady = 1)
    del_bth.grid(row = 2, sticky = W+E, padx = 3, pady = 1)
    edit_bth.grid(row = 3, sticky = W+E, padx = 3, pady = 1)



    #########################################################################################
    #FRIDAY WIDGETS -------------------------------------------------------------------------
    
    flabf = LabelFrame(main_screen,
                       text = 'Friday',
                       font = ("terminal", "10", "bold italic"),
                       padx = 3,
                       pady = 3,
                       bg = 'slate gray',
                       fg = 'white')
                        
    flabf.grid(row = 5,
               column = 0,
               columnspan = 2,
               padx = 5)

    #Scrollbar amd listbox creation ---- LEFT side of the frame 
    fscroll = Scrollbar(flabf,
                        orient = VERTICAL)
        
    f_lbox = Listbox(flabf,
                     height = 4,
                     width = 75,
                     cursor = 'pencil',
                     bg = 'slate gray',
                     fg = 'white',
                     yscrollcommand = fscroll.set,
                     activestyle = 'dotbox',
                     selectbackground = 'dark goldenrod')
                        
    f_lbox.grid(row=5,
                column= 2,
                pady = 5,
                padx = 5)    

    #Load pulled data
    for i in FRI:
        f_lbox.insert(END,i)
                        
    fscroll.config(command = f_lbox.yview)
    fscroll.grid(row=5,
                 column=3,
                 sticky = N+S)

    #Labelframe and widgets to control listbox ---- RIGHT side
    flabfc = LabelFrame(main_screen,
                        text = 'Friday Options',
                        font = ("terminal", "10", "bold italic"),
                        padx = 3,
                        pady = 3,
                        bg = 'slate gray',
                        fg = 'white')
                        
    flabfc.grid(row = 5,
                column = 2,
                columnspan = 3,
                padx = 3,
                sticky = NSEW)


    #Button widgets to provide functional interaction with listbox
    add_bf = Button(flabfc,
                    text = 'ADD',
                    bg = 'slate gray',
                    fg = 'white',
                    command = lambda: NewEntry(frame,r"C:\Users\Mechkro\Desktop\Sales DXP\PumpCommander\Call Log\TFriday_Temp.txt"),
                    width = 25)
                        
    del_bf = Button(flabfc,
                    text = 'DELETE',
                    bg = 'slate gray',
                    fg = 'white',
                    command = lambda: DeleteEntry(f_lbox),
                    width = 25)
                        
    edit_bf = Button(flabfc,
                     text = 'EDIT',
                     bg = 'slate gray',
                     fg = 'white',
                     command = lambda: EditEntry(f_lbox),
                     width = 25)
    
    add_bf.grid(row = 1, sticky = W+E, padx = 3, pady = 1)
    del_bf.grid(row = 2, sticky = W+E, padx = 3, pady = 1)
    edit_bf.grid(row = 3, sticky = W+E, padx = 3, pady = 1)


    #Bottom window textbox 
    txtlf = LabelFrame(main_screen,
                       text = 'NOTE FOR LOG',
                       font = ("terminal", "10", "bold italic"),
                       padx = 3,
                       pady = 3,
                       bg = 'slate gray',
                       fg = 'white')
                        
    txtlf.grid(row = 6,
               column = 0,
               columnspan = 5,
               padx = 1,
               pady = 1)

    #Textbox - widge for user to put a note to the call log
    txtbox = Text(txtlf,
                  height = 4,
                  bg = 'slate gray',
                  fg = 'white',
                  cursor = 'pencil')
                        
    txtbox.grid(row = 0,
                column = 0,
                columnspan = 5,
                padx = 2,
                pady = 2)

    #Button Widget - to capture txtbox text and send callback func
    txtbut = Button(txtlf,
                    text = 'Add Note',
                    bg = 'slate gray',
                    fg = 'white',
                    font = ("terminal", "10"),
                    command = lambda: txtbox.get(1.0,END))

    txtbut.grid(row = 0,
                column = 6,
                padx = 2,
                pady = 2,
                sticky = N+S)
                    

    #Calling mainloop for the window
    main_screen.grid(row = 0,
                     column = 0)

    ########################## END OF MAINWIN ###########################################





#### START ##############################################################################
    
if __name__ == '__main__':
    '''
    Start of the program - making a main Tkinter window and passing
    to func to create and place widgets
    '''
                        
    root = Tk()
    root.title('Call Logger - Week of {}'.format(date.today()))    
    MainWin(root)
    root.mainloop()

#########################################################################################












    
