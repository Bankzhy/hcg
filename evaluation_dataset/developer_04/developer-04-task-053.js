function G(cmd, coords) {
      var parts = [
        'G' + cmd,
      ];
      for (var coord in coords) {
        if (coords.hasOwnProperty(coord)) {
          var lcoord = coord.toLowerCase();
          if (lcoord === 'x') {
            coords[coord] += offsetX;
          } else if (lcoord == 'y') {
            coords[coord] += offsetY;
          }
          parts.push(coord.toUpperCase() + ((negate) ? -coords[coord] : coords[coord]));
        }
      }
      if (!coords.f && !coords.F) {
        parts.push('F' + feedRate);
      }
      gcode.push(parts.join(' '));
    }