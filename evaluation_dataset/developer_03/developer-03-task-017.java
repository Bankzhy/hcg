@Override
	public void writeExternal(ObjectOutput out) throws IOException {
		out.writeUTF(raEntity.getName());
		if (activityHandle.getClass() == ActivityHandleReference.class) {
			out.writeBoolean(true);
			final ActivityHandleReference reference = (ActivityHandleReference) activityHandle;
			out.writeObject(reference.getAddress());
			out.writeUTF(reference.getId());
		}
		else {
			out.writeBoolean(false);
			final Marshaler marshaler = raEntity.getMarshaler();
			if (marshaler != null) {
				marshaler.marshalHandle(activityHandle, out);
			}
			else {
				throw new IOException("marshaller from RA is null");
			}
		}
	}