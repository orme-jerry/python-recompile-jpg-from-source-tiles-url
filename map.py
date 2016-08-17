import Image
import urllib
import cStringIO


directory = "/home/usr/Pictures/"

def getImages():
    for tile_group in range(0, 2):
        for x in range(0, 16):
            for y in range(0, 13):
                filename = "http://ogimages.bl.uk/images/zoomify/007/007000000000016U00016000/TileGroup" + str(
                    tile_group) + "/4-" + str(
                    x) + "-" + str(y) + ".jpg"
                try:
                    file1 = cStringIO.StringIO(urllib.urlopen(
                        filename).read())
                    img = Image.open(file1)
                    img.save(directory + "tile_" + str(x) + "_" + str(y) + ".jpg", "JPEG", quality=100)
                except IOError:
                    print "Image at (" + str(x) + ", " + str(y) + ") does not exist in Tile Group " + str(
                        tile_group) + "!"
                    pass

def reconstruct():
    new_canvas = Image.new("RGB", (15*256+160, 12*256+31), (255, 255, 255))
    for x in range(0, 16):
        for y in range(0, 13):
            filename = directory + "tile_" + str(x) + "_" + str(y) + ".jpg"
            img = Image.open(filename)
            new_canvas.paste(img, (256 * x, 256 * y))
    new_canvas.save(directory + "map.jpg", "JPEG", quality = 100)

def main():

    getImages()
    reconstruct()

if __name__ == "__main__":
    main()
