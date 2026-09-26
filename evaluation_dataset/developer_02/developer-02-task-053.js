function hideNodeContextMenu(event)
   {
      if (typeof selectedContextNode === 'undefined') { return; }
      var contextMenuButton = $('#context-menu');
      var popupmenu = $('#contextpopup .mdl-menu__container');
      if (event)
      {
         event.preventDefault();
         if (!$(event.target).parents('#contextpopup').length > 0)
         {
            if (popupmenu.hasClass('is-visible')) { contextMenuButton.click(); }
            fadeRelatedNodes(selectedContextNode, false, nodes, links);
            selectedContextNode = undefined;
         }
      }
      else
      {
         if (popupmenu.hasClass('is-visible')) { contextMenuButton.click(); }
         fadeRelatedNodes(selectedContextNode, false, nodes, links);
         selectedContextNode = undefined;
      }
   }