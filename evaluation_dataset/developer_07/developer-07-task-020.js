function sortByOrder(elements, order, splitBy) {
        var results = [];
        order.forEach (function(name) {
            if (splitBy)
                elements.forEach (function(element) {
                    var parts = element.split(splitBy);
                    var key = parts[1];
                    if (key == name)
                        results.push(element);
                });
            else
                elements.forEach (function(key) {
                    if (key == name)
                        results.push(name);
                });
        });
        elements.forEach(function(element) {
            if (results.indexOf(element) === -1)
                results.push(element);
        });
        return results;
    }