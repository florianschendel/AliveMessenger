# Device information Alive
# Device information Service UUID
# 0x180A
# Device information Alive characteristics, Mode R
MANUF_UUID = "00002a29-0000-1000-8000-00805f9b34fb"
MODEL_UUID = "00002a24-0000-1000-8000-00805f9b34fb"
HW_REV_UUID = "00002a27-0000-1000-8000-00805f9b34fb"
FW_REV_UUID = "00002a28-0000-1000-8000-00805f9b34fb"
SERIAL_UUID = "00002a26-0000-1000-8000-00805f9b34fb"
#
#
# Battery Status Service UUID
# UUID: <0x2a26>
# Battery Status Characteristic, Mode R/N
BT_LVL_UUID = "00002a19-0000-1000-8000-00805f9b34fb"
#
#
# Additional sensors service
# UUID: <5d739d3c-4947-0002-0000-69a2351d7ee5>
# Accelerometer characteristic, Mode R/N
SENS_ACCEL_UUID = "5d739d3c-4947-0002-0001-69a2351d7ee5"
#
# SENS_ACCEL
# Value X part of SENS_ACCEL_UUID, Byte 0-1
SENS_ACCEL_BYTE_SENS_ACCEL_X = [0, 1]
# Value Y part of SENS_ACCEL_UUID, Byte 2-3
SENS_ACCEL_BYTE_SENS_ACCEL_Y = [2, 3]
# Value Z part of SENS_ACCEL_UUID, Byte 4-5
SENS_ACCEL_BYTE_SENS_ACCEL_Z = [4, 5]
#
#
# Device Message Service Characteristics
# UUID: <5d739d3c-4947-0003-0000-69a2351d7ee5>
# Receiver/Sender address can a phone number or mail address UUID (Custom GATT Service), Mode R/W/N
MSG_ADDR_UUID = "5d739d3c-4947-0003-0001-69a2351d7ee5"
# Message itself, emails use the first part of msg data as email subject.
# Body of the mail is separated by a new line (Custom GATT Service), Mode R/W/N
MSG_DATA_UUID = "5d739d3c-4947-0003-0002-69a2351d7ee5"
#
# Outgoing Status of message UUID (Custom GATT Service), Mode R/W/N
MSG_OUT_STATUS_UUID = "5d739d3c-4947-0003-0003-69a2351d7ee5"
# Outgoing Status of message
MSG_OUT_STATUS_IN_PROGRESS = 2
MSG_OUT_STATUS_CORRECTLY_SENT = 3
MSG_OUT_STATUS_MESSAGE_FAILED_TO_BE_SENT = 4
#
# Incoming Status of message UUID (Custom GATT Service), Mode R/W/N
MSG_IN_STATUS_UUID = "5d739d3c-4947-0003-0004-69a2351d7ee5"
# Incoming Status of message
MSG_IN_STATUS_NO_MESSAGE_AVAILABLE = 0
MSG_IN_STATUS_NEW_MESSAGE_IS_AVAILABLE = 1
#
#
# Tracking Characteristics
# UUID: <5d739d3c-4947-0001-0000-69a2351d7ee5>
# Current Tracking mode UUID (Custom GATT Service), Mode R/W/N
TRK_MODE_UUID = "5d739d3c-4947-0001-0001-69a2351d7ee5"
#
# Tracking mode definition status
TRK_MODE_DISABLE = 0
TRK_MODE_STANDARD = 1
TRK_MODE_REALTIME = 2
TRK_MODE_CUSTOM = 3
TRK_MODE_SOS = 4
#
# GSM tracking interval in standard mode (Custom GATT Service), Mode R/W
TRK_GSM_STD_ITVL_UUID = "5d739d3c-4947-0001-0002-69a2351d7ee5"
# Iridium tracking interval in standard mode, Mode R/W
TRK_IRM_STD_ITVL_UUID = "5d739d3c-4947-0001-0003-69a2351d7ee5"
# GSM tracking interval in event mode, Mode R/W
TRK_GSM_EVT_ITVL_UUID = "5d739d3c-4947-0001-0004-69a2351d7ee5"
# Iridium tracking interval in event mode, Mode R/W
TRK_IRM_EVT_ITVL_UUID = "5d739d3c-4947-0001-0005-69a2351d7ee5"
# GSM tracking interval in custom mode, Mode R/W
TRK_GSM_CTM_ITVL_UUID = "5d739d3c-4947-0001-0006-69a2351d7ee5"
# Iridium tracking interval in custom mode, Mode R/W
TRK_IRM_CTM_ITVL_UUID = "5d739d3c-4947-0001-0007-69a2351d7ee5"
#
#
# SOS / Remotre control service (Custom GATT Service)
SOS_CTRL_SRV_UUID = "5d739d3c-4947-0004-0000-69a2351d7ee5"
# SOS / Remotre control Characteristic, Mode R/W/N
SOS_CTRL_UUID = "5d739d3c-4947-0004-0001-69a2351d7ee5"
# Status of SOS
SOS_DISABLED = 0
SOS_ENABLED = 1
#
#
# Location and Navigation Service UUID
# 1819
# Location and Navigation Characteristics
#
#
# Device Features and supported attributes - 4 bytes long, Mode R
LOC_FTRS_UUID = "00002a6a-0000-1000-8000-00805f9b34fb"
#
# Feature list of the device
LOC_FTRS_BYTES = [0, 1, 2, 3]
# Instand speed part of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_INSTANT_SPEED = 0x1
# Total distance part of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_TOTAL_DISTANCE = 0x2
# Location part of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_LOCATION = 0x4
# Elevation part of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_ELEVATION = 0x8
# Heading part of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_HEADING = 0x10
# Rolling time of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_ROLLING_TIME = 0x20
# UTC time of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_UTC_TIME = 0x40
# Remaining distance of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_REMAINING_DISTANCE = 0x80
# Remaining vertical distance of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_REMAINING_VERTICAL_DISTANCE = 0x100
# Estimated time arrival of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_ESTIMATED_TIME_ARRIVAL = 0x200
# Number of beacon in solution of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_NUMBER_BEACON_IN_SOLUTION = 0x400
# Number of beacon in view of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_NUMBER_BEACON_IN_VIEW = 0x800
# Time to first fix of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_TIME_TO_FIRST_FIX = 0x1000
# Horizontal Position error of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_HORIZONTAL_POSITION_ERROR = 0x2000
# Vertical position error of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_VERTICAL_POSITION_ERROR = 0x4000
# HDOP of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_HDOP = 0x8000
# VDOP of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_VDOP = 0x10000
# LOC and speed masking of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_LOC_SPEED_MASKING = 0x20000
# Fix Rate of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_FIX_RATE = 0x40000
# Elevation setting of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_ELEVATION_SETTING = 0x80000
# Position status of LOC_FTRS_UUID
LOC_FTRS_BYTES_FLAGS_POSITION_STATUS = 0x100000
#
# Location quality string - 4 bytes long, Mode R
LOC_QLTY_UUID = "00002a69-0000-1000-8000-00805f9b34fb"
#
# Flags part of LOC_QLTY_UUID, Byte 0-1
LOC_QLTY_BYTE_FLAGS = [0, 1]
# Nb Sat in solution present part of LOC_QLTY_UUID
LOC_QLTY_BYTE_FLAGS_NBSAT_IN_SOLUTION_PRESENT = 0x1
# Nb Sat in view present part of LOC_QLTY_UUID
LOC_QLTY_BYTE_FLAGS_NBSAT_IN_VIEW_PRESENT = 0x2
# Time to first fix present part of LOC_QLTY_UUID
LOC_QLTY_BYTE_FLAGS_TIME_TO_FIRST_FIX_PRESENT = 0x4
# EHPE present part of LOC_QLTY_UUID
LOC_QLTY_BYTE_FLAGS_EHPE_PRESENT = 0x8
# EVPE present part of LOC_QLTY_UUID
LOC_QLTY_BYTE_FLAGS_EVPE_PRESENT = 0x10
# HDOP present part of LOC_QLTY_UUID
LOC_QLTY_BYTE_FLAGS_HDOP_PRESENT = 0x20
# VDOP present part of LOC_QLTY_UUID
LOC_QLTY_BYTE_FLAGS_VDOP_PRESENT = 0x40
# Position status part of LOC_QLTY_UUID
LOC_QLTY_BYTE_FLAGS_POSITIOM_STATUS = 0x180
#
# NbStat part of LOC_QLTY_UUID, Byte 2
LOC_QLTY_BYTE_NBSAT = [2]
#
# HDOP part of LOC_QLTY_UUID, Byte 3
LOC_QLTY_BYTE_HDOP = [3]
#
#
# Location Data string - 24 bytes long, Mode R/N
LOC_DATA_UUID = "00002a67-0000-1000-8000-00805f9b34fb"
#
# Flags part of LOC_DATA_UUID, Byte 0-1
LOC_DATA_BYTE_FLAGS = [0, 1]
# Speed present FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_SPEED_PRESENT = 0x1
# Total Distance FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_TOTAL_DISTANCE = 0x2
# Location present FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_LOCATION_PRESENT = 0x4
# Elevation present FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_ELEVATION_PRESENT = 0x8
# Heading present FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_HEADING_PRESENT = 0x10
# Rolling time present FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_ROLLING_TIME_PRESENT = 0x20
# UTC time present FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_UTC_TIME_PRESENT = 0x40
# Position Status FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_POSITION_STATUS = 0x180
# Speed and distance format FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_SPEED_DISTANCE_FORMAT = 0x200
# Elevation source FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_ELEVATION_SOURCE = 0xC00
# Heading source FLAG part of LOC_DATA_UUID
LOC_DATA_BYTE_FLAGS_HEADING_SOURCE = 0x1000
#
# Speed part of LOC_DATA_UUID, Byte 2-3
LOC_DATA_BYTE_SPEED = [2, 3]
#
# Latitude part of LOC_DATA_UUID, Byte 4-7
LOC_DATA_BYTE_LATITUDE = [4, 7]
#
# Longitude part of LOC_DATA_UUID, Byte 8-11
LOC_DATA_BYTE_LONGITUDE = [8, 11]
#
# Elevation part of LOC_DATA_UUID, Byte 12-14
LOC_DATA_BYTE_ELEVATION = [12, 14]
#
# Heading part of LOC_DATA_UUID, Byte 15-16
LOC_DATA_BYTE_HEADING = [15, 16]
#
# Date and Time part of LOC_DATA_UUID, Byte 17-23
# Byte 17 - 20 Date
# Byte 17 - 18 = Year
LOC_DATA_BYTE_YEAR = [17, 18]
# Byte 19 = Month
LOC_DATA_BYTE_MONTH = [19]
# Byte 20 = Day of month
LOC_DATA_BYTE_DAY_OF_MONTH = [20]
# Byte 21 - 23 Time in UTC
# Byte 23 = Hours
LOC_DATA_BYTE_HOURS = [21]
# Byte 22 = Minutes
LOC_DATA_BYTE_MINUTES = [22]
# Byte 21 = Seconds
LOC_DATA_BYTE_SECONDS = [23]