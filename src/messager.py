#!/usr/bin/env python

import argparse
import yaml

from utils import str2bool, str2list, str2map

import requests

class Messager(object):
    def __init__(self):
        self.parser = self._create_parser()
        self.args = self.parser.parse_args()

    def _create_parser(self):
        with open("/action.yaml", 'r') as f:
            action = yaml.safe_load(f)
        parser = argparse.ArgumentParser(description = action['description'])
        inputs = action['inputs']

        for key in inputs:
            input_args = inputs[key]
            default_value = input_args.get('default','')
            parser.add_argument(
                "--" + key.replace('_', '-'),
                type = str2bool if isinstance(default_value, bool) else str,
                required = input_args.get('required', False),
                default = default_value,
                help = input_args.get('description', '')
            )

        return parser

    def run(self):
        if not self.args.enable:
            print("Please set --enable to make messager work")
            return
        self.send()

    def send(self):
        url = "https://sctapi.ftqq.com/" + self.args.token + ".send"
        if self.args.content == '':
            url += "?text=" + self.args.title
            requests.get(url)
            return
        payload = {"title": self.args.title, "desp": self.args.content}
        requests.post(url, data=payload)

def main():
    m = Messager()
    m.run()

if __name__ == "__main__":
    main()
