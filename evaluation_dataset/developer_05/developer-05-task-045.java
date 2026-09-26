public T get(Class<?> clazz)
   {
      if (clazz == null)
         throw new IllegalArgumentException("Null class");
      Map<String, WeakReference<T>> classLoaderCache = getClassLoaderCache(clazz.getClassLoader());
      WeakReference<T> weak = classLoaderCache.get(clazz.getName());
      if (weak != null)
      {
         T result = weak.get();
         if (result != null)
            return result;
      }
      T result = instantiate(clazz);
      weak = new WeakReference<T>(result);
      classLoaderCache.put(clazz.getName(), weak);
      generate(clazz, result);
      return result;
   }