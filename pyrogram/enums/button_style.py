#  PyroRatnaGram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2022-present AnmolRatna25 <https://github.com/AnmolRatna25>
#
#  This file is part of PyroRatnaGram.
#
#  PyroRatnaGram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  PyroRatnaGram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with PyroRatnaGram.  If not, see <http://www.gnu.org/licenses/>.

from .auto_name import AutoName
from enum import auto


class ButtonStyle(AutoName):
    """Visual style for inline/reply keyboard buttons.

    Values:
        PRIMARY: Blue/primary colour button.
        DANGER: Red/danger colour button.
        SUCCESS: Green/success colour button.
    """

    PRIMARY = auto()
    DANGER = auto()
    SUCCESS = auto()
