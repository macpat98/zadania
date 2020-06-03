from PIL import Image


# Kolor #FF0000 to po konwersji na RGB -> (255,0,0)
# #00FF00 -> (0,255,0)
# #0000FF -> (0,0,255)

class ImageProcessing:
    def to_main_colors(self,obraz):
        image = Image.open(obraz)
        pixels = image.load()
        for width in range(image.size[0]):
            for height in range(image.size[1]):
                if max(pixels[width,height]) == pixels[width,height][0]: #R
                    pixels[width,height] = (255,0,0)
                elif max(pixels[width,height]) == pixels[width,height][1]: #G
                    pixels[width, height] = (0, 255, 0)
                else: pixels[width, height] = (0, 0, 255) #B
        return image








