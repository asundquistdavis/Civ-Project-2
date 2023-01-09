
# # @sync_to_async
# class Start_Game(Thread):
#     def __init__(self, *players) -> None:
#         self.game = Game(players)
#         for player in players:
#             player.game_id = self.game.id
#         self.game.save()
#         super().__init__(self)

#     def run(self) -> None:

#         return super().run()