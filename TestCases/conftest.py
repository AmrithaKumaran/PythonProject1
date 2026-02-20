""""
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Fixture method will be there in conftest file
#it is a common file used in all our test cases
@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver
"""
#https://github.com/KP953/OpenCart/blob/master/src/test/resources/config.properties
#https://github.com/TapashiRoy/UIAutomationProject-OpenCart/blob/master/logs/opencart.log

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
"""

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Amritha'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\Reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

"""

import os
import pytest
from datetime import datetime


def pytest_configure(config):
    report_dir = os.path.join(os.getcwd(), "Reports")
    os.makedirs(report_dir, exist_ok=True)

    report_file = datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html"
    config.option.htmlpath = os.path.join(report_dir, report_file)


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata["Project Name"] = "PythonProject1"
    metadata["Module Name"] = "CustRegistration"
    metadata["Tester"] = "Amritha"

    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

















""" CROSS BROWSER TESTING---------

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to execute tests: chrome, firefox, edge"
    )


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("browser")

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)

    else:
        raise ValueError("Unsupported browser!")

    yield driver
    driver.quit()
"""




