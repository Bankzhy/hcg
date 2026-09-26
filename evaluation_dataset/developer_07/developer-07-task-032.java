static void getLuma20NoRoundInt(int[] pic, int picW, int[] blk, int blkOff, int blkStride, int x, int y, int blkW,
            int blkH) {
        int off = y * picW + x;
        for (int j = 0; j < blkH; j++) {
            int off1 = -2;
            for (int i = 0; i < blkW; i++) {
                int a = pic[off + off1] + pic[off + off1 + 5];
                int b = pic[off + off1 + 1] + pic[off + off1 + 4];
                int c = pic[off + off1 + 2] + pic[off + off1 + 3];
                blk[blkOff + i] = a + 5 * ((c << 2) - b);
                ++off1;
            }
            off += picW;
            blkOff += blkStride;
        }
    }