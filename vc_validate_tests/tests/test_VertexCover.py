#!/usr/bin/env false
from __future__ import absolute_import

import logging
import unittest
import os
import inspect
import sys

src_path = os.path.abspath(os.path.realpath(inspect.getfile(inspect.currentframe())))
lib_path = os.path.realpath(os.path.join(src_path, '../../../lib/htd_validate'))
#print src_path
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)

import vc_validate
import htd_validate


class TestVertexCover(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)

    def tearDown(self):
        pass

    def testSimple(self):
        VC = vc_validate.vertexcover.VertexCover.from_file(os.path.realpath(os.path.join(src_path, "../v")), strict=True)
        HG = htd_validate.utils.Graph.from_file(os.path.realpath(os.path.join(src_path, "../g")))
        self.assertTrue(VC.validate(HG))
