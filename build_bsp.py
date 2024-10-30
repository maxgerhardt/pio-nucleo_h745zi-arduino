from platformio.builder.tools.piolib import PlatformIOLibBuilder
import os
Import("env")

platform = env.PioPlatform()
FRAMEWORK_DIR = platform.get_package_dir("framework-stm32cubeh7")

class CustomLibBuilder(PlatformIOLibBuilder):
    def build(self):
        if self.env.GetBuildType() == "debug":
            self.env.ConfigureDebugFlags()
        return PlatformIOLibBuilder.build(self)

def build_custom_lib(lib_path, lib_manifest=None):
    if not os.path.isdir(lib_path):
        return
    if lib_path:
        lib_manifest = lib_manifest or {"name": os.path.basename(lib_path)}
        env.Append(EXTRA_LIB_BUILDERS=[CustomLibBuilder(env, lib_path, lib_manifest.copy())])

eval_lib = os.path.join(FRAMEWORK_DIR, "Drivers", "BSP", "STM32H747I-EVAL")
build_custom_lib(eval_lib)