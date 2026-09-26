private void parseLinkObject(String rel, ObjectNode obj, Map<URI, String> linksForRel, Map<String, String> linkTemplates) {
        JsonNode href = obj.findValue("href");
        if (href == null) {
            return;
        }
        JsonNode templated = obj.findValue("templated");
        if (templated != null && templated.isBoolean() && templated.asBoolean()) {
            linkTemplates.put(rel, href.asText());
        } else {
            JsonNode title = obj.findValue("title");
            linksForRel.put(
                    uri.resolve(href.asText()),
                    (title != null && title.getNodeType() == JsonNodeType.STRING) ? title.asText() : null);
        }
    }