from gevent.backdoor import BackdoorServer


class orcaBackdoorServer(BackdoorServer):
    def __init__(self, listener, localf=None, banner=None, **server_args):
        super(orcaBackdoorServer, self).__init__(listener, {}, banner, **server_args)
        self.localf = localf

    def _create_interactive_locals(self):
        obj = super(orcaBackdoorServer, self)._create_interactive_locals()
        obj.update(self.localf())
        return obj
