
from otree.api import *
c = cu

doc = 'Welcome page with instructions'
class C(BaseConstants):
    NAME_IN_URL = 'Welcome_Majo_12_3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    pass
class Waiting(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group < 16 # 15 Players, 3 candidates and 12 voters
class Welcome(Page):
    form_model = 'player'
page_sequence = [Waiting, Welcome]