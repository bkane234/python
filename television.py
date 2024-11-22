class Television:
    """
    Create the class variables that hold the maximum and minimum values

    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self)-> None:
        """
        Initialize the mutable variables
        
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME 
        self.__channel = Television.MIN_CHANNEL
    def power(self)-> None:
        """
        Turns the TV off and on

        """
        
        self.__status = not self.__status
        
    def mute(self)-> None:
        """
        Mutes the TV, making the volume 0
        
        """
        if self.__status:
            self.__muted = not self.__muted 
    def channel_up(self)-> int:
        """
        Increases the channel by one
        
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)
        
            
    def channel_down(self) -> int:
        """
        Decreases the channel by one
        
        """
        if self.__status:
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)
        
            
    def volume_up(self) -> int:
        """
        Turns the volume up on the TV
        
        """
        if self.__status:
            if self.__muted:
                self.__muted = False  
            self.__volume = min(self.__volume + 1, self.MAX_VOLUME)
        
            
    def volume_down(self) -> int:
        """
        Turns the volume down on the TV
        
        """
        if self.__status:
            if self.__muted:
                self.__muted = False 
            self.__volume = max(self.__volume - 1, self.MIN_VOLUME)
    
        
            
    def __str__(self) -> str:
        """
        Outputs a string that gives the Power status, the Channel, and Volume.

        """
        volume_display = 0 if self.__muted else self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume_display}'
