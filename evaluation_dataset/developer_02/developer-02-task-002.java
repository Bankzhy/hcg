@SuppressWarnings("Duplicates")
    protected static void read(File xmlFile) throws SAXException, IOException, ParserConfigurationException, JAXBException {
        LOGGER.info("process file: " + xmlFile.getAbsolutePath());
        if (!xmlFile.isFile()) {
            LOGGER.warn("> provided file is invalid");
            return;
        }
        FilemakerDocument doc = FilemakerUtils.createDocument(xmlFile);
        if (doc == null) {
            LOGGER.warn("> provided XML is not supported");
        } else if (doc.isResult()) {
            printToConsole((FilemakerResultDocument) doc);
        } else if (doc.isLayout()) {
            printToConsole((FilemakerLayoutDocument) doc);
        } else {
            LOGGER.warn("> unsupported type of document: "
                    + doc.getClass().getName());
        }
    }