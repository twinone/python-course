import argparse
import search
import logging
import gui

#Configure logger options and format
logging.basicConfig(filename='catties.log', level=logging.DEBUG,\
        format="%(asctime)s %(levelname)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


def _init_parser():
    #Declare parser
    parser = argparse.ArgumentParser(description='Get images from the web given a keyword')

    #Optional arguments
    parser.add_argument("-k", "--keyword", type=str, help='Word to find. Pex: "Cats"')
    parser.add_argument("-n", "--num_results", type=int, help="Number of images to download")


    parser.add_argument("-u", "--user_interface", action="store_true", help='Height of Cylinder')
    parser.add_argument("-l", "--log", action="store_true", help="Activate loggin")
    parser.add_argument("-c", "--console", action="store_true", help="Do not run UI")

    try:
        # Run the parser
        return parser.parse_args()
    except:
        #if invalid data print help and exit
        parser.print_help()
        exit()

def parse():
    #Get the data from the parser
    args = _init_parser()

    if args.user_interface:
        gui.open_ui()
        exit()

    key = args.keyword
    num = args.num_results

    search.do_search(key, num)



if __name__ == "__main__":
    parse()