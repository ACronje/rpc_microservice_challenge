import base64
from nameko.rpc import rpc
from rpc_microservice_challenge.lib.square_odd_numbers import square_odd_numbers
from rpc_microservice_challenge.lib.string_compression import compress_strings, decompress_bytes


class Service:
    name = 'service'

    @rpc
    def square_odd_numbers(self, *numbers):
        return square_odd_numbers(*numbers)

    @rpc
    def compress_strings(self, *strings):
        return {key: base64.b64encode(value).decode() for key, value in compress_strings(*strings).items()}

    @rpc
    def decompress_string(self, compressed_b64_string):
        return decompress_bytes(base64.b64decode(compressed_b64_string))
