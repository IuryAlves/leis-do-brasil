# coding: utf-8


def get_output_class(type_):
    output_strategy = {
        'file': FileOutput
    }

    try:
        return output_strategy[type_]
    except KeyError:
        raise Exception('Output type: {0} does not exist'.format(type_))


class BaseOutput(object):

    def write(self, *args, **kwargs):
        raise NotImplementedError


class FileOutput(BaseOutput):
    """
    Save the output to a file
    """

    def __init__(self, path=''):
        self.path = path

    def write(self, name, contents):
        with open(self.path + '/' + name, 'w', encoding='utf-8') as fp:
            fp.write(contents)
