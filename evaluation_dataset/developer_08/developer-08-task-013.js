function removeTypesFromUnionType(type, typeKind, isOfTypeKind, allowEmptyUnionResult) {
            if (type.flags & 16384            ) {
                var types = type.types;
                if (ts.forEach(types, function (t) { return !!(t.flags & typeKind) === isOfTypeKind; })) {
                    var narrowedType = getUnionType(ts.filter(types, function (t) { return !(t.flags & typeKind) === isOfTypeKind; }));
                    if (allowEmptyUnionResult || narrowedType !== emptyObjectType) {
                        return narrowedType;
                    }
                }
            }
            else if (allowEmptyUnionResult && !!(type.flags & typeKind) === isOfTypeKind) {
                return getUnionType(emptyArray);
            }
            return type;
        }