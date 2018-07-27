# -*- coding: utf-8 -*-

"""
This is the main file, it is invoked when someone runs python like:
    python -m vegasave
"""
import argparse
from .save_vega import save_from_file


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('spec_file_name', type=str, help='Path to spec to compile into an image.')
    parser.add_argument('mode', type=str, help='vega-lite or vega')
    parser.add_argument('file_name', type=str, help='Where this should be saved too.')

    args = parser.parse_args()

    save_from_file(args.spec_file_name, args.mode, args.file_name)

if __name__ == "__main__":
    main()