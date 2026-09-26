private boolean allHaveSameClassification(String property, Iterable<State> examples)
    {
        OrdinalAttribute firstAttribute = null;
        boolean success = true;
        for (State example : examples)
        {
            OrdinalAttribute nextAttribute = (OrdinalAttribute) example.getProperty(property);
            if (firstAttribute == null)
            {
                firstAttribute = nextAttribute;
            }
            else if (!nextAttribute.equals(firstAttribute))
            {
                success = false;
                break;
            }
        }
        if (success)
        {
            allClassification = firstAttribute;
        }
        return success;
    }