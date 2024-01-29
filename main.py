from src.augmecon import MoipAugmeconR
from src.reader import read_excel_model

mod = read_excel_model("3kp40")
A = MoipAugmeconR(mod)
A.execute()
