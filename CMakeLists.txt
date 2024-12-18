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

execute_process(
    COMMAND python ${CMAKE_CURRENT_SOURCE_DIR}/tool/find_dep.py
    OUTPUT_VARIABLE DEPENDENCY_LIST
    ERROR_VARIABLE SCRIPT_ERROR
    RESULT_VARIABLE SCRIPT_RESULT
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

if(NOT SCRIPT_RESULT EQUAL 0)
    message(FATAL_ERROR "Python script failed: ${SCRIPT_ERROR}")
endif()

include_directories(../Soup/soup)

add_library(AnalogueKeyboardPy
    AnalogueKeyboardPy.cpp
    ${DEPENDENCY_LIST}
)

target_link_libraries(AnalogueKeyboardPy PRIVATE pybind11::module)
