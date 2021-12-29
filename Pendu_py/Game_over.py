from tkinter import*

def game_over():    
    def quit1():
        root2.destroy()
    def jeu2():
        root2.destroy()
        Menu.menu()
    root2 = Tk()
    root2.title("Jeu du Pendu")
    root2.attributes('-fullscreen', True)
    root2.minsize(720, 480)   
    root2.iconbitmap("rope.ico")
    root2.config(background='#2C2C2C')

    top_frame2 = Frame(root2, bg='#2C2C2C')
    label_title=Label(top_frame2, text="GAME OVER", font=("arial", 60), bg='#2C2C2C', fg='#FFFFFF')
    label_title.pack(side=TOP)
    top_frame2.pack()

    frame5 = Frame(root2, bg='#2C2C2C')

    width=376
    height=376
    image = PhotoImage(file="pendu1.png", master=root2)
    canvas = Canvas(frame5, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
    canvas.create_image(width/2, height/2, image=image)
    canvas.image=image
    canvas.grid(row=0, column=0, sticky=W)

    frame4 = Frame(frame5, bg='#2C2C2C')
    quit_button = Button(frame4, text="QUIT", font=("arial", 20), bg='#2C2C2C', fg='#FFFFFF', command = quit1)
    quit_button.pack(pady=10, fill=X)

    frame4.grid(row=0, column=1, sticky=W)
    frame5.pack(expand=YES)
    root2.mainloop()