#!/usr/bin/python3

"""
Load, add, save module
"""


import sys
import json

save_json = __import__('5-save_to_json_file').save_to_json_file
from_json = __import__('6-load_from_json_file').load_from_json_file

if len(sys.argv) == 1:
    args = []
    save_json(args, "add_item.json")

args = from_json("add_item.json")

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        args.append(arg)

save_json(args, "add_item.json")

# if len(sys.argv) > 1:
#     args = [sys.argv[1]]
#     exist_list = from_json("add_item.json")
#     i = 2
#     while i < len(sys.argv):
#         args.append(sys.argv[i])
#         i += 1
# else:
#     args = []

# save_json(args, "add_item.json")
