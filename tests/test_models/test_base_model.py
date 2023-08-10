#!/usr/bin/python3
""" Unitest for Base Model """

import re
import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel

models = BaseModel()


class test_baseModel(unittest.TestCase):
    """
        test cases
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_id(self):
        """ Test base model id """
        new_models_id = BaseModel().id
        self.assertIsNotNone(models.id)
        self.assertIsInstance(models.id, str)
        self.assertTrue((uuid.UUID(models.id)))
        self.assertNotEqual(models.id, new_models_id)

    def test_created_at(self):
        """ Test time created """
        self.assertEqual(models.created_at.isoformat()[:16], datetime.today().isoformat()[:16])

    def test_updated_at(self):
        """ Test time created """
        self.assertEqual(models.updated_at.isoformat()[:16], datetime.today().isoformat()[:16])
    
    def test_save(self):
        """ Test method save() """
        new_model = BaseModel()
        old_created_time = new_model.created_at
        old_updated_time = new_model.updated_at
        new_model.save()
        new_created_time = new_model.created_at
        new_updated_time = new_model.updated_at

        self.assertNotEqual(old_updated_time, new_updated_time)
        self.assertEqual(old_created_time, new_created_time)

    def test_to_dict(self):
        """ Test to dictionary """
        iso_pattern = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$'
        obj_dict = models.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIsNotNone(obj_dict["__class__"])
        if re.match(iso_pattern, obj_dict["created_at"]):
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_str(self):
        iso_pattern = r'\[([\w]+)\] \(([\w-]+)\) \{(.*)\}'

        if re.match(iso_pattern, models.__str__()):
            self.assertTrue(True)
        else:
            self.assertFalse(True)

if __name__ == "__main__":
    unittest.main()
