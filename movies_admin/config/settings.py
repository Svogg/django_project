from pathlib import Path
from dotenv import load_dotenv
from split_settings.tools import include


load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

include(
    'components/secret_key.py',
    'components/debug_mode.py',
    'components/allowed_hosts.py',
    'components/application_definition.py',
    'components/templates.py',
    'components/middleware.py',
    'components/database.py',
    'components/installed_apps.py',
    'components/auth_password_validators.py',
    'components/internationalization.py',
    'components/static_files.py',
    'components/default_auto_field.py',
    'components/locale_paths.py',
    'components/internal_ips.py'
)
