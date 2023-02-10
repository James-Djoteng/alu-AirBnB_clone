#!/usr/bin/python3
""" Unittest for FileStorage class
"""
import unittest
from os import path
import sys
import json
import datetime
from io import StringIO
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test_File_Storage_Model(unittest.TestCase):
    """Tests for FileStorage class
    """
    def test_assignment(self):
        """Testing creatiion instance
        """
        b = FileStorage()
        with self.assertRaises(AttributeError):
            print(b.file_path)
            print(b.object)

    def test_id_has(self):
        """Testing for id
        """
        b = BaseModel()
        self.assertTrue(hasattr(b, 'id'))
        self.assertEqual(type(b.id), str)

    def test_all(self):
        """Testing for all method
        """
        b = FileStorage()
        ret = b.all()
        self.assertEqual(type(ret), dict)

    def test_all_empty(self):
        """Testing empty ret value
        """
        b = FileStorage()
        b.reset_obj()
        b.__objects = {}
        ret = b.all()
        self.assertFalse(b.all())

    def test_all_wrong(self):
        """Testing passing args to all
        """
        b = FileStorage()
        with self.assertRaises(TypeError):
            b.all("sfsdf")
            b.all(234)
            b.all({})
            b.all([])

    def test_all(self):
        """Testing for all method
        """
        b = FileStorage()
        b.reset_obj()
        self.assertFalse(b.all())
        b.new(BaseModel())
        self.assertTrue(b.all())

    def test_new(self):
        """ Using new method
        """
        b = FileStorage()
        b.new(BaseModel())
        self.assertTrue(b.all())
        with self.assertRaises(AttributeError):
            b.new("SDFsdf")
            b.new(123)
            b.new(23.33)
            b.new([1, 2, 3, 4])
            b.new({})
            b.new((1, 2), (3, 4))
            b.new(None)
            b.new(float('inf'))
            b.new(float('nan'))
        with self.assertRaises(NameError):
            b.new(sdfg)

    def test_save(self):
        """Testing save method
        """
        b = FileStorage()
        b.reset_obj()
        b.new(BaseModel())
        b.save()
        self.assertTrue(path.isfile("file.json"))