public int compareTo(ASCIIString comparator)
    {
        int n = Math.min(length, comparator.length());
        for (int i = 0; i < n; i++)
        {
            byte b1 = get(i);
            byte b2 = comparator.get(i);
            if (b1 == b2)
            {
                continue;
            }
            if (b1 < b2)
            {
                return -1;
            }
            return 1;
        }
        return length - comparator.length();
    }