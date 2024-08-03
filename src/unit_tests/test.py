import unittest
import yaml
import os

class TestParamYAML(unittest.TestCase):
    def setUp(self):
        with open('params.yaml', 'r') as file:
            self.config = yaml.safe_load(file)

    def test_train_args_presence(self):

        required_args = ['n_estimators', 'learning_rate', 'max_depth', 'random_state']
        for arg in required_args:
            self.assertIn(arg, self.config['train'], f"Required argument '{arg}' is missing.")

    def test_train_arg_types(self):
        arg_types = {'n_estimators': int, 'learning_rate': float, 'max_depth': int, 'random_state': int} 
        for arg, arg_type in arg_types.items():
            self.assertIn(arg, self.config['train'], f"Required argument '{arg}' is missing.")
            self.assertIsInstance(self.config['train'][arg], arg_type,
                                  f"Type of argument '{arg}' is not {arg_type.__name__}.")
