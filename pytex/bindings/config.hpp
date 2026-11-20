#pragma once

#ifndef PYMODULE_NAME
#define PYMODULE_NAME _core
#warning "PYMODULE_NAME not defined, defaulting to '_core'"
#endif

#ifndef PYMODULE_INIT_PREFIX
#define PYMODULE_INIT_PREFIX PyInit_
#warning "PYMODULE_INIT_PREFIX not defined, defaulting to 'PyInit_'"
#endif

#define PYMODULE_CONCAT_IMPL(a, b) a##b
#define PYMODULE_CONCAT(a, b) PYMODULE_CONCAT_IMPL(a, b)

#define PYMODULE_INIT_POINT \
    PYMODULE_CONCAT(PYMODULE_INIT_PREFIX, PYMODULE_NAME)

#undef PYMODULE_CONCAT_IMPL
#undef PYMODULE_CONCAT
