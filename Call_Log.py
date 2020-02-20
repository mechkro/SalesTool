import tkinter as tk
from tkinter import filedialog as fd
import os



    


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
