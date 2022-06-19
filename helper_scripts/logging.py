"""
This is the module that implements a logger as a class.

Custom designed for the project(MultiInstanceLinux).
"""
# Author: sathya-pramodh
# Github: https://github.com/sathya-pramodh

# Software Licensed under the MIT License.

# License terms:

# MIT License

# Copyright (c) 2022 sathya-pramodh

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Imports
from datetime import datetime


class Logging:
    """
    Custom implementation of a logging class.
    """

    def __init__(self, output_path):
        """
        Initializer method for the class.

        output_path
        The full path to the folder to which you want to output the logs to.
        """
        self._path = output_path
        self._session_log_file = (
            output_path + datetime.now().strftime("%Y-%m-%d") + ".log"
        )

    def log(self, message):
        """
        Method to log a message to a log file.

        message
        A string data type containing the message to be logged.

        Returns None
        """
        with open(self._session_log_file, "a") as file:
            write_string = (
                "\n"
                + "[MultiInstanceLinux {}]".format(datetime.now().strftime("%H:%M:%S"))
                + ": "
                + message
            )
            file.write(write_string)
