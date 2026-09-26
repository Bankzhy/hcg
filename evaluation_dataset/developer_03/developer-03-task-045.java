protected void downgradeAnhangElements(Document doc) throws JaxenException {
        List nodes = XmlUtils.newXPath(
                "/io:openimmo/io:anbieter/io:anhang | " +
                        "/io:openimmo/io:anbieter/io:immobilie/io:anhaenge/io:anhang",
                doc).selectNodes(doc);
        for (Object item : nodes) {
            Element node = (Element) item;
            String value = StringUtils.trimToNull(node.getAttribute("gruppe"));
            if ("QRCODE".equalsIgnoreCase(value))
                node.removeAttribute("gruppe");
            else if ("FILM".equalsIgnoreCase(value))
                node.removeAttribute("gruppe");
            else if ("FILMLINK".equalsIgnoreCase(value))
                node.removeAttribute("gruppe");
            value = StringUtils.trimToNull(node.getAttribute("location"));
            if ("REMOTE".equalsIgnoreCase(value))
                node.setAttribute("location", "EXTERN");
            List childNodes = XmlUtils.newXPath("io:check", doc)
                    .selectNodes(node);
            for (Object childItem : childNodes) {
                node.removeChild((Node) childItem);
            }
        }
    }