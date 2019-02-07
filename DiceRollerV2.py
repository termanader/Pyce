from random             import randint
import pyforms
from pyforms.basewidget import BaseWidget
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
            ('_resultlabel','_resultDisplay0','_resultDisplay1','_resultDisplay2')
        ]   

    def _1d4Action(self):
        self._resultDisplay0.value = rollResults(4)
        self._resultDisplay1.value = results[1]
        self._resultDisplay2.value = results[2]

    def _1d6Action(self):
        self._resultDisplay0.value = rollResults(6)
        self._resultDisplay1.value = results[1]
        self._resultDisplay2.value = results[2]

    def _1d8Action(self):
        self._resultDisplay0.value = rollResults(8)
        self._resultDisplay1.value = results[1]
        self._resultDisplay2.value = results[2]

    def _1d10Action(self):
        self._resultDisplay0.value = rollResults(10)
        self._resultDisplay1.value = results[1]
        self._resultDisplay2.value = results[2]

    def _1d12Action(self):
        self._resultDisplay0.value = rollResults(12)
        self._resultDisplay1.value = results[1]
        self._resultDisplay2.value = results[2]
        
    def _1d20Action(self):
        self._resultDisplay0.value = rollResults(20)
        self._resultDisplay1.value = results[1]
        self._resultDisplay2.value = results[2]
    
 
def rollResults(n = 0):
        results.insert(0, str(randint(1,n)))
        return results[0]

        
if __name__ == '__main__':  pyforms.start_app(DiceRoller)