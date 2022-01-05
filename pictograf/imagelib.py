from PIL import Image

DEFAULT_IMAGE_WIDTH = 600

def get_new_width_and_height(old_width, old_height, new_width):
    wpercent = new_width / float(old_width)
    new_height = int((float(old_height) * float(wpercent)))

    return (new_width, new_height)


def resize(image_full_path):
    img = Image.open(image_full_path)

    width, height = get_new_width_and_height(img.size[0], img.size[1], DEFAULT_IMAGE_WIDTH)
    img = img.resize((width, height), Image.ANTIALIAS)

    img.save(f"{image_full_path}")