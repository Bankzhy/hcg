function getRangeData ( quantifier ) {
	let rangeType = dateRange.DAY;
	let startRange = 'day';
	if ( /seconds?/i.test(quantifier) ) {
		rangeType = dateRange.SEC;
		startRange = 'second';
	} else if ( /minutes?/i.test(quantifier) ) {
		rangeType = dateRange.MIN;
		startRange = 'minute';
	} else if ( /hours?/i.test(quantifier) ) {
		rangeType = dateRange.HOUR;
		startRange = 'hour';
	} else if ( new RegExp(`${days.join('s?|')}s?`, 'i').test(quantifier) ) {
		rangeType = dateRange.DAY * 7;
		startRange = quantifier;
	}
	return {
		rangeType: rangeType,
		startRange: startRange
	};
}