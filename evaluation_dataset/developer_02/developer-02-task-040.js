function( o ) {
		if (this.extends) {
			this.embed = o.embed.concat(this.embed);
			this.properties = o.properties.concat(this.properties);
			this.postInit = o.postInit + this.postInit;
			if (this.init === "default") this.init = o.init;
			if (this.factory === "new") this.factory = o.factory;
			if (!this.propAssign) this.propAssign = o.propAssign;
			for (var k in o.propCustomAssign) {
				if (!this.propCustomAssign[k]) {
					this.propCustomAssign[k] = o.propCustomAssign[k];
				}
			}
		}
	}