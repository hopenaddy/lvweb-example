from fabric.api import put, sudo
from fabvenv import Venv

ROOT = "/opt/lv128/example"

def deploy():
    venv = Venv(ROOT, "requirements.txt")
    if not venv.exists():
        venv.create()
    venv.install()
    put("example.py", ROOT)
    put("lv128.service", "/etc/systemd/user/")
    sudo("systemctl enable lv128")
    sudo("systemctl restart lv128")
