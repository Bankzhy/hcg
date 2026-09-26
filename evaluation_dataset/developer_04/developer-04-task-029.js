function toggleHierarchicalFacetRefinement(facet, value) {
    if (!this.isHierarchicalFacet(facet)) {
      throw new Error(
        facet + ' is not defined in the hierarchicalFacets attribute of the helper configuration');
    }
    var separator = this._getHierarchicalFacetSeparator(this.getHierarchicalFacetByName(facet));
    var mod = {};
    var upOneOrMultipleLevel = this.hierarchicalFacetsRefinements[facet] !== undefined &&
      this.hierarchicalFacetsRefinements[facet].length > 0 && (
      this.hierarchicalFacetsRefinements[facet][0] === value ||
      this.hierarchicalFacetsRefinements[facet][0].indexOf(value + separator) === 0
    );
    if (upOneOrMultipleLevel) {
      if (value.indexOf(separator) === -1) {
        mod[facet] = [];
      } else {
        mod[facet] = [value.slice(0, value.lastIndexOf(separator))];
      }
    } else {
      mod[facet] = [value];
    }
    return this.setQueryParameters({
      hierarchicalFacetsRefinements: defaults({}, mod, this.hierarchicalFacetsRefinements)
    });
  }