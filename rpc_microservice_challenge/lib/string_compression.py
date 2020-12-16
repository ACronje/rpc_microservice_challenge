import zlib


def compress_strings(*strings):
    return {string: zlib.compress(string.encode()) for string in strings}


def decompress_bytes(compressed_bytes):
    return zlib.decompress(compressed_bytes).decode()
