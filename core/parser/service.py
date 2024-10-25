import time
from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By

from ..enums import URLs
from .models import Course, CourseMember

__all__ = ['ParserService']


class ParserService:
    def __init__(
            self,
            login: str | None,
            password: str | None,
            cookie: dict | None
    ) -> None:
        self.login: str | None = login
        self.password: str | None = password
        self.cookie: dict | None = cookie
        self.driver = webdriver.Chrome(keep_alive=True)

    def login_by_data(self) -> None:
        """ Method to login with use login&password"""

        self.driver.get(URLs.BASE_URL + URLs.LOGIN_PAGE)
        self.driver.find_element(By.NAME, 'username').send_keys(self.login)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginbtn').click()

        return None  # TODO: add check to successful login

    def get_courses(self) -> Union[list, list[Course]]:
        """ Method to get all courses and modify it """
        
        self.driver.get(URLs.BASE_URL + URLs.COURSE_PAGE)
        time.sleep(1.5)
        cards = self.driver.find_elements(By.CLASS_NAME, 'dashboard-card')
        courses = []

        for card in cards:
            course_name = card.find_element(By.CLASS_NAME, 'multiline').text
            course_id = card.get_attribute("data-course-id")
            courses.append(Course(id=int(course_id), name=course_name))

        return courses
