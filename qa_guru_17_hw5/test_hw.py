import os

from selene import browser, command


def test_form(browser_manager):

    browser.element('#firstName').type('Kseniya')
    browser.element('#lastName').type('Goryaeva')
    browser.element('#userEmail').type('Goryaeva@mail.ru')
    browser.element('#gender-radio-2').perform(command.js.click)
    browser.element('#userNumber').type('89101234567')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__navigation--previous').double_click()
    browser.element('.react-datepicker__navigation--previous').double_click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1995"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--011').click()
    browser.element('#subjectsInput').type('hist')
    browser.element('#react-select-2-option-0').click()
    browser.element('#hobbies-checkbox-1').perform(command.js.click)
    browser.element('#uploadPicture').send_keys(os.path.abspath('C:\QA\pic.png'))
    browser.element('#currentAddress').type('Нижний Новгород')
    browser.execute_script("window.scrollBy(0,6000)")
    browser.element('#state .css-tlfecz-indicatorContainer').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city .css-tlfecz-indicatorContainer').click()
    browser.element('#react-select-4-option-2').click()
    browser.element('#submit').click()
