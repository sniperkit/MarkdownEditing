import sublime, sublime_plugin
import os, string
import re

from datetime import date

try:
    from MarkdownWiki.open_page import *
except ImportError:
    from open_page import *

class OpenJournalCommand(OpenPageCommand):
    def run(self, edit):
        today = date.today()
        page = today.strftime('%Y-%m-%d')

        self.select_page(page)
