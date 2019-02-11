from random             import randint
import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls   import *
from pyforms.controls   import ControlFile
from pyforms.controls   import ControlText
from pyforms.controls   import ControlSlider
from pyforms.controls   import ControlPlayer
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlLabel

results = ['','','']

class DiceRoller(BaseWidget):

    def __init__(self):
        super().__init__('DiceRoller')
        #PYFORMS_STYLESHEET = 'style.css'
        
        self._resultlabel = ControlLabel('Last 3 Results: ')
        self._resultDisplay0 = ControlLabel()
        self._resultDisplay1 = ControlLabel()
        self._resultDisplay2 = ControlLabel()

        
        self._1d4img    = ControlImage('img\1d4a.jpg')
        self._1d4   = ControlButton('1d4')
        self._1d6   = ControlButton('1d6')
        self._1d8   = ControlButton('1d8')
        self._1d10  = ControlButton('1d10')
        self._1d12  = ControlButton('1d12')
        self._1d20  = ControlButton('1d20')

        #Define the Button Actions

        self._1d4.value = self._1d4Action 


        #Define the organization of the Form Controls
        self._formset = [
            '_1d4',
            '_1d6',
            '_1d8', 
            '_1d10',
            '_1d12',
            '_1d20',
            ('_resultlabel','_resultDisplay0','_resultDisplay1','_resultDisplay2')
        ]   



        
if __name__ == '__main__':  pyforms.start_app(DiceRoller)