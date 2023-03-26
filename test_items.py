from selenium.webdriver.common.by import By
import requests


#Locators
url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
cart_submit_button = "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"

def test_button_cart(browser):
    """Cart button exist test"""
    try:
        browser.get(url)
        cart_button = browser.find_element(By.XPATH, cart_submit_button)

        assert cart_button != None, "Check locator params"

        cart_button_text = browser.find_element(By.XPATH, cart_submit_button).text
        browser_response_JSON = requests.get(browser.current_url)  # For browser language check
        browser_language = browser_response_JSON.headers['Content-Language']  # Browser language

        if browser_language == 'fr':
            assert "Ajouter au panier" == cart_button_text, "OOOPPS! Something going wrong!"
    except Exception as e:
        raise e






