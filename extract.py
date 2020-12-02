import argparse
import common
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-i', action='store', dest='input_file', required=True, help='Input file')
parser.add_argument('-o', '--owner', action='store', required=True)
parser.add_argument('-g', '--guest', action='store', required=True)
args = parser.parse_args()

common.select_from_file(args.input_file, args.owner, args.guest)