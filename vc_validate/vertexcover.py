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
import os

import networkx as nx
import htd_validate


class VertexCover:
    _problem_string = 'vc'

    def __init__(self):
        self._num_vertices = 0
        self._vc = set()

    @staticmethod
    def _read_header(line):
        return {}

    @staticmethod
    def _reader(vc, line):
        return False

    @classmethod
    def from_file(cls, filename, strict=False):
        """
        :param filename: name of the file to read from
        :type filename: string
        :rtype: VertexCover
        :return: a list of edges and number of vertices
        """
        header_seen = False
        nr = 0

        def log_critical(string):
            logging.critical('%s:L(%s). %s  Exiting...' % (os.path.basename(filename), nr, string))

        vc = VertexCover()
        with open(filename, 'r') as fobj:
            num_vertices = 0
            header = {}
            try:
                vertex_seen = False
                for line in fobj.readlines():
                    line = line.split()
                    nr = nr + 1
                    # noinspection PySimplifyBooleanCheck
                    if line == []:
                        continue
                    if line[0] == 'c':
                        logging.info('-' * 20 + 'INFO from vertexcover reader' + '-' * 20)
                        logging.info('%s' % ' '.join(line))
                        logging.info('-' * 80)
                        continue
                    elif line[0] == 's' and line[1] == cls._problem_string:
                        if header_seen:
                            log_critical('Duplicate header.')
                            exit(2)
                        try:
                            header['num_vertices'] = int(line[2])
                            header['num_vertices_vc'] = int(line[3])
                            header.update(cls._read_header(line))
                            vc._num_vertices = header['num_vertices']
                        except ValueError as e:
                            logging.error(e)
                            log_critical('Too many or too few arguments in header.')
                            exit(2)
                        header_seen = True
                    else:
                        if cls._reader(vc, line):
                            continue
                        else:
                            if strict and not header_seen:
                                log_critical('Vertex before header.')
                                exit(2)
                            u = int(line[0])
                            if u > header['num_vertices'] or u < 1:
                                log_critical("Vertex label %s out of bounds (expected max %s vertices)." % (
                                u, header['num_vertices']))
                                exit(2)
                            vc._vc.add(u)
                            vertex_seen = True
            except ValueError as e:
                logging.critical("Undefined input.")
                logging.critical(e)
                logging.warning("Output was:")
                fobj.seek(0)
                for line in fobj.readlines():
                    logging.warning(line)
                for line in traceback.format_exc().split('\n'):
                    logging.critical(line)
                logging.critical('Exiting...')
                exit(143)
            if not header_seen:
                logging.critical('Missing header. Exiting...')
                exit(2)
            if (len(vc._vc) < header['num_vertices_vc'] or len(vc._vc) > header['num_vertices_vc']) and strict:
                logging.warning(
                    'Number of vertices differ. Was %s expected %s.\n' % (len(vc._vc), header['num_vertices_vc']))
                exit(2)
        return vc
        # return clazz._from_file(filename, strict=strict)

    def validate(self, graph):
        for e in graph.edges_iter():
            if not e[0] in self._vc and not e[1] in self._vc:
                logging.critical('Instance not a valid vertex cover since edge %s is not covered\n.' % str(e))
                return False
        return True
