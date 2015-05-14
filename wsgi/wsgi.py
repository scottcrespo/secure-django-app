"""
WSGI file that applies proper settings for the environment it's running on.
"""

from django.core.wsgi import get_wsgi_application

import sys, os, socket

#===================================================================================#

# Add to PYTHONPATH the absolute location of your secure settings repository. 
# Which, we always keep in the same parent directory as the main application.
# We have to jump up TWO directories from the cwd using " ../../ ".
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),'../../secure_django_settings'
        )
    )
)

# Add the project's root directory to PYTHONPATH to ensure the server can find it
sys.path.append(
    os.path.join(
        os.path.dirname(__file__), '../'
    )
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

application = get_wsgi_application()
