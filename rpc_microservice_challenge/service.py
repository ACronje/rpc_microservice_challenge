from nameko.rpc import rpc
from rpc_microservice_challenge.lib.square_odd_numbers import square_odd_numbers


class Service:
    name = "service"

    @rpc
    def square_odd_numbers(self, *numbers):
        return square_odd_numbers(*numbers)
