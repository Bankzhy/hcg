static ReferenceBase xsdParseSkeleton(Node node, XsdAbstractElement element){
        XsdParserCore parser = element.getParser();
        Node child = node.getFirstChild();
        while (child != null) {
            if (child.getNodeType() == Node.ELEMENT_NODE) {
                String nodeName = child.getNodeName();
                BiFunction<XsdParserCore, Node, ReferenceBase> parserFunction = XsdParserCore.getParseMappers().get(nodeName);
                if (parserFunction != null){
                    XsdAbstractElement childElement = parserFunction.apply(parser, child).getElement();
                    childElement.accept(element.getVisitor());
                    childElement.validateSchemaRules();
                }
            }
            child = child.getNextSibling();
        }
        ReferenceBase wrappedElement = ReferenceBase.createFromXsd(element);
        parser.addParsedElement(wrappedElement);
        return wrappedElement;
    }