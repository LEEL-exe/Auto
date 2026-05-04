def pytest_configure(config):
    args = [str(a) for a in (config.args or [])]
    is_api = any("tests/api" in a for a in args)
    is_web = any("tests/web" in a for a in args)

    if is_api and not is_web:
        config.option.htmlpath = "report-api.html"
    elif is_web and not is_api:
        config.option.htmlpath = "report-web.html"