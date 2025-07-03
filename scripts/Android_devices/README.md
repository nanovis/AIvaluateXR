# **Android Devices** 
For Android devices, the evaluation can be done via **Android Debug Bridge (ADB)**.
## Prepare Models
You can download **gguf models** on huggingface. For example, you can download 
## Build Llama.cpp
By following the command below, you can build Llama.cpp specified by different devices. Here we only provide the CLI about the Android devices mentioned in our paper, referencing [Build on Android](https://github.com/ggml-org/llama.cpp/blob/master/docs/android.md). You can modify the command for your device. 
### 1. Get llama.cpp
```
git clone https://github.com/ggml-org/llama.cpp.git
cd ./llama.cpp
```
### 2. Cross-compile using Android NDK
#### For Magic Leap 2
```
$ cmake \ 
  -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
  -DANDROID_ABI=x86_64 \
  -DANDROID_PLATFORM=latest \
  -DCMAKE_C_FLAGS="-march=znver2 -mtune=znver2 -O3" \
  -DCMAKE_CXX_FLAGS="-march=znver2 -mtune=znver2 -O3" \
  -DGGML_OPENMP=OFF \
  -DGGML_LLAMAFILE=OFF \
  -B build-ml2
```
#### For Meta Quest 3
```
$ cmake \
  -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
  -DANDROID_ABI=arm64-v8a \
  -DANDROID_PLATFORM=latest \
  -DCMAKE_C_FLAGS="-march=armv8.7a" \
  -DCMAKE_CXX_FLAGS="-march=armv8.7a" \
  -DGGML_OPENMP=OFF \
  -DGGML_LLAMAFILE=OFF \
  -B build-android-mq3
```
#### For Vivo X100 Pro
```
$ cmake \
  -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
  -DANDROID_ABI=arm64-v8a \
  -DANDROID_PLATFORM=latest \
  -DCMAKE_C_FLAGS="-mtune=cortex-x4+cortex-a720 -O3" \
  -DCMAKE_CXX_FLAGS="-mtune=cortex-x4+cortex-a720 -O3" \
  -DGGML_OPENMP=OFF \
  -DGGML_LLAMAFILE=OFF \
  -B build-android-vivo
```
### 3. Push files to devices
Copy the bin and lib to devices
```
adb shell
cd /data/local/tmp
mkdir llama-cpp
exit

adb push ./build-android/bin /data/local/tmp/llama-cpp/
```
<!-- 
### 4. Check if executable
Check if the bin files executable on devices via ADB.
```
adb shell
cd /data/local/tmp/
```
-->
