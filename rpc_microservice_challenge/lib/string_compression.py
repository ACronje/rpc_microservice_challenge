import zlib


def string_compression(*strings):
    return {string: zlib.compress(string.encode()) for string in strings}
