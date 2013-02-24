class Resource:
    """The Resource class serves to represent game resources. Resources are items required or desired by actors.
    """
    def __init__(self,type,quantity):
        self.type = type
        self.quantity = quantity
    def __add__(self,other):
        value = other
        if isinstance(other,Resource):
            if other.type == self.type:
                value = other.quantity
            else:
                raise TypeError
        return Resource(self.type,self.quantity + value)
    def __sub__(self,other):
        value = other
        if isinstance(other,Resource):
            if other.type == self.type:
                value = other.quantity
            else:
                raise TypeError
        #Note that this allows negative resource quantities. Do we want to do this? It could be useful.
        return Resource(self.type,self.quantity - value)
    def __mul__(self,other):
        value = other
        if isinstance(other,Resource):
            if other.type == self.type:
                value = other.quantity
            else:
                raise TypeError
        #Note that this allows negative resource quantities. Do we want to do this? It could be useful.
        return Resource(self.type,self.quantity * value)
    def __floordiv__(self,other):
        value = other
        if isinstance(other,Resource):
            if other.type == self.type:
                value = other.quantity
            else:
                raise TypeError
        #Note that this allows negative resource quantities. Do we want to do this? It could be useful.
        return Resource(self.type,self.quantity // value)
