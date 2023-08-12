#!/usr/bin/python
import os

# server.py
#
# Responsible for specifying parameters of and starting a Tornado
# web server for the configuration web interface of the AlarmPi.
#
# Mckenna Cisler
# mckennacisler@gmail.com
# 1.13.2019

import daemon
import tornado.ioloop
import tornado.web
import tornado.httpserver

from config.AlarmDate import getFullDayName
from webserver.BaseHandler import BaseHandler
from webserver.ConfigHandler import *
from config.AlarmConfig import *
import UIModules

from webserver.LoginHandler import LoginHandler


class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return

        self.render("index.html",
                    config=GlobalConfig.alarm,
                    days=Days(),
                    dailySettings=DailySettings(),
                    globalSettings=GlobalSettings(),
                    sounds=GlobalConfig.audio.Sounds(),
                    getFullDayName=getFullDayName,
                    getPrettyName=getPrettyName)


def make_app(config):
    """ Sets up a tornado web application for AlarmPi and returns it. """
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/login", LoginHandler),
        (r"/config", ConfigHandler, dict(config=GlobalConfig.alarm)),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": GlobalConfig.server.WEB_ROOT})
    ],
        static_path=GlobalConfig.server.WEB_ROOT,
        template_path=GlobalConfig.server.WEB_ROOT,
        ui_modules=UIModules,
        debug=GlobalConfig.debug,
        cookie_secret=str(os.urandom(24))
    )


if __name__ == "__main__":
    # TODO: logfile is a memory hazard now... add max size or cyclic write feature.
    logFile = open(GlobalConfig.server.logfile, "a")
    with daemon.DaemonContext(working_directory=GlobalConfig.server.workingdir, stdout=logFile, stderr=logFile):
        app = make_app(GlobalConfig.alarm)
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(GlobalConfig.server.LISTEN_PORT)
        logging.info("Starting webserver at localhost:%d" % GlobalConfig.server.LISTEN_PORT)
        tornado.ioloop.IOLoop.instance().start()
