private void deserializeSingle(DataInputStream source, ServerVersion sv,
                                   StatusUI statusUI)
            throws IOException, EOFException, DataReadException {
        Vector newInstance = new Vector();
        for (int i = 0; i < varTemplate.size(); i++) {
            BaseType bt = (BaseType) varTemplate.elementAt(i);
            newInstance.addElement(bt.clone());
        }
        for (Enumeration e = newInstance.elements(); e.hasMoreElements();) {
            if (statusUI != null && statusUI.userCancelled())
                throw new DataReadException("User cancelled");
            ClientIO bt = (ClientIO) e.nextElement();
            bt.deserialize(source, sv, statusUI);
        }
        allValues.addElement(newInstance);
    }