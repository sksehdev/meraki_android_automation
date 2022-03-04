import pytest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


locators = {"apiKeyLabel" : 'com.meraki.mapidemo:id/apiKeyLabel'

}

constants = {"apiKeyLabel" : 'Enter API Key',
              "APIKEY" : "",  ## Please Enter API key
             "device_ips" : ['172.29.4.159', '172.29.4.135', '172.29.6.59', '172.29.6.38']
}

@pytest.fixture
def driver():
    ## Please enter the arguments according to your local setup
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "automationName": "uiautomator2",
        "app": "C:/Users/ssehdev/Downloads/app-debug.apk",  #
        "appWaitForLaunch": False,
        "adbExecTimeout": 120000
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print("Connected to Meraki android app")
    time.sleep(10)
    return driver

@pytest.fixture(scope = 'module')
def main_page_data():
    return {}

@pytest.fixture(scope = 'module')
def first_group_data():
    return {}


def test_app_opens(driver):
        opening1_text = driver.find_element(by=AppiumBy.ID, value='com.meraki.mapidemo:id/apiKeyLabel')
        assert opening1_text.text == constants['apiKeyLabel']


def test_input_api_key_and_get_data(driver,main_page_data,first_group_data):
            ## Test that heading of main page connect after login is correct
            ## get elements from main page
            ## This test also fetched all the information from app and create data to verify

            driver.find_element(by=AppiumBy.ID, value='com.meraki.mapidemo:id/apiKeyTxt').send_keys(
                                constants["APIKEY"])
            driver.find_element(by=AppiumBy.ID, value='com.meraki.mapidemo:id/goButton').click()
            time.sleep(10)
            main_page = driver.find_element(by=AppiumBy.ID,
                                                 value='com.meraki.mapidemo:id/action_bar_root').is_displayed()
            assert main_page == True
            app_text_field = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
            main_page_data["app_text_field"] = [element.text for element in app_text_field]
            main_page_data["main_page_icons"] = [driver.find_elements(By.CLASS_NAME, "android.widget.ImageView")]
            device_names = driver.find_elements(by=AppiumBy.ID, value='com.meraki.mapidemo:id/deviceName')
            main_page_data["device_names"] = [deviceName.text for deviceName in device_names]
            device_details = driver.find_elements(by=AppiumBy.ID, value='com.meraki.mapidemo:id/deviceDetails')
            main_page_data["device_details"] = [deviceDetail.text for deviceDetail in device_details]
            # print(f'The data is {main_page_data}')
            groups = driver.find_elements(by=AppiumBy.ID, value='com.meraki.mapidemo:id/user_list_item')
            # print(f'The groups are {groups}')
            groups[0].click()
            time.sleep(10)
            first_group_data["first_group_contents"] = [element.text for element in
                                                        driver.find_elements(By.CLASS_NAME, 'android.widget.TextView')]
            first_group_data["first_group_model"] = driver.find_element(by=AppiumBy.ID,
                                                                        value='com.meraki.mapidemo:id/modelValue').text
            first_group_data["first_group_sn"] = driver.find_element(by=AppiumBy.ID,
                                                                     value='com.meraki.mapidemo:id/serialValue').text
            first_group_data["first_group_usage"] = driver.find_element(by=AppiumBy.ID,
                                                                        value='com.meraki.mapidemo:id/usageValue').text
            first_group_data["first_group_clients"] = driver.find_element(by=AppiumBy.ID,
                                                                          value='com.meraki.mapidemo:id/numClientsValue').text
            # print(f'the first_group_data is {first_group_data}')


def test_user_main_heading(main_page_data):
        ## Test that heading of main page after login is correct
        assert main_page_data['app_text_field'][0] == "Wireless AP's"

def test_check_device_names(main_page_data):
      ## Test that device names are correct after login is correct
      assert main_page_data['device_names'] == ['Wireless New Stadium', 'AP', 'Wireless AP 1', 'Wireless other desk']

def test_check_device_details(main_page_data):
    assert main_page_data['device_details'] == constants["device_ips"]

def test_check_device_icons(main_page_data):
    assert len(main_page_data['main_page_icons'][0]) == 4

def test_check_first_group_heading(first_group_data):
    assert first_group_data["first_group_contents"][0] == 'Wireless New Stadium'

def test_check_first_group_model_number(first_group_data):
    assert first_group_data["first_group_model"] == 'MR34'

def test_check_first_group_serial_number(first_group_data):
    assert first_group_data["first_group_sn"] == 'Q2FD-257W-K29Z'

def test_check_first_group_usage(first_group_data):
    assert first_group_data["first_group_usage"] == '0.0 Bytes'

def test_check_first_group_clients(first_group_data):
    assert first_group_data["first_group_clients"] == '0'

def test_close_app(driver):
        driver.close_app()
        driver.quit()