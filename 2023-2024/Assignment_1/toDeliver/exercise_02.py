import matplotlib.pyplot as plt
import sys
from pathlib import Path

from exercise_02_a import Exerc2Gui_a
from exercise_02_b_1 import Exerc2Gui_b_1
from exercise_02_b_2 import Exerc2Gui_b_2

if __name__ == "__main__":
    try:
        gui_1 = Exerc2Gui_a(
            plt, name="Feasible Region", figsize=(15, 8), save_images=True
        )
        gui_1.main()

        gui_2 = Exerc2Gui_b_1(
            plt, name="Feasible Region", figsize=(15, 8), save_images=True
        )
        gui_2.main()

        gui_3 = Exerc2Gui_b_2(
            plt, name="Feasible Region", figsize=(15, 8), save_images=True
        )
        gui_3.main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
