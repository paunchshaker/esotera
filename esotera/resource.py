class Resource:
    """The Resource class serves to represent game resources. Resources are
    items required or desired by actors."""

    def __init__(self, kind, quantity):
        """Setup the kind and quantity of the resource"""
        self.kind = kind
        self.quantity = quantity

    def __add__(self, other):
        """Increase the quantity of resources of the same kind or by a number"""
        value = other
        if isinstance(other, Resource):
            if other.kind == self.kind:
                value = other.quantity
            else:
                raise TypeError
        return Resource(self.kind, self.quantity + value)
    
    def __iadd__(self, other):
        """Increase the quantity of resources of the same kind or by a number"""
        value = other
        if isinstance(other, Resource):
            if other.kind == self.kind:
                value = other.quantity
            else:
                raise TypeError
        self.quantity = self.quantity + value
        return self
    
    def __sub__(self, other):
        """Decrease the quantity of resources of the same kind or by a number"""
        value = other
        if isinstance(other, Resource):
            if other.kind == self.kind:
                value = other.quantity
            else:
                raise TypeError
        #Note that this allows negative resource quantities. Do we want to 
        #do this? It could be useful.
        return Resource(self.kind, self.quantity - value)
    
    def __isub__(self, other):
        """Decrease the quantity of resource by the same kind or by a number"""
        value = other
        if isinstance(other, Resource):
            if other.kind == self.kind:
                value = other.quantity
            else:
                raise TypeError
        #Note that this allows negative resource quantities. Do we want to 
        #do this? It could be useful.
        self.quantity = self.quantity - value
        return self
    
    def __mul__(self, other):
        """Multiply the quantity of a resource by the quantity of the same 
        kind or by a number"""
        value = other
        if isinstance(other, Resource):
            if other.kind == self.kind:
                value = other.quantity
            else:
                raise TypeError
        #Note that this allows negative resource quantities. Do we want to do 
        #this? It could be useful.
        return Resource(self.kind, self.quantity * value)
    
    def __floordiv__(self, other):
        """Divide the quantity of a resource by the quantity of the same kind 
        or by a number"""
        value = other
        if isinstance(other, Resource):
            if other.kind == self.kind:
                value = other.quantity
            else:
                raise TypeError
        #Note that this allows negative resource quantities. Do we want to 
        #do this? It could be useful.
        return Resource(self.kind, self.quantity // value)

    def __str__(self):
        return "{0} {1}".format(self.quantity, self.kind)

    def __hash__(self):
        return self.kind.__hash__() ^ self.__class__.__name__.__hash__()

    def __eq__(self, other):
        return self.kind == other.kind

    def __ne__(self, other):
        return not self.__eq__(other)
