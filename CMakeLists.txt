cmake_minimum_required(VERSION 3.10)
project(AnalogueKeyboardPy)

# Set C++17 as the standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

execute_process(
    COMMAND python -c "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE PYBIND11_CMAKE_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
list(APPEND CMAKE_PREFIX_PATH "${PYBIND11_CMAKE_DIR}")

find_package(pybind11 REQUIRED)

include_directories(../Soup/soup)

add_library(AnalogueKeyboardPy SHARED
    AnalogueKeyboardPy.cpp
    # ... add dependencies ...
    ../Soup/soup/AnalogueKeyboard.cpp
    ../Soup/soup/DigitalKeyboard.cpp
    ../Soup/soup/Process.cpp
    ../Soup/soup/string.cpp
    ../Soup/soup/base.cpp
    ../Soup/soup/hwHid.cpp
    ../Soup/soup/Key.cpp
    ../Soup/soup/HidReportDescriptor.cpp
    ../Soup/soup/Reader.cpp
    ../Soup/soup/ProcessHandle.cpp
    ../Soup/soup/Range.cpp
    ../Soup/soup/Regex.cpp
    ../Soup/soup/os.cpp
    ../Soup/soup/filesystem.cpp
    ../Soup/soup/unicode.cpp
    ../Soup/soup/SharedLibrary.cpp
    ../Soup/soup/BitReader.cpp
    ../Soup/soup/Module.cpp
    ../Soup/soup/memGuard.cpp
    ../Soup/soup/Pointer.cpp
    ../Soup/soup/bitutil.cpp
    ../Soup/soup/CpuInfo.cpp
    ../Soup/soup/Pattern.cpp
    ../Soup/soup/RegexGroup.cpp
    ../Soup/soup/rand.cpp
    ../Soup/soup/LcgRng.cpp
    ../Soup/soup/memAllocator.cpp
    ../Soup/soup/MemoryBuffer.cpp
    ../Soup/soup/HardwareRng.cpp
    ../Soup/soup/alloc.cpp
)

target_link_libraries(AnalogueKeyboardPy PRIVATE pybind11::module)
