import pyautogui
screenshot = pyautogui.screenshot()
screenshot.save("C:/Users/towne/Code/Pepper/pepperv1/backend/paint-pyautogui.png")
print(f"Screenshot saved: {screenshot.size}")
