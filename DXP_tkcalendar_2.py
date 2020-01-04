import Tkinter as tk
import collections as clc
import calendar
import datetime as dt
import itertools as itools
import ttk



def return_date_data(yr, weekstrt = None):
    '''Func to provide datetime objects and iters of days repping the year
            - wkstrt is default to 6 (Sunday)
            - yr is the year to have outputted data from
    '''
    if weekstrt:
        cal_obj = calendar.Calendar(wkstrt)                                                  #Setting weekstart day to user defined
    else:
        cal_obj = calendar.Calendar(6)                                                         #Setting Sunday to beginning of the week (matches windows calendar)
        
    cal_obj_dates = cal_obj.yeardatescalendar(2019)                                   #Getting all the days of the year in datetime objects
    cal_obj_tupdays = cal_obj.yeardays2calendar(2019)                               #Getting tuple iteration of the year in days(rep by #'s 0-6)
    cal_obj_just_days = cal_obj.yeardayscalendar(2019)                              #just rep's the year in order of weekday #'s (0 - 6)

    #Breaking down the output by quarter - make call to funcs
    obj_dates = return_cal_obj_dates(cal_obj_dates)
    obj_tupdays = return_cal_obj_dates(cal_obj_dates)
    obj_just_days = return_cal_obj_dates(cal_obj_dates)

    return (obj_dates, obj_tupdays, obj_just_days)
    

#Functions to breakdown of the objects into respective months ---------------------------------------------
def return_cal_obj_dates(itr_container):
    ''' '''
    q1_dates,q2_dates,q3_dates,q4_dates = [i for i in itr_container]
    
    #Breaking down the quarters by month
    jan_dates, feb_dates, mar_dates = [i for i in q1_dates]
    apr_dates, may_dates, jun_dates = [i for i in q2_dates]
    jul_dates, aug_dates, sep_dates = [i for i in q3_dates]
    oct_dates, nov_dates, dec_dates = [i for i in q4_dates]

    return (jan_dates, feb_dates, mar_dates,apr_dates, may_dates, jun_dates, jul_dates, aug_dates, sep_dates, oct_dates, nov_dates, dec_dates)

def return_cal_obj_tupdays(itr_container):
    ''' '''
    q1_tups,q2_tups,q3_tups,q4_tups = [i for i in itr_container]
    
    jan_dates, feb_dates, mar_dates = [i for i in q1_tups]
    apr_dates, may_dates, jun_dates = [i for i in q2_tups]
    jul_dates, aug_dates, sep_dates = [i for i in q3_tups]
    oct_dates, nov_dates, dec_dates = [i for i in q4_tups]

    return (jan_dates, feb_dates, mar_dates,apr_dates, may_dates, jun_dates, jul_dates, aug_dates, sep_dates, oct_dates, nov_dates, dec_dates)

def return_cal_obj_jdays(itr_container):
    ''' '''
    q1_jdays,q2_jdays,q3_jdays,q4_jdays = [i for i in itr_container]    

    jan_jdays, feb_jdays, mar_jdays = [i for i in q1_jdays]
    apr_jdays, may_jdays, jun_jdays = [i for i in q2_jdays]
    jul_jdays, aug__jdays, sep_jdays = [i for i in q3_jdays]
    oct_jdays, nov__jdays, dec_jdays = [i for i in q4_jdays]

    return (jan_dates, feb_dates, mar_dates,apr_dates, may_dates, jun_dates, jul_dates, aug_dates, sep_dates, oct_dates, nov_dates, dec_dates)




class MakeCal(tk.Frame):

    default_bg = None
    default_fg = None
    
    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.frame = tk.Frame(parent)
        self.frame.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.frame_nb = tk.Frame(parent)
        self.frame_nb.grid(row = 0, column = 1, padx = 5, pady = 5)
        
        self.layout = self.check_current_month_layout()
        self.make_notebook_widget()
        self.make_day_buttons()
        self.make_view_widget()

    def make_notebook_widget(self):

        self.nb = ttk.Notebook(self.frame_nb)
        #self.wid.append(self.nb)
        self.nb.grid(padx = 5, pady = 5)

        self.page1 = ttk.Frame(self.nb)
        #self.wid.append(self.page1)
        #self.detail_labframe = tk.LabelFrame(self.page1, text = 'Date Selected - Details Window') #bg = BG, fg = FG, font = ('system', 8), width = 500, height = 250)
        #self.detail_labframe.grid(row = 0, padx = 5, pady = 5)

        #self.wid.append(self.detail_labframe)
        self.datedetails = tk.Text(self.page1)            #detail_labframe) #bg = BG, fg = FG, insertbackground = 'white', font = ('system',6))
        self.datedetails.grid(padx = 5, pady = 5)                  

        #self.wid.append(self.datedetails)

        self.page2= ttk.Frame(self.nb)
        #self.wid.append(self.page2)

        self.page3= ttk.Frame(self.nb)
        #self.wid.append(self.page3)

        self.page4= ttk.Frame(self.nb)
        #self.wid.append(self.page4)

        self.page5= ttk.Frame(self.nb)
        #self.wid.append(self.page5)

        self.page6 = ttk.Frame(self.nb)
        #self.wid.append(self.page6)

        self.page7 = ttk.Frame(self.nb)
        #self.wid.append(self.page7)

        self.page8 = ttk.Frame(self.nb)
        #self.wid.append(self.page8)
        
        self.nb.add(self.page1, text = "Date Selected")
        self.nb.add(self.page2, text = "To Do's")
        self.nb.add(self.page3, text = "Accounts")
        self.nb.add(self.page4, text = "Call Log")
        self.nb.add(self.page5, text = "Treeview")
        self.nb.add(self.page6, text = "Projects")
        self.nb.add(self.page7, text = "Reminders")
        self.nb.add(self.page8, text = "Email")

    def check_current_month_layout(self):
        today = dt.date.today()
        today_str = dt.datetime.strftime(today, '%Y,%m,%d').split(',')
        date_init = calendar.month(int(today_str[0]), int(today_str[1]))
        dsplit = date_init.split('\n')

        self.but_lab_contain = clc.OrderedDict()
        
        lab = tk.Label(self.frame, text = '{}'.format(dsplit[0]),  font = ("system", 6, "bold"))
        lab.grid(row = 0, column = 1, columnspan = 5)
        but_prev = tk.Button(self.frame, text = '<-',  font = ("system", 6, "bold"))
        but_prev.grid(row = 0, column = 0)
        but_next = tk.Button(self.frame, text = '->',  font = ("system", 6, "bold"))
        but_next.grid(row = 0, column = 6)

        #Bindings and events
        but_prev.bind('<Enter>', self.widge_enter_color_edit)
        but_prev.bind('<Leave>', self.widge_leave_color_edit)
        #FIX ------ but_prev.bind('<Button-1>', self.prev_month)
        but_next.bind('<Enter>', self.widge_enter_color_edit)
        but_next.bind('<Leave>', self.widge_leave_color_edit)
        #FIX ------- but_prev.bind('<Button-1>', self.next_month)

        #Establsih default program color
        MakeCal.default_bg = lab.cget('bg')
        MakeCal.default_bg = lab.cget('fg')
        
        self.but_lab_contain['<-'] = but_prev
        self.but_lab_contain['lab'] = lab
        self.but_lab_contain['->'] = but_next
        
        day_split = dsplit[1].split(' ')
        self.make_day_labels(*day_split)

    def make_day_labels(self, *args):
        self.daylab_contain = clc.OrderedDict()
        row_id = 1
        column_id = 0
        for j,i in enumerate(args):
            lab = tk.Label(self.frame, text = '|{}|'.format(i), fg = 'blue')
            lab.grid(row = row_id, column = column_id)
            self.daylab_contain[str(j)] = lab
            column_id += 1
    

    def make_day_buttons(self):
        '''Need 7 Day label buttons and 6 rows of week buttons x7 ea row == 42'''
        self.row_id_contain = clc.OrderedDict()

        row_itr = 2
        column_itr = 0
        
        for i in range(1,43):
            b = tk.Button(self.frame, text = '{}'.format(i), width = 2,  font = ("system", 6, "bold"))
            b.grid(row = row_itr, column = column_itr)

            #Bindings and events
            b.bind('<Enter>', self.widge_enter_color_edit)
            b.bind('<Leave>', self.widge_leave_color_edit)
            
            self.row_id_contain[str(i)] = b
            column_itr += 1
            if column_itr >= 7:
                column_itr = 0
                row_itr += 1

    def widge_enter_color_edit(self, event):
        event.widget.config(fg = 'red')        


    def widge_leave_color_edit(self, event):
        event.widget.config(fg = 'black')


    def make_view_widget(self):
        pass
        #self.text = tk.Text(self.frame, font = ("system", 6, "bold"), width = 60, height =5)
        #self.text.grid(row = 0, rowspan = 7, column = 8, padx =5, pady = 5)

       


if __name__ ==  '__main__':
    root = tk.Tk()
    MakeCal(root)
    root.mainloop()



        

    
###INITIALIZE VALUES TO BE USED IN LOOP BELOW
##year_2019 = return_date_data(2019)
##tod = dt.date.today()
##date_times, yr_tups, yr_jdays = [i for i in year_2019]
##months = list('January Febuary March April May June July August September October November December'.split(' '))
##
##for x,y in enumerate(date_times):
##    print '\n\n--------- Month {} ----------\n\n'.format(months[x])
##    j = yr_tups[x]
##    for a,b in enumerate(y):
##        print 'Week {}:'.format(a)
##        for v in b:
##            jj = j[a]
##            temp = dt.datetime.strftime(v, '%Y,%m,%d').split(',')
##            if temp[0] == '2018' or temp[0] == '2020':
##                pass
##            else:
##                print '{} --- day of week:'.format(temp)
##                diffdays = (tod - v).days
##                print 'Difference in days: {}'.format(diffdays)
            

        


    


    

    
    

##currentdate = dt.datetime.today()
##currentdate_str = dt.datetime.strftime(currentdate, '%Y,%m,%d').split(',')
##current_year = currentdate_str[0]
##
##
###cal_obj_dates, days are length of 4 ---- Broken into quarters
##cal_obj = calendar.Calendar(6)                                               #Setting Sunday to beginning of the week (matches windows calendar)     
##cal_obj_dates = cal_obj.yeardatescalendar(2019,1)                     #Getting all the days of the year in datetime objects
##cal_obj_days = cal_obj.yeardays2calendar(2019,width =1)                      #Getting tuple iteration of the year in days(rep by #'s 0-6)
##caldays = cal_obj.yeardayscalendar(2019)
##
##print cal_obj_dates
##print cal_obj_days
##print caldays







##def return_cals(y,m):
##    itr = 0
##    weekout = calendar.monthcalendar(y,m)
##    dys = ('mon','tue','wed','thu','fri','sat','sun')
##    for j in weekout:
##        for i,x in enumerate(j):
##            if x == 0:
##                pass
##            else:
##                itr+=1
##                #print "{} : {}".format(dys[i], x)
##    return itr
##
##
##k = 0
##for j in range(1,13):
##    k += return_cals(2019,j)
###print k
##
##
##
##root = tk.Tk()
##frame = tk.Frame(root)
##frame.grid(row = 0, column = 0, padx = 5, pady = 5)
##frame2 = tk.Frame(root)
##frame2.grid(row = 0, column = 1, padx = 5, pady = 5)
##
##
##txt_lf = tk.LabelFrame(frame2, text = 'Current Date -- Entity View')
##txt_lf.grid(row = 0 , column = 0, padx = 5, pady = 5)
##
##calendar.setfirstweekday(6)             #Make week start on sunday to match microsoft windows calendar
##p = calendar.calendar(2020)
##today = dt.datetime.today()
##x = dt.datetime.strftime(today, '%Y,%m,%d')
##y,m,d = x.split(',')
##
##def return_week_outlook(y,m):
##    a = clc.OrderedDict()
##    weeks = ['WEEK 1','WEEK 2','WEEK 3','WEEK 4','WEEK 5']
##    try:
##        for i,j in enumerate(calendar.monthcalendar(int(y), int(m))):
##            a[weeks[i]] = j
##        print a.items()
##    except IndexError:
##        print m
##
##    days = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
##    f = itools.chain(*[i for i in a.values()])
##    d = itools.izip_longest(*[i for i in a.values()])
##    print '------- Year {} Month {} ----------'.format(y,calendar.month_name(y,m))
##    for r,unit in enumerate(d):
##        for u,k in enumerate(unit):
##            print 'Unit(h) {}'.format(unit[u])
##        print 'Unit {}'.format(unit)
##
##
##yrs = [i for i in range(2019,2022)]
##m = [i for i in range(1,13)]
##master_cont = clc.OrderedDict()
##
##for i in yrs:
##    for h in m:
##        return_week_outlook(i,h)





    





##place_dict = clc.OrderedDict({'sunday':0,
##               'monday': 1,
##               'tueday': 2,
##               'wednesday': 3,
##               'thursday': 4,
##               'friday': 5,
##               'saturday': 6})
##
##widges = clc.OrderedDict()
##
##
##
##def reload_widge(wx,wy):
##    global root, frame, widges
##    print wx, wy
##    try:
##        widges['{},{}'.format(wx,wy)].configure(fg = 'red')
##    except Exception as e:
##        print e
##
##
##
##def return_order(y,*m):
##    d = clc.OrderedDict()
##    #ntup = clc.namedtuple(list, [)
##    for x in m:
##        weekout = calendar.monthcalendar(y,x)
##        for j in weekout:
##            daYs = [('mon,{}'.format(x), j[0]),
##                    ('tue,{}'.format(x),j[1]),
##                    ('wed,{}'.format(x), j[2]),
##                    ('thu,{}'.format(x),j[3]),
##                    ('fri,{}'.format(x), j[4]),
##                    ('sat,{}'.format(x),j[5]),
##                    ('sun,{}'.format(x), j[6])]
##            for k,v in daYs:
##                d.setdefault(k, []).append(v)
##    return d
##            
##            
##            
##
##widges = clc.OrderedDict()
##
##
###print place_dict
##itr = 0
##
##
##
##
##
##
##year = 2019
##res = return_order(year, *range(1,13))
##cont = []
##d =  clc.OrderedDict()
##for k,v in res.items():
##    d.setdefault(k.split(',')[-1], []).append(v)
##
##    
##print d['1'][0], '\n'
##
##for k,v in d.items():
##    print 'Month: {}'.format(k)
##    print 'Monday:  {}'.format(v[0])
##    print 'Tues: {}'.format(v[1])
##    print 'Wed: {}'.format(v[2])
##    print 'Thur: {}'.format(v[3])
##    print 'Fri: {}'.format(v[4])
##    print 'Sat: {}'.format(v[5])
##    print 'Sun: {}'.format(v[6])
##
##
##
##widge_container = clc.OrderedDict()
##itr = 0
##
###CREATING TEXT BOX
##txt = tk.Text(txt_lf, height = 9)
##txt.grid(padx = 3, pady = 3)
##
##
##root.title('January 2019')
##
##
###CREATING BUTTONS
##buttonRows = [i[:3].upper() for i in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']]
##
##left = tk.Button(frame, text='<', width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = None)
##left.grid(row=0, column=0)
##widge_container[str(itr)] = left
##itr+=1
##
##header = tk.Label(frame,  text = 'January 2019', cursor = 'hand2',font = ('Verdana',8,'bold'), command = None)
##header.grid(row=0, column=1, columnspan=5)
##widge_container[str(itr)] = header
##itr+=1
## 
##right = tk.Button(frame, text='>',width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = lambda: change_month(root,frame, '2'))
##right.grid(row=0, column=6)
##widge_container[str(itr)] = right
##itr+=1
##
##
##
##
##
##def print_numb(event):
##    global header, frame
##    try:
##        inp = event.widget.cget('text')
##        comb = '{} : Day Selected --- {}\n'.format(header.cget('text'),inp)
##        txt.insert(tk.END, comb)
##        txt.insert(tk.END, '---------------------------------\n')
##    except (Exception, tk.EXCEPTION) as e:
##        print e
##
##
##def change_month(parent, w, m):
##    w.destroy()
##    frame = tk.Frame(parent)
##    frame.grid(row = 0, column = 0, padx = 5, pady = 5)
##
##    widge_container = clc.OrderedDict()
##    itr = 0
##    
##    #CREATING BUTTONS
##    buttonRows = [i[:3].upper() for i in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']]
##
##    left = tk.Button(frame, text='<', width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = None)
##    left.grid(row=0, column=0)
##    widge_container[str(itr)] = left
##    itr+=1
##
##    header = tk.Label(frame,  text = 'January 2019', cursor = 'hand2',font = ('Verdana',8,'bold'), command = None)
##    header.grid(row=0, column=1, columnspan=5)
##    widge_container[str(itr)] = header
##    itr+=1
##     
##    right = tk.Button(frame, text='>',width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = lambda: change_month(root,frame, '2'))
##    right.grid(row=0, column=6)
##    widge_container[str(itr)] = right
##    itr+=1
##
##    for i,j in enumerate(buttonRows):
##        widge_container[str(itr)] = tk.Button(frame, text=j, width =5, cursor = 'hand2', bg = 'yellow', font = ('Verdana',8,'bold'), command = None, state = tk.DISABLED)
##        widge_container[str(itr)].grid(row=1, column=i)
##        widge_container[str(itr)].bind('<Button-1>', print_numb)
##        itr+=1
##
##    for i,j in enumerate(d['1']):
##        print 'Month {}'.format(i)
##        for h,u in enumerate(j):
##            if int(u) == 0:
##                widge_container[str(itr)] = tk.Button(frame, text='-', width=5, command = None, state = tk.DISABLED, font = ('Verdana',8,'bold'))
##                widge_container[str(itr)].grid(row=h+2, column=i)
##                widge_container[str(itr)].bind('<Button-1>', print_numb)
##                itr+=1
##            else:
##                widge_container[str(itr)] = tk.Button(frame, text=u, width=5, font = ('Verdana',8,'bold'), cursor = 'hand2',
##                                     command = None)
##                widge_container[str(itr)].grid(row=h+2, column=i)
##                widge_container[str(itr)].bind('<Button-1>', print_numb)
##                itr+=1
##
##
##
##                
##
##for i,j in enumerate(buttonRows):
##    widge_container[str(itr)] = tk.Button(frame, text=j, width =5, cursor = 'hand2', bg = 'yellow', font = ('Verdana',8,'bold'), command = None, state = tk.DISABLED)
##    widge_container[str(itr)].grid(row=1, column=i)
##    widge_container[str(itr)].bind('<Button-1>', print_numb)
##    itr+=1
##
##for i,j in enumerate(d['1']):
##    print 'Month {}'.format(i)
##    for h,u in enumerate(j):
##        if int(u) == 0:
##            widge_container[str(itr)] = tk.Button(frame, text='-', width=5, command = None, state = tk.DISABLED, font = ('Verdana',8,'bold'))
##            widge_container[str(itr)].grid(row=h+2, column=i)
##            widge_container[str(itr)].bind('<Button-1>', print_numb)
##            itr+=1
##        else:
##            widge_container[str(itr)] = tk.Button(frame, text=u, width=5, font = ('Verdana',8,'bold'), cursor = 'hand2',
##                                 command = None)
##            widge_container[str(itr)].grid(row=h+2, column=i)
##            widge_container[str(itr)].bind('<Button-1>', print_numb)
##            itr+=1
##
##
##
##
##left.bind('<Button-1>', None)
##right.bind('<Button-1>', None)place_dict = clc.OrderedDict({'sunday':0,
##               'monday': 1,
##               'tueday': 2,
##               'wednesday': 3,
##               'thursday': 4,
##               'friday': 5,
##               'saturday': 6})
##
##widges = clc.OrderedDict()
##
##
##
##def reload_widge(wx,wy):
##    global root, frame, widges
##    print wx, wy
##    try:
##        widges['{},{}'.format(wx,wy)].configure(fg = 'red')
##    except Exception as e:
##        print e
##
##
##
##def return_order(y,*m):
##    d = clc.OrderedDict()
##    #ntup = clc.namedtuple(list, [)
##    for x in m:
##        weekout = calendar.monthcalendar(y,x)
##        for j in weekout:
##            daYs = [('mon,{}'.format(x), j[0]),
##                    ('tue,{}'.format(x),j[1]),
##                    ('wed,{}'.format(x), j[2]),
##                    ('thu,{}'.format(x),j[3]),
##                    ('fri,{}'.format(x), j[4]),
##                    ('sat,{}'.format(x),j[5]),
##                    ('sun,{}'.format(x), j[6])]
##            for k,v in daYs:
##                d.setdefault(k, []).append(v)
##    return d
##            
##            
##            
##
##widges = clc.OrderedDict()
##
##
###print place_dict
##itr = 0
##
##
##
##
##
##
##year = 2019
##res = return_order(year, *range(1,13))
##cont = []
##d =  clc.OrderedDict()
##for k,v in res.items():
##    d.setdefault(k.split(',')[-1], []).append(v)
##
##    
##print d['1'][0], '\n'
##
##for k,v in d.items():
##    print 'Month: {}'.format(k)
##    print 'Monday:  {}'.format(v[0])
##    print 'Tues: {}'.format(v[1])
##    print 'Wed: {}'.format(v[2])
##    print 'Thur: {}'.format(v[3])
##    print 'Fri: {}'.format(v[4])
##    print 'Sat: {}'.format(v[5])
##    print 'Sun: {}'.format(v[6])
##
##
##
##widge_container = clc.OrderedDict()
##itr = 0
##
###CREATING TEXT BOX
##txt = tk.Text(txt_lf, height = 9)
##txt.grid(padx = 3, pady = 3)
##
##
##root.title('January 2019')
##
##
###CREATING BUTTONS
##buttonRows = [i[:3].upper() for i in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']]
##
##left = tk.Button(frame, text='<', width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = None)
##left.grid(row=0, column=0)
##widge_container[str(itr)] = left
##itr+=1
##
##header = tk.Label(frame,  text = 'January 2019', cursor = 'hand2',font = ('Verdana',8,'bold'), command = None)
##header.grid(row=0, column=1, columnspan=5)
##widge_container[str(itr)] = header
##itr+=1
## 
##right = tk.Button(frame, text='>',width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = lambda: change_month(root,frame, '2'))
##right.grid(row=0, column=6)
##widge_container[str(itr)] = right
##itr+=1
##
##
##
##
##
##def print_numb(event):
##    global header, frame
##    try:
##        inp = event.widget.cget('text')
##        comb = '{} : Day Selected --- {}\n'.format(header.cget('text'),inp)
##        txt.insert(tk.END, comb)
##        txt.insert(tk.END, '---------------------------------\n')
##    except (Exception, tk.EXCEPTION) as e:
##        print e
##
##
##def change_month(parent, w, m):
##    w.destroy()
##    frame = tk.Frame(parent)
##    frame.grid(row = 0, column = 0, padx = 5, pady = 5)
##
##    widge_container = clc.OrderedDict()
##    itr = 0
##    
##    #CREATING BUTTONS
##    buttonRows = [i[:3].upper() for i in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']]
##
##    left = tk.Button(frame, text='<', width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = None)
##    left.grid(row=0, column=0)
##    widge_container[str(itr)] = left
##    itr+=1
##
##    header = tk.Label(frame,  text = 'January 2019', cursor = 'hand2',font = ('Verdana',8,'bold'), command = None)
##    header.grid(row=0, column=1, columnspan=5)
##
##
##root.mainloop()
##
