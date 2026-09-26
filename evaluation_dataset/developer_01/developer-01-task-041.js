function(action, method, form, callback, scope) {
        var me = this,
            transaction, isUpload, params;
        transaction = new Ext.direct.Transaction({
            provider: me,
            action: action,
            method: method.getName(),
            args: [form, callback, scope],
            callback: scope && Ext.isFunction(callback) ? Ext.Function.bind(callback, scope) : callback,
            isForm: true
        });
        if (me.fireEvent('beforecall', me, transaction, method) !== false) {
            Ext.direct.Manager.addTransaction(transaction);
            isUpload = String(form.getAttribute('enctype')).toLowerCase() == 'multipart/form-data';
            params = {
                extTID: transaction.id,
                extAction: action,
                extMethod: method.getName(),
                extType: 'rpc',
                extUpload: String(isUpload)
            };
            Ext.apply(transaction, {
                form: Ext.getDom(form),
                isUpload: isUpload,
                params: callback && Ext.isObject(callback.params) ? Ext.apply(params, callback.params) : params
            });
            me.fireEvent('call', me, transaction, method);
            me.sendFormRequest(transaction);
        }
    }