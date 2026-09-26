@Override
	public void readExternal(ObjectInput in) throws IOException,
			ClassNotFoundException {
		final String raEntityName = in.readUTF();
		this.raEntity = SleeContainer.lookupFromJndi().getResourceManagement()
		.getResourceAdaptorEntity(raEntityName);
		if (raEntity == null) {
			throw new IOException("RA Entity with name " + raEntityName
					+ " not found.");
		}
		boolean handleReference = in.readBoolean();
		if (handleReference) {
			activityHandle = new ActivityHandleReference(null, (Address) in.readObject(), in.readUTF());
		} else {
			final Marshaler marshaler = raEntity.getMarshaler();
			if (marshaler != null) {
				activityHandle = marshaler.unmarshalHandle(in);
			} else {
				throw new IOException("marshaller from RA is null");
			}
		}
	}