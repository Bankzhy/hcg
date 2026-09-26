function compareRefs(driver, base, head) {
    const baseRef = base instanceof Branch ? base.getFullName() : base;
    const headRef = head instanceof Branch ? head.getFullName() : head;
    return driver.findParentCommit(baseRef, headRef)
    .then((parentCommit) => {
        return Q.all([
            parentCommit ? parentCommit.getSha() : null,
            baseRef,
            headRef
        ].map((ref) => {
            return ref ? driver.fetchWorkingState(ref) : WorkingState.createEmpty();
        }));
    })
    .spread((parent, base, head) => {
        const conflicts = _compareTrees(parent.getTreeEntries(),
                                     base.getTreeEntries(),
                                     head.getTreeEntries());
        return new TreeConflict({
            base,
            head,
            parent,
            conflicts
        });
    });
}