public void blockDecrypt(final long[] c, final long[] p) {
		System.arraycopy(c, 0, vd, 0, nw);
		for (int d = nr; d > 0; d--) {
			if (d % SUBKEY_INTERVAL == 0) {
				final int s = d / SUBKEY_INTERVAL;
				keySchedule(s);
				for (int i = 0; i < nw; i++) {
					fd[i] = vd[i] - ksd[i];
				}
			} else {
				System.arraycopy(vd, 0, fd, 0, nw);
			}
			for (int i = 0; i < nw; i++) {
				ed[i] = fd[rpi[i]];
			}
			for (int j = 0; j < nw / 2; j++) {
				y[0] = ed[j * 2];
				y[1] = ed[j * 2 + 1];
				demix(j, d - 1);
				vd[j * 2] = x[0];
				vd[j * 2 + 1] = x[1];
			}
		}
		keySchedule(0);
		for (int i = 0; i < nw; i++) {
			p[i] = vd[i] - ksd[i];
		}
	}