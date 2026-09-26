function getTimeWithTicks(date, ticks) {
  if (!(date instanceof Date) || isNaN(date.getTime())) {
    date = new Date();
    const time = date.getTime();
    _ticksForCurrentTime++;
    if(_ticksForCurrentTime > _ticksInMs || time > _lastTimestamp) {
      _ticksForCurrentTime = 0;
      _lastTimestamp = time;
    }
    ticks = _ticksForCurrentTime;
  }
  return {
    time: date.getTime(),
    ticks: getTicks(ticks)
  };
}