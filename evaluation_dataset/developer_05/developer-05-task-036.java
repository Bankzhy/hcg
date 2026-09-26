@OnMessage
	public void onMessage(String messageParam) {
		boolean handlerFoundForMsg = false;
		for(IMessageResponseHandler handler : new ArrayList<>(this.messageHandlers.values())) {
			Object qualifyObj = handler.doesHandlerQualifyForProcessing(messageParam);
			if(qualifyObj instanceof Error) {
				handler.handleMessage(qualifyObj);
			} else if(qualifyObj instanceof JSONObject) {
				handler.handleMessage(qualifyObj);
				handlerFoundForMsg = true;
				break;
			}
		}
		if(!handlerFoundForMsg) {
			throw new FluidClientException(
					"No handler found for message;\n"+messageParam,
					FluidClientException.ErrorCode.IO_ERROR);
		}
	}