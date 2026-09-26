boolean initialize(EllipseRotated_F64 ellipseA, EllipseRotated_F64 ellipseB,
					   Point2D_F64 tangentA0, Point2D_F64 tangentA1,
					   Point2D_F64 tangentA2, Point2D_F64 tangentA3,
					   Point2D_F64 tangentB0, Point2D_F64 tangentB1,
					   Point2D_F64 tangentB2, Point2D_F64 tangentB3) {
		centerLine.set(ellipseA.center,ellipseB.center);
		UtilLine2D_F64.convert(centerLine, lineGeneral);
		Intersection2D_F64.intersection(lineGeneral, ellipseA, temp0, temp1, -1);
		if (temp0.distance2(ellipseB.center) < temp1.distance2(ellipseB.center)) {
			tangentA0.set(temp0);
		} else {
			tangentA0.set(temp1);
		}
		if( !tangentLines(tangentA0,ellipseB,tangentB0,tangentB1) )
			return false;
		if( !selectTangent(tangentB0,tangentA0,ellipseA,tangentA0, false))
			return false;
		if( !selectTangent(tangentB0,tangentA0,ellipseA,tangentA1, true))
			return false;
		if( !selectTangent(tangentB1,tangentA0,ellipseA,tangentA2, true))
			return false;
		if( !selectTangent(tangentB1,tangentA0,ellipseA,tangentA3, false))
			return false;
		return true;
	}