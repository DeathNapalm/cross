# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


credentials = {}
catalogs = []


def parse_credentials():

    with open('credentials.txt', 'r') as cr_file:
        for line in cr_file:
            if not line.startswith('#'):
                if line.strip():
                    k, v = line.strip().split('$$')
                    credentials[k.strip()] = v.strip()


# def parse_catalogs():
#     with open('catalogs.txt', 'r') as cat_file:
#         for line in cat_file:
#             catalogs.append(line.strip())


def parsnew():
    url = credentials['url']
    options = Options()

    #options.headless = True
    options.add_experimental_option("prefs", {
    "download.default_directory": credentials['download_folder'],
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(credentials['webdriver_location'],
                                chrome_options=options)
    #обрезаем адрес если нужно
    if not url.startswith('http'):
        driver.get("http://"+url.rstrip())
    else:
        driver.get(url.rstrip())

    #логинимся на сайте
    log_in_button  = driver.find_element_by_link_text(u'Войти')
    log_in_button.click()
    login_email_box = driver.find_element_by_name('LoginEmail')
    login_email_box.send_keys(credentials['email'])
    login_password_box = driver.find_element_by_name('LoginPassword')
    login_password_box.send_keys(credentials['password'])
    auth_button = driver.find_element_by_class_name('auth-form__btns')
    auth_button.click()
    #переходим во вкладку мои загрузки
    history_ref = driver.find_element_by_class_name("c-menu__i5")
    history_ref.click()
    list_of_downloads = driver.find_elements_by_class_name("jsRepeatBtn")
    #print(len(list_of_downloads ))
    quantity_of_catalogs = len(list_of_downloads )
    counter = 0
    for i in range(quantity_of_catalogs):
        list_of_downloads = driver.find_elements_by_class_name("jsRepeatBtn")
        list_of_downloads[counter].click()
        #здесь скачка файла с ожиданием парсинга
        history_repeat_btn = driver.find_element_by_class_name('primary-button')
        history_repeat_btn.click()
        #ждем пока закончится перепарсинг
        while True:
            try:
                form = driver.find_element_by_class_name('jsExportPrice')
                break
            except NoSuchElementException:
                continue
        download_btn = driver.find_element_by_class_name('jsExportPrice')
        download_btn.click()
        while True:
            try:
                form = driver.find_element_by_id('exportBtn')
                break
            except NoSuchElementException:
                continue
        final_download_btn = driver.find_element_by_id('exportBtn')
        final_download_btn.click()
        close_dwnld_btn = driver.find_element_by_id('cancelFileExportBtn')
        close_dwnld_btn.click()

        #<button class="button" id="cancelFileExportBtn" style="float:right;">Закрыть</button>


        #возвращаемся на вкладку с каталогами
        #sleep(1)
        counter+=2
        history_ref = driver.find_element_by_class_name("c-menu__i5")
        history_ref.click()

    #удаление самых старых каталогов
    for i in range(quantity_of_catalogs):
        list_of_deletions = driver.find_elements_by_class_name("jsDelBtn")
        list_of_deletions[-1].click()
        sleep(6)




    # for i in range(len(list_of_downloads)):
    #     list_of_downloads[i].click()
    #     history_repeat_btn = driver.find_element_by_class_name('primary-button')
    #     history_repeat_btn.click()
    #     history_ref = driver.find_element_by_class_name("c-menu__i5")
    #     history_ref.click()
    #     list_of_downloads = driver.find_elements_by_class_name("jsRepeatBtn")

    #sleep(3)
    # for ii in list_of_downloads:
    #     ii.click
    #     print(ii.tag_name)
    #     print(ii.get_attribute('id'))    # id name as string
    #print(list_of_downloads)
    #driver.save_screenshot('screen.png')

    # пробегаем по всем загруженным каталогам

    # search_bar_box = driver.find_element_by_id('searchText')
    # for catalog in catalogs:
    #     search_bar_box.send_keys(catalog)
            # sleep(2)

    # sleep(60)


if __name__ == '__main__':
    parse_credentials()
    # parse_catalogs()
    parsnew()
