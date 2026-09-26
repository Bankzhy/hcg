def prepare_epoch(self):
        self.epoch += 1
        if self.epoch >= self.epoch_start_halving and ((self.epoch - self.epoch_start_halving) % self._halving_freq == 0):
            self._lr *= 0.5
        self._current_iter = 0
        self._iters_from_last_valid = 0
        self._train_costs = []
        self.prepared_worker_pool.clear()
        self.batch_pool = range(self.num_train_batches)
        self.rand.shuffle(self.batch_pool)
        if self.epoch > self.end_at:
            self.log("Training is done, wait all workers to stop")
            return False
        else:
            self.log("start epoch {} with lr={}".format(self.epoch, self._lr))
            return True