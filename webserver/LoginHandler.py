import hashlib
from random import random

from config.Config import GlobalConfig
from webserver.BaseHandler import BaseHandler


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html", message=None)

    def post(self):
        # check password
        password = self.get_argument("password")
        if hashlib.sha256(password).hexdigest() == GlobalConfig.server.LOGIN_PASSWORD_HASH:
            self.set_secure_cookie("user", str(random()))
            self.redirect("/")
        else:
            self.render("login.html",
                        message="Incorrect password")
