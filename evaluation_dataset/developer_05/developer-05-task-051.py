def search(self, conn, filters, order_by, offset=None, count=None, timeout=None):
        pipe, intersect, temp_id = self._prepare(conn, filters)
        if order_by:
            reverse = order_by and order_by.startswith('-')
            order_clause = '%s:%s:idx'%(self.namespace, order_by.lstrip('-'))
            intersect(temp_id, {temp_id:0, order_clause: -1 if reverse else 1})
        if timeout is not None:
            pipe.expire(temp_id, timeout)
            pipe.execute()
            return temp_id
        offset = offset if offset is not None else 0
        end = (offset + count - 1) if count and count > 0 else -1
        pipe.zrange(temp_id, offset, end)
        pipe.delete(temp_id)
        return pipe.execute()[-2]