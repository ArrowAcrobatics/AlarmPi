from pathlib import Path


class ServerConfig:
    def __init__(self, rootdirpath: Path):
        self.workingdir = rootdirpath
        self.logfile = rootdirpath/"alarmpi-server.log"
        self.WEB_ROOT = rootdirpath / "public"
        self.LISTEN_PORT = 8888
        self.LOGIN_PASSWORD_HASH = "0127ce4151c7694e87b9e50e71049ebbf39302de88dc6ed72be8e5ae294e9c33"

