function (node) {
            var result = '',
                i, n, attr, child;
            if (node.nodeType === document.TEXT_NODE) {
                return node.nodeValue;
            }
            result += '<' + node.nodeName;
            if (node.attributes.length) {
                for (i = 0, n = node.attributes.length; i < n; i++) {
                    attr = node.attributes[i];
                    result += ' ' + attr.name + '="' + attr.value + '"';
                }
            }
            result += '>';
            if (node.childNodes && node.childNodes.length) {
                for (i = 0, n = node.childNodes.length; i < n; i++) {
                    child = node.childNodes[i];
                    result += this.serializeNode(child);
                }
            }
            result += '</' + node.nodeName + '>';
            return result;
        }