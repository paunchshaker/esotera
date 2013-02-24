class Event:
    """
    The Event class serves as a notification that an event has happened in the game world.
    
    In general, an event has a source and optional targets. It may eventually contain information about its location, the type of information it is (audio, visual etc) and their ranges.
    Events are used by other objects to observe what has happened in the world. Thus, actions taken by objects will fire events.
    """

    def __init__(self, source, targets = None):
        self.source = source
        self.targets = targets

    def __str__(self):
        target_strings = 'nothing'
        if self.targets:
            target_strings = ', '.join(self.targets)
        return '{0} generated a generic Event targeted at: {1}.'.format(self.source, target_strings)

