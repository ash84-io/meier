import os
import sys
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

import unittest
from meier_app.resources.blog.meta_tag.og_meta_tag import OpenGraphGenerator


class OpenGraphGenTestCase(unittest.TestCase):

    def setUp(self):
        empty_answer_list = []
        empty_answer_list.append('<meta property="og:title" content="" />')
        empty_answer_list.append('<meta property="og:site_name" content="" />')
        empty_answer_list.append('<meta property="og:description" content="" />')
        empty_answer_list.append('<meta property="og:url" content="" />')
        empty_answer_list.append('<meta property="og:image" content="" />')
        empty_answer_list.append('<meta property="og:type" content="website" />')
        self.empty_answer = '\n'.join(empty_answer_list)

        data_answer_list = []
        data_answer_list.append('<meta property="og:title" content="test" />')
        data_answer_list.append('<meta property="og:site_name" content="test" />')
        data_answer_list.append('<meta property="og:description" content="tech blog" />')
        data_answer_list.append('<meta property="og:url" content="http://ash84.net" />')
        data_answer_list.append('<meta property="og:image" content="http://ash84.net/images/favicon.ico" />')
        data_answer_list.append('<meta property="og:type" content="blog" />')
        self.data_answer = '\n'.join(data_answer_list)

    def test_for_empty(self):
        opg = OpenGraphGenerator()
        assert opg() == self.empty_answer

    def test_for_data(self):
        opg = OpenGraphGenerator(site_name='test',
                                 title='test',
                                 description='tech blog',
                                 url='http://ash84.net',
                                 image='http://ash84.net/images/favicon.ico',
                                 type='blog')
        assert opg() == self.data_answer

    def tearDown(self):
        pass