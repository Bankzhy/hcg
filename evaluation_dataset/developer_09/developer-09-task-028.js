function FlowFile(flowObj, file, uniqueIdentifier) {
    this.flowObj = flowObj;
    this.bytes = null;
    this.file = file;
    this.name = file.fileName || file.name;
    this.size = file.size;
    this.relativePath = file.relativePath || file.webkitRelativePath || this.name;
    this.uniqueIdentifier = (uniqueIdentifier === undefined ? flowObj.generateUniqueIdentifier(file) : uniqueIdentifier);
    this.chunks = [];
    this.paused = false;
    this.error = false;
    this.averageSpeed = 0;
    this.currentSpeed = 0;
    this._lastProgressCallback = Date.now();
    this._prevUploadedSize = 0;
    this._prevProgress = 0;
    this.bootstrap();
  }