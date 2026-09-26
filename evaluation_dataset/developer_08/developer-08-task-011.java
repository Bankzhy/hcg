@Override public <G,B> Or<G,B> foldUntil(G accum,
                                             Fn2<? super G,? super A,B> terminator,
                                             Fn2<? super G,? super A,G> reducer) {
        if (terminator == null) {
            return Or.good(fold(accum, reducer));
        }
        if (reducer == null) {
            throw new IllegalArgumentException("Can't fold with a null reduction function.");
        }
        List<A> as = this.toMutableList();
        for (A a : as) {
            B term = terminator.apply(accum, a);
            if (term != null) {
                return Or.bad(term);
            }
            accum = reducer.apply(accum, a);
        }
        return Or.good(accum);
    }