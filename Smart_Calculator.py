from tkinter import *



# For mathematical functions

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
def mod(a,b):
    return a % b
def lcm(a,b):
    l = a if a>b else b
    while l<= a+b:
        if l %a == 0 and l%b == 0:
            return l
        l+=1

def hcf(a,b):
    h = a if a < b else b
    while h>=1:
        if a%h == 0 and b%h ==0:
            return h
        h-=1



# Extract number from list

def extract_from_text(text):
    l = []
    for t in text.split(' '):
        # take number from the text
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0, END)
                list.insert(END, 'something went wrong please enter again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0, END)
            list.insert(END, 'something went wrong please enter again')


        # user can use these to perform operations


operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add ,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
                 'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul,
                 'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                  'REMAINDER':mod , 'MODULUS':mod}




win  = Tk()
win.geometry('500x300')
win.title('Smart Calculator')
win.configure(bg = 'skyblue')

l1 = Label(win,text = 'I am a  Smart Calculator',width = 20,padx=3)
l1.place(x=150,y=10)

l2 = Label(win,text = 'My name is Jerry',padx=3)
l2.place(x=180,y=40)

l3 = Label(win,text = 'How can i help you', padx =3)
l3.place(x=176,y = 130)


textin = StringVar()
e1 = Entry(win,width=30, textvariable = textin )
e1.place(x=140,y=160)


b1 = Button(win,text = 'Just do',command = calculate)
b1.place(x=210,y=190)

list = Listbox(win,width=40,height = 3)
list.place(x=120,y = 230)

















win.mainloop()