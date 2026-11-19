import time
from selenium.webdriver.common.by import By

def test_user_can_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Пауза 30 секунд, чтобы вы могли визуально проверить язык кнопки (требование задания)
    time.sleep(30)
    
    # Ищем кнопку добавления в корзину (уникальный селектор для этой страницы)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    
    # Проверяем, что кнопка отображается на странице
    assert button.is_displayed(), "Кнопка добавления в корзину не найдена на странице"