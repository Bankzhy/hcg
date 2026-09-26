def append(self, passes, ignore_requires=None, ignore_preserves=None, max_iteration=None,
               **flow_controller_conditions):
        passset_options = {'ignore_requires': ignore_requires,
                           'ignore_preserves': ignore_preserves,
                           'max_iteration': max_iteration}
        options = self._join_options(passset_options)
        if isinstance(passes, BasePass):
            passes = [passes]
        for pass_ in passes:
            if not isinstance(pass_, BasePass):
                raise TranspilerError('%s is not a pass instance' % pass_.__class__)
        for name, param in flow_controller_conditions.items():
            if callable(param):
                flow_controller_conditions[name] = partial(param, self.fenced_property_set)
            else:
                raise TranspilerError('The flow controller parameter %s is not callable' % name)
        self.working_list.append(
            FlowController.controller_factory(passes, options, **flow_controller_conditions))