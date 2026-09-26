public static ParabolaParametric_F64 convert( ParabolaGeneral_F64 src , ParabolaParametric_F64 dst ) {
		if( dst == null )
			dst = new ParabolaParametric_F64();
		double A = src.A;
		double C = src.C;
		double D = src.D;
		double E = src.E;
		double F = src.F;
		double bottom = C*D-A*E;
		if( bottom == 0 ) {
			throw new RuntimeException("Not a parabola");
		} else {
			dst.A = -C / bottom;
			dst.B = E / bottom;
			dst.C = -C * F / bottom;
			dst.D = A / bottom;
			dst.E = -D / bottom;
			dst.F = A * F / bottom;
		}
		return dst;
	}