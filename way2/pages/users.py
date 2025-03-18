from dataclasses import dataclass



@dataclass
class User:
    firstName: str
    lastName: str
    email: str
    gender: str
    mobile: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: str
    hobby: str
    picture: str
    address: str
    state: str
    city: str
    text_birth_month: str


test_user = User(firstName='Kseniya', lastName='Goryaeva', email='Goryaeva@mail.ru', gender='Male', mobile='8912345688',
                 text_birth_month='September',
                 birth_day='15', birth_month='8', birth_year='1995', subjects='Maths', hobby='Sports',
                 picture='pic.png', address='Нижний Новгород', state='NCR', city='Delhi')
