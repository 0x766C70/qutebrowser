# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2014-2021 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <https://www.gnu.org/licenses/>.

"""Keychain string displayed in the statusbar."""

from qutebrowser.qt.core import pyqtSlot

from qutebrowser.mainwindow.statusbar import textbase
from qutebrowser.utils import usertypes


class KeyString(textbase.TextBase):

    """Keychain string displayed in the statusbar."""

    @pyqtSlot(usertypes.KeyMode, str)
    def on_keystring_updated(self, _mode, keystr):
        self.setText(keystr)
