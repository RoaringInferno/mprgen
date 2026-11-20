cmake_minimum_required(VERSION 3.18)

project(pytex LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS ON)

set(PY_LIBNAME pytex)
set(PY_MODULENAME ${PY_LIBNAME}_core)
set(CXX_LIBNAME cpptex)

add_library(${CXX_LIBNAME} STATIC
)
target_include_directories(${CXX_LIBNAME} PUBLIC cpp/include/cpptex)
set_target_properties(${CXX_LIBNAME} PROPERTIES
    POSITION_INDEPENDENT_CODE ON
)

find_package(Python3 REQUIRED COMPONENTS
    Interpreter
    Development.Module
)

Python3_add_library(${PY_MODULENAME} MODULE WITH_SOABI
    bindings/module.cpp
)
target_link_libraries(${PY_MODULENAME} PRIVATE ${CXX_LIBNAME})
target_include_directories(${PY_MODULENAME} PRIVATE bindings)

target_compile_definitions(${PY_MODULENAME} PRIVATE
)

install(TARGETS ${PY_MODULENAME}
    LIBRARY DESTINATION ${PROJECT_NAME}
    RUNTIME DESTINATION ${PROJECT_NAME}
)
