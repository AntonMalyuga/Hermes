import argparse
from Sys import SysAPI
from Hermes import HermesAPI

choices = [
    'delete_order',
    'rollback_order'
]
parser = argparse.ArgumentParser()

parser.add_argument('-a', '--action', required=True, choices=choices)
parser.add_argument('-v', type=int, help='First argument', nargs=1)

args = parser.parse_args()

match args.action:
    case 'delete_order':
        SysAPI().delete_order(args.v)
    case 'rollback_order':
        HermesAPI().rollback_order(args.v)
