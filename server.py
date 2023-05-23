import grpc
import example_pb2
import example_pb2_grpc
from concurrent import futures

class ExampleServicer(example_pb2_grpc.ExampleServiceServicer):
    def SayHello(self, request, context):
        name = request.name
        message = f"Hello, {name}!"
        return example_pb2.HelloResponse(message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_ExampleServiceServicer_to_server(
        ExampleServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
