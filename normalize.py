import argparse
import hockey
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-i', action='store', dest='input_file', required=True, help='Input file')
parser.add_argument('-o', action='store', dest='output_file', required=True, help='Output file')
parser.add_argument('-a', action='store_true', dest='append')
parser.add_argument('-s', '--sport', action='store', dest='sport', choices=["hockey"], required=True,
                    help='Kind of sport')
args = parser.parse_args()

if args.sport == "hockey":
    hockey.normalize_file(args.input_file, args.output_file, args.append)
