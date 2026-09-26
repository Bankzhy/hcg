def pivot(self, index, column, value):
        assert_is_type(index, str)
        assert_is_type(column, str)
        assert_is_type(value, str)
        col_names = self.names
        if index not in col_names:
            raise H2OValueError("Index not in H2OFrame")
        if column not in col_names:
            raise H2OValueError("Column not in H2OFrame")
        if value not in col_names:
            raise H2OValueError("Value column not in H2OFrame")
        if self.type(column) not in ["enum","time","int"]:
            raise H2OValueError("'column' argument is not type enum, time or int")
        if self.type(index) not in ["enum","time","int"]:
            raise H2OValueError("'index' argument is not type enum, time or int")
        return H2OFrame._expr(expr=ExprNode("pivot",self,index,column,value))