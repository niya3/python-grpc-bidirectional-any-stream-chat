# make parameters
SHELL = bash
.ONESHELL:

.PHONY: all
all: venv protos server

venv: requirements.txt
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

.PHONY: protos
protos: ./proto/chat_pb2_grpc.py ./proto/chat_pb2.py

./proto/chat_pb2_grpc.py: ./proto/chat.proto
	python -m grpc_tools.protoc -I. --grpc_python_out=. $<

./proto/chat_pb2.py: ./proto/chat.proto
	python -m grpc_tools.protoc -I. --python_out=. $<

.PHONY: client server
client server:
	source venv/bin/activate
	python ./$@.py

.PHONY: clean
clean:
	rm -rf ./__pycache__/
	rm -rf ./proto/*pb*
	rm -rf ./proto/__pycache__/
	rm -rf ./venv/
