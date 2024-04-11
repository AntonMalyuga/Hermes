import argparse
from HermesSys import Sys


choices = [
    'delete_order',
    'create_order'
]
parser = argparse.ArgumentParser()
parser.add_argument('-v', type=int, help='First argument', nargs=1)

parser.add_argument('-a', '--action', required=True, choices=choices)

args = parser.parse_args()

match args.action:
    case 'delete_order':
        Sys().delete_order(args.v)