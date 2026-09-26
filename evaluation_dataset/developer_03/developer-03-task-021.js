function Transform( that ) {
        that = that || {};
        if ( that.data instanceof Array ) {
            that = that.decompose();
            this.rotation = that.rotation;
            this.translation = that.translation || new Vec3();
            this.scale = that.scale;
        } else {
            this.rotation = that.rotation ? new Quaternion( that.rotation ) : new Quaternion();
            this.translation = that.translation ? new Vec3( that.translation ) : new Vec3();
            if ( typeof that.scale === 'number' ) {
                this.scale = new Vec3( that.scale, that.scale, that.scale );
            } else {
                this.scale = that.scale ? new Vec3( that.scale ) : new Vec3( 1, 1, 1 );
            }
        }
    }