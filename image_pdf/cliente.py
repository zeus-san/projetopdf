from script1 import image_to_pdf
import os.path
import os

# Codigo exemplo de como utilizar

# Obter os bytes das imagens
images_bytes = []

arquivos = os.listdir('imgs')
for imagem in arquivos:
    with open(f'imgs/{imagem}', 'rb') as file:
        images_bytes.append(file.read())

# Submeter ao codigo
bytesarquiv = image_to_pdf(images_bytes).iniciar_conversao()

# Gravar num arquivo
with open('teste1.pdf', 'wb') as file:
    file.write(bytesarquiv)
