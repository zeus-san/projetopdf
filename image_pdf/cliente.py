from script1 import image_to_pdf
import os.path
import os

images_bytes = []

arquivos = os.listdir('imgs')
for imagem in arquivos:
    with open(f'imgs/{imagem}', 'rb') as file:
        images_bytes.append(file.read())


bytesarquiv = image_to_pdf(images_bytes).iniciar_conversao()

with open('teste1.pdf', 'wb') as file:
    file.write(bytesarquiv)
