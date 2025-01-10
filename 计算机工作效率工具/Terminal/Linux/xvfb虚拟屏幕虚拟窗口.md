

# check status

$ ps aux | grep Xvfb
atatlan   673934  0.0  0.0 206356 63872 pts/9    S    09:52   0:00 Xvfb :99 -screen 0 1024x768x16


# use on client side

```
from selenium import webdriver
from pyvirtualdisplay import Display

# Start the virtual display
display = Display(visible=0, size=(1024, 768))
display.start()

# Use Selenium with the virtual display
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("http://www.example.com")
print(driver.title)

# Stop the display and driver
driver.quit()
display.stop()


```
