def run_query(self, cmd="", **kwargs):
        spark_sql_cmd = self._prepare_command(cmd)
        self._sp = subprocess.Popen(spark_sql_cmd,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT,
                                    **kwargs)
        for line in iter(self._sp.stdout.readline, ''):
            self.log.info(line)
        returncode = self._sp.wait()
        if returncode:
            raise AirflowException(
                "Cannot execute {} on {}. Process exit code: {}.".format(
                    cmd, self._conn.host, returncode
                )
            )