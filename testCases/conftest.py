import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "Oprera":
        driver = webdriver.Opera(executable_path=".\\Drivers\\operadriver.exe")
    elif browser == "Firefox":
        driver = webdriver.Firefox(executable_path=".\\Drivers\\geckodriver.exe")
    elif browser == "Chrome":
        driver = webdriver.Chrome(executable_path=".\\Drivers\\chromedriver.exe")
    else:
        driver = webdriver.Chrome(executable_path=".\\Drivers\\chromedriver.exe")
    return driver

#Browser Hook
def pytest_addoption(parser):       #This will get the value from CLI\hook
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):               #This will return the browser value to setup method
    return request.config.getoption("--browser")

#HTML Reports Hook - Add Environment info
def pytest_configure(config):
    config._metadata['Project Name'] = 'Hybrid Model using Pytest'
    config._metadata['Module Name'] = 'Pytest HTML Report Generation'
    config._metadata['Tester'] = 'Deepesh'

#Add\Modify Environment info
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

