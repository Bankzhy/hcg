function clearRefinements(attribute) {
    var clear = RefinementList.clearRefinement;
    var patch = {
      numericRefinements: this._clearNumericRefinements(attribute),
      facetsRefinements: clear(this.facetsRefinements, attribute, 'conjunctiveFacet'),
      facetsExcludes: clear(this.facetsExcludes, attribute, 'exclude'),
      disjunctiveFacetsRefinements: clear(this.disjunctiveFacetsRefinements, attribute, 'disjunctiveFacet'),
      hierarchicalFacetsRefinements: clear(this.hierarchicalFacetsRefinements, attribute, 'hierarchicalFacet')
    };
    if (patch.numericRefinements === this.numericRefinements &&
        patch.facetsRefinements === this.facetsRefinements &&
        patch.facetsExcludes === this.facetsExcludes &&
        patch.disjunctiveFacetsRefinements === this.disjunctiveFacetsRefinements &&
        patch.hierarchicalFacetsRefinements === this.hierarchicalFacetsRefinements) {
      return this;
    }
    return this.setQueryParameters(patch);
  }