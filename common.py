from google.protobuf.any_pb2 import Any
from proto import chat_pb2 as messages

def pack_message_from_input():
    text = input("send< ")
    a = Any()
    a.Pack(messages.InternalMessage(text=text))
    message = messages.Message(detail=a)
    print(f"sending: '{message}'")
    return message

def unpack_message(message) -> None:
    if message.detail.type_url == "type.googleapis.com/InternalMessage":
        unpacked = messages.InternalMessage()
        message.detail.Unpack(unpacked)
        print(f"got> '{unpacked}'")
    else:
        print(f"got> '{detail}'")
