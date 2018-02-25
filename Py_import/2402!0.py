import argparse


parser = argparse.ArgumentParser(description='Process some int')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help ='an integer for accumulate')
parser.add_argument('--sum', dest='accumulate', action ='store_const',
                    const=sum, default=max,
                    help='sum the integers(default:find teh max)')
args = parser.parse_args()
print(args.accumulate(args.imtegers))

