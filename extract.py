import argparse
import common
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-i', action='store', dest='input_file', required=True, help='Input file')
parser.add_argument('-o', action='store', dest='output_file', required=True, help='Output file')
parser.add_argument('--league', action='store')
parser.add_argument('--owner', action='store')
parser.add_argument('--guest', action='store')
args = parser.parse_args()

key_to_val = {}

if args.league:
    key_to_val['league_name'] = args.league
if args.owner:
    key_to_val['owner'] = args.owner
if args.guest:
    key_to_val['guest'] = args.guest

common.select_from_file(args.input_file, args.output_file, key_to_val)