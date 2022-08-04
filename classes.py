class Television:
    """
    - A class representing the state of the television.
    - Contains methods to turn power ON / OFF
    - Change the channels
    - Change the volume up / down
    """
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        - Constructor to create initial state of the Television object.
        - It sets the channel to the min and volume to minimum
        - It sets the power to OFF state
        """
        self.__tv_channel = Television.MIN_CHANNEL
        self.__tv_volume = Television.MIN_VOLUME
        self.__tv_status = False

    def power(self) -> None:
        """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """
        if not self.__tv_status:
            self.__tv_status = True
        else:
            self.__tv_status = False

    def channel_up(self) -> None:
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """
        if self.__tv_status == True:
            if self.__tv_channel >= Television.MAX_CHANNEL:
                self.__tv_channel = Television.MIN_CHANNEL
            else:
                self.__tv_channel += 1

    def channel_down(self) -> None:
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        if self.__tv_status:
            if self.__tv_channel - 1 <= Television.MIN_CHANNEL:
                self.__tv_channel = Television.MAX_CHANNEL
            else:
                self.__tv_channel -= 1

    def volume_up(self) -> None:
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
        if self.__tv_status == True:
            if self.__tv_volume >= Television.MAX_VOLUME:
                self.__tv_volume = self.__tv_volume + 0
            else:
                self.__tv_volume = self.__tv_volume + 1

    def volume_down(self) -> None:
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """
        if self.__tv_status == True:
            if self.__tv_volume == Television.MIN_VOLUME:
                self.__tv_volume = self.__tv_volume + 0
            else:
                self.__tv_volume = self.__tv_volume - 1

    def __str__(self) -> str:
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        :return: Return the string with tv status channel and valume.
        """
        return f"TV Status: Is on = {self.__tv_status}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}"
