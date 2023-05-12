from PyQt6.QtWidgets import *
from TV_Remote import *
from PyQt6.QtGui import *


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes controller for GUI, creating connection with view.py file to enable interaction with GUI
        :param args: Essential for initialization of controller
        :param kwargs: Same as above
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Creates connections between functions and buttons
        self.Volume_Up_Button.clicked.connect(lambda: self.volume_up())
        self.Channel_Up_Button.clicked.connect(lambda: self.channel_up())
        self.Channel_Down_Button.clicked.connect(lambda: self.channel_down())
        self.Volume_Down_Button.clicked.connect(lambda: self.volume_down())
        self.One_Button.clicked.connect(lambda: self.number_click('1'))
        self.Two_Button.clicked.connect(lambda: self.number_click('2'))
        self.Three_Button.clicked.connect(lambda: self.number_click('3'))
        self.Four_Button.clicked.connect(lambda: self.number_click('4'))
        self.Five_Button.clicked.connect(lambda: self.number_click('5'))
        self.Six_Button.clicked.connect(lambda: self.number_click('6'))
        self.Seven_Button.clicked.connect(lambda: self.number_click('7'))
        self.Eight_Button.clicked.connect(lambda: self.number_click('8'))
        self.Nine_Button.clicked.connect(lambda: self.number_click('9'))
        self.Zero_Button.clicked.connect(lambda: self.number_click('0'))
        self.Enter_Button.clicked.connect(lambda: self.enter_click())
        self.Clear_Button.clicked.connect(lambda: self.clear_click())
        self.Mute_Button.clicked.connect(lambda: self.mute_click())
        self.Off_Button.clicked.connect(lambda: self.off_click())

        # Image variables used for the channel display
        self.image_static = QPixmap('images/static.jpg')
        self.image_nick = QPixmap('images/nick.jpg')
        self.image_cartoon = QPixmap('images/cartoon.jpg')
        self.image_disney = QPixmap('images/disney.jpg')
        self.image_HBO = QPixmap('images/HBO.jpg')
        self.image_showtime = QPixmap('images/showtime.jpg')
        self.image_CNN = QPixmap('images/CNN.jpg')
        self.image_FOX = QPixmap('images/FOX.jpg')
        self.image_ESPN = QPixmap('images/ESPN.jpg')
        self.image_GSN = QPixmap('images/GSN.jpg')
        self.image_PBS = QPixmap('images/PBS.jpg')
        self.image_food = QPixmap('images/food.jpg')
        self.image_TVLand = QPixmap('images/TVLand.jpg')
        self.image_ABC = QPixmap('images/ABC.jpg')
        self.image_hallmark = QPixmap('images/hallmark.jpg')
        self.image_history = QPixmap('images/history.jpg')
        self.image_black = QPixmap('images/black.jpg')

        # Image list used to cycle through the channels
        self.channels = [self.image_history, self.image_nick, self.image_cartoon, self.image_disney, self.image_HBO,
                         self.image_showtime, self.image_CNN, self.image_FOX, self.image_ESPN, self.image_GSN,
                         self.image_PBS, self.image_food, self.image_TVLand, self.image_ABC, self.image_hallmark,
                         self.image_static]

        # Volume and channel variables used to hold temporary number values
        self.volume = 0
        self.channel = 0
        self.channel_display = 0
        self.temp_channel = '0'

        # Sets the screen to static when the GUI is opened
        self.TV_Screen_Label.setPixmap(self.channels[self.channel - 1])
        self.TV_Screen_Label.setScaledContents(True)

    def volume_up(self) -> None:
        """
        Increases the value of the volume label by one unless the value is 30, which returns 30 again.
        Changes the value of muted to the previous volume number value. Does nothing if volume label is off.
        """
        if self.volume < 30 and self.Volume_Number_Label.text() != 'Muted' and self.Volume_Number_Label.text() != 'Off':
            self.volume += 1
            self.Volume_Number_Label.setText(f'{self.volume}')
        elif self.Volume_Number_Label.text() == 'Muted':
            self.Mute_Button.setChecked(False)
            self.Volume_Number_Label.setText(f'{self.volume}')
        elif self.Volume_Number_Label.text() == 'Off':
            pass
        else:
            self.Volume_Number_Label.setText(f'{30}')

    def channel_up(self) -> None:
        """
        Increases the value of the channel label by one unless the value is 15 , which changes it to 0. Changes
        the TV Display every time the number increases to the new number's corresponding channel. Does
        nothing if off.
        """
        if self.channel < 15 and self.Channel_Number_Label.text() != 'Off':
            self.channel += 1
            self.Channel_Number_Label.setText(f'{self.channel}')
            self.TV_Screen_Label.setPixmap(self.channels[self.channel - 1])
            self.TV_Screen_Label.setScaledContents(True)
        elif self.channel == 15 and self.Channel_Number_Label.text() != 'Off':
            self.channel = 0
            self.Channel_Number_Label.setText(f'{self.channel}')
            self.TV_Screen_Label.setPixmap(self.channels[self.channel - 1])
            self.TV_Screen_Label.setScaledContents(True)

    def channel_down(self) -> None:
        """
        Reduces the value of the channel label by one unless the value is 0, which changes it to 15. Changes
        the TV Display every time the number decreases to the new number's corresponding channel. Does
        nothing if off.
        """
        if self.channel > 0 and self.Channel_Number_Label.text() != 'Off':
            self.channel -= 1
            self.Channel_Number_Label.setText(f'{self.channel}')
            self.TV_Screen_Label.setPixmap(self.channels[self.channel - 1])
            self.TV_Screen_Label.setScaledContents(True)
        elif self.channel == 0 and self.Channel_Number_Label.text() != 'Off':
            self.channel = 15
            self.Channel_Number_Label.setText(f'{self.channel}')
            self.TV_Screen_Label.setPixmap(self.channels[self.channel - 1])
            self.TV_Screen_Label.setScaledContents(True)

    def volume_down(self) -> None:
        """
        Reduces the value of the volume label by one unless the value is 0, which returns 0 again.
        Changes the value of muted to the previous volume number value. Does nothing if volume label is off.
        """
        if self.volume > 0 and self.Volume_Number_Label.text() != 'Muted' and self.Volume_Number_Label.text() != 'Off':
            self.volume -= 1
            self.Volume_Number_Label.setText(f'{self.volume}')
        elif self.Volume_Number_Label.text() == 'Muted':
            self.Mute_Button.setChecked(False)
            self.Volume_Number_Label.setText(f'{self.volume}')
        elif self.Volume_Number_Label.text() == 'Off':
            pass
        else:
            self.Volume_Number_Label.setText(f'{0}')

    def number_click(self, num: str) -> None:
        """
        If the keypad label says enter channel number, replaces enter channel number with the clicked button's number
        value. If the keypad label is a number value, appends newly clicked button's number to the end to a maximum
        of three digits. Does nothing if the keypad label is off.
        """
        if self.Temp_Channel_Number_Label.text() == 'Enter Channel Number:' and self.Temp_Channel_Number_Label.text() \
                != 'Off':
            self.temp_channel = num
            self.Temp_Channel_Number_Label.setText(f'{num}')
        elif self.Temp_Channel_Number_Label.text() != 'Off' and len(self.Temp_Channel_Number_Label.text()) < 3:
            self.temp_channel += num
            self.Temp_Channel_Number_Label.setText(f'{self.temp_channel}')

    def enter_click(self) -> None:
        """
        If the value inside the keypad label is a number, replaces the value inside the channel label with
        that number unless that number is greater than 15, in which case the value is replaced with 15. Changes
        the TV display to the numbers corresponding channel. Does nothing if the value is off or enter channel number.
        """
        if self.Temp_Channel_Number_Label.text() != 'Enter Channel Number:' and self.Temp_Channel_Number_Label.text() \
                != 'Off' and int(self.Temp_Channel_Number_Label.text()) < 16:
            self.channel = int(self.Temp_Channel_Number_Label.text())
            self.Channel_Number_Label.setText(f'{self.channel}')
            self.Temp_Channel_Number_Label.setText('Enter Channel Number:')
            self.TV_Screen_Label.setPixmap(self.channels[self.channel - 1])
            self.TV_Screen_Label.setScaledContents(True)
        elif self.Temp_Channel_Number_Label.text() != 'Enter Channel Number:' and self.Temp_Channel_Number_Label.text()\
                != 'Off' and int(self.Temp_Channel_Number_Label.text()) >= 16:
            self.channel = 15
            self.Channel_Number_Label.setText(f'{self.channel}')
            self.Temp_Channel_Number_Label.setText('Enter Channel Number:')
            self.TV_Screen_Label.setPixmap(self.channels[self.channel - 1])
            self.TV_Screen_Label.setScaledContents(True)

    def clear_click(self) -> None:
        """
        Restores the value of the keypad label to enter channel number.
        """
        if self.Temp_Channel_Number_Label.text() != 'Enter Channel Number:' and self.Temp_Channel_Number_Label.text() \
                != 'Off':
            self.temp_channel = '0'
            self.Temp_Channel_Number_Label.setText('Enter Channel Number:')

    def mute_click(self) -> None:
        """
        Turns the volume label to muted when activated. When deactivated, returns previous number value.
        Can also be deactivated by clicking volume up or down buttons.
        """
        if self.Mute_Button.isChecked() and self.Off_Button.isChecked():
            self.Mute_Button.setChecked(False)
        elif self.Mute_Button.isChecked():
            self.Volume_Number_Label.setText('Muted')
        else:
            self.Volume_Number_Label.setText(f'{self.volume}')

    def off_click(self) -> None:
        """
        Updates channel, keypad, and volume labels to off when the button is activated,
        along with making the TV display image black. When deactivated, restores labels' previous information.
        """
        if self.Off_Button.isChecked():
            self.Volume_Number_Label.setText('Off')
            self.Channel_Number_Label.setText('Off')
            self.Temp_Channel_Number_Label.setText('Off')
            self.Mute_Button.setChecked(False)
            self.TV_Screen_Label.setPixmap(self.image_black)
            self.TV_Screen_Label.setScaledContents(True)

        else:
            self.Volume_Number_Label.setText(f'{self.volume}')
            self.Channel_Number_Label.setText(f'{self.channel}')
            self.Temp_Channel_Number_Label.setText('Enter Channel Number:')
            self.TV_Screen_Label.setPixmap(self.channels[self.channel - 1])
            self.TV_Screen_Label.setScaledContents(True)
