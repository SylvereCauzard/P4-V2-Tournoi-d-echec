
from tkinter import *

# creat a window
window = Tk()

# customize this window
window.title("Tournoi d'échec")
window.geometry("720x480")
window.iconbitmap("chess.ico")
window.config(background='#0C0C4B')

# créer la frame principale
frame = Frame(window, bg='#0C0C4B')

# make an image
width = 200
height = 200
image = PhotoImage(file="img_chess.png").zoom(35).subsample(100)
canvas = Canvas(frame, width=width, height=height, bg='#0C0C4B', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0)

# créer une sous boite
right_frame = Frame(frame, bg='#0C0C4B')

# créer un bouton
creat_tournament_button = Button(right_frame, text="Créer un nouveau tournoi", font=("Helvetica", 20), bg='#0C0C4B',
                                 fg="white")
creat_tournament_button.pack(fill=X)

# on place la sous boite à droite de la frame principal
right_frame.grid(row=0, column=1, sticky=E)

# afficher la frame
frame.pack(expand=YES)

# création de la barre de menu
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau Tournoi")
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# configurer notre fenetre pour ajouter cette menu bar
window.config(menu=menu_bar)

# afficher
window.mainloop()
