class Actor:
    """The actor class is the base class for entities that can perform actions. They are not necessarily organic (i.e. they might represent political, religious or social bodies)."""
    
    #class variables
    number = 0

    def __init__(self, name = None):
        if name:
            self.name = name
        else:
            Actor.number += 1
            self.name = "Actor" + str(Actor.number)
    def offer(self, target, give, receive):
        pass
    def exchange(self, target, give, receive):
        pass
    def accept(self, source, give, receive):
        pass
