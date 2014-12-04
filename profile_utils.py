import time
import sys
import numpy as np


class Timer():
    def __init__(self):
        self._manual_start_time = None
        self.start_time = None
        if sys.platform == 'win32':
            self.default_timer = time.clock
        else:
            self.default_timer = time.time

    def tic(self):
        self._manual_start_time = self.default_timer()

    def toc(self):
        return self.default_timer() - self._manual_start_time

    def __enter__(self):
        self.start_time = self.default_timer()
        return self

    def __exit__(self, *args):
        self.end_time = self.default_timer()
        self.interval = self.start_time - self.end_time


class Profiler():
    def __init__(self):
        self.timer = Timer()

    def profile(self, eval_str, number=10000):
        times = np.empty(number)
        for i in range(number):
            self.timer.tic()
            eval(eval_str)
            times[i] = self.timer.toc()

        stats = {
            "mean": np.mean(times),
            "stdev": np.std(times),
            "min": np.min(times),
            "max": np.max(times)
        }

        print("Runs: {}\nMean time: {}us\nStandard deviation: {}us".format(number, stats["mean"], stats["stdev"]))
        return stats