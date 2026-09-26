private ValueMember[] getValueMembers() {
        if (valueMembers != null)
            return valueMembers;
        LocalContained[] c = _contents(DefinitionKind.dk_ValueMember, false);
        valueMembers = new ValueMember[c.length];
        for (int i = 0; i < c.length; ++i) {
            ValueMemberDefImpl vmdi = (ValueMemberDefImpl) c[i];
            valueMembers[i] = new ValueMember(vmdi.name(), vmdi.id(),
                    ((LocalContained) vmdi.defined_in).id(),
                    vmdi.version(),
                    vmdi.type(), vmdi.type_def(),
                    vmdi.access());
        }
        return valueMembers;
    }