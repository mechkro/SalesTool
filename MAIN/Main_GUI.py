import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3 as sq3
import os
from calllog_test import WidgetMaker as wm







#File Overview -----------------------------------------------------------------
""" 
This module is for the implementation of a call log input to be eventually written to file 
@ the end of the week. This is part of the larger project program to help increase my time
management in sales. 

This is to help fill gaps in shortcomings for my workflow that I see missing in
programs I have come across.
"""
#-----------------------------------------------------------------------------------




customer = ['AZ_Canning', 'Abrams_Airborne', 'Air_Liquide_Bagdad', 'Air_Products_and_Chemicals', 'Apache_Nitrogen', 'Arizona_Electric_Power', 'Arizona_LNG_Applied_LNG',
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




#Configuration Variables -----------------------------------------------------
BG = '#0C1021'
FG = 'white'
DGR = 'dark goldenrod'
SFG = 'black'
#-----------------------------------------------------------------------------------







#Main class for creation of GUI Interface ------------------------------------------------
class CallLogWindow:
    
    edit_track = 'N'                    #This variable storing stste, to allow us to track if text is disbaled (N) or normal (Y)
    cur_active = None               #We start in neutral selection mode ---- (there is no  activated Listbox)
    
    
    def __init__(self, parent, *args, **kwargs):
        """ 
        
        """
        
        self.parent = parent 
        self.database_init()
      
        
        #Menu Creation 
        #----------------------------------------------------------------------------------------------------------
        self.calllog_menu = tk.Menu(self.parent, background = '#0C1021', foreground='white', activebackground= DGR, activeforeground='white')

        self.writemenu = tk.Menu(self.calllog_menu, tearoff=0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.writemenu.add_command(label="Write Log to File", command = lambda: self.write_to_file()) 

        self.calllog_menu.add_cascade(label="Write Log", menu = self.writemenu)

        
        #STATE CHOICE 
        #---------------------------------------------------------------------------------------------------------
        self.resetmenu = tk.Menu(self.calllog_menu, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.resetmenu.add_command(label = "Reset Call File", command = lambda: None) #self.reset_log_protocol())

        self.calllog_menu.add_cascade(label = "Reset", menu = self.resetmenu)


        #LOAD DATABASE
        #---------------------------------------------------------------------------------------------------------
        self.loadmenu = tk.Menu(self.calllog_menu, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.loadmenu.add_command(label = "New DB", command = lambda:  None)  #self.ask_db_filename())      #self.new_database())
        self.loadmenu.add_command(label = "Load Database", command = lambda: None)  #self.open_db_file())           #self.Database('START'))
        self.loadmenu.add_command(label = "Add Note", command = lambda: None) #self.check_if_db_open())       #add_note_to_db())
        
        self.calllog_menu.add_cascade(label = "Load", menu = self.loadmenu)
        
        #Help Menu 
        #--------------------------------------------------------------------------------------------------------
        self.helpmenu = tk.Menu(self.calllog_menu, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.helpmenu.add_command(label = "Tips on Apps Usage", command = lambda: None) 
        
        self.calllog_menu.add_cascade(label = "Help", menu = self.helpmenu)


        #Testing - Print feature
        #--------------------------------------------------------------------------------------------------------
        self.testmenu = tk.Menu(self.calllog_menu, tearoff = 0, background='#0C1021', foreground='white', activebackground='dark goldenrod', activeforeground='white')
        self.testmenu.add_command(label = "Print Mon", command = lambda: self.test_print('MONDAY')) 
        self.testmenu.add_command(label = "Print Tue", command = lambda: self.test_print('TUESDAY'))
        self.testmenu.add_command(label = "Print Wed", command = lambda: self.test_print('WED'))
        self.testmenu.add_command(label = "Print Thur", command = lambda: self.test_print('THURSDAY')) 
        self.testmenu.add_command(label = "Print Fri", command = lambda: self.test_print('FRIDAY'))        
        
        self.calllog_menu.add_cascade(label = "Test", menu = self.testmenu)        


        #LOAD TO WINDOW
        # ----------------------------------------------------------------------------------------------------------
        self.parent.config(bg='#0C1021', menu = self.calllog_menu)
        
       
       #Widget Frames
       # ----------------------------------------------------------------------------------------------------------
        self.display_frame =  wm.create_frames(self.parent, *[0, 0, 1])  #tk.Frame(self.parent,  bg = BG)
        #self.display_frame.grid(row = 0, column = 0, sticky = tk.NS)
        
        self.selection_frame = wm.create_frames(self.parent, *[0, 1, 2]) #tk.Frame(self.parent,  bg =  BG)
        #self.selection_frame.grid(row = 0, column = 1, columnspan = 2,  sticky = tk.NS)        
                
        self.todo_frame = wm.create_frames(self.parent, *[0, 3, 2])  #tk.Frame(self.parent,  bg =  BG)
        #self.todo_frame.grid(row = 0, column = 3, columnspan = 2,  sticky = tk.NS)            
        
       #Label Creation
       # ----------------------------------------------------------------------------------------------------------
        self.lab_accounts = tk.Label(self.display_frame, text = 'Accounts',  bg = BG, fg = FG, 
                              font = ('Verdana', 20, 'bold'))
        self.lab_accounts.grid(row = 0, column = 0 , padx = 5, pady = 5, sticky = tk.EW)
        
        self.lab_selection= tk.Label(self.selection_frame, text = 'Selection',  bg = BG, fg = FG,
                               font = ('Verdana', 20, 'bold'))        
        self.lab_selection.grid(row = 0, column = 0 , columnspan = 2,  padx = 5, pady = 5, sticky = tk.EW) 
        
        
        ### Automate labelframe creation w/ widget
        #-----------------------------------------------------------------------------------------------------------
        self.mon_labelframe =  wm.create_labframe(self.parent, self.display_frame, 'MONDAY')                 #self.create_labframe(self.display_frame, 'MONDAY')
        self.mon_labelframe.grid(row = 1, padx = 3, pady = 3, sticky = tk.NS)
        
        self.tue_labelframe = wm.create_labframe(self.parent, self.display_frame, 'TUESDAY') 
        self.tue_labelframe.grid(row = 2 ,padx = 3, pady = 3, sticky =  tk.NS)
        
        self.wed_labelframe = wm.create_labframe(self.parent, self.display_frame, 'WED') 
        self.wed_labelframe.grid(row = 3, padx = 3, pady = 3, sticky =  tk.NS)
        
        self.thur_labelframe = wm.create_labframe(self.parent, self.display_frame, 'THURSDAY') 
        self.thur_labelframe.grid(row = 4, padx = 3, pady = 3, sticky =  tk.NS)
        
        self.fri_labelframe = wm.create_labframe(self.parent, self.display_frame, 'FRIDAY') 
        self.fri_labelframe.grid(row = 5, padx = 3, pady = 3, sticky =  tk.NS) 
        
        #self.m = wm.create_labframe(self.display_frame, 'MONDAY')
        #self.m.grid(row = 1, padx = 3, pady = 3, sticky = tk.NS)
        
        ### Automate listbox creation w/ widget
        #-----------------------------------------------------------------------------------------------------------        
        self.mon_lbox = self.create_listbox(self.mon_labelframe, 5, 30)
        self.mon_lbox.grid(padx = 5, pady = 5)
   
        self.tue_lbox = self.create_listbox(self.tue_labelframe, 5, 30)
        self.tue_lbox.grid(padx = 5, pady = 5)
         
        self.wed_lbox = self.create_listbox(self.wed_labelframe, 5, 30)
        self.wed_lbox.grid(padx = 5, pady = 5)        
        
        self.th_lbox = self.create_listbox(self.thur_labelframe, 5, 30)
        self.th_lbox.grid(padx = 5, pady = 5)        
  
        self.f_lbox = self.create_listbox(self.fri_labelframe, 5, 30)
        self.f_lbox.grid(padx = 5, pady = 5) 
        
        
        #To DO labelframe----------------------------------------------------------------------------------------
        self.todo_lab = tk.Label(self.todo_frame, text = "TODO's", bg = BG, fg = FG,
                                 font = ('Verdana', 20, 'bold'))
        self.todo_lab.grid(row = 0, padx = 5, pady = 5)
        
        self.todo_lframe = tk.LabelFrame(self.todo_frame, text = 'Detail Window',
                                         bg = BG, fg = FG, font = ('Verdana', 8, 'bold'), cursor = 'hand2')
        self.todo_lframe.grid(padx = 5, pady = 5)
        
        self.todo_scroll = tk.Scrollbar(self.todo_lframe, bg = BG, highlightcolor = BG,  highlightbackground = BG,  troughcolor = BG)
        self.todo_scroll.grid(row = 1, column = 1 , sticky = tk.NS)   
        
        self.todo_text = tk.Text(self.todo_lframe, height = 31, width = 70, bg = BG, fg = FG, 
                                 yscrollcommand = self.todo_scroll.set, wrap = tk.WORD)
        self.todo_text.grid(row = 1, column = 0, padx = 5, pady = 5)
        
        self.todo_scroll.config(command = self.todo_text.yview)
        
        self.todo_frame.bind()
        
        self.todo_text.tag_config('nline', background=BG, foreground=DGR)
        
        #Write to file ----------------------
        with open(r'C:\Users\kinse\Anaconda3\DXPE Sales Tool\SalesTool-master\SalesTool-master\pump_applications.txt', 'r')as F:
            lines = F.readlines()
            itr = 0            
            for line in lines:                
                if itr % 2 == 0:
                    self.todo_text.insert(tk.END, line, 'nline')
                else:
                    self.todo_text.insert(tk.END, line)
                itr += 1                
                    
        
        
        #Edit mode button --------------------------------------------------------------------------------------------------
        self.edit_entry_button = tk.Button(self.display_frame, text = 'Edit Entries', bg = BG, 
                                           fg = FG,  font = ('Verdana',8,'bold'), cursor = 'hand2')
        self.edit_entry_button.grid(row = 6, padx = 3, pady = 5, sticky = tk.EW)
        
        self.unitholdr = [(self.mon_labelframe, 'a', self.mon_lbox),
                                   (self.tue_labelframe, 'a', self.tue_lbox),
                                   (self.wed_labelframe, 'a', self.wed_lbox),
                                   (self.thur_labelframe, 'a', self.th_lbox),
                                   (self.fri_labelframe, 'a', self.f_lbox),
                                   (self.selection_frame, 's', None),
                                   (self.todo_lframe,'t',None),]
        
        
        #Iterate through dictionary to add binding functionality -----------------------------------
        for i in self.unitholdr:                                                              
            self.bind_enter_leave(i[1],i[0])
            
            if i[0] == self.selection_frame or i[0] == self.todo_lframe:
                pass            
            else:
                    self.bind_clicking_widge(i[-1])
                    
                    
        #Selection Frame Side
        #------------------------------------------------------------------------------------------------------------------
        
        #Top Section------------------
        self.det_labelframe_1 = tk.LabelFrame(self.selection_frame, text = 'Enter Info', 
                                            bg =  BG,  fg =  FG,  font = ('Verdana',9,'bold'))
        self.det_labelframe_1.grid(row = 1, padx = 3, pady = 5, sticky =  tk.NS) 
        
        #Spinbox to assign and send data to correct field for viewing--------------------------
        self.choices = ('MONDAY', 'TUESDAY', 'WED', 'THURSDAY', 'FRIDAY')
        self.spinbox = tk.Spinbox(self.det_labelframe_1, values = self.choices, bg =  '#0C1021', fg = DGR,  
                                  font = ('Verdana',8), cursor = 'hand2', justify = tk.CENTER)
        
        self.spinbox.grid(row = 0, column =1, columnspan = 2, padx = 3, pady = 3, sticky = tk.EW)        
        
        
        #Company name-------------------------------
        self.complab = tk.Label(self.det_labelframe_1, text = 'Company Name', bg = BG, fg = FG, font = ('Verdana',8))         #some type of auto populate
        self.complab.grid(row = 1 , column = 1, padx = 3, pady = 3, sticky = tk.W)
        
        #self.comp_ent =  tk.Entry(self.det_labelframe_1, bg = BG, fg = FG, font = ('Verdana',8), width = 50,
                               #cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white')
        #self.comp_ent.grid(row = 1 , column = 2, padx = 3, pady = 3, sticky = tk.E)        
        
        #-----------------------------------------------
        #Combo Box Styling and creation------------------
        
        style = ttk.Style()
        style.theme_settings("default", {
           "TCombobox": {
               "configure": {"padding": 5},
               "map": {
                   "background": [("active", BG),
                                  ("!disabled", FG)],
                   "fieldbackground": [("!disabled", DGR)],
                   "foreground": [("focus", FG),
                                  ("!disabled", FG)]
               }
           }
        })
        
        self.company_combo = ttk.Combobox(self.det_labelframe_1, values = [i for i in customer])
        self.company_combo.grid(row = 1 , column = 2, padx = 3, pady = 3, sticky = tk.EW)
        
        #------------------------------------------------------
        #Contact Info------------------------------------
        self.contlab = tk.Label(self.det_labelframe_1, text = 'Contact Name', bg = BG, fg = FG, font = ('Verdana',8))
        self.contlab.grid(row = 2 , column = 1, padx = 3, pady = 3, sticky = tk.W)
        
        self.cont_ent =  tk.Entry(self.det_labelframe_1, bg = BG, fg = FG,  font = ('Verdana',8), width = 50,
                               cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white' )
        self.cont_ent.grid(row = 2 , column = 2, padx = 3, pady = 3, sticky = tk.E) 
        
        
        #Medium used i.e. email, phone call, meeting , etc.--------------------------------------
        self.medlab = tk.Label(self.det_labelframe_1, text = 'Medium Used', bg = BG, fg = FG, font = ('Verdana',8))           #Think about using a spinbox
        self.medlab.grid(row = 3 , column = 1, padx = 3, pady = 3, sticky = tk.W)
        
        self.med_ent =  tk.Entry(self.det_labelframe_1, bg = BG, fg = FG, font = ('Verdana',8), width = 50,
                              cursor = 'xterm', selectbackground = 'dark goldenrod', insertbackground = 'white' )
        self.med_ent.grid(row = 3 , column = 2, padx = 3, pady = 3, sticky = tk.E)        
        
        
        #Description of transaction-------------------------------------
        self.desclab = tk.Label(self.det_labelframe_1, text = 'Description', bg = BG, fg = FG, font = ('Verdana',8))
        self.desclab.grid(row = 4 , column = 1, padx = 3, pady = 3, sticky = tk.W)
        
        self.desc_scroll = tk.Scrollbar(self.det_labelframe_1, bg = BG, highlightcolor = BG,  highlightbackground = BG,  troughcolor = BG)
        self.desc_scroll.grid(row = 4, column = 3 , sticky = tk.NS)
        
        self.desc_text = tk.Text(self.det_labelframe_1, bg = BG, fg = FG, font = ('Verdana',8), height = 5, width = 50,
                                 cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.desc_text.grid(row = 4, column = 2, padx = 3, pady = 3) 

        #Assigning binding events to the text widget-------------------------------------------
        self.desc_text.bind('<Button-3>', self.copy_highlighted_text)           
        self.desc_text.bind('<Button-1>', self.display_widge_shrink)


        #Going forward what to do---------------------------------------------------
        self.fwdlab = tk.Label(self.det_labelframe_1, text = 'Forward', bg = BG, fg = FG, font = ('Verdana',8))
        self.fwdlab.grid(row = 5, column = 1, padx = 3, pady = 3, sticky = tk.W) 
        
        self.fwd_scroll = tk.Scrollbar(self.det_labelframe_1, bg = BG, highlightcolor = BG,  highlightbackground = BG,  troughcolor = BG)
        self.fwd_scroll.grid(row = 5, column = 3 , sticky = tk.NS) 
        
        self.fwd_text = tk.Text(self.det_labelframe_1, bg = BG, fg = FG, font = ('Verdana',8), height = 5, width = 50,
                                cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.fwd_text.grid(row = 5, column = 2, padx = 3, pady = 3, sticky = tk.E)  
        
        
        #Assigning binding events to the text widget-------------------------------------------
        self.fwd_text.bind('<Button-3>', self.copy_highlighted_text)            
        self.fwd_text.bind('<Button-1>', self.display_widge_shrink)
        
        
        #BUTTON WIDGET -----------------------------------------------------------------------------------------------------
        self.submitbutton = tk.Button(self.det_labelframe_1, bg = BG, fg = FG, font = ('Verdana',8), cursor = 'hand2',
                                   text = 'SUBMIT', command = lambda: self.pull_entry_data())   #self.enter_new_entry())     
        self.submitbutton.grid(row = 6, column = 1, columnspan = 2,  padx = 3, pady = 3, sticky = tk.EW)
        
        
        #Bottom Section-------------- 
        self.det_labelframe_2 = tk.LabelFrame(self.selection_frame, text = 'NoteAdder', 
                                            bg =  BG,  fg =  FG,  font = ('Verdana',9,'bold'))
        self.det_labelframe_2.grid(row = 2, padx = 3, pady = 5, sticky =  tk.NS) 
        
        
        #Have decided to make this the notes section for displaying stored DB notes for whatever day of the wek listbox has the current focus
        self.det_scroll = tk.Scrollbar(self.det_labelframe_2, bg = BG, highlightcolor = BG,  highlightbackground = BG,  troughcolor = BG)
        self.det_scroll.grid(row = 0, column = 1 , sticky = tk.NS) 
        
        self.det_text = tk.Text(self.det_labelframe_2, bg = BG, fg = FG, font = ('Verdana',8), height = 11, width = 65,
                                cursor = 'xterm', selectbackground = 'dark goldenrod', selectforeground = 'black', insertbackground = 'white')
        self.det_text.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = tk.NS) 
        
        
        self.det_text.config(state = tk.DISABLED)                                       #Disabled the text box. Will have to check edit radiobutton to return NORMAL state
        self.det_text.bind('<Button-3>', self.copy_highlighted_text)          #Add binding event to the text widget
        
        
        #Radio button to toggle on and off editability to the text widget--------------------------------
        self.edit_note_switch = tk.Radiobutton(self.det_labelframe_2, text = 'Edit Mode', command = self.det_text_state_change, value = 1, fg = FG, bg = BG)
        self.edit_note_switch.grid(row = 1, column = 0, sticky = tk.EW)
    
        self.add_new_note = tk.Button(self.det_labelframe_2, text = 'Add Note', command = self.add_note_to_current_day, bg = BG, fg = FG)
        self.add_new_note.grid(row = 2, column = 0,  sticky = tk.EW)
    
    
    
    #----------------------------------------------------------------------------------------------
    def add_note_to_current_day(self):
        """ 
        Func to add the text to the database for the current day. 
        
        *** Should we make it just a notes file period????
        """
        
        txtgrab = self.det_text.get(1.0, tk.END)
        
        if len(txtgrab) > 1:
            print(len(txtgrab))
            print(txtgrab)
            #Will need to send to database function to add entry then delete
            self.det_text.delete(1.0, tk.END)
            
        else:
            print('No Text found')
     
    
    
    #----------------------------------------------------------------------------------------------
    def test_print(self, day_of_week):
        """
        Temporary testing function to see whats in the database for each of the assigned days
        """
        
        c = self.conn.cursor()
        log = self.conn.cursor()
        cnt = self.conn.cursor()
        
        #Priniting all the notes for the day of the week
        c.execute('SELECT * FROM {}'.format(day_of_week))
        for row in c.fetchall():
            print(row)
            
        cnt.execute('SELECT COUNT(*) FROM calllog WHERE day = ?',(day_of_week,))
        numb = cnt.fetchone()
        print(numb[0])
            
        log.execute('SELECT * FROM calllog WHERE day = ?',(day_of_week,))
        for row in log.fetchall():
            print(row)
            
        return       
        
        
        
    #----------------------------------------------------------------------------------------------
    def det_text_state_change(self):
        """
        
        """
        
        if CallLogWindow.edit_track == 'N':
            self.det_text.config(state = tk.NORMAL)
            CallLogWindow.edit_track = 'Y'
            
        else:
            self.det_text.config(state = tk.DISABLED)
            CallLogWindow.edit_track = 'N'
            
        return
          
    
    #----------------------------------------------------------------------------------------------
    def database_init(self):
        """ 
        
        """
        
        db_dir = r'C:\Users\kinse\Anaconda3\DB\Test_1.db'
        self.conn = sq3.connect(db_dir)                                                  #:memory:')
        self.create_db_tables()
        print('SQL Connection and table created Successfully')
        
        return
    
    
    
    #----------------------------------------------------------------------------------------------
    def create_db_tables(self):
        """ 
        
        """
        
        #Call log entries database
        self.conn.execute("""CREATE TABLE IF NOT EXISTS calllog (day TEXT, comp TEXT, cont TEXT, med TEXT, desc TEXT, fwd TEXT) """)  
        self.conn.commit()

        #Days Notes database
        self.conn.execute("""CREATE TABLE IF NOT EXISTS  notes (day TEXT,  daynote TEXT) """)  
        self.conn.commit()
        
        #Creating table for each day will prove to be easier and less messy to handle
        choices = ('MONDAY', 'TUESDAY', 'WED', 'THURSDAY', 'FRIDAY')
        
        for chc in choices:
            
            self.conn.execute("""CREATE TABLE IF NOT EXISTS  {}(daynote TEXT) """.format(chc))  
            self.conn.commit()
            print('TABLE {} SUCCESFULLY CREATED'.format(chc))
        
        return
    
        
        
    #----------------------------------------------------------------------------------------------
    def db_entry_print(self):
        """ 
        
        """
        
        c = self.conn.cursor()
        c.execute("""SELECT * FROM calllog""")
        
        try: 
            
            for row in c.fetchall():
                print(row)
                
        except AttributeError as e:
            
            print(e)
            print(c.fetchone())
        
        
        c.close()
        return
        
    
    
    #-----START WIDGET CREATION-----------------------------------------------------------------------------------------
    ####################################################################################
    def create_labels(self, w):
        """
        To aid in cleanup of the __init__ function. Cleaner and easier to read code is the goal.
        Create Label widget 
        """
        
        pass
    
    #----------------------------------------------------------------------------------------------
    def create_entries(self, w):
        """
        To aid in cleanup of the __init__ function. Cleaner and easier to read code is the goal.
        Create Entry widget 
        """
        
        pass
    
    #----------------------------------------------------------------------------------------------
    def create_labframe(self, frm, txt):
        """
        To aid in cleanup of the __init__ function. Cleaner and easier to read code is the goal.
        Create LabelFrame widget 
        """
        
        return tk.LabelFrame(frm, text = txt, bg =  BG,  fg =  FG, font = ('Verdana',8,'bold'), cursor = 'hand2')
 
    
    
    #----------------------------------------------------------------------------------------------
    def create_listbox(self, frm, h, w):
        """
        To aid in cleanup of the __init__ function. Cleaner and easier to read code is the goal.
        Create LabelFrame widget 
        
        frm = Frame or parent widget
        h = height of widget
        w = width of widget
        """
        return tk.Listbox(frm, height = h, width = w, bg = BG, fg = FG, font = ('Verdana', 8, 'normal'), cursor = 'hand2')
    
    
    #------END----------------------------------------------------------------------------------------
    ####################################################################################



    #---START--------------Functions for GUI Functionality --------------------------------------------------------------
    #####################################################################################################
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
        
        self.pulled_data_array = [sbox, comp_E, cont_E, med_E, desc_T, fwd_T]
        self.write_data_to_db(*self.pulled_data_array)
        
        #for i in pulled_data_array:
            #print(i)

        self.add_entry_data_to_field(*self.pulled_data_array)
        self.clear_entry_widgets()
        
    
    
    
    #----------------------------------------------------------------------------------------------
    def write_data_to_db(self,*args):
        """ 
        Func - takes all the arguments from the pulled entry fields and writes them to the aooprpriate 
        listbox, by splitting them amongst days
        """
        
        self.conn.execute("""INSERT INTO calllog (day, comp, cont, med, desc, fwd) VALUES (?,?,?,?,?,?)""", (args))
        self.conn.commit()
        self.db_entry_print()
        
        return    




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
        After widgets text has been pulled this function clears the widgets so there ready
        for the next entry
        """
        
        self.comp_ent.delete(0, tk.END)
        self.cont_ent.delete(0, tk.END)
        self.med_ent.delete(0, tk.END)
        self.desc_text.delete(1.0, tk.END)
        self.fwd_text.delete(1.0, tk.END)
    
        return
    
    
    #-----END--------------Functions for GUI Functionality --------------------------------------------------------------
    #####################################################################################################
    
    
    #----------------------------------------------------------------------------------------------
    def bind_enter_leave(self, c, widge):
        """
         c - catagory, either 'a' for account or 's' for selection_frames
         *new add - letter 't' for todo
         widge - widget being passed to get assigned a binding action
        """
        
        #Binding of the accoutns section
        if c == 'a':
            widge.bind('<Enter>', self.change_acc_color)
            widge.bind('<Leave>', self.change_acc_def_color)
        
        #Binding of the new entry section
        if c == 's':
            widge.bind('<Enter>', self.change_select_color)
            widge.bind('<Leave>', self.change_select_def_color)
        
        #Binding of the TO DO Section
        if c == 't':
            widge.bind('<Enter>', self.change_todo_color)
            widge.bind('<Leave>', self.change_todo_def_color)        
        
        return      
    
    
    #----------------------------------------------------------------------------------------------
    def bind_clicking_widge(self, widge):
        """ 
        widge is given bind method to call resizing function when it is clicked
        """
        
        widge.bind('<Button-1>', self.widge_enlarge_shrink)                                        #Each listbox widget will be passed to this function assigning them click event instruction
                 
        return
    
    
    
    #----------------------------------------------------------------------------------------------
    def widge_enlarge_shrink(self, event):
        """
        Func to resize the clicked listbox (enlarge) as well as the other 4 listboxes (shrink)
        """
        
        #ADD FUNCTIONALITY------\
        #make is so when widget is focused you see the text. Otherwise when small you only see the count of 
        #the widget containers entries
        
       #Dictionary storing the day in string form as keys and the listbox associated with the data cooresponding to it
        fields = {'MONDAY': self.mon_lbox,
                  'TUESDAY': self.tue_lbox,
                  'WED': self.wed_lbox,
                  'THURSDAY': self.th_lbox,
                  'FRIDAY':self.f_lbox}
        
        for k,v in fields.items():
            
            if fields[k] == event.widget:
                
                self.pull_current_acc_text(k)                     #Pull current text whether edited or not and replace with current entry. Then proceed to pull next data
                event.widget.config(height = 17)
                event.widget.master.config(fg = DGR)   
                self.widge_content_display(k)
                self.change_text_acc_lbox(k)                    #Pass along the day
                
        
            else:
                v.config(height = 2)
                v.master.config(fg = FG)

        return

    
   
    #----------------------------------------------------------------------------------------------
    def widge_content_display(self, d):
        """ 
        When one of the day of week listboxes is selected, we want to pull all the data from our database that has the same matching
        day, ex. 'MONDAY'
        """
        
        #Pull the data from the associated day
        c = self.conn.cursor()        
        c.execute("""SELECT * FROM {}""".format(d))                                   
        
        self.det_text.delete(1.0, tk.END)
        
        try:            
            for row in c.fetchall():
                print(row)
                self.det_text.insert(tk.END, row)
    
        except AttributeError as e:
            self.det_text.insert(tk.END, c.fetchone())
    
    
        #Get the count of entries for the day currently focused on
        cnt = c.execute("""SELECT COUNT(*) FROM calllog WHERE day == ?""",(d[0],))
        self.det_labelframe_2.config(text = '{} Notepad -----  Entries: {}'.format(d[0],cnt.fetchone()[0]))
        
        c.close()
        return    
    
        
    
    
    
    #----------------------------------------------------------------------------------------------
    def display_widge_shrink(self, event):
        """ 
        Func to make active text widget larger to ease users writability with app. Other text box shrinks in size to maintain
        the window size
        """
        
        widgs = [self.desc_text, self.fwd_text]         #Store the widgets
        d1 = self.desclab.grid_info()                         #Check each of there grid coordinates
        d2 = self.fwdlab.grid_info()
        chk = event.widget.grid_info()
        
        
        if d1['row'] == chk['row']:
            self.desclab.config(fg = DGR, text = 'DESC', font = 16)
            self.fwdlab.config(text = 'Forward', fg = FG, font = ('Verdana',8))
            
        else:
            self.fwdlab.config(fg = DGR,  text = 'FWD', font = 16)
            self.desclab.config(text = 'Description', fg = FG, font = ('Verdana',8))
        
        for i in widgs:
            
            if i == event.widget:
                event.widget.config(height = 8)
                
            else:
                i.config(height = 3)
                
        return
    
    
    
    #----------------------------------------------------------------------------------------------
    def pull_current_acc_text(self, d):
        """ 
        Func to take current text at time of click and add it to the DB.
        """
        
        widge_text = self.desc_text.get(1.0, tk.END)
        if len(widge_text) <= 1:
            return
        
        else:
            c = self.conn.cursor()
            c.execute("""INSERT INTO ? VALUES(?)""", (d, widge_text,))
            self.conn.commit()

        return
    
    
    
    #----------------------------------------------------------------------------------------------
    def change_text_acc_lbox(self, d):
        """ 
        d - day of the week that will correlate with the note in database (long string entry that gets added on)
        Pull the data entry and pass to the text box where users can view it or opt to press edit button and edit entry.
        After edit user can load new edoited string
        
        If user clicks to another days box --- before that switch, need func to pull whats there and replace existing. Then delete and
        fill with what day was chosen next
        """
        
        c = self.conn.cursor()
        c.execute("""SELECT * FROM notes WHERE day = ?""",(d,))
        print(d)
        
        
    
    
    ######################################################################
    """
    #Followoing functions are utilized to change the FG color of the given Label widgets for each frame section
    #The binding is based on an enter / leave combo for each of the frames. We made seperate funcs as we wanted the
    #label to change but not the label being a small widget we needed a bigger targetr to attach the bind to
    """
    #----------------------------------------------------------------------------------------------
    def change_acc_color(self, event):
        """ 
        
        """
        
        self.lab_accounts.config(fg = DGR)
        self.lab_selection.config(fg = 'white')
        self.todo_text
        
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
        """ 
        
        """
        
        self.lab_selection.config(fg = 'white')
        
        return
    
    #----------------------------------------------------------------------------------------------
    def change_todo_color(self, event):
        """ 
        
        """
        
        self.todo_lab.config(fg = DGR)
        
        return
    
    #----------------------------------------------------------------------------------------------
    def change_todo_def_color(self, event):
        """ 
        
        """
        
        self.todo_lab.config(fg = 'white')
        
        return
    
    #END OF BIND -------------------------------------------------------------------------------------------
    ######################################################################
    
    
    
    #----------------------------------------------------------------------------------------------
    def copy_highlighted_text(self, event):
        """
        Func - the widgets have been binded to this function to take all the highlighted text and copy it to
        the computers clipboard
        
        Binded to Button-2 - which is Middle Mouse Button
        """
        
        try:
            copytext = event.widget.selection_get()                                      #Pull the text that is currently selected by highlight in widget
            
            if len(copytext) <= 1:                                                                   #Check if length is too short and should warn user
                self.clipboard_warning()
                
            else:
                self.parent.clipboard_append(copytext)
                print('Succesful copy of selected text to Clipboard')
            
        except Exception:
            self.clipboard_error_warning()
        
        return
    
    
    #----------------------------------------------------------------------------------------------
    def clipboard_warning(self):
        """ 
        Func is called to warn users that it has been detected nothing was actually copied to clipboard
        """
        
        mb.showwarning(title = 'Warning', message =  'App detected its possible that\nno text was actually selected')
        
        return
    
    
    #----------------------------------------------------------------------------------------------
    def clipboard_error_warning(self):
        """ 
        Func - error message box popup to let user know there was an error attempting to copy text.        
        FORWARD - Move to a double cliick (some users may accidently right click and become a nusence.
        - or - 
        Make it a turn on or off functionality
        """
        
        mb.showerror(title = 'Error with Clipboard', message = 'No items highlighted. Please try again.\n(Text needs to be highlighted before right click is applied)')
        
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
    """ 
    Start of the app. Create a root instance of the Tkinter module and pass it to CallLog window
    """
    
    root = tk.Tk()
    CallLogWindow(root)
    root.mainloop()
