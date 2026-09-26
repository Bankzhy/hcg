function() {
        var me = this,
            pressedButtons = [],
            ln, i, item, items;
        me.callParent(arguments);
        items = this.getItems();
        ln = items.length;
        for (i = 0; i < ln; i++) {
            item = items.items[i];
            if (item.getInitialConfig('pressed')) {
                pressedButtons.push(items.items[i]);
            }
        }
        me.updateFirstAndLastCls(items);
        me.setPressedButtons(pressedButtons);
    }