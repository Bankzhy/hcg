function inspectFunctionDeclaration(emitted) {
            let node = emitted.node, params = node.params || [];
            let startLine = sourceCode.getLine(node),
                lastArgLine = params.length ? sourceCode.getEndingLine(params.slice(-1) [0]) : startLine,
                functionDeclarationLineText, currentIndent, currentIndentLevel;
            function inspectParam(paramIndent, paramIndentDesc, param) {
                let indentRegExp = new RegExp("^" + paramIndent + "[^\\s(\/\*)]"),
                    paramLineText = sourceCode.getTextOnLine(sourceCode.getLine(param));
                !indentRegExp.test(paramLineText) && context.report({
                    node: param,
                    message: `Only use indent of ${paramIndentDesc}.`
                });
            }
            if (emitted.exit || startLine === lastArgLine) {
                return;
            }
            functionDeclarationLineText = sourceCode.getTextOnLine(startLine);
            currentIndent = functionDeclarationLineText.slice(
                0,
                functionDeclarationLineText.indexOf(functionDeclarationLineText.trim())
            );
            currentIndentLevel = (currentIndent.match(BASE_INDENTATION_STYLE_REGEXP_GLOBAL) || []).length;
            if (getIndentString(BASE_INDENTATION_STYLE, currentIndentLevel) !== currentIndent) {
                return;
            }
            const paramIndent = getIndentString(BASE_INDENTATION_STYLE, currentIndentLevel + 1);
            const paramIndentDesc = getIndentDescription(BASE_INDENTATION_STYLE, currentIndentLevel + 1);
            params.forEach(inspectParam.bind(null, paramIndent, paramIndentDesc));
        }