#include "config.hpp"

#include <Python.h>

namespace pytex::Python {
    // Function decl
}

static PyMethodDef methods[] = {
    //{"name", sig, METH_VARARGS, nullptr}
    {nullptr, nullptr, 0, nullptr}
};

static PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
#PYMODULE_NAME,
    nullptr,
    -1,
    methods
};

PyMODINIT_FUNC PYMODULE_INIT_POINT() { return PyModule_Create(&module); }
