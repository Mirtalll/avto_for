from selenium.webdriver.common.by import By


class FormPageLocators:
    #Локаторы формы
    MAIN_IMPUT= (By.CLASS_NAME,"gos-input-main")
    REGION_IMPUT = (By.CLASS_NAME, "gos-input-region")
    # Нет номера
    NO_NOMBER = (By.CLASS_NAME,"gos-sign-link")
    # Кнопка
    BTN_CONT = (By.CLASS_NAME,"v-btn__content")
    BTN_CONT_BAKE =(By.CLASS_NAME,"mt-2")

