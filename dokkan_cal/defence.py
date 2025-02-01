from .gui import PhaseFrame,OutputFrame,StatusFrame,LeaderFrame,LinkFrame
from .base import Base
from .core import Core

class Defence(Base):
    def __init__(self,stat:StatusFrame,leader:LeaderFrame, phase1:PhaseFrame, phase2:PhaseFrame, link:LinkFrame, out:OutputFrame):
        super().__init__()
        self._statFrame = stat
        self._leaderFrame = leader
        self._phase1Frame = phase1
        self._phase2Frame = phase2
        self._linkFrame = link
        self._outFrame = out
    
    def _collectData(self):
        self.base = self._statFrame.getDef()
        self.buffLeader = self._leaderFrame.getBuff()
        self.buffPhase1 = self._phase1Frame.getBuff()
        self.buffPhase2 = self._phase2Frame.getBuff()
        self.buffLink = self._linkFrame.getBuff()

    def cal(self):
        self._collectData()
        self.beforeAttack = Core.buff(self.base,[self.buffLeader,self.buffPhase1,self.buffLink])
        #add afterattck calculation here
    
    def show(self):
        self._outFrame.show(self)