class Resource:
    """The Resource class serves to represent game resources. Resources are items required or desired by actors.
    """
    def __init__(self,type,quantity):
        self.type = type
        self.quantity = quantity
    def __add__(self,other):
        if isinstance(other,Resource):
            value = other
            if other.type == self.type:
                value = other.quantity
            else:
                raise TypeError
        return Resource(self.type,self.quantity + value)
