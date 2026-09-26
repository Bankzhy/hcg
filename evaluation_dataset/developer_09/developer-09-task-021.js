function getStartOffset(line, pos, prefix) {
	if (!prefix) {
		return 0;
	}
	const stream = new StreamReader(line);
	const compiledPrefix = String(prefix).split('').map(code);
	stream.pos = pos;
	let result;
	while (!stream.sol()) {
		if (consumePair(stream, SQUARE_BRACE_R, SQUARE_BRACE_L) || consumePair(stream, CURLY_BRACE_R, CURLY_BRACE_L)) {
			continue;
		}
		result = stream.pos;
		if (consumeArray(stream, compiledPrefix)) {
			return result;
		}
		stream.pos--;
	}
	return -1;
}