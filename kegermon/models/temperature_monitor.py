import time

class TemperatureMonitor:

    def record(self, data):
        dat = data.copy()
        dat['timestamp'] = self._currentTimestamp()
        print("Recording data: ", dat)

    @staticmethod
    def _currentTimestamp():
        return int(time.time())
