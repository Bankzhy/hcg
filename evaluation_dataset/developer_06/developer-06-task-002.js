function() {
      var template = this.getTemplate();
      if (template === false) {
        return;
      }
      if (!template) {
        throw new Marionette.Error({
          name: 'UndefinedTemplateError',
          message: 'Cannot render the template since it is null or undefined.'
        });
      }
      var data = this.mixinTemplateHelpers(this.serializeData());
      var html = Marionette.Renderer.render(template, data, this);
      this.attachElContent(html);
      return this;
    }