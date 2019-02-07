from random             import randint
import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls   import ControlFile
from pyforms.controls   import ControlText
from pyforms.controls   import ControlSlider
from pyforms.controls   import ControlPlayer
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlLabel



class DiceRoller(BaseWidget):

    def __init__(self):
        super().__init__('DiceRoller')
        #PYFORMS_STYLESHEET = 'style.css'
        self._resultlabel = ControlLabel('Last Result: ')
        self._results = ControlLabel()


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
            ('_resultlabel','_results')
        ]

    def _1d4Action(self):
        self._results.value = str(randint(1,4)) 
       
    def _1d6Action(self):
        self._results.value = str(randint(1,6)) 
    
    def _1d8Action(self):
        self._results.value = str(randint(1,8)) 

    def _1d10Action(self):
        self._results.value = str(randint(1,10)) 

    def _1d12Action(self):
        self._results.value = str(randint(1,12)) 

    def _1d20Action(self):
        self._results.value = str(randint(1,20)) 


if __name__ == '__main__':  pyforms.start_app(DiceRoller)