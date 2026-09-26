public D1 getCoordinateArray1D(int timeIndex, int xIndex, int yIndex)
    		throws IOException, InvalidRangeException {
    	ArrayDouble.D3 data = original.getCoordinateArray(timeIndex);
    	int[] origin = new int[3];
    	int[] shape = new int[3];
    	shape[0] = subsetList.get(0).length();
    	shape[1] =1;
    	shape[2] =1;
    	origin[0] = timeIndex;
        if (isTimeDependent() && (t_range != null)) {
        	origin[0] = t_range.element(timeIndex);
        }
    	origin[1] = yIndex;
    	origin[2] = xIndex;
    	Array section = data.section(origin, shape);
    	return (ArrayDouble.D1) section.reduce();
    }