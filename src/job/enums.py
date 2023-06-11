from ..core.enums import BaseEnum


class JobCategoryEnum(BaseEnum):
    FOOD_SERVICE = "food_service"
    SALE = "sale"
    MANUFACTURING = "manufacturing"
    TRANSPORTATION = "transportation"
    AGRICULTURE = "agriculture"
    EDUCATION = "education"
    CONSTRUNCTION = "construration"
    OFFICE_WORK = "office_work"
    CONSULTING = "consulting"
    OTHER = "other"


class JobPostingStatusEnum(BaseEnum):
    PUBLISHED = "published"
    DELETED = "deleted"
    EXPIRED = "expired"