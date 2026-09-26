def __check_disk(self):
        cmd = "sh -c \"df --no-sync -m -P -l -x fuse -x tmpfs -x devtmpfs -x davfs -x nfs "
        cmd += self.core.artifacts_base_dir
        cmd += " | tail -n 1 | awk '{print \$4}' \""
        res = execute(cmd, True, 0.1, True)
        logging.debug("Result: %s", res)
        if not len(res[1]):
            self.log.debug("No disk usage info: %s", res[2])
            return
        disk_free = res[1]
        self.log.debug(
            "Disk free space: %s/%s", disk_free.strip(), self.disk_limit)
        if int(disk_free.strip()) < self.disk_limit:
            raise RuntimeError(
                "Not enough local resources: disk space less than %sMB in %s: %sMB"
                % (
                    self.disk_limit, self.core.artifacts_base_dir,
                    int(disk_free.strip())))