public void print (@Nonnull final PrintStream aPW)
  {
    aPW.println ("------------------------------");
    if (isDouble ())
      aPW.println ("double value = " + doubleValue ());
    else
      aPW.println ("float value = " + floatValue ());
    aPW.print ("sign=" + signBit ());
    aPW.print (", exponent=" + exponentBits () + " (biased=" + biasedExponent ());
    if (isZero ())
      aPW.println (", zero)");
    else
      if (isExponentReserved ())
        aPW.println (", reserved)");
      else
        if (isDenormalized ())
          aPW.println (", denormalized, use " + unbiasedExponent () + ")");
        else
          aPW.println (", normalized, unbiased=" + unbiasedExponent () + ")");
    aPW.println ("significand=" + significandBits ());
  }