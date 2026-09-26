function (all) {
        var byDepth = {};
        all.forEach(function (seed) {
            if (!byDepth[seed.name]) {
                byDepth[seed.name] = {};
            }
            if (!byDepth[seed.name][seed.npmDepth]) {
                byDepth[seed.name][seed.npmDepth] = [];
            }
            byDepth[seed.name][seed.npmDepth].push(seed);
        });
        return Object.keys(byDepth).map(function (name) {
            return this._dedupeSeeds(byDepth[name]);
        }, this);
    }