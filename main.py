import tkinter as tk

from db.conexao import conectar
from ui.menu import *
from ui.terminal import *
from ui.janela import *

janela.after(100, desenhar_menu(janela, menu_area))
janela.mainloop()