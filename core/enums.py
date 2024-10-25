from enum import IntEnum, StrEnum


class URLs(StrEnum):
    BASE_URL = "https://moodle.ehu.lt/"
    LOGIN_PAGE = "login/index.php"
    COURSES_PAGE = "my/courses.php"
    COURSE_PAGE = "course/view.php?id="
    ATTENDANCE_COURSE_PAGE = "https://moodle.ehu.lt/mod/attendance/view.php?id="


class Language(StrEnum):
    RU = "ru"
    EN = "en-US"
    NULL = "None"
