#Create hiracchical treeview Application  
from Tkinter import *  
import ttk
import sqlite3 as sql
import random
import calendar as cal
import datetime as dt
import time



def add_table(cur,curent):
    cur.execute('INSERT INTO test (state, compname, date) VALUES (?,?,?)',(curent))
    cur.commit()
    

def db_entry(cur):
    tempcont = []
    for i in range(100):        
        states = random.choice(['AZ','NV','NM'])
        cn = random.choice(['Envirogen', 'CCWRD', 'LVWWD', 'Frito-Lay'])
        d = cal.Calendar(0)
        h = d.monthdatescalendar(2019,12)[random.randint(0,3)]
        dat = random.choice(h)
        curent = (states,cn,dat)
        add_table(cur,curent)
        tempcont.append(curent)
    return tempcont

    
def db_init():
    global cur
    cur = sql.connect(':memory:')
    cur.execute('CREATE TABLE IF NOT EXISTS test (state TEXT, compname TEXT, date TEXT)')
    cur.commit()

    getents = db_entry(cur)
    return getents


app=Tk()  
#App Title  
app.title("DXP Pump Commander - Treeview Test")
app.config(bg = 'gray')
#Lable

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('system', 8), background = 'gray', foreground = 'black', cursor = 'hand2') # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('system', 9,'bold')) # Modify the font of the headings
style.configure("mystyle.Label", background ='gray', foreground = 'black')

'''
https://stackoverflow.com/questions/42708050/tkinter-treeview-heading-styling

You are on the right track but need to change the border element rather than the cell element. As you are working on Windows,
the treeview cells are being displayed using a system provided theme element from the Visual Styles API. In this case it is a
HP_HEADERITEM part from the HEADER class. As this is drawn by the system theme engine you don't get to customise it from
Tk aside from selecting alternate looks according to the state.

If you must customise the look of the header then you have to replace the theme part with one that Tk can customise and the
default theme is a good choice. I would also recommend that you define this as a custom style so that you can re-style
specific widgets and not necessarily all of them.

style = ttk.Style()
style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky':'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky':'nswe', 'children': [
            ("Custom.Treeheading.image", {'side':'right', 'sticky':''}),
            ("Custom.Treeheading.text", {'sticky':'we'})
        ]})
    ]}),
])

style.configure("Custom.Treeview.Heading",
    background="blue", foreground="white", relief="flat")
style.map("Custom.Treeview.Heading",
    relief=[('active','groove'),('pressed','sunken')])
What we are doing is defining a new widget style using the same layout as for the standard treeview style and replacing the
border element. While we have not defined the other custom elements, these are looked up hierarchically so in the absence
of a Custom.Treeheading.text it will use a Treeheading.text. To use this, we set the style of the treeview widget:

t=ttk.Treeview(_frame, style="Custom.Treeview")

'''


style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


'''
SOURCE : https://riptutorial.com/tkinter/example/31885/customize-a-treeview

Then, the widget is created giving the above style:

tree=ttk.Treeview(master,style="mystyle.Treeview")
If you would like to have a different format depending on the rows, you can make use of tags:

tree.insert(folder1, "end", "", text="photo1.png", values=("23-Jun-17 11:28","PNG file","2.6 KB"),tags = ('odd',))
tree.insert(folder1, "end", "", text="photo2.png", values=("23-Jun-17 11:29","PNG file","3.2 KB"),tags = ('even',))
tree.insert(folder1, "end", "", text="photo3.png", values=("23-Jun-17 11:30","PNG file","3.1 KB"),tags = ('odd',))
Then, for instance, a background color can be associated to the tags:

tree.tag_configure('odd', background='#E8E8E8')
tree.tag_configure('even', background='#DFDFDF')
The result is a treeview with modified fonts on both the body and headings, no border and different colors for the rows:
'''

ttk.Label(app, text="Accounts/Contacts", style = "mystyle.Label").pack(pady = 5)
#Treeview
#tree = Treeview(root, columns = ('col1', 'col2', 'col3',.. 'colnth'))
#tree['columns'] =  ('col1', 'col2', 'col3',.. 'colnth')
#Edit columns ----
#tree.column('col1', width = 100, anchor = 'center')
#tree.heading('col1', text = 'Column 1')   #text = is what will show for column label
treeview=ttk.Treeview(app, columns = ('c1','c2','c3','c4','c5','c6','c7'), style="mystyle.Treeview")
treeview['columns'] = ('c1','c2','c3','c4','c5','c6','c7')
treeview.heading('c1', text = 'State')
treeview.heading('c2', text = 'Comp. Name')
treeview.heading('c3', text = 'Date Last')
treeview.heading('c4', text = 'File Location')
treeview.heading('c5', text = 'Industry')
treeview.heading('c6', text = 'Manf.')
treeview.heading('c7', text = 'Address')

treeview.column('c1', width = 55, anchor = 'center')
treeview.column('c2', width = 100, anchor = 'center')
treeview.column('c3', width = 100, anchor = 'center')
treeview.column('c4', width = 125, anchor = 'center')
treeview.column('c5', width = 125, anchor = 'center')
treeview.column('c6', width = 125, anchor = 'center')


treeview.pack(padx = 5, pady = 5)

#Treeview items
# .insert(parent, index, iid=None, **kw)
# Parent leave blank if new toplevel treeview item wanted
# If not put iid value in parent to place item under it

#If were loading up accounts:
# Each parent ID will be blank or "STATE" value
# Each iid will be SQL id? and text == Company name?

'''When trying SQLlite inquiry look into RowFactory type
output to make easy plug and play with treeview --'''

##treeview.insert('','0','item1',text='Parent tree')  
##treeview.insert('','1','item2',text='1st Child')  
##treeview.insert('','end','item3',text='2nd Child')  
##treeview.insert('item2','end','A',text='A') 
##treeview.insert('item2','end','B',text='B')  
##treeview.insert('item2','end','C',text='C')  
##treeview.insert('item3','end','D',text='D')  
##treeview.insert('item3','end','E',text='E')  
##treeview.insert('item3','end','F',text='F')  
##treeview.move('item2','item1','end')  
##treeview.move('item3','item1','end')
treeview.insert('','0','AZ',text='Arizona')
treeview.insert('','1','NV',text='Nevada')  
treeview.insert('','2','NM',text='New Mexico')





def toplabel(vars):
    tl = Toplevel(bg = 'gray')
    lab = Label(tl, bg = 'gray', fg = 'black', font = ('system', 12, 'bold'))
    lab.pack(padx = 10, pady = 10)
    labtxt = """
                State = {}
                Company = {}
                Date Last = {}
                
                """.format(vars[0],vars[1],vars[2])
    lab.config(text = labtxt)
    tl.mainloop()



def OnDoubleClick(event):
    item = treeview.identify('item',event.x,event.y)
    if treeview.item(item,"text"):
        print "you clicked on:\n"
        print treeview.item(item,"text")

    else:
        item = treeview.identify('item',event.x,event.y)
        print "you clicked on:\n"
        seltup = treeview.item(item,"values")
        toplabel(seltup)
        
##    print "you clicked on:\n"
##    print treeview.item(item,"text")
##    c = cur.cursor()
##    z = c.execute("""SELECT * FROM test WHERE compname = ?""",(treeview.item(item,"text"),))
##    xx = dt.datetime.today()
##    for row in z.fetchall():
##        s = str(row[0])
##        c = str(row[1])
##        d = str(row[2])
##        sd = dt.datetime.strptime(d, '%Y-%m-%d')
##        print s,c,d
##        print 'Been {} days since ----'.format((xx-sd).days)

        #if (xx-sd).days >= 25:
            #print 'ATTENTION!!!!'
            #time.sleep(2)
        

    
treeview.bind("<Double-1>", OnDoubleClick)


def rest_of_ents():
    for i in ['AZ','NV','NM']:
        c = cur.cursor()
        z = c.execute("""SELECT * FROM test WHERE state = ?""", (i,))
        for row in z.fetchall():
            s = str(row[0])
            c = str(row[1])
            d = str(row[2])
            if s == 'AZ':
                treeview.insert('AZ', 'end',values = (s,c,d,' ',' ' ,' ' ,' '))
            if s == 'NV':
                treeview.insert('NV','end','',values = (s,c,d,' ' ,' ' ,' ' ,' '))
            if s == 'NM':
                treeview.insert('NM','end','',values = (s,c,d,' ',' ' ,' ' ,' '))
            


x = db_init()
#[('NV', 'LVWWD', datetime.date(2019, 11, 25)), ('NV', 'CCWRD', datetime.date(2019, 11, 25)),
#('NM', 'Envirogen', datetime.date(2019, 11, 28)), ('NM', 'CCWRD', datetime.date(2019, 11, 25)), ('NV', 'Frito-Lay', datetime.date(2019, 11, 29))]


##for i in x:
##    treeview.insert(i[0],'end','',text=i[1])

rest_of_ents()



#Calling Main()  
app.mainloop()










"""

treeview=ttk.Treeview(app, columns = ('State', 'Company Name', 'Industry'), style="mystyle.Treeview")
treeview['columns'] = ('State', 'Company Name', 'Date Last')
treeview.heading('State', text = 'State')
treeview.heading('Company Name', text = 'Company Name')
treeview.heading('Date Last', text = 'Date Last')
treeview.pack(padx = 5, pady = 5)

treeview.insert('','0','AZ',text='Arizona')
treeview.insert('','1','NV',text='Nevada')  
treeview.insert('','2','NM',text='New Mexico')

f s == 'AZ':
    treeview.insert('AZ', 'end',values = (s,c,d))
if s == 'NV':
    treeview.insert('NV','end','',values = (s,c,d))
if s == 'NM':
    treeview.insert('NM','end','',values = (s,c,d))


"""
