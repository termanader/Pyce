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

    results = ['0','1','2']

    def __init__(self):
        super().__init__('DiceRoller')

        #PYFORMS_STYLESHEET = 'style.css'

        self._resultlabel = ControlLabel('Last Result: ')
        self._results0 = ControlLabel(results[0])
        self._results1 = ControlLabel(results[1])
        self._results2 = ControlLabel(results[2])
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
            ('_resultlabel','_results0','_results1','_results2')
        ]
    def _1d4Action(self):

        rollResults(4)

       
    def _1d6Action(self):

        rollResults(6)

    
    def _1d8Action(self):

        rollResults(8)


    def _1d10Action(self):

        rollResults(10)
      

    def _1d12Action(self):
        
        rollResults(12) 
      

    def _1d20Action(self):
        
        rollResults(20)        

 
def rollResults(n = 0):
    global results
    results.insert(0, str(randint(1,n))

if __name__ == '__main__':  pyforms.start_app(DiceRoller)