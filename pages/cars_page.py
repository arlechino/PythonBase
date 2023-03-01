from .base_page import BasePage
from selenium.webdriver.common.by import By

class CarsPage(BasePage):
    __button_add_car = 'button.btn.btn-primary'
    __modal_window = '.modal-content'
    __select_brand = '#addCarBrand'
    __brand_porsche = '//select[@id="addCarBrand"]/option[contains(text(), "Porsche")]'
    __select_car_model = '#addCarModel'
    __model_porsche_panamera = '//select[@id="addCarModel"]/option[contains(text(), "Panamera")]'
    __input_car_millage = '#addCarMileage'
    __button_cancel = f'{__modal_window} button.btn.btn-secondary'
    __button_add_car_modal_window = f'{__modal_window} button.btn.btn-primary'
    __millage_first_car = 'ul.car-list>li:first-child input[name="miles"]'

    def click_button_add_car(self):
        self.wait_and_click_on_element(By.CSS_SELECTOR, self.__button_add_car, timeout=10)

    def is_open_modal_window(self):
        return self.is_element_clickable(By.CSS_SELECTOR, self.__modal_window)

    def click_on_select_brand(self):
        self.wait_and_click_on_element(By.CSS_SELECTOR, self.__select_brand)

    def choose_brand_porsche(self):
        self.wait_and_click_on_element(By.XPATH, self.__brand_porsche)

    def click_on_select_model(self):
        self.wait_and_click_on_element(By.CSS_SELECTOR, self.__select_car_model)

    def choose_model_panamera(self):
        self.wait_and_click_on_element(By.XPATH, self.__model_porsche_panamera)

    def enter_car_millage(self, millage: int):
        self.browser.find_element(By.CSS_SELECTOR, self.__input_car_millage).send_keys(millage)

    def click_button_add_in_modal_window(self):
        self.browser.find_element(By.CSS_SELECTOR, self.__button_add_car_modal_window).click()

    def click_button_cancel_in_modal_window(self):
        self.browser.find_element(By.CSS_SELECTOR, self.__button_cancel).click()

    def get_millage_first_car(self) -> str:
        return self.browser.find_element(By.CSS_SELECTOR, self.__millage_first_car).get_attribute('value')