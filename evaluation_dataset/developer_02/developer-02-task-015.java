public void optimize() {
        final List<BaseVertex> sorted = new ArrayList<BaseVertex>( this.vertices );
        Collections.sort(sorted, new Comparator<BaseVertex>() {
            public int compare(final BaseVertex v1, final BaseVertex v2) {
                int v1OutDegree = v1.getSourceConnections().size();
                int v2OutDegree = v2.getSourceConnections().size();
                if (v1OutDegree < v2OutDegree) {
                    return 1;
                }
                if (v1OutDegree > v2OutDegree) {
                    return -1;
                }
                return 0;
            }
        });
        final LinkedList<BaseVertex> optimized = new LinkedList<BaseVertex>();
        boolean front = false;
        for ( final Iterator<BaseVertex> vertexIter = sorted.iterator(); vertexIter.hasNext(); ) {
            final BaseVertex vertex = vertexIter.next();
            if ( front ) {
                optimized.addFirst( vertex );
            } else {
                optimized.addLast( vertex );
            }
            front = !front;
        }
        this.vertices = optimized;
    }