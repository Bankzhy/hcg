public void updateFilters(FilterOptions[] filterOptions)
            throws XZIOException {
        if (blockEncoder != null)
            throw new UnsupportedOptionsException("Changing filter options "
                    + "in the middle of a XZ Block not implemented");
        if (filterOptions.length < 1 || filterOptions.length > 4)
            throw new UnsupportedOptionsException(
                        "XZ filter chain must be 1-4 filters");
        filtersSupportFlushing = true;
        FilterEncoder[] newFilters = new FilterEncoder[filterOptions.length];
        for (int i = 0; i < filterOptions.length; ++i) {
            newFilters[i] = filterOptions[i].getFilterEncoder();
            filtersSupportFlushing &= newFilters[i].supportsFlushing();
        }
        RawCoder.validate(newFilters);
        filters = newFilters;
    }