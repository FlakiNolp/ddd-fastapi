import pytest

from app.domain.models.card import Card
from app.domain.models.notification import Notification
from app.domain.models.user import User
from app.domain.values.card_number import CardNumber
from app.domain.values.cvv import CVV
from app.domain.values.email import Email
from app.domain.values.first_name import FirstName
from app.domain.values.last_name import LastName
from app.domain.values.password import Password
from app.domain.models.project import Project
from app.domain.values.project_name import ProjectName

from app.domain.exceptions.email import EmailValidationException
from app.domain.exceptions.password import PasswordValidationException
from app.domain.exceptions.card_number import CardNumberValidationException
from app.domain.exceptions.cvv import CVVValidationException
from app.domain.exceptions.first_name import FirstNameValidationException
from app.domain.exceptions.last_name import LastNameValidationException
from app.domain.exceptions.project_name import ProjectNameTooLongException


def test_create_wrong_email():
    with pytest.raises(EmailValidationException):
        Email('m@gmail.ru')


def test_create_wrong_password():
    with pytest.raises(PasswordValidationException):
        Password('FFFFFFFF')
    with pytest.raises(PasswordValidationException):
        Password('aaaaaaaaa')
    with pytest.raises(PasswordValidationException):
        Password('aaaaaFaaa')
    with pytest.raises(PasswordValidationException):
        Password('aaaaaFaa9')
    with pytest.raises(PasswordValidationException):
        Password('Af9.')


def test_create_wrong_card_number():
    with pytest.raises(CardNumberValidationException):
        CardNumber('1234567890123456')


def test_create_wrong_cvv():
    with pytest.raises(CVVValidationException):
        CVV(99)


def test_create_wrong_first_name():
    with pytest.raises(FirstNameValidationException):
        FirstName('MaXIM')
    with pytest.raises(FirstNameValidationException):
        FirstName('MАXIM')
    with pytest.raises(FirstNameValidationException):
        FirstName('MАXIM6')


def test_create_wrong_last_name():
    with pytest.raises(LastNameValidationException):
        LastName('MaXIM')
    with pytest.raises(LastNameValidationException):
        LastName('MАXIM')
    with pytest.raises(LastNameValidationException):
        LastName('MAXIM6')


def test_create_wrong_project_name():
    with pytest.raises(ProjectNameTooLongException):
        ProjectName('ab')
    with pytest.raises(ProjectNameTooLongException):
        ProjectName('a' * 151)


