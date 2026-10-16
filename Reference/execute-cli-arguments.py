#!/usr/bin/python3

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--count', type=int, help="number of values to count")
    parser.add_argument('-s','--string', type=str, help="string to read")

    args = parser.parse_args()

    print(args.string[0:args.count])


if __name__ == "__main__":
    main()
