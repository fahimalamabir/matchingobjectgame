import os

IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 4

ASSETS_DIR = 'assets'
ASSETS_FILES = [x for x in os.listdir(ASSETS_DIR) if x[-3:].lower() == 'png']

assert len(ASSETS_FILES) == 8
