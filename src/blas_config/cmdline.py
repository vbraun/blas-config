# -*- coding: utf-8 -*-
"""
Command Line Option Parsing
"""

import sys

import logging
log = logging.getLogger()


import argparse


description = \
"""
Automatic Blas Configuration
"""


def make_parser():
    parser = argparse.ArgumentParser(description=description, add_help=False)
    parser.add_argument('-h', dest='option_help', action='store_true',
                        default=False, 
                        help='show this help message and exit')
    parser.add_argument('--log', dest='log', default=None,
                        help='one of [DEBUG, INFO, ERROR, WARNING, CRITICAL]')

    subparsers = parser.add_subparsers(dest='subcommand')

    parser_cblas = subparsers.add_parser('cblas', help='CBLAS configuration')
    parser_f77blas = subparsers.add_parser('f77blas', help='F77BLAS configuration')

    return parser


def launch(app):
    parser = make_parser()
    args = parser.parse_args(sys.argv[1:])
    if args.log is not None:
        level = getattr(logging, args.log.upper())
        log.setLevel(level=level)

    if args.option_help:
        parser.print_help()
    elif args.subcommand == 'cblas':
        app.write_pc(app.cblas())
    elif args.subcommand == 'f77blas':
        app.write_pc(app.f77blas())
