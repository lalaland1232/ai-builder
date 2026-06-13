
class UserRepository:
    def __init__(self):
        print("User Repository Created")
    def get_user(self,id):
        print ("recieved id is ",id)
        if id == 1:
            return {
    "id": 1,
    "name": "Baba"
}
    