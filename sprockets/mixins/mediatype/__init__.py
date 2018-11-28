"""
sprockets.mixins.media_type

"""

try:
    from .content import (ContentMixin, ContentSettings,
                          add_binary_content_type, add_text_content_type,
                          set_default_content_type)

except ImportError as error:  # pragma no cover
    def _error_closure(*args, **kwargs):
        raise error

    class ErrorClosureClass:
        def __init__(self, *args, **kwargs):
            raise error

    ContentMixin = ErrorClosureClass
    ContentSettings = ErrorClosureClass
    add_binary_content_type = _error_closure
    add_text_content_type = _error_closure
    set_default_content_type = _error_closure


version_info = (2, 2, 2)
__version__ = '.'.join(str(v) for v in version_info)
__all__ = ['ContentMixin', 'ContentSettings', 'add_binary_content_type',
           'add_text_content_type', 'set_default_content_type',
           'version_info', '__version__']
