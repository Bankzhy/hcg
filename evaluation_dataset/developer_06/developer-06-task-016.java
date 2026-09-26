public void init(Properties properties)
	{
		super.init(properties);
		String strPathname = properties.getProperty(LOG_FILENAME_PARAM);
		if (strPathname == null)
		{
			strPathname = "";
			properties.setProperty(LOG_FILENAME_PARAM, strPathname);
		}
		String strGetFileLength = properties.getProperty(CALC_FILE_LENGTH_PARAM);
		if (strGetFileLength == null)
		{
			strGetFileLength = TRUE;
			properties.setProperty(CALC_FILE_LENGTH_PARAM, strGetFileLength);
		}
	}