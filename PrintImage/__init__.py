from .classes import Output


def convert(args):
    Output(args).convert()


def export(args):
    Output(args).export()


if '__name__' == '__main__':
    exit(0)
