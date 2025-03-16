from HW_way_2.data.users import User
from HW_way_2.pages.registration_page import RegistrationPage



def test_form(browser_manager):

    registration_page = RegistrationPage()
    ksusha = User(first_name='Kseniya', last_name='Goryaeva', email='Goryaeva@mail.ru', mobile='8910123456', currentAddress='Нижний Новгород')
    registration_page.open()

    registration_page.fill_first_name(ksusha.first_name)
    registration_page.fill_last_name(ksusha.last_name)
    registration_page.email(ksusha.email)
    registration_page.gender()
    registration_page.mobile(ksusha.mobile)
    registration_page.dateOfBirth('November', '11', '1995')
    registration_page.subject('hist')
    registration_page.hobbies()
    registration_page.picture()
    registration_page.currentAddress(ksusha.currentAddress)
    registration_page.scroll()
    registration_page.state()
    registration_page.city()
    registration_page.submit()
    registration_page.finish_form()
