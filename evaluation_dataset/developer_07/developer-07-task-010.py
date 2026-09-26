def get_index_type(self, loop_nest=None):
        if loop_nest is None:
            loop_nest = self.get_kernel_loop_nest()
        if type(loop_nest) is c_ast.For:
            loop_nest = [loop_nest]
        index_types = (None, None)
        for s in loop_nest:
            if type(s) is c_ast.For:
                if type(s.stmt) in [c_ast.For, c_ast.Compound]:
                    other = self.get_index_type(loop_nest=s.stmt)
                else:
                    other = None
                index_types = (s.init.decls[0].type.type.names, other)
                break
        if index_types[0] == index_types[1] or index_types[1] is None:
            return index_types[0]
        else:
            raise ValueError("Loop indices must have same type, found {}.".format(index_types))