from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class MineField:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.mine_field = None
    
    def update_mine_field(self):
        self.mine_field = []
        for x in range(self.x):
            for y in range(self.y):

# class MineField:
#     def __init__(self):
#         self._mine_field = [["" for x in range(9)] for y in range(9)]
#         self._overlap_data = [[0 for x in range(9)] for y in range(9)]
#         self._mines = []
#         self.dig((5, 5))
#         time.sleep(2)
#         self.solve()
    
#     def update(self):
#         self._update_mine_field()
#         self._update_overlap_data()

#     def _update_mine_field(self):
#         for i in range(9):
#             for k in range(9):
#                 square_details = driver.find_element(By.ID, f"{i + 1}_{k + 1}").get_attribute("class")
#                 if "0" in square_details:
#                     self._mine_field[i][k] = "_"
#                 elif "blank" in square_details:
#                     self._mine_field[i][k] = "?"
#                 else:
#                     self._mine_field[i][k] = square_details[11:]
#         for mine in self._mines:
#             self._mine_field[mine[0]][mine[1]] = "M"

#     def _update_overlap_data(self):
#         for i, row in enumerate(self._mine_field):
#             for k, square in enumerate(row):
#                 overlap = 0
#                 if square == "?":
#                     for x in range(-1, 2):
#                         for y in range(-1, 2):
#                             if i + x in range(9) and k + y in range(9):
#                                 if self._mine_field[i + x][k + y] not in ("_", "?", "M"):
#                                     overlap += 1
#                 self._overlap_data[i][k] = overlap

#     def _find_mine(self):
#         self.update()
#         max = 0
#         mine_coords = None
#         for i, row in enumerate(self._overlap_data):
#             for k, square in enumerate(row):
#                 if int(square) > max:
#                     max = int(square)
#                     mine_coords = (i, k)
#         self._mines.append(mine_coords)
#         actions.context_click(driver.find_element(By.ID, f"{mine_coords[0] + 1}_{mine_coords[1] + 1}"))
#         actions.perform()
#         actions.reset_actions()
#         return mine_coords

#     def _test_adjacent(self, coords: tuple):
#         row = coords[0]
#         col = coords[1]
#         for i in range(-1, 2):
#             for k in range(-1, 2):
#                 if row + i not in range(9) or col + k not in range(9):
#                     continue
#                 if self._mine_field[row + i][col + k] in ("_", "M", "?"):
#                     continue
#                 blank_squares = []
#                 mines = 0
#                 for x in range(-1, 2):
#                     for y in range(-1, 2):
#                         if row + i + x not in range(9) or col + k + y not in range(9):
#                             continue
#                         if self._mine_field[row + i + x][col + k + y] == "M":
#                             mines += 1
#                         elif self._mine_field[row + i + x][col + k + y] == "?":
#                             blank_squares.append((row + i + x, col + k + y))
#                 if int(self._mine_field[row + i][col + k]) == mines:
#                     for square in blank_squares:
#                         self.dig(square)
#                 self._update_mine_field()

#     def solve(self):
#         while len(self._mines) != 10 and not driver.find_element(By.ID, "face").get_attribute("class") == "facewin":
#             coord = self._find_mine()
#             self.update()
#             self._test_adjacent(coord)
#             self.update()


#     def dig(self, square: tuple):
#         driver.find_element(By.ID, f"{square[0] + 1}_{square[1] + 1}").click()


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://minesweeperonline.com/#beginner")
actions = ActionChains(driver)
mine_field = MineField()
time.sleep(2)
driver.quit()
