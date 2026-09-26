function _eachDependencies( packageName, bowerJson, packageFunc, options, packageList, firstLevel, dotBowerJson ){
        bowerJson = bowerJson || {};
        dotBowerJson = dotBowerJson || {};
        var dependenciesPackageName,
            dependencies = bowerJson.dependencies || dotBowerJson.dependencies || {};
        packageFunc(packageName, bowerJson, options, firstLevel, dotBowerJson);
        for (dependenciesPackageName in dependencies)
            if ( dependencies.hasOwnProperty(dependenciesPackageName) ){
                if (packageList[ dependenciesPackageName ])
                  continue;
                packageList[ dependenciesPackageName ] = true;
                _eachDependencies(
                    dependenciesPackageName,
                    common.readJSONFile(paths.bower_components + dependenciesPackageName + '/bower.json'),
                    packageFunc,
                    options,
                    packageList,
                    false,
                    common.readJSONFile(paths.bower_components + dependenciesPackageName + '/.bower.json')
                );
        }
    }