from PIL import Image, ImageDraw, ImageFont,ImageEnhance, ImageFilter,ImageOps
import PIL

class ControladorCertificado():
  def __init__(self):
    pass

  def criador(self, dados):
    img = PIL.Image.open('images/certificado.png')

    draw = ImageDraw.Draw(img)
    widthImage, heightImage = img.size

    # Maximo Width que quero no texto
    maxW = 1150

    size = 90
    font1 = ImageFont.truetype("arial.ttf", size=size)
    widthFonte, heighFonte = draw.textsize(dados["nome_aluno"], font=font1)

    # caso Width da fonte for maior, temos que ver o maior que possa encaixar  
    while widthFonte > maxW:
      size -= 5
      font1 = ImageFont.truetype("arial.ttf", size=size)
      widthFonte, heighFonte = draw.textsize(dados["nome_aluno"], font=font1)


    pointX = (widthImage/2 - widthFonte/2) #metade da foto

    # nome
    draw.text((pointX, (517 - (heighFonte/2))), dados["nome_aluno"], fill = 'rgb(255, 255, 255)', font=font1)

    # Curso
    draw.text((pointX, (517 - (heighFonte/2)+250)), dados["nome_curso"], fill = 'rgb(255, 255, 255)', font=font1)

    # horas
    font1 = ImageFont.truetype("arial.ttf", size=65)
    draw.text((1255, 900), str(dados["horas_curso"]), fill = 'rgb(255, 255, 255)', font=font1)

    img.save('images/certificado_'+dados["email"]+'.png')