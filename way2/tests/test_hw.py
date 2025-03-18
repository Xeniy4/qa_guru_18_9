

from way2.pages.page import RegistrationPage
from way2.pages.users import test_user


def test_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.register(test_user)

    registration_page.assert_form_registration(test_user)
