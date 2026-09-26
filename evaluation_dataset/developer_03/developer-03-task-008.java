private void writeFilePassivationStores(XMLExtendedStreamWriter writer, ModelNode model) throws XMLStreamException {
        if (model.hasDefined(EJB3SubsystemModel.FILE_PASSIVATION_STORE)) {
            List<Property> caches = model.get(EJB3SubsystemModel.FILE_PASSIVATION_STORE).asPropertyList();
            for (Property property : caches) {
                writer.writeStartElement(EJB3SubsystemXMLElement.FILE_PASSIVATION_STORE.getLocalName());
                ModelNode store = property.getValue();
                writer.writeAttribute(EJB3SubsystemXMLAttribute.NAME.getLocalName(), property.getName());
                LegacyPassivationStoreResourceDefinition.IDLE_TIMEOUT.marshallAsAttribute(store, writer);
                LegacyPassivationStoreResourceDefinition.IDLE_TIMEOUT_UNIT.marshallAsAttribute(store, writer);
                FilePassivationStoreResourceDefinition.MAX_SIZE.marshallAsAttribute(store, writer);
                FilePassivationStoreResourceDefinition.RELATIVE_TO.marshallAsAttribute(store, writer);
                FilePassivationStoreResourceDefinition.GROUPS_PATH.marshallAsAttribute(store, writer);
                FilePassivationStoreResourceDefinition.SESSIONS_PATH.marshallAsAttribute(store, writer);
                FilePassivationStoreResourceDefinition.SUBDIRECTORY_COUNT.marshallAsAttribute(store, writer);
                writer.writeEndElement();
            }
        }
    }