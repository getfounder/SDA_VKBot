from PIL import ImageGrab


def make_screenshot(bbox, filename):
    image = ImageGrab.grab(bbox=bbox)
    image.save(f"screens/{filename}")
