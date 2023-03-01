from selenium import webdriver
from pages.main_page import MainPage
from pages.cars_page import CarsPage
from data.data import BaseData
from time import sleep

def test_demo():
    driver = webdriver.Chrome()
    driver.get('https://youtube.com')
    assert driver.title == 'YouTube', f'Error: Title must be {driver.title}'

def test_demo_test():
    driver = webdriver.Chrome()
    driver.get('https://youtube.com')
    print(driver.get_credentials)
    assert 'youtube.com' in driver.current_url

def test_open_garage(browser):
    mp = MainPage(browser, 'https://qauto.forstudy.space/')
    # mp.open()
    # mp.auth_form(BaseData.baseLogin, BaseData.basePassword)
    mp.auth_by_url(BaseData.baseLogin, BaseData.basePassword, BaseData.host)
    mp.click_sign_in()
    mp.is_open_modal_window()
    mp.enter_login('1.test3131@gmail.com')
    mp.enter_password('Test1test')
    mp.click_login_button()
    assert mp.is_url_changed('/panel/garage')

def test_add_new_car(browser):
    mp = MainPage(browser, BaseData.base_url)
    car_page = CarsPage(browser, BaseData.car_url)
    # mp.open()
    # mp.auth_form(BaseData.baseLogin, BaseData.basePassword)
    mp.auth_by_url(BaseData.baseLogin, BaseData.basePassword, BaseData.host)
    mp.click_sign_in()
    mp.is_open_modal_window()
    mp.enter_login('1.test3131@gmail.com')
    mp.enter_password('Test1test')
    mp.click_login_button()
    assert mp.is_url_changed(BaseData.car_url), 'Url Not changed!'
    sleep(3)
    car_page.click_button_add_car()
    car_page.is_open_modal_window()
    car_page.click_on_select_brand()
    car_page.choose_brand_porsche()
    car_page.click_on_select_model()
    car_page.choose_model_panamera()
    millage = BaseData.get_millage()
    car_page.enter_car_millage(millage)
    car_page.click_button_add_in_modal_window()
    sleep(3)
    assert int(car_page.get_millage_first_car()) == millage



    # https://youtu.be /3K3W_Gfd-e0