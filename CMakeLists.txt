cmake_minimum_required(VERSION 3.12.2)
project(mc_proto_project C)

set(CMAKE_C_STANDARD 23)
set(CMAKE_C_STANDARD_REQUIRED TRUE)

add_library(mc_proto src/universal_types.c)
target_include_directories(mc_proto PUBLIC include/)
