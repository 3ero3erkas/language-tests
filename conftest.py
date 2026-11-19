import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help='Choose language for browser')

@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из командной строки
    language = request.config.getoption("--language")
    print(f"\nstart browser for test with language: {language}..")
    
    options = Options()
    # Устанавливаем язык браузера
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    
    # Если у вас снова возникнет ошибка драйвера, раскомментируйте 3 строчки ниже и укажите свой путь:
    # from selenium.webdriver.chrome.service import Service
    # service = Service(executable_path=r"D:\stepik\chromedriver-win64\chromedriver.exe")
    # browser = webdriver.Chrome(service=service, options=options)
    
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    
    yield browser
    print("\nquit browser..")
    browser.quit()