import time
import kegermon

class TemperatureMonitor:

    def __init__(self, redis_store):
        self.redis_store = redis_store
        self.logger = kegermon.app.logger

    def record(self, data):
        event_id  = str(self.redis_store.incr('events:id'))
        event_key = 'event:{id}'.format(id=event_id)
        data['id'] = event_id
        data['timestamp'] = self._currentTimestamp()

        pipe = self.redis_store.pipeline(True)
        pipe.hmset(event_key, data)
        self.redis_store.zadd('events', **{event_key: data['timestamp']})
        pipe.execute()

        self.logger.debug(f"Record data: {data}")

    def fetch(self, num=10):
        ids  = self.redis_store.zrevrangebyscore('events', '+inf', '-inf', start=0, num=num)
        pipe = self.redis_store.pipeline(True)
        [pipe.hgetall(id) for id in ids]
        events = pipe.execute()

        return events

    @staticmethod
    def _currentTimestamp():
        return int(time.time())
