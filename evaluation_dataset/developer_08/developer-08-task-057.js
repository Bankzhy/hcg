function getAngleForPoint(x: number, y: number) {
    if (x == 0 && y == 0) return 0;
    const angle = Math.atan(x / y);
    let angleDeg = angle * 180 / Math.PI;
    const quadrant = getQuadrant(x, y);
       if( quadrant === 1 ) {
         angleDeg = 90 - angleDeg;
       }
       if (quadrant === 2) {
        angleDeg = 90 - angleDeg;
      }
      if (quadrant === 3) {
        angleDeg = 270 - angleDeg;
      }
      if (quadrant === 4) {
        angleDeg = 270 - angleDeg;
      }
    return angleDeg;
  }