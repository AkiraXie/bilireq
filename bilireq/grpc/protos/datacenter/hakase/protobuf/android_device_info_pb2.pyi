"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class AndroidDeviceInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class PropsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    @typing_extensions.final
    class SysEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    SDKVER_FIELD_NUMBER: builtins.int
    APP_ID_FIELD_NUMBER: builtins.int
    APP_VERSION_FIELD_NUMBER: builtins.int
    APP_VERSION_CODE_FIELD_NUMBER: builtins.int
    MID_FIELD_NUMBER: builtins.int
    CHID_FIELD_NUMBER: builtins.int
    FTS_FIELD_NUMBER: builtins.int
    BUVID_LOCAL_FIELD_NUMBER: builtins.int
    FIRST_FIELD_NUMBER: builtins.int
    PROC_FIELD_NUMBER: builtins.int
    NET_FIELD_NUMBER: builtins.int
    BAND_FIELD_NUMBER: builtins.int
    OSVER_FIELD_NUMBER: builtins.int
    T_FIELD_NUMBER: builtins.int
    CPU_COUNT_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    BRAND_FIELD_NUMBER: builtins.int
    SCREEN_FIELD_NUMBER: builtins.int
    CPU_MODEL_FIELD_NUMBER: builtins.int
    BTMAC_FIELD_NUMBER: builtins.int
    BOOT_FIELD_NUMBER: builtins.int
    EMU_FIELD_NUMBER: builtins.int
    OID_FIELD_NUMBER: builtins.int
    NETWORK_FIELD_NUMBER: builtins.int
    MEM_FIELD_NUMBER: builtins.int
    SENSOR_FIELD_NUMBER: builtins.int
    CPU_FREQ_FIELD_NUMBER: builtins.int
    CPU_VENDOR_FIELD_NUMBER: builtins.int
    SIM_FIELD_NUMBER: builtins.int
    BRIGHTNESS_FIELD_NUMBER: builtins.int
    PROPS_FIELD_NUMBER: builtins.int
    SYS_FIELD_NUMBER: builtins.int
    WIFIMAC_FIELD_NUMBER: builtins.int
    ADID_FIELD_NUMBER: builtins.int
    OS_FIELD_NUMBER: builtins.int
    IMEI_FIELD_NUMBER: builtins.int
    CELL_FIELD_NUMBER: builtins.int
    IMSI_FIELD_NUMBER: builtins.int
    ICCID_FIELD_NUMBER: builtins.int
    CAMCNT_FIELD_NUMBER: builtins.int
    CAMPX_FIELD_NUMBER: builtins.int
    TOTAL_SPACE_FIELD_NUMBER: builtins.int
    AXPOSED_FIELD_NUMBER: builtins.int
    MAPS_FIELD_NUMBER: builtins.int
    FILES_FIELD_NUMBER: builtins.int
    VIRTUAL_FIELD_NUMBER: builtins.int
    VIRTUALPROC_FIELD_NUMBER: builtins.int
    GADID_FIELD_NUMBER: builtins.int
    GLIMIT_FIELD_NUMBER: builtins.int
    APPS_FIELD_NUMBER: builtins.int
    GUID_FIELD_NUMBER: builtins.int
    UID_FIELD_NUMBER: builtins.int
    ROOT_FIELD_NUMBER: builtins.int
    CAMZOOM_FIELD_NUMBER: builtins.int
    CAMLIGHT_FIELD_NUMBER: builtins.int
    OAID_FIELD_NUMBER: builtins.int
    UDID_FIELD_NUMBER: builtins.int
    VAID_FIELD_NUMBER: builtins.int
    AAID_FIELD_NUMBER: builtins.int
    ANDROIDAPP20_FIELD_NUMBER: builtins.int
    ANDROIDAPPCNT_FIELD_NUMBER: builtins.int
    ANDROIDSYSAPP20_FIELD_NUMBER: builtins.int
    BATTERY_FIELD_NUMBER: builtins.int
    BATTERY_STATE_FIELD_NUMBER: builtins.int
    BSSID_FIELD_NUMBER: builtins.int
    BUILD_ID_FIELD_NUMBER: builtins.int
    COUNTRY_ISO_FIELD_NUMBER: builtins.int
    FREE_MEMORY_FIELD_NUMBER: builtins.int
    FSTORAGE_FIELD_NUMBER: builtins.int
    KERNEL_VERSION_FIELD_NUMBER: builtins.int
    LANGUAGES_FIELD_NUMBER: builtins.int
    MAC_FIELD_NUMBER: builtins.int
    SSID_FIELD_NUMBER: builtins.int
    SYSTEMVOLUME_FIELD_NUMBER: builtins.int
    WIFIMACLIST_FIELD_NUMBER: builtins.int
    MEMORY_FIELD_NUMBER: builtins.int
    STR_BATTERY_FIELD_NUMBER: builtins.int
    IS_ROOT_FIELD_NUMBER: builtins.int
    STR_BRIGHTNESS_FIELD_NUMBER: builtins.int
    STR_APP_ID_FIELD_NUMBER: builtins.int
    IP_FIELD_NUMBER: builtins.int
    USER_AGENT_FIELD_NUMBER: builtins.int
    LIGHT_INTENSITY_FIELD_NUMBER: builtins.int
    DEVICE_ANGLE_FIELD_NUMBER: builtins.int
    GPS_SENSOR_FIELD_NUMBER: builtins.int
    SPEED_SENSOR_FIELD_NUMBER: builtins.int
    LINEAR_SPEED_SENSOR_FIELD_NUMBER: builtins.int
    GYROSCOPE_SENSOR_FIELD_NUMBER: builtins.int
    BIOMETRIC_FIELD_NUMBER: builtins.int
    BIOMETRICS_FIELD_NUMBER: builtins.int
    LAST_DUMP_TS_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    COUNTRY_FIELD_NUMBER: builtins.int
    CITY_FIELD_NUMBER: builtins.int
    DATA_ACTIVITY_STATE_FIELD_NUMBER: builtins.int
    DATA_CONNECT_STATE_FIELD_NUMBER: builtins.int
    DATA_NETWORK_TYPE_FIELD_NUMBER: builtins.int
    VOICE_NETWORK_TYPE_FIELD_NUMBER: builtins.int
    VOICE_SERVICE_STATE_FIELD_NUMBER: builtins.int
    USB_CONNECTED_FIELD_NUMBER: builtins.int
    ADB_ENABLED_FIELD_NUMBER: builtins.int
    UI_VERSION_FIELD_NUMBER: builtins.int
    ACCESSIBILITY_SERVICE_FIELD_NUMBER: builtins.int
    SENSORS_INFO_FIELD_NUMBER: builtins.int
    DRMID_FIELD_NUMBER: builtins.int
    BATTERY_PRESENT_FIELD_NUMBER: builtins.int
    BATTERY_TECHNOLOGY_FIELD_NUMBER: builtins.int
    BATTERY_TEMPERATURE_FIELD_NUMBER: builtins.int
    BATTERY_VOLTAGE_FIELD_NUMBER: builtins.int
    BATTERY_PLUGGED_FIELD_NUMBER: builtins.int
    BATTERY_HEALTH_FIELD_NUMBER: builtins.int
    CPU_ABI_LIST_FIELD_NUMBER: builtins.int
    CPU_ABI_LIBC_FIELD_NUMBER: builtins.int
    CPU_ABI_LIBC64_FIELD_NUMBER: builtins.int
    CPU_PROCESSOR_FIELD_NUMBER: builtins.int
    CPU_MODEL_NAME_FIELD_NUMBER: builtins.int
    CPU_HARDWARE_FIELD_NUMBER: builtins.int
    CPU_FEATURES_FIELD_NUMBER: builtins.int
    sdkver: builtins.str
    """?"""
    app_id: builtins.str
    """产品id
    粉 白 蓝 直播姬 HD 海外 OTT 漫画 TV野版 小视频 网易漫画 网易漫画 网易漫画HD 国际版 东南亚版
    1  2  3    4    5   6    7   8     9     10      11       12       13       14       30
    """
    app_version: builtins.str
    """版本号, 如 "7.39.0" """
    app_version_code: builtins.str
    """版本号, 如 "7390300" """
    mid: builtins.str
    """用户 mid"""
    chid: builtins.str
    """渠道号, 如 "master" """
    fts: builtins.int
    """APP 首次安装启动时间戳"""
    buvid_local: builtins.str
    """此处实际为 fp, 但不知为何命名为 buvid_local"""
    first: builtins.int
    """留空为 0"""
    proc: builtins.str
    """进程名, 如 "tv.danmaku.bili" """
    net: builtins.str
    """网络信息, 为一数组直接 toString() 的结果
    如 \"\"\"["dummy0,fe80::18d8:6ff:fe46:c2ba%dummy0,", "wlan0,fe80::a0f4:6dff:fea8:2d37%wlan0,192.168.1.5,", "lo,::1,127.0.0.1,", "rmnet_ims00,fe80::5a02:3ff:fe04:512%rmnet_ims00,2409:815a:7c38:cee1:1773:d0b9:d163:b023,"]\"\"\"
    """
    band: builtins.str
    """手机无线电固件版本号(`Build.getRadioVersion()`). 如 `21C20B686S000C000,21C20B686S000C000`."""
    osver: builtins.str
    """OS 版本号, 如 "12" """
    t: builtins.int
    """当前毫秒时间戳"""
    cpu_count: builtins.int
    """CPU 逻辑核心计数"""
    model: builtins.str
    """手机 Model, 如 "NOH-AN01" """
    brand: builtins.str
    """手机品牌, 如 "HUAWEI" """
    screen: builtins.str
    """屏幕信息, 如 "1288,2646,560", 即 "{width},{height},{pixel}" """
    cpu_model: builtins.str
    """CPU 型号, 留空或根据实际情况确定"""
    btmac: builtins.str
    """蓝牙 MAC, 留空或根据实际情况确定"""
    boot: builtins.int
    """Linux 内核 bootid"""
    emu: builtins.str
    """模拟器(?), 如 "000" """
    oid: builtins.str
    """移动网络 MCC MNC, 如中国移动为 46007"""
    network: builtins.str
    """当前网络类型, 如 "WIFI", 见 bilibili.metadata.network.NetworkType"""
    mem: builtins.int
    """运行内存(Byte)"""
    sensor: builtins.str
    """传感器信息, 为一数组直接 toString() 的结果
    如 \"\"\"["accelerometer-icm20690,invensense", "akm-akm09918,akm", "orientation,huawei", "als-tcs3718,ams", "proximity-tcs3718,ams", "gyroscope-icm20690,invensense", "gravity,huawei", "linear Acceleration,huawei", "rotation Vector,huawei", "airpress-bmp280,bosch", "HALL sensor,huawei", "uncalibrated Magnetic Field,Asahi Kasei Microdevices", "game Rotation Vector,huawei", "uncalibrated Gyroscope,STMicroelectronics", "significant Motion,huawei", "step Detector,huawei", "step counter,huawei", "geomagnetic Rotation Vector,huawei", "phonecall sensor,huawei", "RPC sensor,huawei", "agt,huawei", "color sensor,huawei", "uncalibrated Accelerometer,huawei", "drop sensor,huawei"]\"\"\"
    """
    cpu_freq: builtins.int
    """CPU 频率, 如 2045000"""
    cpu_vendor: builtins.str
    """CPU 架构, 如 "ARM" """
    sim: builtins.str
    """?"""
    brightness: builtins.int
    """光照传感器数值"""
    @property
    def props(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Android Build.prop 信息, key 包括 net.hostname, ro.boot.hardware, etc.
        具体 key-value 需要技术手段自行确定
        """
    @property
    def sys(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """系统信息, key 包括 product, cpu_model_name, display, cpu_abi_list, etc.
        具体 key-value 需要技术手段自行确定
        """
    wifimac: builtins.str
    """Wifi MAC, 一般无法获取, 留空"""
    adid: builtins.str
    """Android ID"""
    os: builtins.str
    """OS 名称, 如 "android" """
    imei: builtins.str
    """IMEI, 一般无法获取, 留空"""
    cell: builtins.str
    """?, 留空"""
    imsi: builtins.str
    """IMSI, 一般无法获取, 留空"""
    iccid: builtins.str
    """ICCID, 一般无法获取, 留空"""
    camcnt: builtins.int
    """摄像头数量, 留空"""
    campx: builtins.str
    """摄像头像素, 留空"""
    total_space: builtins.int
    """手机内置存储空间(Byte)"""
    axposed: builtins.str
    """?, 例如 "false" """
    maps: builtins.str
    """?, 留空"""
    files: builtins.str
    """如: "/data/user/0/tv.danmaku.bili/files" """
    virtual: builtins.str
    """是否为虚拟化(?), 如 "0" """
    virtualproc: builtins.str
    """虚拟进程, 如 "[]" """
    gadid: builtins.str
    """?, 留空"""
    glimit: builtins.str
    """?, 留空"""
    apps: builtins.str
    """设备安装的 APP 列表, 如 "[]" """
    guid: builtins.str
    """客户端 GUID"""
    uid: builtins.str
    """?, 区分于用户 UID"""
    root: builtins.int
    """?, 留空"""
    camzoom: builtins.str
    """摄像头放大倍数(?), 留空"""
    camlight: builtins.str
    """摄像头闪光灯(?), 留空"""
    oaid: builtins.str
    """OAID 匿名设备标识符, 参见 T/TAF 095-2021 安卓系统补充设备标识技术规范, 默认 "00000000-0000-0000-0000-000000000000" """
    udid: builtins.str
    """UDID 设备唯一标识符, 参见 T/TAF 095-2021 安卓系统补充设备标识技术规范, 可留空"""
    vaid: builtins.str
    """VAID 开发者匿名设备标识符, 参见 T/TAF 095-2021 安卓系统补充设备标识技术规范, 可留空"""
    aaid: builtins.str
    """AAID, 应用匿名设备标识符, 参见 T/TAF 095-2021 安卓系统补充设备标识技术规范, 可留空"""
    androidapp20: builtins.str
    """?, 设置为 "[]" """
    androidappcnt: builtins.int
    """?, 留空"""
    androidsysapp20: builtins.str
    """?, 设置为 "[]" """
    battery: builtins.int
    """当前剩余电量, 如 100"""
    battery_state: builtins.str
    """Android 监听电量状态, 如 "BATTERY_STATUS_DISCHARGING" """
    bssid: builtins.str
    """Wifi BSSID, 一般无法获取, 留空"""
    build_id: builtins.str
    """?, 如 "NOH-AN01 4.0.0.102(DEVC00E100R7P5)" """
    country_iso: builtins.str
    """ISO 国家代码, 如 "CN" """
    free_memory: builtins.int
    """可用运行内存(Byte)"""
    fstorage: builtins.str
    """可用内置存储空间(Byte)"""
    kernel_version: builtins.str
    """Linux kernel version"""
    languages: builtins.str
    """语言, 如 "zh" """
    mac: builtins.str
    """ Wifi 网卡 MAC(?), 留空"""
    ssid: builtins.str
    """当前连接 Wifi 的 SSID, 留空"""
    systemvolume: builtins.int
    """?, 留空"""
    wifimaclist: builtins.str
    """ Wifi 网卡 MAC 列表(?), 留空"""
    memory: builtins.int
    """运行内存(Byte)"""
    str_battery: builtins.str
    """当前剩余电量, 如 "100" """
    is_root: builtins.bool
    """设备是否 Root(?), 留空"""
    str_brightness: builtins.str
    """光照传感器数值字符串"""
    str_app_id: builtins.str
    """产品id, 见 2"""
    ip: builtins.str
    """当前 IP(?), 留空"""
    user_agent: builtins.str
    """留空即可"""
    light_intensity: builtins.str
    """?, 如: "1.25" """
    @property
    def device_angle(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]:
        """设备 xyz 方向角度"""
    gps_sensor: builtins.int
    """GPS 传感器数量(或者是否有 GPS 传感器?), 如 "1" """
    speed_sensor: builtins.int
    """速度传感器数量(或者是否有速度传感器?), 如 "1" """
    linear_speed_sensor: builtins.int
    """线性加速度传感器数量(或者是否有线性加速度传感器?), 如 "1" """
    gyroscope_sensor: builtins.int
    """ 陀螺仪传感器数量(或者是否有陀螺仪传感器?), 如 "1" """
    biometric: builtins.int
    """生物识别传感器数量(或者是否有生物识别传感器?), 如 "1" """
    @property
    def biometrics(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """生物识别传感器类型(?), 如 "touchid" """
    last_dump_ts: builtins.int
    """上次 Crash Dump 时的毫秒时间戳"""
    location: builtins.str
    """留空即可"""
    country: builtins.str
    """留空即可"""
    city: builtins.str
    """留空即可"""
    data_activity_state: builtins.int
    """?, 默认为 0"""
    data_connect_state: builtins.int
    """?, 默认为 0"""
    data_network_type: builtins.int
    """?, 默认为 0"""
    voice_network_type: builtins.int
    """?, 默认为 0"""
    voice_service_state: builtins.int
    """?, 默认为 0"""
    usb_connected: builtins.int
    """USB 是否连接, 启用为 "1", 否则为 "0" """
    adb_enabled: builtins.int
    """ADB 是否启用, 启用为 "1", 否则为 "0" """
    ui_version: builtins.str
    """系统 UI 软件版本(?), 如 "14.0.0" """
    @property
    def accessibility_service(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """辅助服务"""
    @property
    def sensors_info(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SensorInfo]:
        """传感器信息(需要和前面的 sensor 对应)"""
    drmid: builtins.str
    """DrmId"""
    battery_present: builtins.bool
    """是否存在电池"""
    battery_technology: builtins.str
    """电池技术, 如 "Li-poly" """
    battery_temperature: builtins.int
    """电池温度(m℃)"""
    battery_voltage: builtins.int
    """电池电压(mV)"""
    battery_plugged: builtins.int
    """电池是否被拔开(?), 可以为 0"""
    battery_health: builtins.int
    """电池健康, 如 2"""
    @property
    def cpu_abi_list(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """留空即可"""
    cpu_abi_libc: builtins.str
    """留空即可"""
    cpu_abi_libc64: builtins.str
    """留空即可"""
    cpu_processor: builtins.str
    """留空即可"""
    cpu_model_name: builtins.str
    """留空即可"""
    cpu_hardware: builtins.str
    """留空即可"""
    cpu_features: builtins.str
    """留空即可"""
    def __init__(
        self,
        *,
        sdkver: builtins.str = ...,
        app_id: builtins.str = ...,
        app_version: builtins.str = ...,
        app_version_code: builtins.str = ...,
        mid: builtins.str = ...,
        chid: builtins.str = ...,
        fts: builtins.int = ...,
        buvid_local: builtins.str = ...,
        first: builtins.int = ...,
        proc: builtins.str = ...,
        net: builtins.str = ...,
        band: builtins.str = ...,
        osver: builtins.str = ...,
        t: builtins.int = ...,
        cpu_count: builtins.int = ...,
        model: builtins.str = ...,
        brand: builtins.str = ...,
        screen: builtins.str = ...,
        cpu_model: builtins.str = ...,
        btmac: builtins.str = ...,
        boot: builtins.int = ...,
        emu: builtins.str = ...,
        oid: builtins.str = ...,
        network: builtins.str = ...,
        mem: builtins.int = ...,
        sensor: builtins.str = ...,
        cpu_freq: builtins.int = ...,
        cpu_vendor: builtins.str = ...,
        sim: builtins.str = ...,
        brightness: builtins.int = ...,
        props: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        sys: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        wifimac: builtins.str = ...,
        adid: builtins.str = ...,
        os: builtins.str = ...,
        imei: builtins.str = ...,
        cell: builtins.str = ...,
        imsi: builtins.str = ...,
        iccid: builtins.str = ...,
        camcnt: builtins.int = ...,
        campx: builtins.str = ...,
        total_space: builtins.int = ...,
        axposed: builtins.str = ...,
        maps: builtins.str = ...,
        files: builtins.str = ...,
        virtual: builtins.str = ...,
        virtualproc: builtins.str = ...,
        gadid: builtins.str = ...,
        glimit: builtins.str = ...,
        apps: builtins.str = ...,
        guid: builtins.str = ...,
        uid: builtins.str = ...,
        root: builtins.int = ...,
        camzoom: builtins.str = ...,
        camlight: builtins.str = ...,
        oaid: builtins.str = ...,
        udid: builtins.str = ...,
        vaid: builtins.str = ...,
        aaid: builtins.str = ...,
        androidapp20: builtins.str = ...,
        androidappcnt: builtins.int = ...,
        androidsysapp20: builtins.str = ...,
        battery: builtins.int = ...,
        battery_state: builtins.str = ...,
        bssid: builtins.str = ...,
        build_id: builtins.str = ...,
        country_iso: builtins.str = ...,
        free_memory: builtins.int = ...,
        fstorage: builtins.str = ...,
        kernel_version: builtins.str = ...,
        languages: builtins.str = ...,
        mac: builtins.str = ...,
        ssid: builtins.str = ...,
        systemvolume: builtins.int = ...,
        wifimaclist: builtins.str = ...,
        memory: builtins.int = ...,
        str_battery: builtins.str = ...,
        is_root: builtins.bool = ...,
        str_brightness: builtins.str = ...,
        str_app_id: builtins.str = ...,
        ip: builtins.str = ...,
        user_agent: builtins.str = ...,
        light_intensity: builtins.str = ...,
        device_angle: collections.abc.Iterable[builtins.float] | None = ...,
        gps_sensor: builtins.int = ...,
        speed_sensor: builtins.int = ...,
        linear_speed_sensor: builtins.int = ...,
        gyroscope_sensor: builtins.int = ...,
        biometric: builtins.int = ...,
        biometrics: collections.abc.Iterable[builtins.str] | None = ...,
        last_dump_ts: builtins.int = ...,
        location: builtins.str = ...,
        country: builtins.str = ...,
        city: builtins.str = ...,
        data_activity_state: builtins.int = ...,
        data_connect_state: builtins.int = ...,
        data_network_type: builtins.int = ...,
        voice_network_type: builtins.int = ...,
        voice_service_state: builtins.int = ...,
        usb_connected: builtins.int = ...,
        adb_enabled: builtins.int = ...,
        ui_version: builtins.str = ...,
        accessibility_service: collections.abc.Iterable[builtins.str] | None = ...,
        sensors_info: collections.abc.Iterable[global___SensorInfo] | None = ...,
        drmid: builtins.str = ...,
        battery_present: builtins.bool = ...,
        battery_technology: builtins.str = ...,
        battery_temperature: builtins.int = ...,
        battery_voltage: builtins.int = ...,
        battery_plugged: builtins.int = ...,
        battery_health: builtins.int = ...,
        cpu_abi_list: collections.abc.Iterable[builtins.str] | None = ...,
        cpu_abi_libc: builtins.str = ...,
        cpu_abi_libc64: builtins.str = ...,
        cpu_processor: builtins.str = ...,
        cpu_model_name: builtins.str = ...,
        cpu_hardware: builtins.str = ...,
        cpu_features: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["aaid", b"aaid", "accessibility_service", b"accessibility_service", "adb_enabled", b"adb_enabled", "adid", b"adid", "androidapp20", b"androidapp20", "androidappcnt", b"androidappcnt", "androidsysapp20", b"androidsysapp20", "app_id", b"app_id", "app_version", b"app_version", "app_version_code", b"app_version_code", "apps", b"apps", "axposed", b"axposed", "band", b"band", "battery", b"battery", "battery_health", b"battery_health", "battery_plugged", b"battery_plugged", "battery_present", b"battery_present", "battery_state", b"battery_state", "battery_technology", b"battery_technology", "battery_temperature", b"battery_temperature", "battery_voltage", b"battery_voltage", "biometric", b"biometric", "biometrics", b"biometrics", "boot", b"boot", "brand", b"brand", "brightness", b"brightness", "bssid", b"bssid", "btmac", b"btmac", "build_id", b"build_id", "buvid_local", b"buvid_local", "camcnt", b"camcnt", "camlight", b"camlight", "campx", b"campx", "camzoom", b"camzoom", "cell", b"cell", "chid", b"chid", "city", b"city", "country", b"country", "country_iso", b"country_iso", "cpu_abi_libc", b"cpu_abi_libc", "cpu_abi_libc64", b"cpu_abi_libc64", "cpu_abi_list", b"cpu_abi_list", "cpu_count", b"cpu_count", "cpu_features", b"cpu_features", "cpu_freq", b"cpu_freq", "cpu_hardware", b"cpu_hardware", "cpu_model", b"cpu_model", "cpu_model_name", b"cpu_model_name", "cpu_processor", b"cpu_processor", "cpu_vendor", b"cpu_vendor", "data_activity_state", b"data_activity_state", "data_connect_state", b"data_connect_state", "data_network_type", b"data_network_type", "device_angle", b"device_angle", "drmid", b"drmid", "emu", b"emu", "files", b"files", "first", b"first", "free_memory", b"free_memory", "fstorage", b"fstorage", "fts", b"fts", "gadid", b"gadid", "glimit", b"glimit", "gps_sensor", b"gps_sensor", "guid", b"guid", "gyroscope_sensor", b"gyroscope_sensor", "iccid", b"iccid", "imei", b"imei", "imsi", b"imsi", "ip", b"ip", "is_root", b"is_root", "kernel_version", b"kernel_version", "languages", b"languages", "last_dump_ts", b"last_dump_ts", "light_intensity", b"light_intensity", "linear_speed_sensor", b"linear_speed_sensor", "location", b"location", "mac", b"mac", "maps", b"maps", "mem", b"mem", "memory", b"memory", "mid", b"mid", "model", b"model", "net", b"net", "network", b"network", "oaid", b"oaid", "oid", b"oid", "os", b"os", "osver", b"osver", "proc", b"proc", "props", b"props", "root", b"root", "screen", b"screen", "sdkver", b"sdkver", "sensor", b"sensor", "sensors_info", b"sensors_info", "sim", b"sim", "speed_sensor", b"speed_sensor", "ssid", b"ssid", "str_app_id", b"str_app_id", "str_battery", b"str_battery", "str_brightness", b"str_brightness", "sys", b"sys", "systemvolume", b"systemvolume", "t", b"t", "total_space", b"total_space", "udid", b"udid", "ui_version", b"ui_version", "uid", b"uid", "usb_connected", b"usb_connected", "user_agent", b"user_agent", "vaid", b"vaid", "virtual", b"virtual", "virtualproc", b"virtualproc", "voice_network_type", b"voice_network_type", "voice_service_state", b"voice_service_state", "wifimac", b"wifimac", "wifimaclist", b"wifimaclist"]) -> None: ...

global___AndroidDeviceInfo = AndroidDeviceInfo

@typing_extensions.final
class SensorInfo(google.protobuf.message.Message):
    """传感器信息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    VENDOR_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    MAX_RANGE_FIELD_NUMBER: builtins.int
    RESOLUTION_FIELD_NUMBER: builtins.int
    POWER_FIELD_NUMBER: builtins.int
    MIN_DELAY_FIELD_NUMBER: builtins.int
    name: builtins.str
    """传感器名称, 如 "rotation Vector" """
    vendor: builtins.str
    """制造商"""
    version: builtins.int
    """"""
    type: builtins.int
    """"""
    max_range: builtins.float
    """"""
    resolution: builtins.float
    """"""
    power: builtins.float
    """耗电量(mA)"""
    min_delay: builtins.int
    """"""
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        vendor: builtins.str = ...,
        version: builtins.int = ...,
        type: builtins.int = ...,
        max_range: builtins.float = ...,
        resolution: builtins.float = ...,
        power: builtins.float = ...,
        min_delay: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max_range", b"max_range", "min_delay", b"min_delay", "name", b"name", "power", b"power", "resolution", b"resolution", "type", b"type", "vendor", b"vendor", "version", b"version"]) -> None: ...

global___SensorInfo = SensorInfo
