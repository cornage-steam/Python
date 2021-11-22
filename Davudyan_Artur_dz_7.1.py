import os

root = os.path.dirname('Davudyan_Artur_dz_7')
project_name = 'my_project'
paths = [os.path.join(project_name, 'settings'), os.path.join(project_name, 'mainapp'),
         os.path.join(project_name, 'adminapp'), os.path.join(project_name, 'authapp')]
for _path in paths:
    os.makedirs(os.path.join(root, _path), exist_ok=True)
