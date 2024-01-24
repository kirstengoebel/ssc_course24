import argparse


def argument_parser():
    parser = argparse.ArgumentParser(
        description="Input Reads for Analysis Measured Data package"
    )
    parser.add_argument("-p", "--path", help="Input File")

    args = parser.parse_args()

    return args
