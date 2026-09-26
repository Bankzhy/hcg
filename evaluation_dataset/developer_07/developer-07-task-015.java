public static IJavaStackFrame getStackFrame(IValue value)
            throws CoreException {
        IStatusHandler handler = getStackFrameProvider();
        if (handler != null) {
            IJavaStackFrame stackFrame = (IJavaStackFrame) handler
                    .handleStatus(fgNeedStackFrame, value);
            if (stackFrame != null) {
                return stackFrame;
            }
        }
        IDebugTarget target = value.getDebugTarget();
        IJavaDebugTarget javaTarget = (IJavaDebugTarget) target
                .getAdapter(IJavaDebugTarget.class);
        if (javaTarget != null) {
            IThread[] threads = javaTarget.getThreads();
            for (int i = 0; i < threads.length; i++) {
                IThread thread = threads[i];
                if (thread.isSuspended()) {
                    return (IJavaStackFrame) thread.getTopStackFrame();
                }
            }
        }
        return null;
    }