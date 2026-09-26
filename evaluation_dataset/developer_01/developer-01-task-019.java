private String getSearchPath(ITreeNode node) {
        List l = new LinkedList();
        node.getUserObjectPathFromRoot(l);
        Iterator it = l.iterator();
        StringBuffer ret = new StringBuffer();
        int i = 0;
        String token;
        while (it.hasNext()) {
            token = it.next().toString();
            if (i != 0) {
                ret.append(token);
                if (it.hasNext()) {
                    ret.append('/');
                }
            }
            i++;
        }
        return ret.toString();
    }