

url = "https://www.google.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.maximize_window()

#driver.close()# close only the active webpage
driver.quit()#close the entire browser

#getting title and current url of ur webpage
#print(driver.title)
#print(driver.current_url)



