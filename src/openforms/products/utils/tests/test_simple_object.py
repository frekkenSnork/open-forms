from django.test import TestCase

from ..entry import convert_json_schema_to_py


class NumberFieldTestCase(TestCase):
    def setUp(self):
        self.json_schema_object = {
            "title": "person",
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "user_name": {
                            "type": "string",
                            "maxLength": 120,
                            "minLenth": 2,
                        },
                        "user_email": {"type": "string", "format": "email"},
                    },
                    "required": ["user_name", "user_email"],
                }
            },
        }

    def test_object(self):
        result = convert_json_schema_to_py(self.json_schema_object)["components"]
        self.assertEqual(result[0]["type"], "fieldset")
        self.assertEqual(len(result[0]["components"]), 2)
        self.assertEqual(result[0]["components"][0]["key"], "user_name")
        self.assertEqual(result[0]["components"][0]["type"], "textfield")
        self.assertEqual(result[0]["components"][1]["key"], "user_email")
        self.assertEqual(result[0]["components"][1]["type"], "email")
