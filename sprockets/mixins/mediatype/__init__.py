"""
sprockets.mixins.media_type

"""

from .content import (ContentMixin, ContentSettings,
                      add_binary_content_type, add_text_content_type,
                      set_default_content_type)


__all__ = ['ContentMixin', 'ContentSettings', 'add_binary_content_type',
           'add_text_content_type', 'set_default_content_type',
           'version_info', '__version__']
