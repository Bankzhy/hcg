function(hash) {
		this.addFeatures(hash);
		var array = [];
		for (var featureIndex=0; featureIndex<this.featureIndexToFeatureName.length; ++featureIndex)
			array[featureIndex]=0;
		if (hash instanceof Array) {
			for (var i in hash)
				array[this.featureNameToFeatureIndex[hash[i]]] = true;
		} else if (hash instanceof Object) {
			for (var feature in hash)
				array[this.featureNameToFeatureIndex[feature]] = hash[feature];
		}
		else throw new Error("Unsupported type: "+JSON.stringify(hash));
		return array;
	}