#!/usr/bin/env false
# -*- coding: utf-8 -*-
#
# Copyright 2018
# Johannes K. Fichte, TU Wien, Austria
# Markus Hecher, TU Wien, Austria
#
# vc_validate is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.  hypergraph.py is distributed in
# the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.  You should have received a copy of the GNU General Public
# License along with hypergraph.py.  If not, see
# <http://www.gnu.org/licenses/>.
#
from __future__ import print_function

import logging

import networkx as nx

class VertexCover:
    def __init__(self):
        pass

    @classmethod
    def from_file(clazz, filename, strict=False):
        """
        :param filename: name of the file to read from
        :type filename: string
        :rtype: Graph
        :return: a list of edges and number of vertices
        """
        pass
        #return clazz._from_file(filename, strict=strict)

    def validate(self, graph):
        pass

