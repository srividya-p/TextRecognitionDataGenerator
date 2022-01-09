"""
Utility functions
"""

import os
import numpy as np
from PIL import Image

def load_dict(lang):
    """Read the dictionnary file and returns all words in it.
    """

    lang_dict = []
    with open(
        os.path.join(os.path.dirname(__file__), "dicts", lang + ".txt"),
        "r",
        encoding="utf8",
        errors="ignore",
    ) as d:
        lang_dict = [l for l in d.read().splitlines() if len(l) > 0]
    return lang_dict


def load_fonts(lang):
    """Load all fonts in the fonts directories
    """

    if lang in os.listdir(os.path.join(os.path.dirname(__file__), "fonts")):
        return [
            os.path.join(os.path.dirname(__file__), "fonts/{}".format(lang), font)
            for font in os.listdir(
                os.path.join(os.path.dirname(__file__), "fonts/{}".format(lang))
            )
        ]
    else:
        return [
            os.path.join(os.path.dirname(__file__), "fonts/latin", font)
            for font in os.listdir(
                os.path.join(os.path.dirname(__file__), "fonts/latin")
            )
        ]

def mask_to_bboxes(mask, splitted_text, tess=False):
    """Process the mask and turns it into a list of AABB bounding boxes
    """

    mask_arr = np.array(mask)

    bboxes = []

    i = 0
    space_thresh = 1
    while True:
        try:
            color_tuple = ((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255)
            letter = np.where(np.all(mask_arr == color_tuple, axis=-1))
            if space_thresh == 0 and letter:
                xmin = min(bboxes[-1][2] + 1, np.min(letter[1]) - 1)
                ymin = min(bboxes[-1][3] + 1, np.min(letter[0]) - 1) if not tess else min(mask_arr.shape[0] - np.min(letter[0]) + 2, bboxes[-1][1] - 1)
                xmax = max(bboxes[-1][2] + 1, np.min(letter[1]) - 2)
                ymax = max(bboxes[-1][3] + 1, np.min(letter[0]) - 2) if not tess else max(mask_arr.shape[0] - np.min(letter[0]) + 2, bboxes[-1][1] - 1)
                
                bboxes.append([xmin, ymin, xmax, ymax])

                space_thresh += 1
            
            xmin = max(0, np.min(letter[1]) - 1)
            ymin = max(0, np.min(letter[0]) - 1) if not tess else max(0, mask_arr.shape[0] - np.max(letter[0]) - 1)
            xmax = min(mask_arr.shape[1] - 1, np.max(letter[1]) + 1)
            ymax = min(mask_arr.shape[0] - 1, np.max(letter[0]) + 1) if not tess else min(mask_arr.shape[0] - 1, mask_arr.shape[0] - np.min(letter[0]) + 1)

            bboxes.append([xmin, ymin, xmax, ymax])
            i += 1
        except Exception as ex:
            if space_thresh == 0:
                break
            space_thresh -= 1
            i += 1
    
    char_index_mapping, i = dict(), 0
    space_names_file = open('/home/pika/Desktop/TIFR/YOLO-AppV2.0/TRDG/trdg/gu_dict/distribution_final_363/space_363.names', 'r')

    for line in space_names_file.readlines():
        char = line.replace('\n', '')
        char_index_mapping[char] = i
        i += 1

    for char, bbox in zip(splitted_text, bboxes):
        xmin, ymin, xmax, ymax = bbox
        
        xcen = float((xmin + xmax)) / 2 / mask_arr.shape[1]
        ycen = float((ymin + ymax)) / 2 / mask_arr.shape[0]
        w = float((xmax - xmin)) / mask_arr.shape[1]
        h = float((ymax - ymin)) / mask_arr.shape[0]

        # bbox[0] = xcen
        # bbox[1] = ycen
        # bbox[2] = w
        # bbox[3] = h
        
        if char != ' ':
            try:
                bbox.insert(0, char_index_mapping[char])
            except:
                bbox.insert(0, char)
        else:
            bbox.insert(0, char_index_mapping['Space'])
        
    return bboxes        

def draw_bounding_boxes(img, bboxes, color="green"):
    d = ImageDraw.Draw(img)

    for bbox in bboxes:
        d.rectangle(bbox, outline=color)


