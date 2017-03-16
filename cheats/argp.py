import argparse
from math import pi
import logging

# Configure logger options and format
logging.basicConfig(filename='cylinder.log', level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


def cylinder_volume(radius, height):
    return pi * (radius ** 2) * height


def init_parser():
    # Declare parser
    parser = argparse.ArgumentParser(
        description='Calculate volume of a Cylinder')

    # Mandatory arguments
    parser.add_argument("radius", type=int,
                        help='Radius of Cylinder', default="1")

    # Optional arguments
    parser.add_argument("-H", "--height", type=int, metavar="",
                        required=True, help='Height of Cylinder')
    # Mutex optional arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quiet", action="store_true",
                       help="Print quiet")
    group.add_argument("-v", "--verbose",
                       action="store_true", help="Print vervose")
    try:
        # Run the parser
        return parser.parse_args()
    except:
        # if invalid data print help and exit
        parser.print_help()
        exit()


if __name__ == "__main__":
    # Get the data from the parser
    args = init_parser()
    volume = cylinder_volume(args.radius, args.height)
    logging.info("Volume of a Cylinder with radius {} and height {} is {}".format(
        args.radius, args.height, volume))
    if args.quiet:
        # Executed with "-q"
        print(volume)
    elif args.verbose:
        # Executed with "-v"
        print("Volume of a Cylinder with radius {} and height {} is {}".format(
            args.radius, args.height, volume))
    else:
        # Executed if no optional argument
        print("Volume of Cylinder = {}".format(volume))
