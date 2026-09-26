@SuppressWarnings("unused")
    public void userEncountered() {
        List<String> descriptors = new ArrayList<>();
        descriptors.add(CommonEvents.Descriptors.NOT_INTERRUPT);
        boolean known = !fireUnknownIfNotPresent || present;
        boolean firstPresent = (!strict && !present) || (strict && !strictPresent);
        long lastSeen = this.lastSeen.until(LocalDateTime.now(), ChronoUnit.SECONDS);
        Optional<Event> presenceEvent = IdentificationManagerM.getInstance()
                .getIdentification(this)
                .flatMap(id -> PresenceEvent.createPresenceEvent(id, strict, known, firstPresent, descriptors, lastSeen))
                .map(event -> event.addEventLifeCycleListener(EventLifeCycle.APPROVED, lifeCycle -> {
                    if (known) {
                        this.lastSeen = LocalDateTime.now();
                        if (strict)
                            this.strictPresent = true;
                        present = true;
                    }
                }));
        if (!presenceEvent.isPresent()) {
            error("unable to create PresenceEvent");
        } else {
            fire(presenceEvent.get(), 5);
        }
    }