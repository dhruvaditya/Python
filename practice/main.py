class User:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.user_name=user_name
        self.follower=0;
        self.following=0

    def follow(self,user):
        user.follower+=1;
        self.following+=1
User1=User("001","Aditya")
User2=User("002","Abhigyan")
User1.follow(User2)
print(User2.follower)
print(User2.following)
print(User1.follower)
print(User1.following)
User3=User("003","Satyam")
User3.follow(User1)
User2.follow(User1)
print(User1.follower)