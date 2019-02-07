from random             import randint
import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls   import ControlFile
from pyforms.controls   import ControlText
from pyforms.controls   import ControlSlider
from pyforms.controls   import ControlPlayer
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlButton

class DiceRoller(BaseWidget):

    def __init__(self):
        super().__init__('DiceRoller')

        #Definition of the forms fields
        #self._videofile  = ControlFile('Video')
        #self._threshold  = ControlSlider('Threshold', default=114, minimum=0, maximum=255)
        #self._blobsize   = ControlSlider('Minimum blob size', default=110, minimum=100, maximum=2000)
        #self._player     = ControlPlayer('Player')
        #self._runbutton  = ControlButton('Run')
        self._outputfile = ControlText('Last Result')
        self._1d4   = ControlButton('1d4')
        self._1d6   = ControlButton('1d6')
        self._1d8   = ControlButton('1d8')
        self._1d10  = ControlButton('1d10')
        self._1d12  = ControlButton('1d12')
        self._1d20  = ControlButton('1d20')
        #Define the Button Actions

        self._1d4.value = self._1d4Action
        self._1d6.value = self._1d6Action
        self._1d8.value = self._1d8Action
        self._1d10.value = self._1d10Action
        self._1d12.value = self._1d12Action
        self._1d20.value = self._1d20Action


        #Define the organization of the Form Controls
        self._formset = [
            '_1d4',
            '_1d6',
            '_1d8', 
            '_1d10',
            '_1d12',
            '_1d20',
            '_outputfile'
        ]

    def _1d4Action(self):

        self._outputfile.value = str(randint(1,4)) 
       
    def _1d6Action(self):

        self._outputfile.value = str(randint(1,6)) 
    
    def _1d8Action(self):

        self._outputfile.value = str(randint(1,8)) 

    def _1d10Action(self):

        self._outputfile.value = str(randint(1,10)) 

    def _1d12Action(self):

        self._outputfile.value = str(randint(1,12)) 

    def _1d20Action(self):

        self._outputfile.value = str(randint(1,20)) 
if __name__ == '__main__':  pyforms.start_app(DiceRoller)