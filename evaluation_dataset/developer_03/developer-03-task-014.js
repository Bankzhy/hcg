function recycleGraph()
   {
      var childNodes = graph.selectAll('g > *').remove();
      if (!Array.isArray(childNodes) && !Array.isArray(childNodes['0'])) { return; }
      childNodes = childNodes['0'];
      for (var cntr = 0; cntr < childNodes.length; cntr++)
      {
         var childNode = childNodes[cntr];
         if (childNode instanceof SVGPathElement) { svgElementMap['path'].push(childNode); }
         else if (childNode instanceof SVGCircleElement) { svgElementMap['circle'].push(childNode); }
         else if (childNode instanceof SVGTextElement) { svgElementMap['text'].push(childNode); }
         else if (childNode instanceof SVGGElement)
         {
            childNode.removeAttribute('transform');
            svgElementMap['g'].push(childNode);
         }
      }
   }