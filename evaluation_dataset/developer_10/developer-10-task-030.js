function() {
				if (!self) {
					return;
				}
				var shimContainer = Dom.get(this.shimid);
				if (shimContainer) {
					shimContainer.parentNode.removeChild(shimContainer);
				}
				if (_shim) {
					_shim.removeAllInstances();
				}
				this.unbindAll();
				delete runtimes[this.uid];
				this.uid = null;
				_uid = self = _shim = shimContainer = null;
			}