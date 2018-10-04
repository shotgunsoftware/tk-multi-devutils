# Copyright (c) 2018 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sys

from sgtk.platform.qt import QtCore, QtGui


class StdinRedirector(QtCore.QObject):
    """
    Handles redirecting stdin.
    Sends an input signal when stdin is read from.
    """

    def __init__(self, readline_callback, parent=None):
        """
        Initialize the redirection object.

        :param readline_callback: Method that will be executed when
            the system is looking for input. Should return
            a string of input as it would be provided by a user.
        :param parent: The parent qt object.
        """
        super(StdinRedirector, self).__init__(parent)
        self._handle = None
        self._readline_callback = readline_callback

    def __enter__(self):
        """
        Begin redirection.
        Temporarily assigns stdin to this object for writing.
        """
        self._handle = sys.stdin
        sys.stdin = self
        return self

    def __exit__(self, type, value, traceback):
        """
        Finish redirection.
        Repoint sys.stdin to the original handle.
        """
        sys.stdin = self._handle


class StdoutRedirector(QtCore.QObject):
    """Handles redirecting stdout.

    Sends an output signal when stdout is written to.
    """

    output = QtCore.Signal(str)

    def __init__(self, tee=False, parent=None):
        """Initialize the redirection object.

        :param tee: Also write to sys stdout when True.
        :param parent: The parent qt object.
        """
        super(StdoutRedirector, self).__init__(parent)
        self._handle = None
        self._tee = tee

    def __enter__(self):
        """Begin redirection.

        Temporarily assigns stdout to this object for writing.
        """
        self._handle = sys.stdout
        sys.stdout = self
        return self

    def __exit__(self, type, value, traceback):
        """Finish redirection.

        Repoint sys.stdout to the original handle.
        """
        sys.stdout = self._handle

    def flush(self):
        """Nothing to emit for the redirector. Flush the original if tee'ing."""
        if self._tee:
            self._handle.flush()

    def write(self, msg):
        """Forward the written output to the output signal.

        If tee, then also write to stdout.
        """
        if isinstance(msg, unicode):
            msg = unicode.encode(msg, "utf-8")

        self.output.emit(msg)
        QtCore.QCoreApplication.processEvents()

        if self._tee and self._handle:
            self._handle.write(msg)


class StderrRedirector(QtCore.QObject):
    """Handles redirecting stderr.

    Sends an output signal when stderr is written to.
    """

    error = QtCore.Signal(str)

    def __init__(self, tee=False, parent=None):
        """Initialize the redirection object.

        :param tee: Also write to sys stderr when True.
        :param parent: The parent qt object.
        """
        super(StderrRedirector, self).__init__(parent)
        self._handle = None
        self._tee = tee

    def __enter__(self):
        """Begin redirection.

        Temporarily assigns stderr to this object for writing.
        """
        self._handle = sys.stderr
        sys.stderr = self
        return self

    def __exit__(self, type, value, traceback):
        """Finish redirection.

        Repoint sys.stderr to the original handle.
        """
        sys.stderr = self._handle

    def flush(self):
        """Nothing to emit for the redirector. Flush the original if tee'ing."""
        if self._tee:
            self._handle.flush()

    def write(self, msg):
        """Forward the written output to the error signal.

        If tee, then also write to stderr.
        """
        if isinstance(msg, unicode):
            msg = unicode.encode(msg, "utf-8")

        self.error.emit(msg)
        QtCore.QCoreApplication.processEvents()

        if self._tee:
            self._handle.write(msg)
