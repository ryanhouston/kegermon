class Tap:

    def __init__(self, name=None, style=None, description=None, position=None):
        self.name = name
        self.style = style
        self.description = description
        self.position = position


class TapSummary:

    def __init__(self, redis_store):
        self.redis_store = redis_store

    def clear(self, position):
        self.redis_store.delete(f'tap:{position}')

    def save(self, tap):
        key = f'tap:{tap.position}'
        self.redis_store.hmset(key, tap.__dict__)

    def taps(self):
        pipe = self.redis_store.pipeline()
        [pipe.hgetall(f'tap:{i}') for i in range(1, 5)]
        taps = [Tap(**row) for row in pipe.execute()]
        return taps
