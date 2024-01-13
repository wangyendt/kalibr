cmake_minimum_required(VERSION 3.0.2)
project(common_include)

find_package(catkin REQUIRED)

catkin_package(
  INCLUDE_DIRS .
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  .
)
