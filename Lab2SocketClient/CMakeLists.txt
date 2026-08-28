cmake_minimum_required(VERSION 3.10)
project(Lab2SocketClient)

set(CMAKE_CXX_STANDARD 17)

add_executable(Lab2SocketClient main.cpp)
target_link_libraries(Lab2SocketClient Ws2_32)