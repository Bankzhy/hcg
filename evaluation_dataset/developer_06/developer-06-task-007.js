function(members) {
            var prototype = this.prototype,
                names = [],
                name, member;
            var className = this.$className || '';
            for (name in members) {
                if (members.hasOwnProperty(name)) {
                    member = members[name];
                    if (typeof member == 'function' && !member.$isClass && member !== Ext.emptyFn) {
                        member.$owner = this;
                        member.$name = name;
                        member.displayName = className + '#' + name;
                    }
                    prototype[name] = member;
                }
            }
            return this;
        }