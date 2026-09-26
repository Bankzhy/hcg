def serializationDecision(cls, obj, serializedClasses,
                              serializedConfiguredUnits):
        isDeclaration = isinstance(obj, Entity)
        isDefinition = isinstance(obj, Architecture)
        if isDeclaration:
            unit = obj.origin
        elif isDefinition:
            unit = obj.entity.origin
        else:
            return True
        assert isinstance(unit, Unit)
        sd = unit._serializeDecision
        if sd is None:
            return True
        else:
            prevPriv = serializedClasses.get(unit.__class__, None)
            seriazlize, nextPriv = sd(unit, obj, isDeclaration, prevPriv)
            serializedClasses[unit.__class__] = nextPriv
            return seriazlize