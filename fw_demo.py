import multiprocessing
import multiprocessing.process
import pyautogui as gui
from PIL import ImageGrab


def click_cookie_task():
    x = 841
    y = 380

    try:
        while True:
            gui.click(x, y)
    except gui.FailSafeException:
        print(f"Fail-safe triggered at location: {x}, {y}")
        return


def buy_task():
    left = 1177
    top = 468
    right = 1439
    bottom = 899

    x = 1376

    try:
        while True:
            screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
            pixels = screenshot.load()

            for y in range(screenshot.height):
                px = pixels[x-left, y]
                r = px[0]  # 0 ~ 255
                g = px[1]
                b = px[2]
                if r > 130 and g > 130 and b > 130:
                    gui.click(x, y + top)
    except gui.FailSafeException:
        print(f"Fail-safe triggered at location: {x}, {y}")
        return


def main():
    cookie_click_process = multiprocessing.Process(target=click_cookie_task)
    buy_item_process = multiprocessing.Process(target=buy_task)

    processes = [
        cookie_click_process,
        buy_item_process,
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


if __name__ == "__main__":
    main()