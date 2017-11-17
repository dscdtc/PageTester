#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'Take screenshot on webpage by dscdtc'

from time import sleep
from selenium import webdriver, common

def take_screenshot(url, picname="./capture.png"):
    '''
    :param url: url address
    :param picname: picture name
    '''
    profile = webdriver.FirefoxProfile()
    # Set UserAgent:
    profile.set_preference("general.useragent.override", "Mozilla/5.0 \
        (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) \
        AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20")
    browser = webdriver.Firefox(profile)
    # browser.set_window_size(1200, 900)
    browser.set_window_size(414, 736)
    browser.set_page_load_timeout(20)
    try:
        browser.get(url) # Load page
        sleep(5)
        # Scroll to bottom:
        # browser.execute_script("""
            # (function () {
            #     var y = 0;
            #     var step = 100;
            #     window.scroll(0, 0);

            #     function f() {
            #         if (y < document.body.scrollHeight) {
            #             y += step;
            #             window.scroll(0, y);
            #             setTimeout(f, 100);
            #         } else {
            #             window.scroll(0, 0);
            #             document.title += "scroll-done";
            #         }
            #     }

            #     setTimeout(f, 1000);
            # })();
        # """)
        # Set delay time:
        # for i in range(30):
        #     if "scroll-done" in browser.title:
        #         break
        #     sleep(10)
    except common.exceptions.TimeoutException:
        pass
    finally:
        browser.save_screenshot(picname)
        browser.close()
        # browser.quit()

    print("Get screenshot success !!")

if __name__ == "__main__":

    take_screenshot("https://bilibili.com", './result/img/bili.png')
