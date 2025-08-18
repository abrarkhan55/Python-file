#method overriding

class parentclass:
    def __init__(self):
        print("Im parent class")

class childclass (parentclass):  #ai khane parent class declared kore dissi jonno inharitance kortese
    def __init__(self):  # aita overriding kortese parentclass k
        super().__init__() #aikhane super function used korar jonno amr 2 ta class key print kortese
        print("Im overriding in parent class")

C=childclass()