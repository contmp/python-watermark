# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def watermark_text(input_image_path, output_image_path, text, position='bottom-right'):

    im = Image.open(input_image_path)
    width, height = im.size
    padding = (10, 10, 10, 10)

    # make the image editable
    drawing = ImageDraw.Draw(im)

    black = (3, 8, 12)
    white = (255, 255, 255)
    font = ImageFont.truetype("/Users/contmp/Desktop/FreeMono.ttf", 40)

    if position == 'bottom-right':
        text_size = drawing.textsize(text, font=font)
        watermark_shadow_position = (width - text_size[0] - padding[1], height - text_size[1] - padding[2])
        watermark_position = (watermark_shadow_position[0] - 1, watermark_shadow_position[1] - 1)

        drawing.text(watermark_shadow_position, text, fill=white, font=font)
        drawing.text(watermark_position, text, fill=black, font=font)

    im.show()
    im.save(output_image_path)

    print("asdasd")
    # pync.notify('X Bilder wurden gebrandmarkt', title='Watermarker', subtitle='Erfolg', sound='Pop')
