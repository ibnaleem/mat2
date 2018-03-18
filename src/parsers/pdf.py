""" Handle PDF

"""

import os
import logging
import tempfile
import shutil
import io
import tempfile

import cairo
import gi
gi.require_version('Poppler', '0.18')
from gi.repository import Poppler

from . import abstract

logging.basicConfig(level=logging.DEBUG)


class PDFParser(abstract.AbstractParser):
    def __init__(self, filename):
        super().__init__(filename)
        self.meta_list = {'author', 'creation-date', 'creator', 'format', 'keywords',
                'metadata', 'mod-date', 'producer', 'subject', 'title',
                'viewer-preferences'}
        self.uri = 'file://' + os.path.abspath(self.filename)
        self.password = None

    def remove_all(self):
        """
            Load the document into Poppler, render pages on PNG,
            and shove those PNG into a new PDF. Metadata from the new
            PDF are removed via Poppler, because there is no way to tell
            cairo to not add "created by cairo" during rendering.
        """
        document = Poppler.Document.new_from_file(self.uri, self.password)
        pages_count = document.get_n_pages()

        _, tmp_path = tempfile.mkstemp()
        pdf_surface = cairo.PDFSurface(tmp_path, 128, 128)
        pdf_context = cairo.Context(pdf_surface)

        for pagenum in range(pages_count):
            page = document.get_page(pagenum)
            page_width, page_height = page.get_size()
            logging.info("Rendering page %d/%d", pagenum + 1, pages_count)

            img_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(page_width)*2, int(page_height)*2)
            img_context = cairo.Context(img_surface)

            img_context.scale(2, 2)
            page.render_for_printing(img_context)
            img_context.show_page()

            buf = io.BytesIO()
            img_surface.write_to_png(buf)
            img_surface.finish()
            buf.seek(0)

            img = cairo.ImageSurface.create_from_png(buf)
            pdf_surface.set_size(page_width*2, page_height*2)
            pdf_context.set_source_surface(img, 0, 0)
            pdf_context.paint()
            pdf_context.show_page()

        pdf_surface.finish()

        # This is removing metadata added by Poppler
        document = Poppler.Document.new_from_file('file://' + tmp_path)
        document.set_producer('')
        document.set_creator('')
        document.save('file://' + os.path.abspath(self.output_filename))
        os.remove(tmp_path)

        return True

    def get_meta(self):
        """ Return a dict with all the meta of the file
        """
        print("URI: %s", self.uri)
        document = Poppler.Document.new_from_file(self.uri, self.password)
        metadata = {}
        for key in self.meta_list:
            if document.get_property(key):
                metadata[key] = document.get_property(key)
        return metadata
