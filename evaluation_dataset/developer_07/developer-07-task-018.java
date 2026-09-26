public void visit(IntegerType literal)
    {
        if (isEnteringContext())
        {
            SymbolKey key = currentSymbolTable.getSymbolKey(currentPosition);
            literal.setSymbolKey(key);
        }
        else if (isLeavingContext())
        {
            literal.setTermTraverser(null);
        }
        if (delegate != null)
        {
            delegate.visit(literal);
        }
    }