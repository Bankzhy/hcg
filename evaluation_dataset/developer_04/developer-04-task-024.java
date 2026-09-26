public static void browse(String url) throws Exception {
        if (OS_NAME.startsWith("Mac OS")) {
            Method openURL = ClassUtil.getDeclaredMethod(
                    Class.forName("com.apple.eio.FileManager"), true,
                    "openURL", String.class);
            openURL.invoke(null, url);
        } else if (OS_NAME.startsWith("Windows")) {
            Runtime.getRuntime().exec(
                    "rundll32 url.dll,FileProtocolHandler " + url);
        } else {
            String[] browsers = {"firefox", "opera", "konqueror", "epiphany",
                    "mozilla", "netscape"};
            String browser = null;
            for (int count = 0; count < browsers.length && browser == null; count++)
                if (Runtime.getRuntime()
                        .exec(new String[]{"which", browsers[count]})
                        .waitFor() == 0)
                    browser = browsers[count];
            if (browser == null)
                throw new NoSuchMethodException("Could not find web browser");
            else
                Runtime.getRuntime().exec(new String[]{browser, url});
        }
    }