# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.6

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/Jack/Documents/Projects/ACM/WorkSpace

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/Jack/Documents/Projects/ACM/WorkSpace/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/WorkSpace.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/WorkSpace.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/WorkSpace.dir/flags.make

CMakeFiles/WorkSpace.dir/main.cpp.o: CMakeFiles/WorkSpace.dir/flags.make
CMakeFiles/WorkSpace.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/Jack/Documents/Projects/ACM/WorkSpace/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/WorkSpace.dir/main.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/WorkSpace.dir/main.cpp.o -c /Users/Jack/Documents/Projects/ACM/WorkSpace/main.cpp

CMakeFiles/WorkSpace.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/WorkSpace.dir/main.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/Jack/Documents/Projects/ACM/WorkSpace/main.cpp > CMakeFiles/WorkSpace.dir/main.cpp.i

CMakeFiles/WorkSpace.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/WorkSpace.dir/main.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/Jack/Documents/Projects/ACM/WorkSpace/main.cpp -o CMakeFiles/WorkSpace.dir/main.cpp.s

CMakeFiles/WorkSpace.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/WorkSpace.dir/main.cpp.o.requires

CMakeFiles/WorkSpace.dir/main.cpp.o.provides: CMakeFiles/WorkSpace.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/WorkSpace.dir/build.make CMakeFiles/WorkSpace.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/WorkSpace.dir/main.cpp.o.provides

CMakeFiles/WorkSpace.dir/main.cpp.o.provides.build: CMakeFiles/WorkSpace.dir/main.cpp.o


# Object files for target WorkSpace
WorkSpace_OBJECTS = \
"CMakeFiles/WorkSpace.dir/main.cpp.o"

# External object files for target WorkSpace
WorkSpace_EXTERNAL_OBJECTS =

WorkSpace: CMakeFiles/WorkSpace.dir/main.cpp.o
WorkSpace: CMakeFiles/WorkSpace.dir/build.make
WorkSpace: CMakeFiles/WorkSpace.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/Jack/Documents/Projects/ACM/WorkSpace/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable WorkSpace"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/WorkSpace.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/WorkSpace.dir/build: WorkSpace

.PHONY : CMakeFiles/WorkSpace.dir/build

CMakeFiles/WorkSpace.dir/requires: CMakeFiles/WorkSpace.dir/main.cpp.o.requires

.PHONY : CMakeFiles/WorkSpace.dir/requires

CMakeFiles/WorkSpace.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/WorkSpace.dir/cmake_clean.cmake
.PHONY : CMakeFiles/WorkSpace.dir/clean

CMakeFiles/WorkSpace.dir/depend:
	cd /Users/Jack/Documents/Projects/ACM/WorkSpace/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/Jack/Documents/Projects/ACM/WorkSpace /Users/Jack/Documents/Projects/ACM/WorkSpace /Users/Jack/Documents/Projects/ACM/WorkSpace/cmake-build-debug /Users/Jack/Documents/Projects/ACM/WorkSpace/cmake-build-debug /Users/Jack/Documents/Projects/ACM/WorkSpace/cmake-build-debug/CMakeFiles/WorkSpace.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/WorkSpace.dir/depend
