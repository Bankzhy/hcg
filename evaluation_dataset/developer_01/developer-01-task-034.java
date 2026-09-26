public static int[] readScalingList(BitReader src, int sizeOfScalingList)  {
        int[] scalingList = new int[sizeOfScalingList];
        int lastScale = 8;
        int nextScale = 8;
        for (int j = 0; j < sizeOfScalingList; j++) {
            if (nextScale != 0) {
                int deltaScale = readSE(src, "deltaScale");
                nextScale = (lastScale + deltaScale + 256) % 256;
                if (j == 0 && nextScale == 0)
                    return null;
            }
            scalingList[j] = nextScale == 0 ? lastScale : nextScale;
            lastScale = scalingList[j];
        }
        return scalingList;
    }