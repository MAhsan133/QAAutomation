from WebAutomation.common.BrowserHelper import CreateBrowser


def before_all(context):
    context.browser, context.base_url = CreateBrowser.Instance().initiate_instance()


def after_all(context):
    context.browser.close()
    context.browser.quit()
