def find_function(self, context, funname):
        if funname in self.builtins:
            return self.builtins[funname]
        func = None
        if isinstance(context, dict):
            if funname in context:
                func = context[funname]
                if isinstance(func, str):
                    func = self._deferred_add(func)
                    context[funname] = func
        elif hasattr(context, funname):
            func = getattr(context, funname)
        if func is None:
            raise NotFoundError("Function not found", function=funname)
        return func