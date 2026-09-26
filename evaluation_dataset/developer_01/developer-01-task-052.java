@CheckReturnValue
    @BackpressureSupport(BackpressureKind.FULL)
    @SchedulerSupport(SchedulerSupport.NONE)
    public final Flowable<T> takeLast(int count) {
        if (count < 0) {
            throw new IndexOutOfBoundsException("count >= 0 required but it was " + count);
        } else
        if (count == 0) {
            return RxJavaPlugins.onAssembly(new FlowableIgnoreElements<T>(this));
        } else
        if (count == 1) {
            return RxJavaPlugins.onAssembly(new FlowableTakeLastOne<T>(this));
        }
        return RxJavaPlugins.onAssembly(new FlowableTakeLast<T>(this, count));
    }