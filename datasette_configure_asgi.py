from datasette import hookimpl
import importlib


@hookimpl
def asgi_wrapper(datasette):
    def wrap_with_classes(app):
        configs = datasette.plugin_config("datasette-configure-asgi") or []
        for config in configs:
            module_path, class_name = config["class"].rsplit(".", 1)
            mod = importlib.import_module(module_path)
            klass = getattr(mod, class_name)
            args = config.get("args") or {}
            app = klass(app, **args)
        return app

    return wrap_with_classes
