from jinja2 import Template
template = Template("Hello {{ something }}!")
print(template.render(something="World"))