def need_processing(self):
        readers = []
        writers = []
        timer_heap = []
        for c in iter(self._connections.values()):
            if c.needs_input > 0:
                readers.append(c)
            if c.has_output > 0:
                writers.append(c)
            if c.deadline:
                heapq.heappush(timer_heap, (c.next_tick, c))
        timers = []
        while timer_heap:
            x = heapq.heappop(timer_heap)
            timers.append(x[1])
        return (readers, writers, timers)