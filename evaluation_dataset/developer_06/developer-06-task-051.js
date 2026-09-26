function (configA, configB, flagsNames, isMasterConfig) {
    flagsNames.forEach(function (optionsName) {
        if (typeof configB[optionsName] === "undefined") {
            return;
        }
        if (isMasterConfig) {
            configA[optionsName] = configB[optionsName];
        } else {
            if (configB[optionsName] instanceof Array && !(configA[optionsName] instanceof Array) ) {
                configA[optionsName] = configB[optionsName];
            } else if (configB[optionsName] instanceof Array && configA[optionsName] instanceof Array) {
                configA[optionsName] = configA[optionsName].concat(configB[optionsName]);
            } else {
                configA[optionsName] = configA[optionsName] || configB[optionsName];
            }
        }
    });
}