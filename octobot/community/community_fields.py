#  This file is part of OctoBot (https://github.com/Drakkar-Software/OctoBot)
#  Copyright (c) 2022 Drakkar-Software, All rights reserved.
#
#  OctoBot is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  OctoBot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with OctoBot. If not, see <https://www.gnu.org/licenses/>.
import enum 


class CommunityFields(enum.Enum):
    ID = "_id"
    CURRENT_SESSION = "currentsession"
    STARTED_AT = "startedat"
    UP_TIME = "uptime"
    VERSION = "version"
    SIMULATOR = "simulator"
    TRADER = "trader"
    EVAL_CONFIG = "evalconfig"
    PAIRS = "pairs"
    EXCHANGES = "exchanges"
    EXCHANGE_TYPES = "exchangetypes"
    NOTIFICATIONS = "notifications"
    TYPE = "type"
    PLATFORM = "platform"
    REFERENCE_MARKET = "referencemarket"
    PORTFOLIO_VALUE = "portfoliovalue"
    PROFITABILITY = "profitability"
    TRADED_VOLUMES = "tradedvolumes"
    SUPPORTS = "supports"
    ROLES = "roles"
    DONATIONS = "donations"
    SIGNAL_EMITTER = "signalemitter"
    SIGNAL_RECEIVER = "signalreceiver"
    COMMUNITY_BOT_TYPE = "communitybottype"
    PROFILE_NAME = "profilename"
    PROFILE_ID = "profileid"
    PROFILE_IMPORTED = "profileimported"
