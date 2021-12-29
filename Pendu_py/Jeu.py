import random
from tkinter import *
from itertools import repeat
import string

def choix_mot(): 
    f=open('dico_modifie.txt','r')
    longueur=1
    nombre_de_lignes=len(f.readlines())
    
    while longueur<=5 or longueur >10:
        choix=random.randint(1,nombre_de_lignes)
        i=0
        f=open('dico_modifie.txt','r')
        for i in range(choix):
            ligne=f.readline()
            mot=ligne.rstrip('\n')
        f.close()
        longueur=len(mot)
    return mot

sol = choix_mot()
underscore="_"
essai = 10

def jeu_final():
  essai=10
  def quit3():
    root.destroy()
  
  def tentatives():
    global essai
    essai-=1
    if essai == 9:
      label_vie.config(text='vies : {}'.format(essai))
      image1 = PhotoImage(file="pendu1.1.png", master=root)
      canvas.destroy()
      canvas2 = Canvas(root, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
      canvas2.create_image(width/2, height/2, image=image1)
      canvas2.image=image1
      canvas2.place(x=0, y=0)
    elif essai == 8:
      label_vie.config(text='vies : {}'.format(essai))
      image2 = PhotoImage(file="pendu1.2.png", master=root)
      canvas3 = Canvas(root, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
      canvas3.create_image(width/2, height/2, image=image2)
      canvas3.image=image2
      canvas3.place(x=0, y=0)
    elif essai == 7:
      label_vie.config(text='vies : {}'.format(essai))
      image3 = PhotoImage(file="pendu1.3.png", master=root)
      canvas4 = Canvas(root, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
      canvas4.create_image(width/2, height/2, image=image3)
      canvas4.image=image3
      canvas4.place(x=0, y=0)
    elif essai == 6:
      label_vie.config(text='vies : {}'.format(essai))
      image4 = PhotoImage(file="pendu1.4.png", master=root)
      canvas5 = Canvas(root, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
      canvas5.create_image(width/2, height/2, image=image4)
      canvas5.image=image4
      canvas5.place(x=0, y=0)
    elif essai == 5:
      label_vie.config(text='vies : {}'.format(essai))
      image5 = PhotoImage(file="pendu1.5.png", master=root)
      canvas6 = Canvas(root, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
      canvas6.create_image(width/2, height/2, image=image5)
      canvas6.image=image5
      canvas6.place(x=0, y=0)
    elif essai == 4:
      label_vie.config(text='vies : {}'.format(essai))
      image6 = PhotoImage(file="pendu1.6.png", master=root)
      canvas7 = Canvas(root, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
      canvas7.create_image(width/2, height/2, image=image6)
      canvas7.image=image6
      canvas7.place(x=0, y=0)
    elif essai == 3:
      label_vie.config(text='vies : {}'.format(essai))
      image7 = PhotoImage(file="pendu1.7.png", master=root)
      canvas8 = Canvas(root, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
      canvas8.create_image(width/2, height/2, image=image7)
      canvas8.image=image7
      canvas8.place(x=0, y=0)
    elif essai == 2:
      label_vie.config(text='vies : {}'.format(essai))
      image8 = PhotoImage(file="pendu1.8.png", master=root)
      canvas9 = Canvas(root, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
      canvas9.create_image(width/2, height/2, image=image8)
      canvas9.image=image8
      canvas9.place(x=0, y=0)
    elif essai == 1:
      label_vie.config(text='vies : {}'.format(essai))
      image9 = PhotoImage(file="pendu1.9.png", master=root)
      canvas10 = Canvas(root, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
      canvas10.create_image(width/2, height/2, image=image9)
      canvas10.image=image9
      canvas10.place(x=0, y=0)
    else:
      root.destroy()

  def affichage():
    if essai > 0:
      global label_letter
      label_letter.config(text=nouvelle_liste_underscore)
      if underscore not in liste_underscore:
        label_gagne= Label(text="Vous avez gagné !", font=("arial", 40), bg='#2C2C2C', fg='#FFFFFF')
        label_gagne.place(x=450, y=20)
        
  def text_entry():
    global letter
    global letter_entry
    if essai > 0:
      letter_entry=Entry(root, font=("arial", 30), bg='dimgray', fg='#FFFFFF')
      letter_entry.bind('<Return>', reconvertion)
      letter_entry.pack(side=BOTTOM, fill=X)
  

  def reconvertion(event):
    global nouvelle_liste_underscore
    global essai
    global liste_underscore
    global liste_underscore_convert

    if essai > 0:
      letter = letter_entry.get()
      letter_entry.delete(0, END)
      x=letter
      caracteres_possibles = string.ascii_lowercase
      if letter not in caracteres_possibles:
        print("Veuillez entrer une lettre minuscule")
      else:
        if letter in list_sol:
          if list_sol.count(letter) > 1:
            liste_underscore[list_sol.index(letter)]=letter
            for x in list_sol:
              if x in letter:
                liste_underscore[list_sol.index(letter, int(list_sol.index(letter) + 1), nombre_underscore)]=letter
              else :
                pass
          else:
            liste_underscore[list_sol.index(letter)]=letter
        elif letter not in list_sol:
          tentatives()
      nouvelle_liste_underscore = (" ".join(liste_underscore))
      affichage()

  global underscore
  global nombre_underscore
  global label_letter
  global list_sol
  global liste_underscore
  root = Tk()
  root.title("Jeu du Pendu")
  root.attributes('-fullscreen', True)
  root.minsize(720, 480)   
  root.iconbitmap("rope.ico")
  root.config(background='#2C2C2C')

  label_vie= Label(text='vies : {}'.format(essai), font=("arial", 45), bg='#2C2C2C', fg='#FFFFFF')
  label_vie.pack(padx=40, pady=40, side=TOP, anchor=E)

  quit_button2 = Button(root, text="QUIT", font=("arial", 28), bg='#2C2C2C', fg='#FFFFFF', command = quit3)
  quit_button2.place(x=1130, y=200)

  width=300
  height=300
  image0 = PhotoImage(file="pendu1.0.png", master=root)
  canvas = Canvas(root, width=width, height=height, bg='#2C2C2C', bd=0, highlightthickness=0)
  canvas.create_image(width/2, height/2, image=image0)
  canvas.image=image0
  canvas.place(x=0, y=0)

  nombre_underscore = len(sol)
  liste_underscore = []
  list_sol= list(sol)
  liste_underscore.extend(repeat(underscore, nombre_underscore))
  print(list_sol)
  liste_underscore_convert = (" ".join(liste_underscore))

  frame_pendu = Frame(root, bg='#2C2C2C')
  label_letter=Label(frame_pendu, text=(liste_underscore_convert), font=("arial", 50), bg='#2C2C2C', fg='#FFFFFF')
  label_letter.pack()
  frame_pendu.pack(expand=YES)

  text_entry()
  root.mainloop()