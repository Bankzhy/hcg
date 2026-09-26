function barycenterVerticesAndFaces(sphere, options, done) {
  var n         = sphere._Fields.length,
      positions = new Float32Array(n * 3),
      indices   = sphere._interfieldTriangles,
      colors    = new Float32Array(indices.length * 3);
  for (let f = 0; f < sphere._Fields.length; f += 1) {
    let field = sphere._Fields[f],
        f_φ   = sphere._positions[2 * f + 0],
        f_λ   = sphere._positions[2 * f + 1],
        color = options.colorFn.call(field);
    positions[f * 3 + 0] = cos(f_φ) * cos(f_λ);
    positions[f * 3 + 2] = cos(f_φ) * sin(f_λ);
    positions[f * 3 + 1] = sin(f_φ);
    colors[f * 3 + 0] = color.r;
    colors[f * 3 + 1] = color.g;
    colors[f * 3 + 2] = color.b;
  }
  var normals = positions.slice(0);
  if (done) done.call(null, null, {
    positions,
    normals,
    indices,
    colors
  });
}