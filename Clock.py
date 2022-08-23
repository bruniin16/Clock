from tkinter import *
from datetime import *


cond = False

hr = 0
min = 0
sec = 0

meses = ("","Janeiro","Fevereiro",
"Março","Abril","Maio","Junho",
"Julho","Agosto","Setembro",
"Outubro","Novembro","Dezembro")

data = ""

def time():
    global hr, min, sec, data, meses

    if cond == True:
        sec = str(0) + str(sec)
        min = str(0) + str(min)
        hr = str(0) + str(hr)

        crono["text"] = str(hr[-2:]) + ":" + str(min[-2:]) + ":" + str(sec[-2:])
        info["text"] = data

        crono.after(1000, time)
        hr = datetime.today().hour
        min = datetime.today().minute
        sec = datetime.today().second
        data = f"{date.today().day}/{meses[date.today().month]}"


def start():
    global cond
    cond = True
    inic["state"] = "disabled"
    time()


corbg = "#242323"

main = Tk()
main.title("RELÓGIO")
main.geometry("500x230+700+300")
main.config(bg = "#242323")
main.resizable(width = False, height = False)


crono = Label(main, text="00:00:00", font=("Courier 70 bold"), bg=corbg, fg="#16f59f")
crono.place(x=25,y=20)

info = Label(main, text="", font=("Courier 18 bold"), bg=corbg, fg="#ac12c7")
info.place(x=30,y=120)


inic = Button(main, text="Start", command = start, relief="solid", overrelief="ridge", bg=corbg, fg= "white", font="Courier 15 bold")
inic.place(x=380, y= 160)

main.mainloop()