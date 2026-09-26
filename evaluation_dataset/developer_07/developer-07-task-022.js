function(left, right) {
		if ((left === null) && (right === null)) {
			return true;
		} else if ((left === null) || (right === null)) {
			return false;
		}
		if (!Buffer.isBuffer(left)) {
			left = new Buffer(left);
		}
		if (!Buffer.isBuffer(right)) {
			right = new Buffer(right);
		}
		var same = (left.length === right.length),
			i = 0,
			max = left.length;
		while (i < max) {
			same &= (left[i] == right[i]);
			i++;
		}
		return same;
	}