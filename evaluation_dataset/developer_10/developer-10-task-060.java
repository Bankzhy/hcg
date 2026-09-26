private void handleMessageFromServer(String textResponse) {
        if (verbose) {
            puts("RESPONSE", url, ProtocolConstants.prettyPrintMessage(textResponse));
            puts("RESPONSE", url);
            puts(ProtocolConstants.prettyPrintMessageWithLinesTabs(textResponse));
        }
        if (textResponse.startsWith(Action.GET.response().startsWith()) ||
                textResponse.startsWith(Action.SET_BROADCAST.response().startsWith())) {
            queue.put(SingleResult.fromTextMessage(textResponse));
        } else if (textResponse.startsWith(Action.BATCH_READ.response().startsWith())) {
            queue.put(BatchResult.fromTextMessage(textResponse));
        } else if (textResponse.startsWith(Action.GET_STATS.response().startsWith())) {
            queue.put(StatsResults.fromTextMessage(textResponse));
        } else {
            if (verbose) {
                puts(textResponse);
            }
        }
    }