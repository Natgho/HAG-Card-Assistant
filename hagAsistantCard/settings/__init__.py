# Created by SezerBozkir<admin@sezerbozkir.com> at 11/6/2020
import os

# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)
if os.environ.get('hagAsistantCard', 'prod') == 'prod':
    from .prod import *
else:
    from .dev import *
