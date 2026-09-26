def delete(self, blocksize=100):
        from .columns import MODELS_REFERENCED
        if not self._model._no_fk or self._model._namespace in MODELS_REFERENCED:
            raise QueryError("Can't delete entities of models with foreign key relationships")
        de = []
        i = 0
        for result in self.iter_result(pagesize=blocksize):
            de.append(result)
            i += 1
            if i >= blocksize:
                session.delete(de)
                del de[:]
                i = 0
        if de:
            session.delete(de)