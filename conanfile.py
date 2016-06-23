from conans import ConanFile, CMake
from conans.tools import download, unzip, replace_in_file
import os
import shutil

class RtMidiConan(ConanFile):
    name = "RtMidi"
    version = "2.1.1"
    settings = "os", "compiler", "build_type", "arch"
    # No exports necessary

    def source(self):
        zip_name = "rtmidi-%s.tar.gz" % self.version
        # this will create a hello subfolder, take it into account
        download("http://www.music.mcgill.ca/~gary/rtmidi/release/%s" % zip_name, zip_name)
        unzip(zip_name)
        # strip version from  folder name so it does not have to be used later
        shutil.move("rtmidi-%s" % self.version, "rtmidi")
        os.unlink(zip_name) 

    def build(self):
        self.run('cd rtmidi && ./configure')
        self.run('cd rtmidi && make')

    def package(self):
        self.run('echo $(pwd)')
        self.copy("*.h", dst="include", src="rtmidi")
        self.copy("*.dylib", dst="lib", src="rtmidi/.libs", keep_path=False)
        self.copy("*.a", dst="lib", src="rtmidi/.libs", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["rtmidi"]
