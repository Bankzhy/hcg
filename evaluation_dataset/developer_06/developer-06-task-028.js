function toNativeCursorDirection(direction, unique) {
  if (typeof direction === "string") {
    if (CURSOR_DIRECTIONS.indexOf(direction.toUpperCase()) === -1) {
      throw new Error("When using a string as cursor direction, use NEXT " +
          `or PREVIOUS, ${direction} provided`);
    }
  } else {
    direction = direction.value
  }
  let cursorDirection = direction.toLowerCase().substring(0, 4)
  if (unique) {
    cursorDirection += "unique"
  }
  return cursorDirection
}