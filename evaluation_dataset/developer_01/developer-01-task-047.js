function constructSelectEvent(nativeEvent, nativeEventTarget) {
  var doc = getEventTargetDocument(nativeEventTarget);
  if (mouseDown || activeElement$1 == null || activeElement$1 !== getActiveElement(doc)) {
    return null;
  }
  var currentSelection = getSelection(activeElement$1);
  if (!lastSelection || !shallowEqual(lastSelection, currentSelection)) {
    lastSelection = currentSelection;
    var syntheticEvent = SyntheticEvent.getPooled(eventTypes$3.select, activeElementInst$1, nativeEvent, nativeEventTarget);
    syntheticEvent.type = 'select';
    syntheticEvent.target = activeElement$1;
    accumulateTwoPhaseDispatches(syntheticEvent);
    return syntheticEvent;
  }
  return null;
}