from time import sleep
from AnalogueKeyboardPy import AnalogueKeyboard

kb = AnalogueKeyboard()

if kb.isConnected():
    print("Keyboard connected:", kb.getName())
    
    try:
        while True:
            active_keys = kb.getActiveKeys()
            if active_keys:
                print(active_keys)
            sleep(0.001)
    except RuntimeError as e:
        print("Error:", e)
else:
    print("No analogue keyboard detected")