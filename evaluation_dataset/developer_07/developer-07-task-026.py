def get_browser(browser_name, capabilities=None, **options):
    if browser_name == "chrome":
        return webdriver.Chrome(desired_capabilities=capabilities, **options)
    if browser_name == "edge":
        return webdriver.Edge(capabilities=capabilities, **options)
    if browser_name in ["ff", "firefox"]:
        return webdriver.Firefox(capabilities=capabilities, **options)
    if browser_name in ["ie", "internet_explorer"]:
        return webdriver.Ie(capabilities=capabilities, **options)
    if browser_name == "phantomjs":
        return webdriver.PhantomJS(desired_capabilities=capabilities, **options)
    if browser_name == "remote":
        return webdriver.Remote(desired_capabilities=capabilities, **options)
    if browser_name == "safari":
        return webdriver.Safari(desired_capabilities=capabilities, **options)
    raise ValueError("unsupported browser: {}".format(repr(browser_name)))