from wagtail.images.formats import Format, register_image_format

register_image_format(Format('thumbnail', 'Thumnail', 'rich-text-image-thumbnail', 'max-220x220'))
