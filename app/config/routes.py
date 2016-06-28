
from system.core.router import routes


routes['default_controller'] = 'Courses'
routes['POST']['/add'] = 'Courses#add'
routes['/destroy/<id>'] = 'Courses#destroy'
routes['/delete/<id>'] = 'Courses#delete'


