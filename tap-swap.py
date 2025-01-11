from pynput.mouse import Button, Controller
import time, datetime

mouse = Controller()

iterations = 0

def tapping(mode, iter=50, clicks=10):
    global iterations
    mouse.position = (150, 350)
    pos = mouse.position
                                                                        # Цикл кликера
    for i in range (0, iter):
        mouse.click(Button.left, clicks)
        time.sleep(0.1)
                                                                        # Отключение кликера, если курсор был подвинут
        if mouse.position != pos:
            print("\n\n\nThe mouse was moved!")
            print(f"Iterations = {iterations} \n\n\n")
            return
    
    iterations += 1
    print(f"{iterations} cycle was successfully completed!")

    if (mode == 1):
        print(f"Next cycle in {(datetime.datetime.now() + datetime.timedelta(minutes=2000/60)).time()}")
        time.sleep(2000)
        tapping(mode)

    if (mode != 0):
        mouse.position = (333, 502)
        mouse.click(Button.left)

    if (mode == 2):
        time.sleep(0.2)
        mouse.position = (271, 288)
        mouse.click(Button.left)
        time.sleep(0.5)
        mouse.position = (192, 605)
        mouse.click(Button.left)
        time.sleep(0.2)
        tapping(0)
        return

    if (mode == 3):
        time.sleep(0.2)
        mouse.position = (98, 288)
        mouse.click(Button.left)
        time.sleep(0.5)
        mouse.position = (192, 605)
        mouse.click(Button.left)
        time.sleep(0.1)
        tapping(0, iter=200, clicks=20)
        return
    
    print("\n\nDone!")


def chek_pos():
    time.sleep(3)
    print(f"Current pos of cursor is {mouse.position}")


def choose_mode():
    try:
        flag = int(input(("""Choose mode: 
            1 - just farming coins (infinity)
            2 - farm coins with full tank (one iterate)
            3 - farm coins with taping guru (one iterate)
            0 - exit\n""")))
        print("\n\n\n\n")
        if (flag < 1 or flag > 3):
            return 0
        else:
            tapping(flag)
    except:
        print("Something wrong...")


choose_mode()



# chek_pos()
#                                       ЕСЛИ MiniApp ОТКАЛИБРОВАН ПО ЛЕВОМУ ВЕРХНМУ КРАЮ ЭКРАНА:
# Позиция кнопки "Boost" = (333, 502)
# Позиция "Full Tank" = (271, 288) / Позиция Taping Guru = (98, 288)
# Позиция "Get it" = (192, 605)
# Позиция центра монетки = (150, 350)           