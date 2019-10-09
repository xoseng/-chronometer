# coding=utf8

from tkinter import Tk, Label, Button, Frame

proceso = 0

def iniciar(h=0, m=0, s=0):
    global proceso

    try:
        parar()
    except:
        pass

    if s >= 60:
        s = 0
        m = m + 1
        if m >= 60:
            m = 0
            h = h + 1
            if h >= 24:
                h = 0

    time['text'] = str(h) + ":" + str(m) + ":" + str(s)
    proceso = time.after(1000, iniciar, (h), (m), (s + 1))

def parar():
    try:
        global proceso
        time.after_cancel(proceso)
    except:
        pass

def reanudar():
    try:
        global proceso
        horas=int(time['text'].split(':')[0])
        mins=int(time['text'].split(':')[1])
        segundos=int(time['text'].split(':')[2])+1 #le sumo 1 para que no pierda tiempo en iniciar
        parar()
        iniciar(h=horas, m=mins, s=segundos)
    except:
        pass

root = Tk()
root.title('Chronometer')
root.resizable(0, 0)
root.config(bd=30)
time = Label(root, fg='black', width=20, font=("", "18"))
time.pack()

time['text'] = "0:0:0"

frame = Frame(root)
btnIniciar = Button(frame, fg='green', text='Iniciar', command=iniciar).grid(row=1, column=1,padx=2, pady=5)
btnParar = Button(frame, fg='red', text='Parar', command=parar).grid(row=1, column=2,padx=2, pady=5)
btnReanudar = Button(frame, fg='blue', text='Reanudar', command=reanudar).grid(row=1, column=3,padx=2, pady=5)
frame.pack()

root.mainloop()