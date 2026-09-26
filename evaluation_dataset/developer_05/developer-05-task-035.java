private void resume() {
		Runnable runnable = new Runnable() {
			public void run() {
				if (scheduledFuture == null) {
					return;
				}
				scheduledFuture.cancel(false);
				scheduledFuture = null;
				for (EventContext ec : barriedEvents) {
					ec.getLocalActivityContext().getExecutorService().routeEvent(ec);
				}
				barriedEvents = null;
				event.getLocalActivityContext().getEventQueueManager().removeBarrier(transaction);
				suspended = false;
				event.getLocalActivityContext().getCurrentEventRoutingTask().run();
			}
		};
		event.getLocalActivityContext().getExecutorService().execute(runnable);
	}