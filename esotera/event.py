class Event:
    """
    The Event class serves as a notification that an event has happened in the
    game world.
    
    In general, an event has a source and optional targets. It may eventually
    contain information about its location, the type of information it is
    (audio, visual etc) and their ranges.  Events are used by other objects to
    observe what has happened in the world. Thus, actions taken by objects will
    fire events.  """

    def __init__(self, source, targets = None):
        """Default constructor for a new Event"""
        self.source = source
        self.targets = targets

    def __str__(self):
        """Convey the Event as a statement in english."""
        target_strings = 'nothing'
        if self.targets:
            target_strings = ', '.join(self.targets)
        message_string = '{0} generated a generic Event targeted at: {1}.' 
        return message_string.format(self.source, target_strings)

