public void installDeployableUnit(DeployableUnit du) throws Exception {
    updateDeployedComponents();
    if (du.isReadyToInstall(true)) {
      sciAction(du.getInstallActions(), du);
      du.setInstalled(true);
      deployedDUs.add(du);
      updateDeployedComponents();
      Iterator<DeployableUnit> duIt = waitingForInstallDUs.iterator();
      while (duIt.hasNext()) {
        DeployableUnit waitingDU = duIt.next();
        if (waitingDU.isReadyToInstall(false)) {
          sciAction(waitingDU.getInstallActions(), waitingDU);
          waitingDU.setInstalled(true);
          deployedDUs.add(waitingDU);
          updateDeployedComponents();
          waitingForInstallDUs.remove(waitingDU);
          duIt = waitingForInstallDUs.iterator();
        }
      }
    }
    else {
      logger.warn("Unable to INSTALL " + du.getDeploymentInfoShortName() + " right now. Waiting for dependencies to be resolved.");
      waitingForInstallDUs.add(du);
    }
  }