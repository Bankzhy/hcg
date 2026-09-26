public void walk(Term term)
    {
        term.setTermTraverser(traverser);
        search.reset();
        if (goalPredicate != null)
        {
            search.setGoalPredicate(goalPredicate);
        }
        search.addStartState(term);
        Iterator<Term> treeWalker = Searches.allSolutions(search);
        if (traverser instanceof TermVisitor)
        {
            term.accept((TermVisitor) traverser);
        }
        while (treeWalker.hasNext())
        {
            Term nextTerm = treeWalker.next();
            nextTerm.accept(visitor);
        }
        term.setTermTraverser(null);
    }