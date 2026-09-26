protected void validatePicture(MediaPicture picture)
  {
    if (picture == null)
      throw new IllegalArgumentException("The picture is NULL.");
    if (!picture.isComplete())
      throw new IllegalArgumentException("The picture is not complete.");
    PixelFormat.Type type = picture.getFormat();
    if ((type != getPictureType()) && (willResample() &&
        type != mToImageResampler.getOutputFormat()))
      throw new IllegalArgumentException(
        "Picture is of type: " + type + ", but must be " +
        getPictureType() + (willResample()
          ? " or " + mToImageResampler.getOutputFormat()
          : "") +
        ".");
  }