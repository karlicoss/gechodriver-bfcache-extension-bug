#!/usr/bin/env python3
from pathlib import Path
import shutil


from selenium import webdriver
from selenium.webdriver.common.by import By


this_dir = Path(__file__).absolute().parent
extension_dir = str(this_dir / 'extension')


use_chrome = False
if use_chrome:
    extension = this_dir / 'extension.zip'
    shutil.make_archive(str(extension.with_suffix('')), format='zip', root_dir=extension_dir)

    options = webdriver.ChromeOptions()
    options.add_extension(str(extension))
    driver = webdriver.Chrome(options=options)
# driver = webdriver.Firefox()  # NOTE: Firefox (gechodriver) passes the test
else:
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    # binary = FirefoxBinary('/L/zzz_borg/soft/firefox-dev-edition/firefox')
    # driver = webdriver.Firefox(firefox_binary=binary)
    driver = webdriver.Firefox()
    driver.install_addon(extension_dir, temporary=True)


# this works as expected
# - under chromedriver
# - under firefox (without geckodriver)
# - under geckodriver, seems that window variables in the inject.js script aren't preserved
def run():
    driver.get('https://example.com')
    print("open page console now, you should see 'injecting <timestamp>' in logs.")
    input("press any key")

    driver.get('https://iana.org')
    driver.back()
    print("in page console, you should see the same message as above, and then 'already injected' with the same timestamp")
    input("press any key")

try:
    run()
finally:
    driver.quit()
