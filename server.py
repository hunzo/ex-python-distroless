from main import app
from gunicorn.app.base import BaseApplication

import multiprocessing


def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


class StandaloneApplication(BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):

        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}

        for key, value in config.items():
            self.cfg.set(key.lower(), value)


    def load(self):
        return self.application


# if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=8080, debug=False)

if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('0.0.0.0', '8080'),
        # 'workers': number_of_workers(),
        'timeout': 5,
        # 'worker_class': 'gevent',
        'threads': 10,
        'workers': 2,
        'raw_env': ["TEST=From Config Files"],
        # 'reload': True
    }
    StandaloneApplication(app, options).run()
