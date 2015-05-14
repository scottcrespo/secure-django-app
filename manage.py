#!./env/bin/python
"""
manage.py

Intelligent manage.py file that knows what host it is running on. Notice above,
that there's a shebang ling, which is a relative path to a virtualenvironment
Python Executable
"""

import os, sys, socket

#===================================================================================#

if __name__ == "__main__":
    
    # Add to PYTHONPATH the absolute location of your secure settings repository. 
    # Which, we always keep in the same parent directory as the main application.
    # Thus, we have to jump up one directory from the cwd using " ../ ".
    sys.path.append(
        os.path.abspath(os.path.join(os.path.dirname(__file__),'../secure_django_settings'))
    )
    
    # get the name of the current host using the socket library
    hostname = socket.gethostname()
    
    # Here we check for key words in the hsotname to tell us which settings file
    # to use for the application instance. If we don't recognize the hostname, then
    # fall back to the local settings file.
    if "development" in hostname:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.develop'

    elif "production" in hostname:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.production'

    else:
        os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_base.base'

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)