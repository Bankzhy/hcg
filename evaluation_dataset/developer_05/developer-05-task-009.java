public void insertHrefBefore(String newHref, String refHref) {
        String refHrefEncoded = encodeHref(refHref);
        String newHrefEncoded = encodeHref(newHref);
        if (isDuplicate(newHrefEncoded))
            return;
        Element child = getFirstChild(root, "href");
        while (child != null) {
            if (refHrefEncoded.equals(getFirstText(child))) {
                insertBefore(child, "href", newHrefEncoded);
                return;
            }
            child = getNextSibling(child, "href");
        }
        Assert.isTrue(false, Policy.bind("assert.noHrefRef"));
    }