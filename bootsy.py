__author__ = 'adityabhasin'

import ConfigParser
import re

pattern = re.compile("\\$\\{(\w+\\.*)\\}")
config = ConfigParser.SafeConfigParser()
config.read("config.ini")

output_confg = open("sample.conf", 'w')
template_config = open("templates/django_template.conf", 'r')

for line in template_config:
    out = line
    if '$' in out:
        matched = pattern.search(line)
        if matched and matched.groups()[0]:
            value = config.get("app", matched.groups()[0])
            out = pattern.sub(value, out)
        out = out.replace("${", "")
        out = out.replace("}", "")
        output_confg.write(out)
    else:
        output_confg.write(line)

output_confg.close()
template_config.close()