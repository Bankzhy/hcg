static public MAMatrix multiply(MAMatrix m1, MAMatrix m2) {
    if (m1.getNcols() != m2.getNrows())
      throw new IllegalArgumentException("MAMatrix.multiply "+m1.getNcols()+" != "+ m2.getNrows());
    int kdims = m1.getNcols();
    ArrayDouble.D2 result = new ArrayDouble.D2(m1.getNrows(), m2.getNcols());
    Index imr = result.getIndex();
    for (int i=0; i<m1.getNrows(); i++) {
      for (int j=0; j<m2.getNcols(); j++) {
        double sum = 0.0;
        for (int k=0; k<kdims; k++)
          sum += m1.getDouble(i, k) * m2.getDouble(k, j);
        result.setDouble( imr.set(i,j), sum);
      }
    }
    return new MAMatrix( result);
  }