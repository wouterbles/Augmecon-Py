from augmecon_py.augmecon import MoipAugmeconR
from augmecon_py.reader import read_excel_model

mod = read_excel_model("3kp40")
A = MoipAugmeconR(mod)
A.execute()
