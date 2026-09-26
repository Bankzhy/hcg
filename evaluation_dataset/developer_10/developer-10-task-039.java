private static boolean hasKey ( final ArtifactInformation art, final String key )
    {
        if ( key == null )
        {
            return false;
        }
        final String keysString = art.getMetaData ().get ( P2RepoConstants.KEY_FRAGMENT_KEYS );
        if ( keysString == null )
        {
            return false;
        }
        final String[] keys = keysString.split ( P2RepoConstants.ENTRY_DELIMITER );
        for ( final String actualKey : keys )
        {
            if ( key.equals ( actualKey ) )
            {
                return true;
            }
        }
        return false;
    }