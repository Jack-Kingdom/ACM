cmake_minimum_required(VERSION 3.6)
project(ACM_WorkSpace)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(ACM_WorkSpace ${SOURCE_FILES})