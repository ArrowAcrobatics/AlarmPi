import tornado


class BaseHandler(tornado.web.RequestHandler):
    # create base handler to override get_current_user to allow authentication
    def get_current_user(self):
        return self.get_secure_cookie("user")
