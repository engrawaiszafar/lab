import pytest
from classes import *


class Test:

    def setup_method(self):
        self.t1 = Television()

    def teardown_method(self):
        del self.t1

    def test_init(self):
        assert self.t1.__str__() == "TV Status: Is on = False, Channel = 0, Volume = 0"

    def test_power(self):
        assert self.t1.__str__() == "TV Status: Is on = False, Channel = 0, Volume = 0"
        self.t1.power()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"
        self.t1.power()
        assert self.t1.__str__() == "TV Status: Is on = False, Channel = 0, Volume = 0"

    def test_channel_up(self):
        self.t1.power()  # Powering on the brand new tv
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"
        self.t1.channel_up()  # Increasing the channel
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 1, Volume = 0"
        self.t1.channel_up()  # Increasing the channel
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 2, Volume = 0"
        self.t1.channel_up()  # Increasing the channel and reached max channel
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 3, Volume = 0"
        self.t1.channel_up()  # Increasing the channel and shold change the channel to min_channel
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"
        self.t1.channel_up()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 1, Volume = 0"

        # Power off the tv again and make sure that channel is still at 1
        self.t1.power()  # Power off
        self.t1.channel_up()  # When tv is power off channel_up should not work
        assert self.t1.__str__() == "TV Status: Is on = False, Channel = 1, Volume = 0"
        self.t1.power()  # Power ON
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 1, Volume = 0"

    def test_channel_down(self):
        self.t1.power()  # Powering on the brand new tv
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"
        self.t1.channel_down()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 3, Volume = 0"
        self.t1.channel_down()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 2, Volume = 0"
        self.t1.channel_down()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 1, Volume = 0"
        self.t1.channel_down()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"
        self.t1.channel_down()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 3, Volume = 0"

        # Power off the tv again and make sure that channel is still at 3
        self.t1.power()  # Power off
        self.t1.channel_down()  # When tv is power off channel_down should not work
        assert self.t1.__str__() == "TV Status: Is on = False, Channel = 3, Volume = 0"
        self.t1.power()  # Power ON
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 3, Volume = 0"

    def test_volume_up(self):
        self.t1.power()  # Powering on the brand new tv
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"
        self.t1.volume_up()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 1"
        self.t1.volume_up()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 2"
        # Now max volume is reached. now volume_up key should not change the volume
        self.t1.volume_up()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 2"

        # Power off the tv again and make sure that volume is still at 2
        self.t1.power()  # Power off
        self.t1.volume_up()  # When tv is power off volume_up should not work
        assert self.t1.__str__() == "TV Status: Is on = False, Channel = 0, Volume = 2"
        self.t1.power()  # Power ON
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        self.t1.power()  # Powering on the brand new tv
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"
        self.t1.volume_down()  # Because the volume is already at min. to volume_down key will not change the volume
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"

        # Now taking the volume to max by using volume_up method
        self.t1.volume_up()
        self.t1.volume_up()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 2"

        self.t1.volume_down()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 1"
        self.t1.volume_down()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"
        self.t1.volume_down()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 0"

        # Now testing that volume_down should not change the volume when tv is turned off
        self.t1.volume_up()
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 1"
        # Power off the tv again and make sure that volume is still at 1
        self.t1.power()  # Power off
        self.t1.volume_down()
        assert self.t1.__str__() == "TV Status: Is on = False, Channel = 0, Volume = 1"
        self.t1.power()  # Power ONN
        assert self.t1.__str__() == "TV Status: Is on = True, Channel = 0, Volume = 1"



