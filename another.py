import pyautogui as gui
import multiprocessing as mp

gui.PAUSE = 0

# gui.displayMousePosition()

def click_main():
    try:
        while True:
            gui.click(988, 351)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_main2():
    try:
        while True:
            gui.click(989, 351)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_main3():
    try:
        while True:
            gui.click(990, 351)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_main4():
    try:
        while True:
            gui.click(991, 366)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_main5():
    try:
        while True:
            gui.click(992, 351)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_main6():
    try:
        while True:
            gui.click(993, 351)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_main7():
    try:
        while True:
            gui.click(987, 351)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_main8():
    try:
        while True:
            gui.click(986, 351)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_main9():
    try:
        while True:
            gui.click(985, 351)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_main10():
    try:
        while True:
            gui.click(984, 351)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_main11():
    try:
        while True:
            gui.click(983, 351)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_upgrade():
    try:
        while True:
            gui.click(1330, 308)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return
def click_upgrade():
    try:
        while True:
            gui.click(240, 870)
    except gui.FailSafeException:
        print(f"Fail-safe triggered.")
        return

if  __name__ == "__main__":


    main_process = mp.Process(target=click_main)
    main2_process = mp.Process(target=click_main2)
    main3_process = mp.Process(target=click_main3)
    main4_process = mp.Process(target=click_main4)
    main5_process = mp.Process(target=click_main5)
    main6_process = mp.Process(target=click_main6)
    main7_process = mp.Process(target=click_main7)
    main8_process = mp.Process(target=click_main8)
    main9_process = mp.Process(target=click_main9)
    main10_process = mp.Process(target=click_main10)
    main11_process = mp.Process(target=click_main11)
    upgrade_process = mp.Process(target=click_upgrade)

    processes = [
        main_process,
        main2_process,
        main3_process,
        main4_process,
        main5_process,
        main6_process,
        main7_process,
        main8_process,
        main9_process,
        main10_process,
        main11_process,
        upgrade_process,
    ]

    for p in processes:
        p.start()
    
    try:
        # Wait for all processes to complete (in this case, they run indefinitely)
        for p in processes:
            p.join()
    except KeyboardInterrupt:
        print("Manual interruption detected. Terminating all processes.")
        for p in processes:
            p.terminate()