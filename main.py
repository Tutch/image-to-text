
from PIL import Image
import argparse
import PrintImage as pi

def get_arg():
    parser = argparse.ArgumentParser(
        description='Converts an image to a text-based version of that image'
    )
    
    parser.add_argument(
        '-image',
        nargs=1,
        type=str,
        dest='image',
        help='Image to convert',
        required=True
    )

    parser.add_argument(
        '-font',
        nargs='?',
        type=str,
        dest='font',
        help='Font to use. Options are lucida (default) and braciola',
        const='lucida',
        default='lucida',
        required=False
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        '-c',
        nargs='?',
        type=str,
        dest='format',
        help='Converts this image to a text image',
        const='png',
        default=None,
        required=False
    )

    group.add_argument(
        '-e',
        action='store_true',
        dest='export',
        help='Exports the results to a text file',
        default=False,
        required=False
    )

    arg = parser.parse_args()
    
    if arg.export is False and arg.format is None:
        parser.error("At least one of -e and -c required")

    return arg

if __name__ == '__main__':
    args = get_arg()

    if args.export is not False:
        pi.export(args)
    elif args.format is not None:
        pi.convert(args)
