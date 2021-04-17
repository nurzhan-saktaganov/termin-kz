#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from jinja2 import Environment, FileSystemLoader
import termin

__author__ = 'Nurzhan Saktaganov'


def main():
    templates_path, render_path, filename = 'j2template', 'static_site', 'index.html'
    file_loader = FileSystemLoader(templates_path)
    env = Environment(loader=file_loader)
    template = env.get_template('{}.j2'.format(filename))

    if not os.path.exists(render_path):
        try:
            os.makedirs(render_path)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    output = template.render(termins=termin.termins, sources=termin.sources)
    with open('{}/{}'.format(render_path, filename), 'w') as f:
        f.write(output)

    return

if __name__ == '__main__':
    main()
