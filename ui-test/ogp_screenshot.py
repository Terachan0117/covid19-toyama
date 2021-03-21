import os
import time

from selenium import webdriver

if not os.path.exists("ogp"):
    os.mkdir("ogp")

PATHS = {
    "/?dummy": (959, 500),
    "/cards/patients-summary": (959, 500),
    "/cards/patients-number": (959, 500),
    "/cards/monitoring-summary": (959, 500),
    "/cards/monitoring-hospitalized-number": (959, 500),
    "/cards/monitoring-severe-bed-occupancy-rate": (959, 500),
    "/cards/monitoring-patients-number": (959, 500),
    "/cards/monitoring-untracked-patients-number": (959, 500),
    "/cards/monitoring-positive-rate": (959, 500),
    "/cards/patients-attribute": (959, 500),
    "/cards/tested-number": (959, 500),
    "/cards/consultation-number": (959, 500),
    "/cards/center-consultation-number": (959, 500),
}

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--hide-scrollbars")

driver = webdriver.Chrome(options=options)

for lang in ("ja", "en"):
    if not os.path.exists("ogp/{}".format(lang)):
        os.mkdir("ogp/{}".format(lang))
    for path, size in PATHS.items():
        driver.set_window_size(*size)
        driver.get(
            "http://localhost:8000{}?ogp=true".format(
                path if lang == "ja" else "/{}{}".format(lang, path)
            )
        )
        path = path.replace("/cards/", "").replace("/", "_")
        if ('heatmap' in path):
            time.sleep(20)
        driver.save_screenshot(
            "ogp/{}.png".format(
                path if lang == "ja" else "{}/{}".format(lang, path)
            )
        )
