function add_cly_events(event){
        if(!event.key){
            log("Event must have key property");
            return;
        }
        if(cluster.isMaster){
            if(!event.count){
                event.count = 1;
            }
            var props = ["key", "count", "sum", "dur", "segmentation"];
            var e = getProperties(event, props);
            e.timestamp = getMsTimestamp();
            var date = new Date();
            e.hour = date.getHours();
            e.dow = date.getDay();
            log("Adding event: ", event);
            eventQueue.push(e);
            storeSet("cly_event", eventQueue);
        }
        else{
            process.send({ cly: {event: event} });
        }
    }