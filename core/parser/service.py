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
        """ Method to log in with use login&password"""

        self.driver.get(URLs.BASE_URL + URLs.LOGIN_PAGE)
        self.driver.find_element(By.NAME, 'username').send_keys(self.login)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.ID, 'loginbtn').click()

        return None  # TODO: add check to successful login

    def get_courses(self) -> Union[list, list[Course]]:
        """ Method to get all courses and modify it """

        self.driver.get(URLs.BASE_URL + URLs.COURSES_PAGE)
        time.sleep(1.5)
        cards = self.driver.find_elements(By.CLASS_NAME, 'dashboard-card')
        courses = []

        for card in cards:
            course_name = card.find_element(By.CLASS_NAME, 'multiline').text
            course_id = card.get_attribute("data-course-id")
            courses.append(Course(id=course_id, name=course_name))

        return courses

    def get_course_info(self, course_id: str) -> dict:
        """ Function to get info about course """

        self.driver.get(URLs.BASE_URL + URLs.COURSE_PAGE + course_id)
        course_info = {}
        time.sleep(1.5)

        elements = self.driver.find_elements(By.CLASS_NAME, 'activityname')

        for element in elements:
            try:
                if "Attendance" in element.text:
                    attendance_link = element.find_element(By.TAG_NAME, 'a').get_attribute("href")
                    course_info['attendance_link'] = attendance_link
                if "Grading" in element.text:
                    grading_link = element.find_element(By.TAG_NAME, 'a').get_attribute("href")
                    course_info['grading_link'] = grading_link
            except Exception as e:
                print(e)

        return course_info

    def set_attendance(self, attendance_id: str) -> str | None:
        """ Function for setting attendance in a lesson """

        try:
            self.driver.get(URLs.ATTENDANCE_COURSE_PAGE + attendance_id)
            attendance_link_element = self.driver.find_element(By.XPATH, '//td[@class="statuscol cell c2 lastcol"]/a')
            attendance_link = attendance_link_element.get_attribute("href")

            self.driver.get(attendance_link)

            present_radio = self.driver.find_element(By.ID, "id_status_686")
            submit_button = self.driver.find_element(By.ID, "id_submitbutton")

            present_radio.click()
            submit_button.click()
        except Exception as e:
            return "ATTENDANCE_NOT_STARTED"
