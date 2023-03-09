import time

from tests.elements_page import FormPageLocators


class TestForm:
    def test_imput(self, driver):
        form_page = FormPageLocators(driver, 'https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983')
        form_page.open()
        form_page.fill_all_fields()

    def test_imput_1(self, driver):
        form_page = FormPageLocators(driver, 'https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983')
        form_page.open()
        form_page.fill_all_reg()

    def test_imput_2(self, driver):
        form_page = FormPageLocators(driver, 'https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983')
        form_page.open()
        form_page.fill_all_fields_n1()

    def test_imput_3(self, driver):
        form_page = FormPageLocators(driver, 'https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983')
        form_page.open()
        form_page.fill_all_fields_n2()

    def test_imput_3(self, driver):
        form_page = FormPageLocators(driver, 'https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983')
        form_page.open()
        form_page.fill_all_fields_no_2()

    def test_imputs_4(self, driver):
        form_page = FormPageLocators(driver, 'https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983')
        form_page.open()
        form_page.fill_all_fields()

    def test_open_no_Nomder_5(self, driver):
        form_page = FormPageLocators(driver, 'https://b2c.pampadu.ru/index.html#49a973bd-2d7c-4b9b-9c28-d986d7757983')
        form_page.open()
        form_page.nomder_all_btn()
