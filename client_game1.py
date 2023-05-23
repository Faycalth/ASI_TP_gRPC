import grpc
import game_pb2
import game_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = game_pb2_grpc.GameServiceStub(channel)
    choice = 1
    while 1 <= int(choice) <= 5:
        print("---------------------")
        print("1 : Retourne la liste des cartes")
        print("2 : Retourne la liste des utilisateurs")
        print("3 : Acheter la carte")
        print("4 : Vendre la carte")
        print("5 : Voir mes informations")
        print("---------------------")
        choice = input("Votre choix : ")
        if int(choice) == 1 :
            response = stub.GetCardList(game_pb2.Empty())
            print(response.message)
        elif int(choice) == 2 :
            response = stub.GetUserList(game_pb2.Empty())
            print(response.message)
        elif int(choice) == 3:
            response = stub.GetCardList(game_pb2.Empty())
            print(response.message)
            choice = input("L'id de votre carte :")
            response = stub.BuyCard(game_pb2.IdCard(id=choice))
            print(response.message)
        elif int(choice) == 4:
            response = stub.GetCardList(game_pb2.Empty())
            print(response.message)
            choice = input("L'id de votre carte :")
            response = stub.SellCard(game_pb2.IdCard(id=str(choice)))
            print(response.message)
        elif int(choice) == 5:
            response = stub.GetInfoUser(game_pb2.Empty())
            print(response.message)
    
    print("FIN")
    

if __name__ == '__main__':
    run()