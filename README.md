# RPC Microservice Challenge

## Getting started

```bash
docker-compose up
```

```bash
➜  rpc_microservice_challenge git:(master) ✗ docker exec -it rpc_microservice_challenge_rpc_microservice_1 ./entrypoint.sh nameko shell --config nameko_config.yml
>>> n.rpc.greeting_service.hello('arnoux')
'Hello, arnoux!'
```