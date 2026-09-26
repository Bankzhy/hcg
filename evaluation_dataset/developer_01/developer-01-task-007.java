public void delete()
   {
     if(swigCPtr != 0) {
       Object object = this;
       if (object instanceof RefCounted && mRefCounter != null) {
         mRefCounter.delete();
       } else if (swigCMemOwn) {
         swigCMemOwn = false;
       }
     }
     mJavaRefCount = null;
     mRefCounter = null;
     mObjectToForceFinalize = null;
     mLifecycleReference = null;
     swigCPtr = 0;
   }