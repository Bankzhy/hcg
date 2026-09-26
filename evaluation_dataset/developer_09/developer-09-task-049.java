protected void leaveFunctor(Functor functor)
    {
        int pos = traverser.getPosition();
        if (!traverser.isInHead() && (pos >= 0))
        {
            Functor transformed = builtInTransform.apply(functor);
            if (functor != transformed)
            {
                BuiltInFunctor builtInFunctor = (BuiltInFunctor) transformed;
                Term parentTerm = traverser.getParentContext().getTerm();
                if (parentTerm instanceof Clause)
                {
                    Clause parentClause = (Clause) parentTerm;
                    parentClause.getBody()[pos] = builtInFunctor;
                }
                else if (parentTerm instanceof Functor)
                {
                    Functor parentFunctor = (Functor) parentTerm;
                    parentFunctor.getArguments()[pos] = builtInFunctor;
                }
            }
        }
    }