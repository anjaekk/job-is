from ..core.enums import BaseEnum


class CountryEnum(BaseEnum):
    KOREA = "korea"
    CHINA = "china"
    PHILIPPINES = "philippines"
    VIETNAM = "vietnam"
    CAMBODIA = "cambodia"
    OTHER = "other"
    UNKNOWN = "unknown"


class JobTypeEnum(BaseEnum):
    FULLTIME = "fulltime"
    PARTTIME = "parttime"
    CONTRACT = "contract"