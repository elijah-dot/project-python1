class User:
    """
    Class that generates new instances of users.
    """
    user_list=[]
    def __init__(self,username,userpassword):
        self.username = username
        self.userpassword = userpassword
        # self.generated_password=generated_password 
        
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        
        User.user_list.append(self)
        
    def  login(self):
        if User in User.user_list:
            print(User)
            return User
 