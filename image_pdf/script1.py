# Versao 0.1
from fpdf import FPDF
from io import BytesIO
from PIL import Image


class image_to_pdf:
    def __init__(self, lista_imagens: list):
        self.lista_imagens = lista_imagens

    def definicao_configuracao_da_pagina(self, imagem_PIL: Image):
        largura, altura = imagem_PIL.size
        proporcao = altura / largura

        if proporcao < 0.9:
            largura_da_pagina = 297
            altura_para_a_pagina = largura_da_pagina * altura / largura
            return {
                'altura': altura_para_a_pagina,
                'largura': largura_da_pagina,
            }
        if proporcao > 0.9:
            largura_da_pagina = 210
            altura_para_a_pagina = largura_da_pagina * altura / largura
            return {
                'altura': altura_para_a_pagina,
                'largura': largura_da_pagina,
            }

    def iniciar_conversao(self):
        pdf = FPDF()
        for image_bytes in self.lista_imagens:
            image = Image.open(BytesIO(image_bytes))
            medidas_pagina = self.definicao_configuracao_da_pagina(image)
            pdf.add_page(
                format=(medidas_pagina['largura'], medidas_pagina['altura'])
            )
            pdf.image(image, x=0, y=0, w=medidas_pagina['largura'])
        return pdf.output()
