import grpc
import game_pb2
import game_pb2_grpc
from GameManager import GameManager
from concurrent import futures

class GameServicer(game_pb2_grpc.GameServiceServicer):
    def __init__(self):
        super().__init__()
        self.game_manager = GameManager()

    def GetCardList(self, request, context):
        message = self.game_manager.get_card_list()
        return game_pb2.CardList(message=message)

    def GetUserList(self, request, context):
        message = self.game_manager.get_user_list()
        return game_pb2.UserList(message=message)
    
    def BuyCard(self, request, context):
        message = self.game_manager.buy_card(request.id)
        return game_pb2.CardBought(message=message)

    def SellCard(self, request, context):
        message = self.game_manager.sell_card(request.id)
        return game_pb2.CardSold(message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    game_pb2_grpc.add_GameServiceServicer_to_server(GameServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
