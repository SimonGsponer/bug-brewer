
from dataclasses import dataclass


@dataclass
class CustomException:
    error: Exception
    resolution: str

error_2034 = CustomException(
    error=ValueError("ERROR2034 - wrong value in function call"),
    resolution="Rectified typo in configuration which passed incorrect parameter value."
)

error_1000 = CustomException(
    error=RuntimeError("ERROR1000 - out of memory"),
    resolution="Increased size of virtual machine"
)

error_5066 = CustomException(
    error=ConnectionError("ERROR5066 - database refuses connection"),
    resolution="Reconfigured VPC settings to allow connection between database and application."
)

error_5057 = CustomException(
    error=OSError("ERROR5057 - forbidden"),
    resolution="Checked application access rights and added read-write permissions for database."
)

error_3310 = CustomException(
    error=NotImplementedError("ERROR3310 - feature not implemented"),
    resolution="Deactivate unsupported feature in configurations."
)

error_2035 = CustomException(
    error=ValueError("ERROR2035 - unsupported value in function call"),
    resolution="Changed configuration of parameter to supported value."
)

error_2033 = CustomException(
    error=OSError("ERROR2033 - invalid configuration"),
    resolution="Checked for missing environmental variables."
)

