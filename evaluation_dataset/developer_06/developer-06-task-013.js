function findInsertIndex(records, record, comparator) {
  if (!records.length) {
    return 0
  }
  if (records.length === 1) {
    let comparison = comparator(records[0].record, record)
    return (comparison > 0) ? 0 : 1
  }
  let comparison = comparator(records[0].record, record)
  if (comparison > 0) {
    return 0
  }
  let bottom = 1
  let top = records.length - 1
  while (bottom <= top) {
    let pivotIndex = Math.floor((bottom + top) / 2)
    let comparison = comparator(records[pivotIndex].record, record)
    if (comparison > 0) {
      let previousElement = records[pivotIndex - 1].record
      if (comparator(previousElement, record) <= 0) {
        return pivotIndex
      }
      top = pivotIndex - 1
    } else {
      bottom = pivotIndex + 1
    }
  }
  return records.length
}