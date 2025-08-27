cmake_minimum_required(VERSION 3.8)
project(sdf_lpkg)
# this is a simple cmakelists for the pkg
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)




install(
  DIRECTORY launch  world
  DESTINATION share/${PROJECT_NAME}/
) # this are the folders to launch the sdf file
ament_package()
