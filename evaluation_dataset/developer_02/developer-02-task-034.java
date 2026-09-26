public static void checkTermLength(final int termLength)
    {
        if (termLength < TERM_MIN_LENGTH)
        {
            throw new IllegalStateException(
                "Term length less than min length of " + TERM_MIN_LENGTH + ": length=" + termLength);
        }
        if (termLength > TERM_MAX_LENGTH)
        {
            throw new IllegalStateException(
                "Term length more than max length of " + TERM_MAX_LENGTH + ": length=" + termLength);
        }
        if (!BitUtil.isPowerOfTwo(termLength))
        {
            throw new IllegalStateException("Term length not a power of 2: length=" + termLength);
        }
    }