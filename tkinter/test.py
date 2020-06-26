import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from os import getcwd

print(getcwd())

folder = 'imagens'
title = "pyvisualizer"
image_location = f"{getcwd()}\\imagemdeteste.jpg"
fist_run = True
arquives = []
widget_bar_height = 30
root = tk.Tk()
largura =int(1920/2)
altura =int(1080/2)-widget_bar_height
display = (root.winfo_screenwidth()), (root.winfo_screenheight())
print(f'tamanho da tela:\nlargura:{display[0]}\naltura:{display[1]}')

def redimensionar():
    global largura
    global altura
    global largura_img
    global altura_img
    global redim_image
    size = Image.open(image_location)
    largura_img, altura_img = size.size
    try:
        if largura < altura:
            factor = largura/largura_img
        elif largura > altura:
            factor = altura/altura_img
        if int(largura_img) > int(largura):
            largura_img = largura_img*factor
            altura_img = altura_img*factor
        elif int(largura_img) < int(largura):
            largura_img = largura_img*factor
            altura_img = altura_img*factor
        redim_image = size.resize((int(largura_img), int(altura_img)))
    except:
        print('erro ao tentar redimensionar a imagem!')
        redim_image = image_location
            
    #print("largura(redimensionada) da imagem:"+str(int(largura_img)))
    #print("altura(redimensionada) da imagem:"+str(int(altura_img)))

def posicionar():
    global img
    render = ImageTk.PhotoImage(redim_image)
    img = tk.Label(root, image=render)
    img.image = render
    img.place(x=(int(largura/2)-int(largura_img/2)), y=(widget_bar_height+int(altura/2)-int(altura_img/2)) )

def abrir():
        global image_location
        global img
        image_location = askopenfilename()
        img.destroy()
        redimensionar()
        posicionar()

def resetar():
    img.destroy()

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        redimensionar()
        posicionar()

app = Window(root)
root.wm_title(title)
root.geometry(f"{largura}x{altura+widget_bar_height}+{int((display[0]/2)-(largura/2))}+{int((display[1]/2)-(altura/2))}")
root.resizable(False, False)
root['bg'] = 'gray'
#root.iconbitmap()

#botoes barra:
btn_bar = [tk.Button(root, text="open", command=abrir, font=f'arial {widget_bar_height//3}',width=widget_bar_height//3)]
btn_bar.append(tk.Button(root, text="reset", command=resetar, font=f'arial {widget_bar_height//3}',width=widget_bar_height//3))
for i in (0,len(btn_bar)-1):
    btn_bar[i].grid(row=0,column=i)
root.mainloop()