import argparse
import search
import gui



def _init_parser():
    #Declare parser
    parser = argparse.ArgumentParser(description='Get images from the web given a keyword')

    #Optional arguments
    parser.add_argument("-k", "--keyword", type=str, help='Word to find. Pex: "Cats"')
    parser.add_argument("-n", "--num_results", type=int, help="Number of images to download")


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

    if not args.console:
        gui.open_ui()
        exit()

    key = args.keyword
    num = args.num_results

    if not key: key = "kittens"
    if not num: num = 5

    search.do_search(key, num)



if __name__ == "__main__":
    parse()