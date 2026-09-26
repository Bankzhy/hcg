function (node) {
        if (!node.isLeaf()) {
            throw new Error('goToLeaf: passed a node which is not a leaf.');
        }
        var me = this,
            card = me.getDetailCard(node),
            container = me.getDetailContainer(),
            sharedContainer = container == this,
            layout = me.getLayout(),
            animation = (layout) ? layout.getAnimation() : false;
        if (card) {
            if (container.getItems().indexOf(card) === -1) {
                container.add(card);
            }
            if (sharedContainer) {
                if (me.getActiveItem() instanceof Ext.dataview.List) {
                    me.setLastActiveList(me.getActiveItem());
                }
                me.setLastNode(node);
            }
            if (animation) {
                animation.setReverse(false);
            }
            container.setActiveItem(card);
            me.syncToolbar();
        }
    }