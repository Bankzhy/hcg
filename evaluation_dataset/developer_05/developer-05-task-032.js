function parseLocalDateAndTimeString(str, normalized = false) {
  let separatorIdx = str.indexOf("T");
  if (separatorIdx < 0 && !normalized) {
    separatorIdx = str.indexOf(" ");
  }
  if (separatorIdx < 0) {
    return null;
  }
  const date = parseDateString(str.slice(0, separatorIdx));
  if (date === null) {
    return null;
  }
  const time = parseTimeString(str.slice(separatorIdx + 1));
  if (time === null) {
    return null;
  }
  return { date, time };
}