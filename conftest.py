import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LANGUAGES = {'ar': 'العربيّة', 'ca' : 'català',
             'cs': 'česky', 'da': 'dansk',
             'de': 'Deutsch', 'en-gb': 'British English', 
             'el': 'Ελληνικά', 'es': 'español',
             'fi': 'suomi', 'fr': 'français', 
             'it': 'italiano', 'ko': '한국어',
             'nl': 'Nederlands', 'pl': 'polski', 
             'pt': 'Português', 'pt-br': 'Português Brasileiro',
             'ro': 'Română', 'ru': 'Русский', 
             'sk': 'Slovensky', 'uk': 'Українська',
             'zh-cn': '简体中文'
}

CHOOSE_LANGUAGE = ' '.join([f'\n{key}: {value}' for key, value in LANGUAGES.items()])

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                      help='Choose language: ' + CHOOSE_LANGUAGE)


@pytest.fixture(scope="function")
def browser(request):
    if request.config.getoption('language') in LANGUAGES:
        language = request.config.getoption('language')
    else:
        raise pytest.UsageError('Choose --language from the list: ' + CHOOSE_LANGUAGE)
    print("\n open browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    """
    #  If you want to choose firefox browser for test:
    fp = webdriver.FirefoxProfile('intl.accept_languages', language)
    browser = webdriver.Firefox(firefox_options=fp)

    """
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()