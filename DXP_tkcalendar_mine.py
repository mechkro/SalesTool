import Tkinter as tk
import collections as clc
import calendar
import datetime as dt
import itertools as itr



class CalendarMain(tk.Frame):
    def __init__(self,parent, *args, **kwargs):
        
        tk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.calendar_data_format()
        #self.cur_month_cal = calendar.monthcalendar(int(self.y), int(self.m))
        #>>> (m, t, w, th, f, sa, su)
        #>>> [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]
        
        self.cal_button_contain = clc.OrderedDict()
        self.year = 2019
        res = return_order(year, *range(1,13))
        cont = []
        
        d =  clc.OrderedDict()
        for k,v in res.items():
            d.setdefault(k.split(',')[-1], []).append(v)


    def return_order(y,*m):
        d = clc.OrderedDict()
        for x in m:
            weekout = calendar.monthcalendar(y,x)
            for j in weekout:
                daYs = [('mon,{}'.format(x), j[0]),
                            ('tue,{}'.format(x),j[1]),
                            ('wed,{}'.format(x), j[2]),
                            ('thu,{}'.format(x),j[3]),
                            ('fri,{}'.format(x), j[4]),
                            ('sat,{}'.format(x),j[5]),
                            ('sun,{}'.format(x), j[6])]
                for k,v in daYs:
                    d.setdefault(k, []).append(v)
        return d


    def calendar_data_format(self, y=None, m=None):
        
        today = dt.datetime.today()
        today_format = dt.datetime.strftime(today, '%Y,%m,%d')
        split_date = today_format.split(',')
        if y and m:
            self.y = y
            self.m = m
            self.d = split_date[-1]
        else:
            self.y, self.m, self.d = today_format.split(',')

        return self.y, self.m, self.d
        
        #self.cur_month_cal = calendar.monthcalendar(int(self.y), int(self.m))
        #>>> (m, t, w, th, f, sa, su)
        #>>> [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]


    def cal_next_month(self):
        if self.m == 12:
            self.m == 1
            self.year += 1

    def cal_prev_month(self):
        if self.m == 1:
            self.m == 12
            self.year -= 1


        

        






def return_cals(y,m):
    itr = 0
    weekout = calendar.monthcalendar(y,m)
    dys = ('mon','tue','wed','thu','fri','sat','sun')
    for j in weekout:
        for i,x in enumerate(j):
            if x == 0:
                pass
            else:
                itr+=1
                #print "{} : {}".format(dys[i], x)
    return itr


k = 0
for j in range(1,13):
    k += return_cals(2019,j)
print k


"""
Month: 1
Weeks: [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, 0, 0, 0]]
Month: 2
Weeks: [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 0, 0, 0]]
Month: 3
Weeks: [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]]
Month: 4
Weeks: [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 0, 0, 0, 0, 0]]
Month: 5
Weeks: [[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 0, 0]]
Month: 6
Weeks: [[0, 0, 0, 0, 0, 1, 2], [3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30]]
Month: 7
Weeks: [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 0, 0, 0, 0]]
Month: 8
Weeks: [[0, 0, 0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24, 25], [26, 27, 28, 29, 30, 31, 0]]
Month: 9
Weeks: [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 0, 0, 0, 0, 0, 0]]
Month: 10
Weeks: [[0, 1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27], [28, 29, 30, 31, 0, 0, 0]]
Month: 11
Weeks: [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 0]]
Month: 12
Weeks: [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]
OrderedDict([('monday', 1), ('friday', 5), ('wednesday', 3), ('thursday', 4), ('sunday', 0), ('tueday', 2), ('saturday', 6)])

##buttonRows = [[i[:3].upper() for i in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']],[None]*7,['4','5','6','/','5','6','/'],
##              ['7','8','9','*','5','6','/'],['.','0','-','+','5','6','/'],['4','5','6','/','5','6','/'],
##              ['7','8','9','*','5','6','/'],['.','0','-','+','5','6','/']]
"""

    



root = tk.Tk()
frame = tk.Frame(root)
frame.grid(row = 0, column = 0, padx = 5, pady = 5)
frame2 = tk.Frame(root)
frame2.grid(row = 0, column = 1, padx = 5, pady = 5)


txt_lf = tk.LabelFrame(frame2, text = 'Current Date -- Entity View')
txt_lf.grid(row = 0 , column = 0, padx = 5, pady = 5)


calendar.prmonth(2019,12)
p = calendar.calendar(2020)
today = dt.datetime.today()
x = dt.datetime.strftime(today, '%Y,%m,%d')
y,m,d = x.split(',')

a = calendar.monthcalendar(int(y), int(m))

print a

p = ['mon','tue','wed','thu','fri','sat', 'sun']
form_dict = clc.OrderedDict()
itr = 0


for i,j in enumerate(p):
    form_dict[j] = [k[i] for k in a]

for g,h in form_dict.items():
    pass
    #print g, h

    

     


place_dict = clc.OrderedDict({'sunday':0,
               'monday': 1,
               'tueday': 2,
               'wednesday': 3,
               'thursday': 4,
               'friday': 5,
               'saturday': 6})

widges = clc.OrderedDict()



def reload_widge(wx,wy):
    global root, frame, widges
    print wx, wy
    try:
        widges['{},{}'.format(wx,wy)].configure(fg = 'red')
    except Exception as e:
        print e



def return_order(y,*m):
    d = clc.OrderedDict()
    #ntup = clc.namedtuple(list, [)
    for x in m:
        weekout = calendar.monthcalendar(y,x)
        for j in weekout:
            daYs = [('mon,{}'.format(x), j[0]),
                    ('tue,{}'.format(x),j[1]),
                    ('wed,{}'.format(x), j[2]),
                    ('thu,{}'.format(x),j[3]),
                    ('fri,{}'.format(x), j[4]),
                    ('sat,{}'.format(x),j[5]),
                    ('sun,{}'.format(x), j[6])]
            for k,v in daYs:
                d.setdefault(k, []).append(v)
    return d
            
            
            

widges = clc.OrderedDict()


#print place_dict
itr = 0






year = 2019
res = return_order(year, *range(1,13))
cont = []
d =  clc.OrderedDict()
for k,v in res.items():
    d.setdefault(k.split(',')[-1], []).append(v)

    
print d['1'][0], '\n'

for k,v in d.items():
    print 'Month: {}'.format(k)
    print 'Monday:  {}'.format(v[0])
    print 'Tues: {}'.format(v[1])
    print 'Wed: {}'.format(v[2])
    print 'Thur: {}'.format(v[3])
    print 'Fri: {}'.format(v[4])
    print 'Sat: {}'.format(v[5])
    print 'Sun: {}'.format(v[6])



widge_container = clc.OrderedDict()
itr = 0

#CREATING TEXT BOX
txt = tk.Text(txt_lf, height = 9)
txt.grid(padx = 3, pady = 3)


root.title('January 2019')


#CREATING BUTTONS
buttonRows = [i[:3].upper() for i in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']]

left = tk.Button(frame, text='<', width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = None)
left.grid(row=0, column=0)
widge_container[str(itr)] = left
itr+=1

header = tk.Label(frame,  text = 'January 2019', cursor = 'hand2',font = ('Verdana',8,'bold'), command = None)
header.grid(row=0, column=1, columnspan=5)
widge_container[str(itr)] = header
itr+=1
 
right = tk.Button(frame, text='>',width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = lambda: change_month(root,frame, '2'))
right.grid(row=0, column=6)
widge_container[str(itr)] = right
itr+=1





def print_numb(event):
    global header, frame
    try:
        inp = event.widget.cget('text')
        comb = '{} : Day Selected --- {}\n'.format(header.cget('text'),inp)
        txt.insert(tk.END, comb)
        txt.insert(tk.END, '---------------------------------\n')
    except (Exception, tk.EXCEPTION) as e:
        print e


def change_month(parent, w, m):
    w.destroy()
    frame = tk.Frame(parent)
    frame.grid(row = 0, column = 0, padx = 5, pady = 5)

    widge_container = clc.OrderedDict()
    itr = 0
    
    #CREATING BUTTONS
    buttonRows = [i[:3].upper() for i in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']]

    left = tk.Button(frame, text='<', width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = None)
    left.grid(row=0, column=0)
    widge_container[str(itr)] = left
    itr+=1

    header = tk.Label(frame,  text = 'January 2019', cursor = 'hand2',font = ('Verdana',8,'bold'), command = None)
    header.grid(row=0, column=1, columnspan=5)
    widge_container[str(itr)] = header
    itr+=1
     
    right = tk.Button(frame, text='>',width =5, cursor = 'hand2', font = ('Verdana',8,'bold'), command = lambda: change_month(root,frame, '2'))
    right.grid(row=0, column=6)
    widge_container[str(itr)] = right
    itr+=1

    for i,j in enumerate(buttonRows):
        widge_container[str(itr)] = tk.Button(frame, text=j, width =5, cursor = 'hand2', bg = 'yellow', font = ('Verdana',8,'bold'), command = None, state = tk.DISABLED)
        widge_container[str(itr)].grid(row=1, column=i)
        widge_container[str(itr)].bind('<Button-1>', print_numb)
        itr+=1

    for i,j in enumerate(d['1']):
        print 'Month {}'.format(i)
        for h,u in enumerate(j):
            if int(u) == 0:
                widge_container[str(itr)] = tk.Button(frame, text='-', width=5, command = None, state = tk.DISABLED, font = ('Verdana',8,'bold'))
                widge_container[str(itr)].grid(row=h+2, column=i)
                widge_container[str(itr)].bind('<Button-1>', print_numb)
                itr+=1
            else:
                widge_container[str(itr)] = tk.Button(frame, text=u, width=5, font = ('Verdana',8,'bold'), cursor = 'hand2',
                                     command = None)
                widge_container[str(itr)].grid(row=h+2, column=i)
                widge_container[str(itr)].bind('<Button-1>', print_numb)
                itr+=1



                

for i,j in enumerate(buttonRows):
    widge_container[str(itr)] = tk.Button(frame, text=j, width =5, cursor = 'hand2', bg = 'yellow', font = ('Verdana',8,'bold'), command = None, state = tk.DISABLED)
    widge_container[str(itr)].grid(row=1, column=i)
    widge_container[str(itr)].bind('<Button-1>', print_numb)
    itr+=1

for i,j in enumerate(d['1']):
    print 'Month {}'.format(i)
    for h,u in enumerate(j):
        if int(u) == 0:
            widge_container[str(itr)] = tk.Button(frame, text='-', width=5, command = None, state = tk.DISABLED, font = ('Verdana',8,'bold'))
            widge_container[str(itr)].grid(row=h+2, column=i)
            widge_container[str(itr)].bind('<Button-1>', print_numb)
            itr+=1
        else:
            widge_container[str(itr)] = tk.Button(frame, text=u, width=5, font = ('Verdana',8,'bold'), cursor = 'hand2',
                                 command = None)
            widge_container[str(itr)].grid(row=h+2, column=i)
            widge_container[str(itr)].bind('<Button-1>', print_numb)
            itr+=1




left.bind('<Button-1>', None)
right.bind('<Button-1>', None)


root.mainloop()


##from PIL import Image
##
##ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']
##
##def scale_image(image, new_width=100):
##    """Resizes an image preserving the aspect ratio.
##    """
##    (original_width, original_height) = image.size
##    aspect_ratio = original_height/float(original_width)
##    new_height = int(aspect_ratio * new_width)
##
##    new_image = image.resize((new_width, new_height))
##    return new_image
##
##def convert_to_grayscale(image):
##    return image.convert('L')
##
##def map_pixels_to_ascii_chars(image, range_width=25):
##    """Maps each pixel to an ascii char based on the range
##    in which it lies.
##
##    0-255 is divided into 11 ranges of 25 pixels each.
##    """
##
##    pixels_in_image = list(image.getdata())
##    pixels_to_chars = [ASCII_CHARS[pixel_value/range_width] for pixel_value in
##            pixels_in_image]
##
##    return "".join(pixels_to_chars)
##
##def convert_image_to_ascii(image, new_width=100):
##    image = scale_image(image)
##    image = convert_to_grayscale(image)
##
##    pixels_to_chars = map_pixels_to_ascii_chars(image)
##    len_pixels_to_chars = len(pixels_to_chars)
##
##    image_ascii = [pixels_to_chars[index: index + new_width] for index in
##            xrange(0, len_pixels_to_chars, new_width)]
##
##    return "\n".join(image_ascii)
##
##def handle_image_conversion(image_filepath):
##    image = None
##    try:
##        image = Image.open(image_filepath)
##    except Exception, e:
##        print "Unable to open image file {image_filepath}.".format(image_filepath=image_filepath)
##        print e
##        return
##
##    image_ascii = convert_image_to_ascii(image)
##    print image_ascii
##
##if __name__=='__main__':
##    import sys
##
##    image_file_path = r"C:\Users\Mechkro\Desktop\crow.jpg"
##    handle_image_conversion(image_file_path)
##
##



        
