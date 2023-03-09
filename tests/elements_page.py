import time
from locator.form_locator import FormPageLocators

from pages.base_page import BasePage


class FormPageLocators(BasePage):
    locator = FormPageLocators

    def fill_all_fields(self):
        self.element_is_visible(self.locator.MAIN_IMPUT).send_keys("Е 010 ВВ")
        self.element_is_visible(self.locator.REGION_IMPUT).send_keys("777")
        self.element_is_visible(self.locator.BTN_CONT).click()


    def nomder_all_btn(self):
        self.element_is_visible(self.locator.NO_NOMBER).click()
        self.element_is_visible(self.locator.BTN_CONT_BAKE).click()

    def nomder_all_btn_Bake(self):
        self.element_is_visible(self.locator.NO_NOMBER).click()
        self.element_is_visible(self.locator.BTN_CONT).click()

    def fill_all_reg(self):
        self.element_is_visible(self.locator.MAIN_IMPUT).send_keys("Е 111 ВВ")
        self.element_is_visible(self.locator.REGION_IMPUT).send_keys("100")
        self.element_is_visible(self.locator.BTN_CONT).click()
        #Принимает не валидные данные
    def fill_all_fields_n1(self):
        self.element_is_visible(self.locator.MAIN_IMPUT).send_keys("Е 111 ВВ")
        self.element_is_visible(self.locator.REGION_IMPUT).send_keys("999")
        self.element_is_visible(self.locator.BTN_CONT).click()

    def fill_all_fields_n2(self):
        self.element_is_visible(self.locator.MAIN_IMPUT).send_keys("m 999 bb")
        self.element_is_visible(self.locator.REGION_IMPUT).send_keys("777")
        self.element_is_visible(self.locator.BTN_CONT).click()

    def fill_all_fields_no_2(self):
        self.element_is_visible(self.locator.MAIN_IMPUT).send_keys("Е 111 ВВ")
        self.element_is_visible(self.locator.REGION_IMPUT).send_keys("")
        self.element_is_visible(self.locator.BTN_CONT).click()
