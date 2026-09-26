def _process_output_chunk(self, start_count, next_idx, sources, i_str,
                              t_path):
        if not self.t_chunk:
            return []
        self.t_chunk.close()
        o_paths = None
        if len(self.t_chunk) > 0:
            logger.info('running batch transforms on %d StreamItems',
                        len(self.t_chunk))
            self._run_batch_transforms(t_path)
            self._maybe_run_post_batch_incremental_transforms(t_path)
            if (self.t_chunk) and (len(self.t_chunk) >= 0):
                o_paths = self._run_writers(start_count, next_idx, sources,
                                            i_str, t_path)
        self.t_chunk = None
        if self.work_unit and o_paths:
            old_o_paths = self.work_unit.data.get('output', [])
            o_paths = old_o_paths + o_paths
            self.work_unit.data['start_count'] = next_idx
            self.work_unit.data['output'] = o_paths
            self.work_unit.update()