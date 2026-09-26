def done(self):
        if self._process is None:
            raise AirflowException("Tried to see if it's done before starting!")
        if self._done:
            return True
        if self._result_queue and not self._result_queue.empty():
            self._result = self._result_queue.get_nowait()
            self._done = True
            self.log.debug("Waiting for %s", self._process)
            self._process.join()
            return True
        if self._result_queue and not self._process.is_alive():
            self._done = True
            if not self._result_queue.empty():
                self._result = self._result_queue.get_nowait()
            self.log.debug("Waiting for %s", self._process)
            self._process.join()
            return True
        return False