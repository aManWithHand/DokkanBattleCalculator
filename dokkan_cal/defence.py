from .gui import PhaseFrame,OutputFrame,StatusFrame
from .base import Base
from .core import Core

class Defence(Base):
    def __init__(self,stat:StatusFrame, phase1:PhaseFrame, phase2:PhaseFrame, out:OutputFrame):
        super().__init__()
        self._statFrame = stat
        self._phase1Frame = phase1
        self._phase2Frame = phase2
        self._outFrame = out
    
    def _collectData(self):
        self.base = self._statFrame.getDef()
        self.buffPhase1 = self._phase1Frame.getBuff()
        self.buffPhase2 = self._phase2Frame.getBuff()

    def cal(self):
        self._collectData()
        self.beforeAttack = Core.buff(self.baseDef,[self.buffPhase1,self.buffPhase2])
    
    def show(self):
        self._outFrame.show(self)