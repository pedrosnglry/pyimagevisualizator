import tkinter as tk
from PIL import Image, ImageTk

folder = 'imagens'
nome = "pyvisualizer"
image_location = "imagemdeteste.jpg"
fist_run = True
arquives = []
widget_bar_height = 20
root = tk.Tk()
largura =int(1920/2)
altura =int(1080/2)-widget_bar_height

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
    render = ImageTk.PhotoImage(redim_image)
    img = tk.Label(root, image=render)
    img.image = render
    img.place(x=(int(largura/2)-int(largura_img/2)), y=(widget_bar_height+int(altura/2)-int(altura_img/2)) )

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=1)
        redimensionar()
        posicionar()

app = Window(root)
root.wm_title(nome)
root.geometry(f"{largura}x{altura+widget_bar_height}")
print("iniciando")
root.mainloop()
print('fechando')