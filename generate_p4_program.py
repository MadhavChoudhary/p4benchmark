#!/usr/bin/env python

import argparse

from parsing.bm_parser import benchmark_parser
from processing.bm_pipeline import benchmark_pipeline
from state_access.bm_memory import benchmark_memory
from packet_modification.bm_modification import benchmark_modification

def main():
    parser = argparse.ArgumentParser(description='A programs that generate a'
                            ' P4 program for benchmarking a particular feature')
    parser.add_argument('-p', '--parser', default=False, action='store_true',
                            help='parser benchmark')
    parser.add_argument('--pipeline', default=False, action='store_true',
                            help='pipeline benchmark')
    parser.add_argument('--memory', default=False, action='store_true',
                            help='memory access benchmark')
    parser.add_argument('--mod-packet', default=False, action='store_true',
                            help='packet modification benchmark')
    parser.add_argument('--tables', default=1, type=int, help='number of tables')
    parser.add_argument('--table-size', default=1, type=int,
                            help='number of rules in the table')
    parser.add_argument('--headers', default=1, type=int, help='number of headers')
    parser.add_argument('--fields', default=1, type=int, help='number of fields')
    parser.add_argument('--registers', default=1, type=int, help='number of registers')
    parser.add_argument('--nb-element', default=1024, type=int,
                            help='number of element in a register')
    parser.add_argument('--element-width', default=32, type=int,
                            help='the bit width of a register element')
    parser.add_argument('--nb-operations', default=1, type=int,
                            help='the number of state access operations')
    parser.add_argument('--write-op', default=False,
                            help='operation is Write op')
    parser.add_argument('--mod-type', default='add', type=str,
                            help='modification type [add, rm, mod]')

    args = parser.parse_args()

    if args.parser:
        benchmark_parser(args.headers, args.fields)
    elif args.pipeline:
        benchmark_pipeline(args.tables, args.table_size)
    elif args.mod_packet:
        benchmark_modification(args.headers, args.fields, args.mod_type)
    elif args.memory:
        benchmark_memory(args.registers, args.element_width, args.nb_element, args.nb_operations, args.operation_op)
    else:
        parser.print_help()

if __name__=='__main__':
    main()