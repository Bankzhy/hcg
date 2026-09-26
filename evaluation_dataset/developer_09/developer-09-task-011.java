protected static boolean isZip ( final ArtifactInformation artifact )
    {
        if ( artifact.getName ().toLowerCase ().endsWith ( ".zip" ) )
        {
            return true;
        }
        final String mdExtension = artifact.getMetaData ().get ( MK_MVN_EXTENSION );
        if ( mdExtension != null && mdExtension.equalsIgnoreCase ( "zip" ) )
        {
            return true;
        }
        final String mdMime = artifact.getMetaData ().get ( MK_MIME_TYPE );
        if ( mdMime != null && mdMime.equalsIgnoreCase ( "application/zip" ) )
        {
            return true;
        }
        return false;
    }