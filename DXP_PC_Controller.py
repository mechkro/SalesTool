import Tkinter as tk

"""
This is the controller file - will act as the traffic director for active and non-active windows based
upon end user.
"""


BG = '#0C1021'
FG = 'white'

def config_frame(index):

    fconfig = {'LoginWindow':(BG,FG,('system',12,'bold')),
                    'AccountsContacts':(BG,FG,('system',12,'bold')),
                    'ToDo':(BG,FG,('system',12,'bold')),
                    'CallLog':(BG,FG,('system',12,'bold')),
                    'Projects':(BG,FG,('system',12,'bold')),
                    'BidSolicits' : (BG,FG,('system',12,'bold'))
                   }
    
    return fconfig[index]


class MainStart(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        frame_foundation = tk.Frame(self)
        frame_foundation.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        frame_foundation.grid_rowconfigure(0, weight = 1)
        frame_foundation.grid_columnconfigure(0, weight = 1)

        self.window_container = {}
        for wins in (LoginWindow, AccountsContacts, ToDo, CallLog, Projects, BidSolicits):
                    window = wins(frame_foundation, self)
                    self.window_container[wins] = window
                    window.grid(row = 0, column = 0, sticky = tk.NSEW)
        
        self.show_window(LoginWindow)


    def show_window(self, logwin):
        """Recieves window to create and changes title of window"""

        window_title = {
                                LoginWindow:'Login',
                                AccountsContacts:'Acc',
                                ToDo:'ToDo',
                                CallLog:'CallLog',
                                Projects:'Projects',
                                BidSolicits:'Bids'
                                }
        
        self.title(window_title[logwin])
        frame = self.window_container[logwin]
        frame.tkraise()



class LoginWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        conf = config_frame('LoginWindow')
        self.config(bg = conf[0])
        
        label = tk.Label(self, text = 'Login')
       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts))
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo))
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog))
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects))
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits))

        for x,i in enumerate((label, b_1,b_2,b_3,b_4,b_5)):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5)
            


class AccountsContacts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        conf = config_frame('AccountsContacts')
        self.config(bg = conf[0])
        
        label = tk.Label(self, text = 'Accounts & Contacts')
       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts))
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo))
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog))
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects))
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits))

        for x,i in enumerate((label, b_1,b_2,b_3,b_4,b_5)):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5)


class ToDo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        conf = config_frame('ToDo')
        self.config(bg = conf[0])
        
        label = tk.Label(self, text = 'To Dos')
       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts))
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo))
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog))
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects))
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits))

        for x,i in enumerate((label, b_1,b_2,b_3,b_4,b_5)):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5)


class CallLog(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        conf = config_frame('CallLog')
        self.config(bg = conf[0])
        
        label = tk.Label(self, text = 'Call Logs')
       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts))
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo))
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog))
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects))
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits))

        for x,i in enumerate((label, b_1,b_2,b_3,b_4,b_5)):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5)


class Projects(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        conf = config_frame('Projects')
        self.config(bg = conf[0])
        
        label = tk.Label(self, text = 'Projects')
       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts))
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo))
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog))
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects))
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits))

        for x,i in enumerate((label, b_1,b_2,b_3,b_4,b_5)):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5)


class BidSolicits(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        conf = config_frame('BidSolicits')
        self.config(bg = conf[0])
        
        label = tk.Label(self, text = 'BidSolicits')
       
        b_1 = tk.Button(self, text = 'Accounts/Contacts', command  = lambda: controller.show_window(AccountsContacts))
        b_2 = tk.Button(self, text = 'ToDo', command  = lambda: controller.show_window(ToDo))
        b_3 = tk.Button(self, text = 'CallLog', command  = lambda: controller.show_window(CallLog))
        b_4 = tk.Button(self, text = 'Projects', command  = lambda: controller.show_window(Projects))
        b_5 = tk.Button(self, text = 'BidSolicits', command  = lambda: controller.show_window(BidSolicits))

        for x,i in enumerate((label, b_1,b_2,b_3,b_4,b_5)):
            i.config(bg = conf[0], fg = conf[1], font = conf[2])
            i.grid(row = x+1, column = 0,  padx = 5, pady = 5)








        
if __name__ == '__main__':
    app = MainStart()
    app.mainloop()
