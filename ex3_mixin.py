"""
This module demonstrates the use of mixin classes to add functionality to classes.
Author: Wolf Paulus (https://wolfpaulus.com)
"""
import json


class ToDictMixin:
    """ A mixin class that provides a method to return a dictionary representation of an object's attributes. """

    def to_dict(self):
        """ Returns a dictionary representation of the object's attributes. """
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        """ Recursively traverses the instance dictionary to convert ToDictMixin objects into dictionaries. """
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        """ Traverses the value, which may be a ToDictMixin object or a list of ToDictMixin objects """
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        if isinstance(value, dict):
            return self._traverse_dict(value)
        if isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        if hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class JsonMixin:
    """ A mixin class that provides a method to return a JSON representation of an object's attributes. """
    @classmethod
    def from_json(cls, data):
        """ Returns a new instance of the class from a JSON representation. """
        kwargs = json.loads(data)
        return cls(**kwargs)

    def to_json(self):
        """ Returns a JSON representation of the object's attributes. """
        return json.dumps(self.to_dict())


class BinaryTree(ToDictMixin, JsonMixin):
    """ A simple binary tree class that can be converted to a dictionary or a JSON representation. """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


tree = BinaryTree(10, left=BinaryTree(7, right=BinaryTree(9)), right=BinaryTree(13, left=BinaryTree(11)))

json_data = tree.to_json()
new_tree = BinaryTree.from_json(json_data)
assert tree == new_tree
