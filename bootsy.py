__author__ = 'adityabhasin'

import ConfigParser
import re

# pattern to match placeholders
pattern = re.compile(r"\$\{(\w+\.*\w*\.*\w*)\}")
config = ConfigParser.SafeConfigParser()
config.read("config.ini")


def build_out(app, output_confg, template_config):
    for line in template_config:
        out = line
        if '$' in out:
            matched = pattern.findall(line)
            if matched:
                for match in matched:
                    value = config.get(app, match)
                    out = out.replace(match, value)
            out = out.replace("${", "")
            out = out.replace("}", "")
        output_confg.write(out)
    template_config.close()
    output_confg.close()


def bootsy(app):
    files = [(open(app + ".conf", 'w'),
              open("templates/django_template.conf", 'r')), (
             open(app + "_wsgi.py", 'w'),
             open("templates/wsgi.template", 'r'))]
    for v in files:
        build_out(app, v[0], v[1])


if __name__ == "__main__":
    import sys

    bootsy(sys.argv[1])