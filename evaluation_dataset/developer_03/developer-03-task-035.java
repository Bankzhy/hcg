public static Type[] getInterfacesGenricTypes(final Class<?> clazz) {
        if (clazz == null)
            return null;
        Type[] types=clazz.getGenericInterfaces();
        Type[] gtypes=new Type[0];
        for(Type t:types){
            if (t instanceof ParameterizedType) {
                Type[] gts=((ParameterizedType) t).getActualTypeArguments();
                int olen=gtypes.length;
                int ilen=gts.length;
                Type[] tmp=new Type[olen+ilen];
                System.arraycopy(gtypes,0,tmp,0,olen);
                System.arraycopy(gts, 0, tmp, olen, ilen);
                gtypes=tmp;
             }
        }
        return gtypes;
    }