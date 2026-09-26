function inspectVariableDeclaration(emitted) {
            let node = emitted.node, code = sourceCode.getText(node);
            if (emitted.exit) {
                return;
            }
            for (let i = 2; i < code.length; i++) {
                if (code [i] === "=") {
                    (!/^[^\/\s] $/.test(code.slice(i-2, i))) && context.report({
                        node: node,
                        message: "There should be only a single space between assignment operator '=' and its left side."
                    });
                    (!/^ [^\/\s]$/.test(code.slice(i+1, i+3))) && context.report({
                        node: node,
                        message: "There should be only a single space between assignment operator '=' and its right side."
                    });
                }
            }
        }