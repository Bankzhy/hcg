function(name, path) {
            var _this    = this;
            var cm       = this.cm;
            var settings = this.settings;
            path = settings.pluginPath + path;
            if (typeof define === "function")
            {
                if (typeof this[name] === "undefined")
                {
                    alert("Error: " + name + " plugin is not found, you are not load this plugin.");
                    return this;
                }
                this[name](cm);
                return this;
            }
            if ($.inArray(path, editormd.loadFiles.plugin) < 0)
            {
                editormd.loadPlugin(path, function() {
                    editormd.loadPlugins[name] = _this[name];
                    _this[name](cm);
                });
            }
            else
            {
                $.proxy(editormd.loadPlugins[name], this)(cm);
            }
            return this;
        }