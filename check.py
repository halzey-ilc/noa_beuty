from escpos.printer import Usb
from PIL import Image, ImageDraw, ImageFont

p = Usb(0x0fe6, 0x811e)

# Создаем изображение
font = ImageFont.truetype("arial.ttf", 22)
img = Image.new("L", (384, 80), 255)  # ширина 384 px для 58мм принтера
draw = ImageDraw.Draw(img)
draw.text((10, 10), "Орчунбаева Айбатбек Жакилович!", font=font, fill=0)

img.save("text.png")

# Печать картинки
p.image("text.png")