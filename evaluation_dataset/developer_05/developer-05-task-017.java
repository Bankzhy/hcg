final int updatePublisherLimit()
    {
        int workCount = 0;
        final long senderPosition = this.senderPosition.getVolatile();
        if (hasReceivers || (spiesSimulateConnection && spyPositions.length > 0))
        {
            long minConsumerPosition = senderPosition;
            for (final ReadablePosition spyPosition : spyPositions)
            {
                minConsumerPosition = Math.min(minConsumerPosition, spyPosition.getVolatile());
            }
            final long proposedPublisherLimit = minConsumerPosition + termWindowLength;
            if (publisherLimit.proposeMaxOrdered(proposedPublisherLimit))
            {
                cleanBuffer(proposedPublisherLimit);
                workCount = 1;
            }
        }
        else if (publisherLimit.get() > senderPosition)
        {
            publisherLimit.setOrdered(senderPosition);
        }
        return workCount;
    }