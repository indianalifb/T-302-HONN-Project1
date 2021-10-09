from src.Repository.leader_board_repository import LeaderBoardRepository

class LeaderBoard():
    def __init__(self, repository: LeaderBoardRepository):
        self.repository = repository

    def get_leaders(self):
        leaders = self.repository.get_leaders()
        if len(leaders) == 0:
            return None
        else:
            return leaders
