public static OSFamily getOSFamily(String osName)
  {
    final OSFamily retval;
    if (osName != null && osName.length() > 0)
    {
      if (osName.startsWith("Windows"))
        retval = OSFamily.WINDOWS;
      else if (osName.startsWith("Mac"))
        retval = OSFamily.MAC;
      else if (osName.startsWith("Linux"))
        retval = OSFamily.LINUX;
      else
        retval = OSFamily.UNKNOWN;
    } else
      retval = OSFamily.UNKNOWN;
    return retval;
  }