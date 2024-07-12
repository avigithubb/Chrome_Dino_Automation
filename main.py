from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "D:\Chrome_Driver\chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)
try:
    driver.get('chrome://dino')
except WebDriverException as e:
    if 'net::ERR_INTERNET_DISCONNECTED' in str(e):
        print("Connect your internet")
        game_obj = driver.find_element(By.TAG_NAME, 'body')
        game_obj.send_keys(Keys.SPACE)
        sleep(2)
        driver.execute_script(""" 
                                this.boxCompare = function(tRexBox, obstacleBox){
                                var crashed = false;
                                var tRexBoxX = tRexBox.x;
                                var tRexBoxY = tRexBox.y;
                                var obstacleBoxX = obstacleBox.x;
                                var obstacleBoxY = obstacleBox.y;
                                // Axis-Aligned Bounding Box method.
                                if (tRexBoxX < obstacleBoxX + obstacleBox.width &&
                                    tRexBoxX + tRexBox.width + 50 > obstacleBoxX &&
                                    tRexBoxY < obstacleBoxY + obstacleBox.height &&
                                    tRexBox.height + tRexBoxY > obstacleBoxY) {
                                    crashed = true;
                                    console.log('the script is running');
                                }
                                return crashed;
                                console.log('the script is not running');
                                }
                                
                                """)
        driver.execute_script("""
                                const spaceEvent = new KeyboardEvent('keydown', {
                                  key: ' ',
                                  code: 'Space',
                                  keyCode: 32,
                                  which: 32,
                                  bubbles: true,
                                  cancelable: true,
                                });
                                
                                Runner.instance_.gameOver = function(){
                                    document.dispatchEvent(spaceEvent);
                                }
                            """)

else:
    print("Turn off the internet")

