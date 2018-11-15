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
import htd_validate


class VertexCover:

    def __init__(self):
        pass

    @classmethod
    def from_file(clazz, filename, strict=False):
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
                edge_seen = False
                for line in fobj.readlines():
                    line = line.split()
                    nr = nr + 1
                    # noinspection PySimplifyBooleanCheck
                    if line == []:
                        continue
                    if line[0] == 'c':
                        logging.info('-' * 20 + 'INFO from decomposition reader' + '-' * 20)
                        logging.info('%s' % ' '.join(line))
                        logging.info('-' * 80)
                        continue
                    elif line[0] == 's' and line[1] == cls._problem_string:
                        if header_seen:
                            log_critical('Duplicate header.')
                            exit(2)
                        try:
                            header['num_bags'] = int(line[2])
                            header['num_vertices'] = int(line[4])
                            header.update(cls._read_header(line))
                        except ValueError as e:
                            logging.error(e)
                            log_critical('Too many or too few arguments in header.')
                            exit(2)
                        header_seen = True
                    else:
                        if cls._reader(decomp, line):
                            continue
                        else:
                            if strict and not header_seen:
                                log_critical('Edge before header.')
                                exit(2)
                            u, v = map(int, line)
                            if u > header['num_bags']:
                                log_critical("Edge label %s out of bounds (expected max %s bags)." % (u, num_bags))
                                exit(2)
                            if v > header['num_bags']:
                                log_critical("Edge label %s out of bounds (expected max %s bags)." % (v, num_bags))
                                exit(2)
                            if u not in decomp.bags.keys():
                                log_critical(
                                    "Edge in the tree (%s,%s) without a corresponding bag for node %s." % (u, v, u))
                                exit(2)
                            if v not in decomp.bags.keys():
                                log_critical(
                                    "Edge in the tree (%s,%s) without a corresponding bag for node %s." % (u, v, v))
                                exit(2)
                            decomp.tree.add_edge(u, v)
                            edge_seen = True
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
            # decomps of single bags require special treatment
            if not header_seen:
                logging.critical('Missing header. Exiting...')
                exit(2)
            if len(decomp) == 1:
                # noinspection PyUnresolvedReferences
                decomp.tree.add_node(decomp.bags.iterkeys().next())
            if decomp.specific_valiation(decomp, header):
                logging.critical('Decomposition specific validation failed.')
                exit(2)
            if len(decomp) != header['num_bags']:
                logging.critical('Number of bags differ. Was %s expected %s.\n' % (len(decomp), header['num_bags']))
                exit(2)
            if decomp.num_vertices > header['num_vertices']:
                logging.critical(
                    'Number of vertices differ (>). Was %s expected %s.\n' % (
                        decomp.num_vertices, header['num_vertices']))
                exit(2)
            if decomp.num_vertices < header['num_vertices'] and strict:
                logging.warning(
                    'Number of vertices differ (<). Was %s expected %s.\n' % (decomp.num_vertices, num_vertices))
                exit(2)
        return decomp
        #return clazz._from_file(filename, strict=strict)

    def validate(self, graph):
        pass

