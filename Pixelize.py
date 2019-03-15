import sys
from PIL import Image

RED_INDEX = 0
GREEN_INDEX = 1
BLUE_INDEX = 2
ALPHA_INDEX = 3


def main():
    image_name = sys.argv[1]
    pixel_size = sys.argv[2]
    image = Image.open(image_name)
    pixelize(image, pixel_size)


def pixelize(image, pixel_size):

    row = 0
    pixel_image = image.copy()
    while row < image.height - pixel_size:

        col = 0
        while col < image.width - pixel_size:
            avg_color = average_color(image, pixel_size, row, col)
            set_color(pixel_image, pixel_size, row, col, avg_color)
            col += pixel_size

        row += pixel_size

    pixel_image.show()


def average_color(image, pixel_size, row, col):

    r = 0
    g = 0
    b = 0
    a = 0

    row_end = row + pixel_size
    col_end = col + pixel_size

    count = 0
    curr_row = row
    while curr_row < row_end:
        curr_col = col
        while curr_col < col_end:
            curr_pixel = image.getpixel((curr_col, curr_row))
            r += curr_pixel[RED_INDEX]
            g += curr_pixel[GREEN_INDEX]
            b += curr_pixel[BLUE_INDEX]
            a += curr_pixel[ALPHA_INDEX]
            curr_col += 1
            count += 1
        curr_row += 1

    avg = (r/count, g/count, b/count, a/count)

    return avg


def set_color(image, pixel_size, row, col, avg):

    row_end = row + pixel_size
    col_end = col + pixel_size

    curr_row = row

    while curr_row < row_end:
        curr_col = col
        while curr_col < col_end:
            image.putpixel(xy=(curr_col, curr_row), value=avg)
            curr_col += 1

        curr_row += 1


if __name__ == "__main__":
    main()
