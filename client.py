from proto import chat_pb2_grpc as services
import common
import grpc


def send_messages():
    while True:
        yield common.pack_message_from_input()


def run():
    channel = grpc.insecure_channel("127.0.0.1:50051")
    stub = services.ChatStub(channel)

    for message in stub.Communicate(send_messages()):
        common.unpack_message(message)


if __name__ == "__main__":
    run()
