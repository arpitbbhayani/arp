import argparse
from services.do import do

parser = argparse.ArgumentParser()

parser.add_argument("image", default=None, help="path of an input image")

args = parser.parse_args()

do(args.image)
