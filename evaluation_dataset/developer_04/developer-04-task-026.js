function startSingleModule(oWrapper, sModuleId, sIdInstance, oData, bSingle) {
  const oModules = getModules();
  var oModule;
  oModule = oModules[sModuleId];
  if ( (bSingle && isModuleStarted(sModuleId)) || isModuleStarted(sModuleId, sIdInstance)) {
    oWrapper.stop(sModuleId, sIdInstance);
  }
  if (!isTypeOf(oModule, sNotDefined)) {
    createInstance(sModuleId, undefined, function (oInstance) {
      oModule.instances[sIdInstance] = oInstance;
      oInstance.__instance_id__ = sIdInstance;
      beforeInit(oInstance, oData, bSingle);
      if (!isTypeOf(oData, sNotDefined)) {
        oInstance.init(oData);
      } else {
        oInstance.init();
      }
    });
  } else {
    const ErrorHandler = errorHandler();
    ErrorHandler.error(new Error(), fpThrowErrorModuleNotRegistered(sModuleId));
  }
}