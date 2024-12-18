## analogue-keyboard-py

Demo Python binding of [AnalogueKeyboard.cpp](https://github.com/calamity-inc/Soup/blob/senpai/soup/AnalogueKeyboard.cpp)

See [here](https://github.com/AnalogSense/universal-analog-plugin/blob/5ace6b40f2fe8441fc003ac9b777518b4e20116a/README.md) for a list of supported keyboards (not tested)

Try it with `demo.py`

_Disclaimer: I'm not familiar with C++ and was largely informed by LLM._

### Build

`AnalogueKeyboardPy.pyd` was built for Python3.12 on Win11 with Visual Studio build tools

```powershell
cd build
cmake .. -G "Visual Studio 17 2022" -A x64 -T v143,host=x64
cmake --build . --config Release
copy Release/AnalogueKeyboardPy.dll ../AnalogueKeyboardPy.pyd
```

### Reference

Reading analog values from keyboard

https://github.com/calamity-inc/Soup/blob/senpai/soup/AnalogueKeyboard.cpp

Triggering MIDI events from analog values

https://github.com/WootingKb/wooting-analog-midi/blob/develop/wooting-analog-midi-core/src/lib.rs

![](https://count.lnfinite.space/repo/analogue-keyboard-py.svg?plus=1)