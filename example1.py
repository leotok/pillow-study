# Pillow examples - The Python Image Library

# http://pillow.readthedocs.io/en/3.2.x/handbook/tutorial.html
# http://effbot.org/imagingbook/
# https://www.codementor.io/python/tutorial/image-manipulation-in-python

from PIL import Image
import os, sys


def convert_to_jpeg(img_path):
    f, e = os.path.splitext(img_path)
    outfile = f + ".jpg"
    if img_path != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", img_path)


def create_thumbnail(img_path):

    outfile = os.path.splitext(img_path)[0] + '.thumbnail'
    
    if img_path != outfile:

        try:
            size = (128, 128)
            img = Image.open(img_path)
            img.thumbnail(size)
            img.save(outfile,"JPEG")
            return img

        except IOError:
            print "Cannot create thumbnail for", img_path
        
    return None

def crop_image(img_path):

    try:
        img = Image.open(img_path)
        box = (100, 100, 400, 400) # left, upper, right, lower
        region = img.crop(box)

        return region
    except:
        return None

def rotate_region(img_path):

    try:
        img = Image.open(img_path)
        box = (100, 100, 400, 400) # left, upper, right, lower
        region = img.crop(box)
        region = region.transpose(Image.ROTATE_180)
        img.paste(region,box)

        return img
    except:
        return None


def roll(img_path, delta):

    try:
        img = Image.open(img_path)
        xsize, ysize = img.size

        delta = delta % xsize
        if delta == 0: return img

        part1 = img.crop((0, 0, delta, ysize))
        part2 = img.crop((delta, 0, xsize, ysize))

        img.paste(part2, (0, 0, xsize - delta, ysize))
        img.paste(part1, (xsize - delta, 0, xsize, ysize))



        return img

    except Exception as e:
        print e
        return None


def invert_bands(img_path):

    img = Image.open(img_path)
    r, g, b = img.split()
    gmi = Image.merge("RGB", (b, g, r))

    return gmi

def invert_colors(img):

    width, height = img.size

    new_img = Image.new("RGB", (width, height), "white")
    pixels = new_img.load()

    for i in range(width):
        for j in range(height):

            pixel = img.getpixel((i,j))
        
            pixels[i, j] = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])        

    return new_img

def apply_tan(img):

    width, height = img.size
    tan = 30

    new_img = Image.new("RGB", (width, height), "white")
    pixels = new_img.load()

    for i in range(width):
        for j in range(height):

            pixel = img.getpixel((i,j))
        
            if pixel[0] > 150:
                pixels[i, j] = (pixel[0] - tan, pixel[1] - tan, pixel[2] - tan)
            else:
                pixels[i, j] = (pixel[0], pixel[1], pixel[2])

    return new_img




if __name__ == '__main__':
    
    # img = create_thumbnail("Leo_profile.jpg")
    # img = crop_image("Leo_profile.jpg")
    # img = rotate_region("Leo_profile.jpg")
    # img = roll("Leo_profile.jpg", 150)
    # img = invert_bands("Leo_profile.jpg")

    img = Image.open("Leo_profile.jpg")
    inverted_img = invert_colors(img)
    tanned_img = apply_tan(img)
    
    inverted_img.show()
    tanned_img.show()



    

