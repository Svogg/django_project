import os

# SECURITY WARNING: don't run with debug turned on in production!
# На проде требуется изменить значение на False
DEBUG = os.environ.get('DEBUG', True)
