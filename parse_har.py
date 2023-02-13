import os


from jinja2 import Environment, FileSystemLoader

working_dir = os.getcwd()

template_dir = os.path.join(os.getcwd(), 'templates')
output_dir = os.path.join(os.getcwd(), 'locustfiles')

input_name = 'ha1.json'
output_name = os.path.splitext(input_name)[0] + '.py'

print(output_name)

env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template('fast_http_user.html')

output_from_parsed_template = template.render(foo='Hello World!')

# to save the results
with open(os.path.join(output_dir, output_name), "w") as fh:
    fh.write(output_from_parsed_template)
