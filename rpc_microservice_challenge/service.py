import base64
from nameko.rpc import rpc
from rpc_microservice_challenge.lib.square_odd_numbers import square_odd_numbers
from rpc_microservice_challenge.lib.string_compression import string_compression, string_decompression


class Service:
    name = 'service'

    @rpc
    def square_odd_numbers(self, *numbers):
        return square_odd_numbers(*numbers)

    @rpc
    def string_compression(self, *strings):
        return {key: base64.b64encode(value).decode() for key, value in string_compression(*strings).items()}

    @rpc
    def string_decompression(self, compressed_b64_string):
        return string_decompression(base64.b64decode(compressed_b64_string))
