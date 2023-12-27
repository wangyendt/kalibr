cmake_minimum_required(VERSION 3.10)
project(bin_generator)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV 4 REQUIRED)

add_executable(bin_generator generate_bin.cpp)
target_link_libraries(bin_generator ${OpenCV_LIBRARIES})

