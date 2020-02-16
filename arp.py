import argparse
from services.do import do

parser = argparse.ArgumentParser()

parser.add_argument("image",
                    default=None,
                    help="path of an input image (JPEG/PNG/ARP)")
parser.add_argument("--out",
                    default=None,
                    required=False,
                    help="path where ARP image will be stored")
parser.add_argument("--hex",
                    default=False,
                    action="store_true",
                    required=False,
                    help="hex dump of image")
parser.add_argument("--add",
                    default=None,
                    required=False,
                    help="image that will be added to the given ARP image")
parser.add_argument(
    "--n_colors",
    default=256,
    required=False,
    help=
    "number of distinct colors to be used for an image frame (pallette size)")
parser.add_argument("--remove",
                    default=-1,
                    required=False,
                    help="image frame index to be removed (defaults to last)")
parser.add_argument(
    "--timeout",
    default=1,
    required=False,
    help="time interval (in seconds) between image frame render")
parser.add_argument("--show",
                    default=False,
                    required=False,
                    action="store_true",
                    help="renders image in using Matplotlib.")
args = parser.parse_args()
do(args)
