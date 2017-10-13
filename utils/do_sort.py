# This file is a part of [[$]] project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@brainfuck.pl>.
import json
import re
import sys

from toposort import toposort

if __name__ == '__main__':
    bean_dir = sys.argv[1]
    bean_files = sys.argv[2:]
    beans = [re.sub('.json', '', file) for file in bean_files]
    graph = {}
    for bean_filename in bean_files:
        bean = re.sub('.json', '', bean_filename)
        with open(bean_dir + '/' + bean_filename) as bean_file:
            bean_json = json.load(bean_file)
            #print(bean_json)
            edges = [(re.sub('\)', '', v)).split('(') for k,v in bean_json.items()]
            #print(sum(edges, []))
            graph[bean] = set(sum(edges, []))
    sorted_graph = list(toposort(graph))
    ordered = [item for sublist in sorted_graph for item in sublist]
    output = [bean for bean in ordered if bean in beans]
    for node in output:
        print(node + '.json')