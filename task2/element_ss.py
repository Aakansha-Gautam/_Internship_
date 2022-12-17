# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.action_chains import ActionChains
# # def element_image(path,query,driver):
# #     driver.set_window_size(1550,926)
# #     driver_height =926

# #     main_height = driver.execute_script("return document.body.scrollHeight")


# #     i = 1
# #     scrolled = 0

# #     scroll=driver.execute_script("return window.pageYOffset + window.innerHeight")

# #     while(scrolled+scroll < main_height):
# #         driver.execute_script(f"window.scrollTo(0,{scrolled+scroll})")
# #         scrolled+= scroll
# #         driver.save_screenshot(f'{path}\\{query}\\{i}_{query}.png')
# #         i += 1

# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.action_chains import ActionChains
# # # def element_image(driver):
# # #     # height=height = driver.execute_script("return document.body.parentNode.scrollHeight")
# # #     width=driver.execute_script("return document.documentElement.scrollWidth")
# # #     driver.set_window_size(1550,1000)
# # #     height=926
# # #     page=driver.find_element(By.TAG_NAME,"html")
# # #     page_height = driver.execute_script("return document.body.scrollHeight")
# # #     i=1
# # #     while True:
# # #         driver.save_screenshot(f'{i}.png')
# # #         page.send_keys(Keys.PAGE_DOWN)
# # #         scrolled = driver.execute_script("return window.pageYOffset + window.innerHeight")
# # #         i+=1
# # #         if(scrolled+1>page_height):
# # #             break
# # def element_image(path,query,driver):
# #     driver.maximize
# #     driver.set_window_size(1000,926)
# #     driver_height =926

# #     main_height = driver.execute_script("return document.body.scrollHeight")

# #     i = 1
# #     scrolled = 0
# #     scroll=0
# #     while True:
# #         driver.execute_script(f"window.scrollTo(0,{scrolled+scroll})")
# #         scroll=driver.execute_script("return window.pageYOffset + window.innerHeight")
# #         scrolled+= scroll
# #         driver.save_screenshot(f'{path}\\{query}\\{i}_{query}.png')
# #         i += 1
# #         if(scrolled+1>main_height):
# #             break



# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# def element_image(path,query,driver):
#     driver.set_window_size(1550,926)
#     driver_height =926
#     body=driver.find_element(By.TAG_NAME,'html')
#     main_height = driver.execute_script("return document.body.scrollHeight")


#     i = 1
#     scrolled = 
#     scroll=0
#     # scroll=driver.execute_script("return window.pageYOffset + window.innerHeight")

#     while True:
#         # driver.execute_script(f"window.scrollTo(0,{scroll})")
#         driver.save_screenshot(f'{path}\\{query}\\{i}_{query}.png')
#         # body.send_keys(Keys.PAGE_DOWN)
#         driver.execute_script(f"window.scrollTo(0,{scroll})")
#         scroll=driver.execute_script("return window.pageYOffset + window.innerHeight")
#         # driver.save_screenshot(f'{path}\\{query}\\{i}_{query}.png')
#         i += 1
#         if scroll == driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight ) - window.innerHeight"):
#             break





