from django.core.exceptions import ValidationError as DjangoValidationError
from django.test import TestCase

from rest_framework.exceptions import ValidationError as DRFValidationError

from openforms.validations.registry import Registry


class DjangoValidator:
    def __call__(self, value):
        if value != "VALID":
            raise DjangoValidationError("not VALID value")


class DRFValidator:
    def __call__(self, value):
        if value != "VALID":
            raise DRFValidationError("not VALID value")


def function_validator(value):
    if value != "VALID":
        raise DjangoValidationError("not VALID value")


class RegistryTest(TestCase):
    def test_register_function(self):
        register = Registry()
        register("plugin", "Plugin")(DjangoValidator)
        plugin = register["plugin"]
        self.assertNotIsInstance(plugin, DjangoValidator)
        self.assertIsInstance(plugin.callable, DjangoValidator)

    def test_duplicate_identifier(self):
        register = Registry()
        register("plugin", "Plugin")(DjangoValidator)

        with self.assertRaisesMessage(
            ValueError,
            "The unique identifier 'plugin' is already present in the registry",
        ):
            register("plugin", "Plugin")(DjangoValidator)

    def test_decorator(self):
        registry = Registry()

        @registry("func", verbose_name="Function")
        def decorated(value):
            pass

        wrapped = list(registry)[0]
        self.assertEqual(wrapped.identifier, "func")
        self.assertEqual(wrapped.verbose_name, "Function")
        self.assertEqual(wrapped.callable, decorated)

    def test_validate(self):
        registry = Registry()
        registry("django", "Django")(DjangoValidator)
        registry("drf", "DRF")(DRFValidator)
        registry("func", "Function")(function_validator)

        res = registry.validate("django", "VALID")
        self.assertEqual(res.is_valid, True)
        self.assertEqual(res.messages, [])
        res = registry.validate("django", "INVALID")
        self.assertEqual(res.is_valid, False)
        self.assertEqual(res.messages, ["not VALID value"])

        res = registry.validate("drf", "VALID")
        self.assertEqual(res.is_valid, True)
        self.assertEqual(res.messages, [])
        res = registry.validate("drf", "INVALID")
        self.assertEqual(res.is_valid, False)
        self.assertEqual(res.messages, ["not VALID value"])

        res = registry.validate("func", "VALID")
        self.assertEqual(res.is_valid, True)
        self.assertEqual(res.messages, [])
        res = registry.validate("func", "INVALID")
        self.assertEqual(res.is_valid, False)
        self.assertEqual(res.messages, ["not VALID value"])

        res = registry.validate("NOT_REGISTERED", "VALID")
        self.assertEqual(res.is_valid, False)
        self.assertEqual(
            res.messages, ["unknown validation plugin_id 'NOT_REGISTERED'"]
        )
