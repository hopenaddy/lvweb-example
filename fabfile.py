from fabric.api import put, sudo
from fabvenv import Venv

ROOT = "/opt/lv128/example"

def deploy():
    venv = Venv(ROOT, "requirements.txt")
    if not venv.exists():
        venv.create()
    venv.install()
    put("example.py", ROOT)
    put("lv128.service", ROOT)
    run("sudo mv lv128.service /etc/systemd/system/")
    run("sudo systemctl enable lv128")
    run("sudo systemctl restart lv128")
