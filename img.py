import pygame, sys, os
from time import sleep
from PIL import Image

folder = 'imagens'
largura =int(1920/2)
altura =int(1080/2)
nome = "visualizador"
image_location = "starting.jpg"
fist_run = True
arquives = []

def imageload():
    global image
    image = pygame.image.load(image_location)

def pegar_imagem():
    global image_location
    global arquives
    global fist_run
    if fist_run:
        try:
            os.mkdir(folder)
            fist_run = False
        except:
            fist_run = False
            for img in os.listdir(folder):os.remove('{}\\{}'.format(folder,img))
    arquives_temp = os.listdir(folder)
    for img in arquives_temp:
        sliced = img.split(".")
        if sliced[1] == "jpg":
            breaker = False
            for image_saved in arquives:
                if image_saved == img:
                    breaker = True
                    break
            if not breaker:
                arquives.append(img)
                image_location = folder+ "\\" +img
                sleep(0.5)
                imageload()


if __name__ == "__main__":

    
    #print("largura da imagem:"+str(largura_img))
    #print("altura da imagem:"+str(altura_img))

    pygame.init()
    pygame.display.set_caption(nome)
    display = pygame.display.set_mode((largura,altura))
    imageload()
    def redimensionar():
        global largura
        global altura
        global largura_img
        global altura_img
        global redim_image
        size = Image.open(image_location)
        largura_img, altura_img = size.size
        if largura < altura:
            factor = largura/largura_img
        elif largura > altura:
            factor = altura/altura_img
        if int(largura_img) > int(largura):
            largura_img = largura_img*factor
            altura_img = altura_img*factor
            redim_image = pygame.transform.smoothscale(image, (int(largura_img), int(altura_img)))
        elif int(largura_img) < int(largura):
            largura_img = largura_img*factor
            altura_img = altura_img*factor
            redim_image = pygame.transform.smoothscale(image, (int(largura_img), int(altura_img)))
        #print("largura(redimensionada) da imagem:"+str(int(largura_img)))
        #print("altura(redimensionada) da imagem:"+str(int(altura_img)))

    redimensionar()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue
        pegar_imagem()
        redimensionar()
        display.fill((54,54,54))
        display.blit(redim_image, ((int(largura/2)-int(largura_img/2)),int(altura/2)-int(altura_img/2)))
        pygame.display.update()
    try:
        for file in os.listdir(folder):os.remove('{}\\{}'.format(folder, file))
        os.rmdir(folder)
    except:print('impossivel excluir a pasta temporaria "{}"'.format(folder))
    pygame.quit()
