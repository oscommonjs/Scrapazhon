from bs4 import BeautifulSoup
import time

import re

class MainPageScraper:
    def __init__(self, raw_html):
        ''' Constructor for this class. '''
        # Initializer
        self.raw_html = raw_html

    def collect_apps(self):
        print("Parsing HTML")
        soup = BeautifulSoup(self.raw_html, "lxml")
        list_of_apps_in_main_page = []
        # Goes through all the rows (like "Games for You" or "Apps for you") on the main page
        for row in soup.select("div.rcm.widget.s9Widget.acswidget-container"):
            list_of_apps_in_main_page.append(self.apps_in_row(row))

        return list_of_apps_in_main_page

    def apps_in_row(self, row):
        row_hash             = {}
        apps_array           = []
        row_hash["apps"]     = []
        row_hash["row_label"] =  row.find("span", {"class": "acswidget-carousel__title"}).get_text()
        for app in row.select("li.a-carousel-card"):
            app_result             = {}
            app_result["app_name"] = app.find("a", {"class": "a-link-normal acs_product-title"}).get_text()
            app_result["app_id"]   = self.extract_app_id_from_link(app.find("a", {"class": "a-link-normal acs_product-title"})["href"])

            apps_array.append(app_result)

        row_hash["apps"] = apps_array

        return row_hash

    def extract_app_id_from_link(self, link_string):
        # HREF is built like /gp/product/B00NF3AF5O/ref=s9_dcacsd_bhz_bw_c_x_6/164-5582622-7399362.....
        # where the last element after /gp/product is the ID
        return re.search(r"(?<=/product/)[\w+.-]+", link_string).group()

    def app_icon_selector(self, img_element):
        if img_element.get("url") is None:
            return img_element.get("src")
        else:
            return img_element.get("url")