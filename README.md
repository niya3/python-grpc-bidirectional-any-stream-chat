**Simple bidirectonal any-stream gRPC-chat in Python**


Provides simple example of bidirectional gRPC streams usage in Python,
in which messages wrapped in [`Any`](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/any.proto)
type are exchanged.

# Set up and run

## "Server" shell

```bash
$ make venv
$ make protos
$ make server
```

## "Client" shell

```bash
$ make client
```

# Usage

Run both server and client sessions, type something in one of them  and press `Enter`

# Example session logs

## "Client" shell

```
make client
...
send< hello
sending: 'detail {
  type_url: "type.googleapis.com/InternalMessage"
  value: "\n\005hello"
}
'
send< got> 'text: "world"
'
```

## "Server" shell

```
make server
...
send< got> 'text: "hello"
'
world
sending: 'detail {
  type_url: "type.googleapis.com/InternalMessage"
  value: "\n\005world"
}
'
send<
```
