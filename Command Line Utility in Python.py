import argparse
import sys

def calc(args):
    if args.o == 'add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x *args.y

    elif args.o == 'sub':
        return args.x - args.y

    elif args.o == 'div':
        return args.x  / args.y

    else:
        return "Something went wrong"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type = float, default=1.0,
                        help = "Enter a number.This is a utility for doing basic calculations")
    parser.add_argument('--y', type=float, default=1.0,
                        help="Enter a number.This is a utility for doing basic calculations")
    parser.add_argument('--o', type=str, default='add',
                        help="Enter operation you want to perform.This is a utility for doing basic calculations")

    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))