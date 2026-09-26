protected void markParseErrors(List<DroolsBuildMarker> markers,
                                   List<BaseKnowledgeBuilderResultImpl> parserErrors) {
        for ( Iterator<BaseKnowledgeBuilderResultImpl> iter = parserErrors.iterator(); iter.hasNext(); ) {
            Object error = iter.next();
            if ( error instanceof ParserError ) {
                ParserError err = (ParserError) error;
                markers.add( new DroolsBuildMarker( err.getMessage(),
                                                    err.getRow() ) );
            } else if ( error instanceof KnowledgeBuilderResult) {
                KnowledgeBuilderResult res = (KnowledgeBuilderResult) error;
                int[] errorLines = res.getLines();
                markers.add( new DroolsBuildMarker( res.getMessage(),
                                                    errorLines != null && errorLines.length > 0 ? errorLines[0] : -1 ) );
            } else if ( error instanceof ExpanderException ) {
                ExpanderException exc = (ExpanderException) error;
                markers.add( new DroolsBuildMarker( exc.getMessage(),
                                                    -1 ) );
            } else {
                markers.add( new DroolsBuildMarker( error.toString() ) );
            }
        }
    }