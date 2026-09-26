function(value, increment, minValue, maxValue) {
        var newValue = value,
            m;
        if (!(increment && value)) {
            return value;
        }
        m = value % increment;
        if (m !== 0) {
            newValue -= m;
            if (m * 2 >= increment) {
                newValue += increment;
            } else if (m * 2 < -increment) {
                newValue -= increment;
            }
        }
        return Ext.Number.constrain(newValue, minValue,  maxValue);
    }