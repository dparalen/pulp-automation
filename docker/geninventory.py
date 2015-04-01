#!/usr/bin/env python

import os

import yaml


pulphost = os.environ['PULPHOST']

with open('inventory-example.yml') as f:
    data = yaml.load(f.read())

data['ROLES']['qpid']['url'] = pulphost
data['ROLES']['pulp']['url'] = 'https://%s/' % pulphost
data['ROLES']['pulp']['hostname'] = pulphost

with open('inventory.yml', 'w') as f:
    f.write(yaml.dump(data))
