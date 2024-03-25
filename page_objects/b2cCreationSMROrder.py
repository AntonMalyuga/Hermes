import random
from page_objects.BasePage import BasePage
from selenium.webdriver.common.by import By
import time


class B2CCreateSMROrder(BasePage):
    path = 'client/createb2c'