def changelist_view(self, request, extra_context=None, *args, **kwargs):
        if 'actions_column' not in self.list_display:
            self.list_display.append('actions_column')
        if request.is_ajax():
            cmd = request.POST.get('__cmd')
            if cmd == 'toggle_boolean':
                return self._toggle_boolean(request)
            elif cmd == 'move_node':
                return self._move_node(request)
            else:
                return HttpResponseBadRequest('Oops. AJAX request not understood.')
        self._refresh_changelist_caches()
        extra_context = extra_context or {}
        extra_context['STATIC_URL'] = settings.STATIC_URL
        extra_context['JQUERY_LIB'] = settings.JQUERY_LIB
        extra_context['JQUERYUI_LIB'] = settings.JQUERYUI_LIB
        extra_context['tree_structure'] = mark_safe(json.dumps(
            _build_tree_structure(self.model)))
        return super(TreeEditor, self).changelist_view(request, extra_context, *args, **kwargs)