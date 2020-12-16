import unittest
from rpc_microservice_challenge.lib.string_compression import compress_strings, decompress_bytes


class TestStringCompression(unittest.TestCase):

    def test_compresses_strings(self):
        self.assertEqual(compress_strings('hello', 'hi', 'howdie'), {
                         'hello': b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15', 'hi': b'x\x9c\xcb\xc8\x04\x00\x01;\x00\xd2', 'howdie': b'x\x9c\xcb\xc8/O\xc9L\x05\x00\x08\xe0\x02\x81'})

    def test_when_no_args_returns_empty_dict(self):
        self.assertEqual(compress_strings(), {})

    def test_decompresses_bytes_back_to_string(self):
        self.assertEquals(decompress_bytes(
            b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15'), 'hello')
