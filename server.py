from concurrent import futures
from proto import chat_pb2_grpc as services
from threading import Thread
import common
import grpc

def receive_messages(requests_iterator):
    for message in requests_iterator:
        common.unpack_message(message)


class ChatServicer(services.ChatServicer):

    def Communicate(self, requests_iterator, context):
        th = Thread(target=receive_messages, args=(requests_iterator,))
        th.start()

        while True:
            yield common.pack_message_from_input()

        th.join()


def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    services.add_ChatServicer_to_server(ChatServicer(), server)
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    run()
