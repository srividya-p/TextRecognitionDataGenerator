from image_utils import ImageText
import os

fonts = list(filter(lambda x: '.ttf' in x, os.listdir()))

spaceNamesFile = open('/home/pika/Desktop/TIFR/YOLO-AppV2.0/TRDG/trdg/gu_dict/distribution_final_363/space_363.names', 'r')
letters = ' '.join([l.strip() if l != 'Space\n' else ' ' for l in spaceNamesFile.readlines()])


for font in fonts:
    color = (50, 50, 50)
    img = ImageText((1000, 800), background=(255, 255, 255)) 

    img.write_text_box((100, 50), letters, box_width=800, font_filename=font,
                    font_size=20, color=color)

    img.save('tests/'+font+'.png')
