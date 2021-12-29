from tkinter import*
from Game_over import game_over
import Jeu

def menu():
    def quit():
        window.destroy()
    def jeu():
        window.destroy()
        if Jeu.essai>0:
            Jeu.jeu_final()
            if Jeu.essai == 0:
                game_over()
    window = Tk()
    window.title("Jeu du Pendu")
    window.attributes('-fullscreen', True)
    window.minsize(720, 480)   
    window.iconbitmap("rope.ico")
    window.config(background='#2C2C2C')

    top_frame = Frame(window, bg='#2C2C2C')
    label_title=Label(top_frame, text="Le Pendu", font=("arial", 60), bg='#2C2C2C', fg='#FFFFFF')
    label_title.pack()

    label_title=Label(top_frame, text="Mayeul Bourdon / Augustin Barras", font=("arial", 20), bg='#2C2C2C', fg='#FFFFFF')
    label_title.pack()
    top_frame.pack(side=TOP)

    frame = Frame(window, bg='#2C2C2C')

    width=376
    height=376
    image = PhotoImage(file="pendu1.png", master=window)
    canvas = Canvas(frame, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
    canvas.create_image(width/2, height/2, image=image)
    canvas.grid(row=0, column=0, sticky=W)

    frame2 = Frame(frame, bg='#2C2C2C')
    play_button = Button(frame2, text="PLAY", font=("arial", 20), bg='#2C2C2C', fg='#FFFFFF', command = jeu)
    play_button.pack(fill=X)

    quit_button = Button(frame2, text="QUIT", font=("arial", 20), bg='#2C2C2C', fg='#FFFFFF', command = quit)
    quit_button.pack(pady=10, fill=X)

    frame2.grid(row=0, column=1, sticky=W)
    frame.pack(expand=YES)
    window.mainloop()
menu()