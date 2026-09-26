function () {
                var bytes = this._messageQueue.reduce(function (acc, message) {
                    if (typeof message === 'string') {
                        acc += message.length;
                    }
                    else if (message instanceof Blob) {
                        acc += message.size;
                    }
                    else {
                        acc += message.byteLength;
                    }
                    return acc;
                }, 0);
                return bytes + (this._ws ? this._ws.bufferedAmount : 0);
            }