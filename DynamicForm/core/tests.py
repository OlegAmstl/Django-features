from django.test import TestCase

from .forms import ContactForm
from .models import Contact


class ContactModelTests(TestCase):
    """
    Тестирование модели Contact.
    """

    def test_contact_model(self):
        """
        Проверяет, что модель Contact
        может быть создана с корректными данными.
        """
        contact = Contact(name="John Doe", phone_number="555-555-5555")
        self.assertEqual(str(contact), "John Doe")


class ContactFormTests(TestCase):
    """
    Тестирование формы ContactForm.
    """

    def test_model_fields(self):
        """
        Проверяет, что форма ContactForm
        может быть создана с корректными данными.
        """
        form = ContactForm(
            data={'name': 'John', 'phone_number': '555-555-5555'})
        self.assertTrue(form.is_valid())

    def test_name_max_length(self):
        """
        Проверяет, максимальную длину значения вводимого в поле имени.
        """
        form = ContactForm(
            data={'name': 'a' * 101, 'phone_number': '555-555-5555'})
        self.assertFalse(form.is_valid())

    def test_phone_number_max_length(self):
        """
        Проверяет, максимальную длину значения вводимого в поле телефона.
        """
        form = ContactForm(
            data={'name': 'John', 'phone_number': '555-555-55555'})
        self.assertFalse(form.is_valid())
