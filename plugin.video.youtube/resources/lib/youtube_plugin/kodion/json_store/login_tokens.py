# -*- coding: utf-8 -*-
"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from . import JSONStore


class LoginTokenStore(JSONStore):
    def __init__(self):
        JSONStore.__init__(self, 'access_manager.json')

    def set_defaults(self):
        data = self._data
        if 'access_manager' not in data:
            data = {'access_manager': {'access_token': '', 'refresh_token': '', 'token_expires': -1}}
        self.save(data)
