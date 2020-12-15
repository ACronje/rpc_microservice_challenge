import zlib


def string_compression(*strings):
    return {string: zlib.compress(string.encode()) for string in strings}


def string_decompression(compressed):
    if isinstance(compressed, str):
        return compressed

    return zlib.decompress(compressed).decode()
