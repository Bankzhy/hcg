function(buttons){
        var buttonContainer = this.el.find('.as-buttons');
        buttonContainer.html('');
        buttons['取消'] = this.hide.bind(this);
        Object.keys(buttons).forEach(function(key){
            var n = buttons[key],
                btn = $($.tpl(buttonTpl, {
                    text: key
                }));
            bindTapEvent(btn[0], function(e){
                e.stopPropagation();
                e.preventDefault();
                if(typeof this.action === 'function'){
                    this.action.call(this.context, e);
                }else if(typeof this.action === 'string'){
                    location.href = this.action;
                };
            }.bind({action: n, context: this}));
            btn.on('touchstart', function(e){
                $(e.target).addClass('as-active');
            }).on('touchend', function(e){
                $(e.target).removeClass('as-active');
            });
            buttonContainer.append(btn);
        }.bind(this));
        return this;
    }