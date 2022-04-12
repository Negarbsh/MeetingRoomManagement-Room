import logging
from concurrent import futures

import room_pb2
import room_pb2_grpc
import grpc


class MyServer(room_pb2_grpc.RoomServicer):
    def GetCapacity(self, request, context):
        print(request)
        print(request.id)
        return room_pb2.RoomCapacity(capacity=1234)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    room_pb2_grpc.add_RoomServicer_to_server(MyServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
