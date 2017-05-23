class Tap:

    def __init__(self, name, style, description, position):
        self.name   = name
        self.style  = style
        self.description = description
        self.position = position

    @classmethod
    def null(cls, position):
        return Tap(name = 'Empty', position = position,
                   style = '', description = '')

    def isEmpty(self):
        return name == 'Empty'

class TapSummary:

    def taps(self):
        return [
                Tap(name     = 'Blondie',
                    style    = 'Blonde Ale',
                    position = 1,
                    description = 'Light and easy'),
                Tap(name     = 'Big Brown',
                    style    = 'American Brown Ale',
                    position = 2,
                    description = 'Dark and bold'),
                Tap.null(position = 3),
                Tap(name     = 'Soda Water',
                    style    = 'not beer',
                    position = 4,
                    description = 'Cool, refreshing, bubbly water.'),
        ]
