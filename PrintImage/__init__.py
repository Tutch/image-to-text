from .classes import Output


def convert(source_image, dest_image):
    Output.convert(source_image, dest_image)


def export(source_image, dest_file):
    Output.export(source_image, dest_file)


if '__name__' == '__main__':
    exit(0)
