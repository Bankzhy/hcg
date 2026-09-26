function getEffectiveCallArguments(node) {
            var args;
            if (node.kind === 170                               ) {
                var template = node.template;
                args = [undefined];
                if (template.kind === 183                         ) {
                    ts.forEach(template.templateSpans, function (span) {
                        args.push(span.expression);
                    });
                }
            }
            else if (node.kind === 139                ) {
                return undefined;
            }
            else {
                args = node.arguments || emptyArray;
            }
            return args;
        }