import tkinter as tk

BG = '#0C1021'
FG = 'white'


class Test:

    w_active = None
    
    def __init__(self, parent, *args, **kwargs):
        
        self.f = tk.Frame(parent, bg = BG)
        self.f.grid()

        self.l = tk.Label(self.f, text = 'None Selected', bg = BG, fg = FG)
        self.l.grid(row = 0, column= 0, columnspan = 2, sticky = tk.EW)

        self.lbox1 = tk.Listbox(self.f, bg = BG, fg = FG, width = 25, height = 5)
        self.lbox1.grid(row = 1, column = 0, padx= 10, pady = 5)

        self.lbox2 = tk.Listbox(self.f, bg = BG, fg = FG, width = 25, height = 5)
        self.lbox2.grid(row = 2, column = 0, padx= 10, pady = 5)

        self.lbox3 = tk.Listbox(self.f, bg = BG, fg = FG, width = 25, height = 5)
        self.lbox3.grid(row = 3, column = 0, padx= 10, pady = 5)

        self.lbox4 = tk.Listbox(self.f, bg = BG, fg = FG, width = 25, height = 5)
        self.lbox4.grid(row = 4, column = 0, padx= 10, pady = 5)

        self.lbox1.bind('<Button-1>', self.mark_active)
        self.lbox2.bind('<Button-1>', self.mark_active)

        self.lbox3.bind('<Button-1>', self.mark_active)
        self.lbox4.bind('<Button-1>', self.mark_active)
        
        self.txt = tk.Text(self.f, bg = BG, fg = FG)
        self.txt.grid(row = 1, rowspan = 3, column = 1, padx = 10, pady = 10)

        self.but = tk.Button(self.f, text = 'Run', bg = BG, fg = FG,
                             command = self.pandstore)
        self.but.grid(row = 4, column = 1, padx = 10, pady = 10)

        self.set_def_active()



    def set_def_active(self):
        Test.w_active = self.lbox1
        return


    def mark_active(self, event):
        
        Test.w_active = event.widget
        self.l.config(text = '{} Selected'.format(str(Test.w_active)))
        self.test_if_active()

    


    def test_if_active(self):
        
        if Test.w_active:
            self.pandstore()
        else:
            print('Listbox not selected')
    

    def pandstore(self):
        
        t = self.txt.get(1.0, tk.END)
        self.txt.delete(1.0, tk.END)
        Test.w_active.insert(tk.END, t)
        
        print(t)

        return


##    def change_active(self, k):
##
##        holdr = {'Mon':self.lbox1,
##                 'Tue':self.lbox2}
##        
##        wa = [k for k,v in holdr.items() if v != Test.w_active]
##        Test.w_active = wa[0]
##
##        return
        
            

        

        



if __name__ == '__main__':

    root = tk.Tk()
    Test(root)
    root.mainloop()
