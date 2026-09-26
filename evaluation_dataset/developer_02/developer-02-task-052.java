public <T> PageData<T> page(PageRequest pageRequest, final String sql, final Map params, final String[] sortColumns, final Class[] target) {
		if (pageRequest == null) {
			pageRequest = getDefaultPageRequest();
		}
		String sortColumName = null;
		boolean ascending = true;
		int sort = pageRequest.getSort();
		if (sort != 0) {
			ascending = sort > 0;
			if (!ascending) {
				sort = -sort;
			}
			int index = sort - 1;
			if (index >= sortColumns.length) {
				index = 1;
			}
			sortColumName = sortColumns[index];
		}
		int page = pageRequest.getPage();
		int pageSize = pageRequest.getSize();
		PageData<T> pageData = page(sql, params, page, pageSize, sortColumName, ascending, target);
		if (pageData.getItems().isEmpty() && pageData.currentPage != 0) {
			if (pageData.currentPage != page) {
				int newPage = pageData.getCurrentPage();
				pageData = page(sql, params, newPage, pageSize, sortColumName, ascending, target);
			}
		}
		return pageData;
	}