@SuppressWarnings("Duplicates")
    protected void downgradeUrlElements(Document doc) throws JaxenException {
        List nodes = XmlUtils.newXPath(
                "/io:root/io:property/io:url",
                doc).selectNodes(doc);
        for (Object item : nodes) {
            Element node = (Element) item;
            String enUrlValue = null;
            String fallbackUrlValue = null;
            List childNodes = XmlUtils.newXPath(
                    "*", doc).selectNodes(node);
            for (Object childItem : childNodes) {
                Element langNode = (Element) childItem;
                if ("en".equalsIgnoreCase(langNode.getLocalName()))
                    enUrlValue = StringUtils.trimToNull(langNode.getTextContent());
                else if (fallbackUrlValue == null)
                    fallbackUrlValue = StringUtils.trimToNull(langNode.getTextContent());
                node.removeChild(langNode);
            }
            node.setTextContent((enUrlValue != null) ? enUrlValue : fallbackUrlValue);
        }
    }