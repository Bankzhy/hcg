public boolean solvePoint(List<Point3D_F64> points , Point3D_F64 pointOnPlane , Vector3D_F64 outputNormal ) {
		final int N = points.size();
		A.reshape(N,3);
		int index = 0;
		for( int i = 0; i < N; i++ ) {
			Point3D_F64 p = points.get(i);
			A.data[index++] = p.x - pointOnPlane.x;
			A.data[index++] = p.y - pointOnPlane.y;
			A.data[index++] = p.z - pointOnPlane.z;
		}
		if( !solverNull.process(A,1,nullspace) )
			return false;
		outputNormal.x = (double) nullspace.unsafe_get(0,0);
		outputNormal.y = (double) nullspace.unsafe_get(1,0);
		outputNormal.z = (double) nullspace.unsafe_get(2,0);
		return true;
	}