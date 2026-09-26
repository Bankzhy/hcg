function markAliasSymbolAsReferenced(symbol) {
            var links = getSymbolLinks(symbol);
            if (!links.referenced) {
                links.referenced = true;
                var node = getDeclarationOfAliasSymbol(symbol);
                if (node.kind === 227                       ) {
                    checkExpressionCached(node.expression);
                }
                else if (node.kind === 230                      ) {
                    checkExpressionCached(node.propertyName || node.name);
                }
                else if (ts.isInternalModuleImportEqualsDeclaration(node)) {
                    checkExpressionCached(node.moduleReference);
                }
            }
        }