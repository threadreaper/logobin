#!/usr/bin/env python
"""
8227l logo.bin helper
Michael Podrybau
email: threadreaper@gmail.com
https://github.com/threadreaper
"""
import argparse
import sys
from pathlib import Path


def get_args():
    """Get command line arguments"""
    description = "Utility to create logo.bin files for 8227l head units"
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("-c", metavar="(file)",
                     help="Test a file for the presence of a valid header.")
    arg.add_argument("-u", metavar="(logo.bin file)",
                     help="Unpack logo.bin to a header and image file.")
    arg.add_argument("-p", metavar='(header file) (image file) '
                                   '(optional: filename)', nargs='?',
                     help="Pack header and image into a flashable binfile."
                          "If not given, filename defaults to logo.bin")
    return arg


def parse_args_exit(parser):
    """Process arguments and exit."""
    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    if args.c:
        file = Path(args.c)
        if not file.is_file():
            print("Target to check must be a file.")
            sys.exit(1)
        with open(file, 'rb') as testfile:
            testbytes = testfile.read()
            if check(testbytes) != 0:
                print("%s does not appear to contain a valid header." % file)
                sys.exit(0)
            print("Valid header detected in %s" % file)
            sys.exit(0)

    if args.u:
        lbin = Path(args.u)
        if not lbin.is_file():
            print("Target to unpack must be a file.")
            sys.exit(1)
        with open(lbin, 'rb') as test:
            testbytes = test.read()
            if check(testbytes) != 0:
                print("%s does not appear to contain a valid header." % lbin)
                sys.exit(1)
        logo_bin_unpack(lbin)
        sys.exit(0)

    if args.p:
        if len(args.p) < 2:
            print("-p option requires at least two arguments.")
            sys.exit(1)
        elif len(args.p) > 3:
            print("Too many arguments given for option -p.")
            sys.exit(1)
        header = Path(args.p[0])
        bmp = Path(args.p[1])
        if not header.is_file() or not bmp.is_file():
            print("You must supply a valid header and bitmap file to pack a bin.")
            sys.exit(1)
        if len(args.p) == 3:
            filename = args.p[2]
        else:
            filename = 'logo.bin'
        logo_bin_pack(header, bmp, filename)


def check(these_bytes):
    """Tests a file for presence of a valid header"""
    test = str(these_bytes[8:12])
    if test[2:6] != 'logo':
        return 1
    return 0


def logo_bin_pack(header, bmp, filename):
    """Packs a flashable bin file given a valid header, a bitmap
    and an optional filename as input"""
    with open(filename, 'wb') as output:
        with open(header, 'rb') as headerbytes:
            headerout = headerbytes.read()
            if check(headerout) != 0:
                print("Header file appears to be invalid. Hint: header"
                      " file must be the first argument.")
                sys.exit(1)
        output.write(headerout)
        with open(bmp, 'rb') as bmpbytes:
            bmpout = bmpbytes.read()
        output.write(bmpout)
        print("%s generated successfully!" % filename)
        sys.exit(0)


def logo_bin_unpack(lbin):
    """Given a logo.bin file as input, tests to make sure it is valid
     and then unpacks it"""
    with open(lbin, 'rb') as file:
        header = file.read(512)
        bmp = file.read()
    if check(header) != 0:
        print("Input does not appear to contain a valid header.")
        sys.exit(1)
    with open('header.bin', 'wb') as headerout:
        headerout.write(header)
    with open('logo.bmp', 'wb') as bmpout:
        bmpout.write(bmp)
    print("%s was successfully unpacked!" % lbin)


def main():
    parser = get_args()
    parse_args_exit(parser)


if __name__ == "__main__":
    main()
