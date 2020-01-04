from Tkinter import *
from tkColorChooser import askcolor



def change_bg_color(master = None):
    '''Returns tuple set of values, tuple[0] is RGB, tuple[-1] is #Hex'''
    backcolor = askcolor(title = 'Choose Background Color', parent = master)
    return backcolor


def change_fg_color(master = None):
    '''Returns tuple set of values, tuple[0] is RGB, tuple[-1] is #Hex'''
    forecolor = askcolor(title = 'Choose Foreground Color', parent = master)
    return forecolor



class Main(object):
    def __init__(self, parent):
        self.parent = parent
        self.button = Button(self.parent, text = 'change color',
                             command = lambda: self.change_color(self.parent))
        self.button.grid(padx = 10, pady = 10)

        self.label = Label(self.parent, text = "No Color")
        self.label.grid(padx = 5, pady = 5)



    def change_color(self, win):
        BG = askcolor(title = 'Choose Background Color', parent  = win)
        FG =  askcolor(title = 'Choose Foreground Color', parent  = win)
        print BG[0], BG[-1]
        print FG[0], FG[-1]
        win.config(bg = BG[-1])
        self.button.config(bg = BG[-1], fg = FG[-1])
        newlab = 'BG = {}, {}\nFG = {}, {}'.format(str(BG[0]),str(BG[-1]), str(FG[0]),str(FG[-1]))
        self.label.config(text = newlab, bg = BG[-1], fg = FG[-1])
        return


if __name__ == '__main__':
    root = Tk()
    Main(root)
    root.mainloop()
