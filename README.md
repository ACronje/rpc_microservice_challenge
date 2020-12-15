# RPC Microservice Challenge

## Getting started

```bash
docker-compose up
```

### Square odd numbers:

```bash
➜  rpc_microservice_challenge git:(master) ✗ docker exec -it rpc_microservice_challenge_rpc_microservice_1 ./entrypoint.sh nameko shell --config nameko_config.yml
>>> n.rpc.service.square_odd_numbers(1,2,3)
[1, 9]
```

### String compression:

```bash
➜  rpc_microservice_challenge git:(master) ✗ docker exec -it rpc_microservice_challenge_rpc_microservice_1 ./entrypoint.sh nameko shell --config nameko_config.yml
>>> n.rpc.service.string_compression('Howdie', 'Hello', 'Hi')
{'Howdie': 'eJzzyC9PyUwFAAggAmE=', 'Hello': 'eJzzSM3JyQcABYwB9Q==', 'Hi': 'eJzzyAQAAPsAsg=='}
```

### String decompression:

```bash
➜  rpc_microservice_challenge git:(master) ✗ docker exec -it rpc_microservice_challenge_rpc_microservice_1 ./entrypoint.sh nameko shell --config nameko_config.yml
>>> n.rpc.service.string_decompression('eJzzyC9PyUwFAAggAmE=')
'Howdie'
```
