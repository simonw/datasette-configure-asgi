from datasette_configure_asgi import asgi_wrapper
import functools


class FakeDatasette:
    def __init__(self, config):
        self.config = config

    def plugin_config(self, name):
        assert "datasette-configure-asgi" == name
        return [self.config]


def test_asgi_wrapper():
    app = object()
    wrapper = asgi_wrapper(FakeDatasette({"class": "functools.wraps"}))
    wrapped = wrapper(app)
    assert app == wrapped.keywords["wrapped"]
    assert isinstance(wrapped, functools.partial)


def test_asgi_wrapper_with_args():
    app = object()
    wrapper = asgi_wrapper(
        FakeDatasette({"class": "functools.wraps", "args": {"assigned": ("foo",)}})
    )
    wrapped = wrapper(app)
    assert app == wrapped.keywords["wrapped"]
    assert isinstance(wrapped, functools.partial)
    assert ("foo",) == wrapped.keywords["assigned"]
