#include <AnalogueKeyboard.hpp>
// in include directory
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
// For automatic conversion of std::vector and std::string

namespace py = pybind11;

class AnalogueKeyboardPy
{
public:
    AnalogueKeyboardPy() : analogue_kbd(nullptr) {}

    ~AnalogueKeyboardPy() = default; // Let pybind11 handle the cleanup

    bool isConnected()
    {
        std::vector<soup::AnalogueKeyboard> analogue_kbds = soup::AnalogueKeyboard::getAll();
        if (!analogue_kbds.empty())
        {
            analogue_kbd = std::make_unique<soup::AnalogueKeyboard>(std::move(analogue_kbds.at(0)));
            keyboard_name = analogue_kbd->name;
            return true;
        }
        return false;
    }

    std::vector<std::pair<int, float>> getActiveKeys()
    {
        if (!analogue_kbd)
        {
            throw std::runtime_error("No analogue keyboard detected.");
        }

        std::vector<std::pair<int, float>> active_keys;
        auto keys = analogue_kbd->getActiveKeys();
        for (const auto &key : keys)
        {
            active_keys.emplace_back(key.getSoupKey(), key.getFValue());
        }
        return active_keys;
    }

    std::string getName() const
    {
        return keyboard_name;
    }

private:
    std::unique_ptr<soup::AnalogueKeyboard> analogue_kbd;
    std::string keyboard_name = "None";
};

PYBIND11_MODULE(AnalogueKeyboardPy, m)
{
    py::class_<AnalogueKeyboardPy>(m, "AnalogueKeyboard")
        .def(py::init<>())
        .def("isConnected", &AnalogueKeyboardPy::isConnected)
        .def("getActiveKeys", &AnalogueKeyboardPy::getActiveKeys)
        .def("getName", &AnalogueKeyboardPy::getName);
}