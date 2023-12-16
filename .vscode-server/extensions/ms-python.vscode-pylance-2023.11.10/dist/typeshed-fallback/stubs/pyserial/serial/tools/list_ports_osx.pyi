import ctypes
import sys

from serial.tools.list_ports_common import ListPortInfo

if sys.platform == "darwin":
    iokit: ctypes.CDLL
    cf: ctypes.CDLL
    kIOMasterPortDefault: int
    kCFAllocatorDefault: ctypes.c_void_p
    kCFStringEncodingMacRoman: int
    kCFStringEncodingUTF8: int
    kUSBVendorString: str
    kUSBSerialNumberString: str
    io_name_size: int
    KERN_SUCCESS: int
    kern_return_t = ctypes.c_int
    kCFNumberSInt8Type: int
    kCFNumberSInt16Type: int
    kCFNumberSInt32Type: int
    kCFNumberSInt64Type: int

    def get_string_property(device_type: ctypes._CData, property: str) -> str | None: ...
    def get_int_property(device_type: ctypes._CData, property: str, cf_number_type: int) -> int | None: ...
    def IORegistryEntryGetName(device: ctypes._CData) -> str | None: ...
    def IOObjectGetClass(device: ctypes._CData) -> bytes: ...
    def GetParentDeviceByType(device: ctypes._CData, parent_type: str) -> ctypes._CData | None: ...
    def GetIOServicesByType(service_type: str) -> list[ctypes._CData]: ...
    def location_to_string(locationID: int) -> str: ...

    # `SuitableSerialInterface` has required attributes `id: int` and `name: str` but they are not defined on the class
    class SuitableSerialInterface: ...

    def scan_interfaces() -> list[SuitableSerialInterface]: ...
    def search_for_locationID_in_interfaces(serial_interfaces: list[SuitableSerialInterface], locationID: int) -> str | None: ...
    def comports(include_links: bool = ...) -> list[ListPortInfo]: ...
