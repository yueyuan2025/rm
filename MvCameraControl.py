from ctypes import *
import os

# 加载系统里已经能用的库
lib = cdll.LoadLibrary("/lib/libMVSDK.so")

# 类型定义
MV_OK = 0
MV_GIGE_DEVICE = 1
MV_USB_DEVICE = 2

class MV_CC_DEVICE_INFO(Structure):
    _fields_ = [
        ("nDeviceType", c_uint),
        ("chUserDefinedName", c_ubyte * 64),
    ]

class MV_CC_DEVICE_INFO_LIST(Structure):
    _fields_ = [
        ("nDeviceNum", c_uint),
        ("pDeviceInfo", POINTER(MV_CC_DEVICE_INFO) * 64),
    ]

class MV_FRAME_OUT_INFO_EX(Structure):
    _fields_ = [
        ("nWidth", c_uint),
        ("nHeight", c_uint),
        ("nFrameNum", c_uint),
    ]

# 函数声明
MV_CC_EnumDevices = lib.MV_CC_EnumDevices
MV_CC_EnumDevices.argtypes = [c_uint, POINTER(MV_CC_DEVICE_INFO_LIST)]

MV_CC_CreateHandle = lib.MV_CC_CreateHandle
MV_CC_OpenDevice = lib.MV_CC_OpenDevice
MV_CC_SetEnumValue = lib.MV_CC_SetEnumValue
MV_CC_StartGrabbing = lib.MV_CC_StartGrabbing
MV_CC_GetOneFrameTimeout = lib.MV_CC_GetOneFrameTimeout
MV_CC_StopGrabbing = lib.MV_CC_StopGrabbing
MV_CC_CloseDevice = lib.MV_CC_CloseDevice
MV_CC_DestroyHandle = lib.MV_CC_DestroyHandle
