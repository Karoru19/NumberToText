import unittest
from django.test import TestCase
from number_to_text.converter.utils import (
    extract_digits,
    pluralize,
    split_number_by_three_digits,
    number_to_words,
    THOUSANDS,
)
from number_to_text.converter.forms import ConverterForm

# Create your tests here.


class UtilsTests(unittest.TestCase):
    def test_extract_digits(self):
        self.assertEqual(extract_digits(315), [5, 1, 3])
        self.assertRaises(Exception, extract_digits)
        with self.assertRaises(Exception):
            extract_digits(1332)
        with self.assertRaises(Exception):
            extract_digits(-1)

    def test_pluralize(self):
        self.assertEqual(pluralize(1, THOUSANDS[1]), "tysiąc")
        self.assertEqual(pluralize(64, THOUSANDS[1]), "tysiące")
        self.assertEqual(pluralize(25, THOUSANDS[1]), "tysięcy")
        self.assertNotEqual(pluralize(111, THOUSANDS[2]), "tysiące")
        with self.assertRaises(KeyError):
            pluralize(111, THOUSANDS[3])
        with self.assertRaises(Exception):
            pluralize("111", THOUSANDS[1])
            pluralize(None, THOUSANDS[1])
            pluralize(111, None)

    def test_split_number_by_three_digits(self):
        self.assertEqual(split_number_by_three_digits(123456), [123, 456])
        self.assertNotEqual(split_number_by_three_digits(123456), [456, 123])
        with self.assertRaises(Exception):
            split_number_by_three_digits("123456")
            split_number_by_three_digits(-1)

    def test_number_to_words(self):
        self.assertEqual(number_to_words(123), "sto dwadzieścia trzy")
        self.assertNotEqual(number_to_words(45), "piędzięsiąt cztery")
        with self.assertRaises(Exception):
            number_to_words("123456")


class ConverterFormTests(TestCase):
    def setUp(self):
        self.valid_number = 1996
        self.invalid_number = 1000001
        self.negative_number = -1

    def test_valid_data(self):
        form = ConverterForm(data={"number": self.valid_number})
        self.assertTrue(form.is_valid())

        in_words = form.convert()
        self.assertEqual(in_words, "tysiąc dziewięćset dziewięćdziesiąt sześć")

    def test_invalid_data(self):
        form1 = ConverterForm(data={"number": self.invalid_number})
        form2 = ConverterForm(data={"number": self.negative_number})
        self.assertFalse(form1.is_valid())
        self.assertFalse(form2.is_valid())

        with self.assertRaises(Exception):
            form1.convert()
            form2.convert()

    def test_blank_data(self):
        form = ConverterForm()
        self.assertFalse(form.is_valid())


class ConverterViewTests(TestCase):
    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_valid_data(self):
        response = self.client.post("/", {"number": 2019})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["text"], "dwa tysiące dziewiętnaście")

    def test_invalid_data(self):
        response = self.client.post("/", {"number": 1000001})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context.get("text", None), None)
