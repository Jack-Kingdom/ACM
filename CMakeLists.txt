cmake_minimum_required(VERSION 3.8)
set(CMAKE_C_STANDARD 11)
project(CodeHub)

set(C_MAIN
        WorkSpace/main.h
        WorkSpace/main.c
        )
add_executable(C_MAIN ${C_MAIN})