import csv
import random
import re
import time
import secrets
import string
import undetected_chromedriver as uc
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

from selenium.webdriver.common.action_chains import ActionChains

# Variable XPATH Selectors #


##iframe_xpath = '//*[@id="vvcm0q"]'
##

pre_reg_button = '/html/body/div[3]/div/div/div[3]/div[2]/header/div/div/div/div/pk-button[2]'
create_account_button = '//*[@id="gigya-login-form"]/div[4]/a'
email_xpath = '//*[@id="gigya-textbox-75074230944436030"]'
password_xpath = '//*[@id="gigya-password-59919533498235100"]'
first_name_xpath = '//*[@id="gigya-textbox-130722358975432270"]'
last_name_xpath = '//*[@id="gigya-textbox-30497114450394400"]'
dob_day_xpath = '//*[@id="gigya-textbox-88315185881230510"]'
dob_month_xpath = '//*[@id="gigya-textbox-105406014904922500"]'
dob_year_xpath = '//*[@id="gigya-textbox-32538633360993784"]'
accept_xpath = '//*[@id="gigya-register-form"]/div[1]/div[11]/label'
national_button_xpath = '//*[@id="gigya-register-form"]/div[1]/div[14]/div/div/div[1]/input'
national_select_xpath = '//*[@id="gigya-register-form"]/div[1]/div[14]/div/div/div[2]/ul/li[5]'
email_pref_1 = '//*[@id="gigya-register-form"]/div[1]/div[12]/label'
email_pref_2 = '//*[@id="gigya-register-form"]/div[1]/div[13]/label'
create_account_button_2 = '//*[@id="gigya-register-form"]/div[1]/div[15]/input'



email_code_xpath_1 = '//*[@id="gigya-custom-pin-code-container"]/div/div/input[1]'
email_code_xpath_2 = '//*[@id="gigya-custom-pin-code-container"]/div/div/input[2]'
email_code_xpath_3 = '//*[@id="gigya-custom-pin-code-container"]/div/div/input[3]'
email_code_xpath_4 = '//*[@id="gigya-custom-pin-code-container"]/div/div/input[4]'
email_code_xpath_5 = '//*[@id="gigya-custom-pin-code-container"]/div/div/input[5]'
email_code_xpath_6 = '//*[@id="gigya-custom-pin-code-container"]/div/div/input[6]'
enter_code_accept = '//*[@id="gigya-otp-update-form"]/div[3]/div/input'



address_xpath = '//*[@id="address_line_1"]'
postcode_xpath = '//*[@id="address_zipcode"]'
city_xpath = '//*[@id="address_town"]'
select_country_xpath = '//*[@id="address_country"]'
click_country_xpath = '//*[@id="address_country"]/option[191]'
select_number_xpath = '//*[@id="mobile_prefix"]'
click_number_xpath = '//*[@id="mobile_prefix"]/option[110]'
phone_number_xpath = '//*[@id="mobile_number"]'

##email, password, first_name, last_name, dob_day, dob_month, dob_year, address, postcode, phone_number




PROXY = "11.456.448.110:8080,11.456.448.110:8080,11.456.448.110:8080,11.456.448.110:8080,11.456.448.110:8080"



def submit_form_with_data(first_name, last_name, email, number, address, postcode):
    try:
##        chrome_options = ChromeOptions()
##
##        ua = UserAgent()
##        user_agent = ua.random
##        print(user_agent)
##
##        #chrome_options.add_argument('--proxy-server=%s' % PROXY)
##        chrome_options.add_argument('--incognito')
##        chrome_options.add_argument(f'--user-agent={user_agent}')
##        chrome_service = ChromeService(executable_path='/Users/elwynfernandes/Desktop/UEFABot/chromedriver/chromedriver')
##        driver = wd.Chrome(service=chrome_service, options=chrome_options)
##        driver.implicitly_wait(10)
##        wait = WebDriverWait(driver, 20)
##
##        # 1) Open up Page and initialise Webdriver
##        driver.get("https://idpassets.uefa.com/saml/ticket-login.html")
##        time.sleep(3)
##
##
####        iframe = driver.find_element(By.XPATH, iframe_xpath)
####        driver.switch_to.frame(iframe)
##        #time.sleep(random.uniform(1.0, 5.0))
##
##        # 2) Click First Element on Page #
##        time.sleep(random.uniform(1.0, 3.0))
####        pre_reg_button_elem = driver.find_element(By.XPATH, pre_reg_button)
####        pre_reg_button_elem.click()
##
##        # 3) Finding Form Elements #
##        time.sleep(random.uniform(1.0, 3.0))
##        create_account_elem = driver.find_element(By.XPATH, create_account_button)
##        create_account_elem.click()
##
##
##
##        time.sleep(random.uniform(1.0, 3.0))
##




        
        chrome_email_options = ChromeOptions()
        chrome_email_options.add_argument("user-data-dir=/Users/elwynfernandes/Library/Application Support/Google/Chrome/Default")
        chrome_email_options.add_argument("--profile-directory=Default")

        chrome_service = ChromeService(executable_path='/Users/elwynfernandes/Desktop/UEFABot/chromedriveremail/chromedriver')
        emaildriver = wd.Chrome(service=chrome_service, options=chrome_email_options)
        emaildriver.implicitly_wait(10)
        wait = WebDriverWait(emaildriver, 20)
        emaildriver.get("https://outlook.live.com/mail/0/")

        parent_div_xpath = '//*[@id="MainModule"]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/div'
        parent_div_elem = emaildriver.find_element(By.XPATH, parent_div_xpath)

        first_child_div = parent_div_elem.find_element(By.XPATH, './div[2]')
        aria_label = first_child_div.get_attribute('aria-label')
        print(aria_label)

        confirmation_code_pattern = r'Here’s your confirmation code: (\d+)'
        match = re.search(confirmation_code_pattern, aria_label)

        if match:
            confirmation_code = match.group(1)
            print("Confirmation Code:", confirmation_code)
        else:
            print("Confirmation code not found.")

        print("confirm code : ", confirmation_code)
        print("confirm code : ", confirmation_code)

        digits = list(confirmation_code)

        # Append each digit to separate variables
        digit1, digit2, digit3, digit4, digit5, digit6 = digits

        print("Digit 1:", digit1)
        print("Digit 2:", digit2)
        print("Digit 3:", digit3)
        print("Digit 4:", digit4)
        print("Digit 5:", digit5)
        print("Digit 6:", digit6)
        print("Hello")


##        # 4) Entering Details
##        time.sleep(random.uniform(1.0, 3.0))
##        email_elem = driver.find_element(By.XPATH, email_xpath)
##        password_elem = driver.find_element(By.XPATH, password_xpath)
##        first_name_elem = driver.find_element(By.XPATH, first_name_xpath)
##        last_name_elem = driver.find_element(By.XPATH, last_name_xpath)
##        dob_day_elem = driver.find_element(By.XPATH, dob_day_xpath)
##        dob_month_elem = driver.find_element(By.XPATH, dob_month_xpath)
##        dob_year_elem =  driver.find_element(By.XPATH, dob_year_xpath)
##
##        # 4.1) Generating Data
##        letters = string.ascii_letters
##        digits = string.digits
##        special_chars = string.punctuation
##
##        # Ensure at least one character from each category
##        upper = random.choice(letters.upper())
##        lower = random.choice(letters.lower())
##        number = random.choice(digits)
##        special = random.choice(special_chars)
##
##        all_chars = letters + digits + special_chars
##
##        remaining_length = 12 - len(upper + lower + number + special)
##        remaining_characters = ''.join(random.choice(all_chars) for _ in range(remaining_length))
##
##        password = upper + lower + number + special + remaining_characters
##
##        password_list = list(password)
##        random.shuffle(password_list)
##        password = ''.join(password_list)
##
##        print(password)
##
##        random_day = str(random.randint(1, 31)).zfill(2)  # To ensure 2-digit format
##        random_month = str(random.randint(1, 12)).zfill(2)  # To ensure 2-digit format
##        random_year = str(random.randint(1976, 2003))
##        
##
##        # 5) Send Details into Form
##        time.sleep(random.uniform(1.0, 2.0))
##        email_elem.send_keys(email)
##        time.sleep(random.uniform(1.0, 2.0))
##        password_elem.send_keys(password)
##        time.sleep(random.uniform(1.0, 2.0))
##        first_name_elem.send_keys(first_name)
##        time.sleep(random.uniform(1.0, 2.0))
##        last_name_elem.send_keys(last_name)
##        time.sleep(random.uniform(1.0, 2.0))
##        
##        dob_day_elem.send_keys(random_day)
##        dob_month_elem.send_keys(random_month)
##        dob_year_elem.send_keys(random_year)
##        time.sleep(random.uniform(1.0, 2.0))
##
##
##
##
##        accept_xpath_elem = driver.find_element(By.XPATH, accept_xpath)
##        driver.execute_script('arguments[0].scrollIntoView(true)', accept_xpath_elem)
##        time.sleep(random.uniform(1.0, 2.0))
##        driver.execute_script("arguments[0].click();", accept_xpath_elem)     
##        time.sleep(random.uniform(1.0, 2.0))
##
##        
##
##        email_pref_1_elem = driver.find_element(By.XPATH, email_pref_1)
##        driver.execute_script('arguments[0].scrollIntoView(true)', email_pref_1_elem)
##        time.sleep(random.uniform(1.0, 2.0))
##        email_pref_1_elem.click()
##        time.sleep(random.uniform(1.0, 2.0))
##
####        email_pref_2_elem = driver.find_element(By.XPATH, email_pref_2)
####        driver.execute_script('arguments[0].scrollIntoView(true)', email_pref_2_elem)
####        time.sleep(random.uniform(1.0, 2.0))
####        email_pref_2_elem.click()
####        time.sleep(random.uniform(1.0, 2.0))
####
####        national_button_elem = driver.find_element(By.XPATH, national_button_xpath)
####        national_select_elem = driver.find_element(By.XPATH, national_select_xpath)
####        national_button_elem.click()
####        time.sleep(random.uniform(1.0, 2.0))
####        national_select_elem.click()
##
##        
##
##        create_account_button_2_elem = driver.find_element(By.XPATH, create_account_button_2)
##        create_account_button_2_elem.click()


##        may have captcha at this point

        #6) Next Page

        
        
##        first_name_elem.send_keys(first_name)
##        driver.execute_script('arguments[0].scrollIntoView(true)', last_name_elem)
##        last_name_elem.send_keys(last_name)
##        driver.execute_script('arguments[0].scrollIntoView(true)', email_elem)
##        email_elem.send_keys(email)
##        button_click_elem = driver.find_element(By.XPATH, button_element)
##        driver.execute_script('arguments[0].scrollIntoView(true)', button_click_elem)
##        button_click_elem.click()


##        time.sleep(random.uniform(1.0, 2.0))
##        agree_element_button = driver.find_element(By.XPATH, agree_element)
##        agree_element_button.click()
##
##        time.sleep(1)
##        next_button_click = wait.until(EC.element_to_be_clickable((By.XPATH, next_button_2_xpath)))
##        next_button_click.click()
##
##        time.sleep(random.uniform(1.0, 3.0))
##        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
##        submit_button.click()







        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form-container"]/div/div/div[1]/div/div[2]/div[1]/div[1]/span/span/u/span')))

        time.sleep(3)
        driver.switch_to.default_content()

        result = (first_name, last_name, email)
        print(f"Form submitted successfully for {email}")

        # Append the data to the CSV file if the submission is successful
        with open('completed.csv', 'a', newline='') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')
            
            # Check if the file is empty. If empty, write the header row.
            if new_file.tell() == 0:
                csv_writer.writerow(["First Name", "Last Name", "Email"])
            
            csv_writer.writerow(result)
        
    except Exception as e:
        print(f"Error occurred for {email}: {e}")
        result = None
    
    finally:
        driver.quit()
    
    return result

def main():
    results = []

    with open('emails.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            first_name = row['first_name']
            last_name = row['last_name']
            email = row['email']
            number = row['number']
            address = row['address']
            postcode = row['postcode']

            result = submit_form_with_data(first_name, last_name, email, number, address, postcode)
            if result:
                results.append(result)
    
if __name__ == "__main__":
    main()
