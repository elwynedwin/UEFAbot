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

berlin_xpath = '//*[@id="contactCriteriaE24TOGO.values1"]'
cologne_xpath = '//*[@id="contactCriteriaE24TOGO.values2"]'
dortmund_xpath = '//*[@id="contactCriteriaE24TOGO.values3"]'
dusseldorf_xpath = '//*[@id="contactCriteriaE24TOGO.values4"]'
frankfurt_xpath = '//*[@id="contactCriteriaE24TOGO.values5"]'
gel_xpath = '//*[@id="contactCriteriaE24TOGO.values6"]'
hamburg_xpath = '//*[@id="contactCriteriaE24TOGO.values7"]'
leip_xpath = '//*[@id="contactCriteriaE24TOGO.values8"]'
mun_xpath = '//*[@id="contactCriteriaE24TOGO.values9"]'
stutt_xpath = '//*[@id="contactCriteriaE24TOGO.values10"]'



england_xpath = '//*[@id="contactCriteriaFan.values14"]'

save_button_xpath = '//*[@id="save"]'



##email, password, first_name, last_name, dob_day, dob_month, dob_year, address, postcode, phone_number




PROXY = "11.456.448.110:8080,11.456.448.110:8080,11.456.448.110:8080,11.456.448.110:8080,11.456.448.110:8080"



def submit_form_with_data(first_name, last_name, email, number, address, postcode):
    try:
        chrome_options = ChromeOptions()

        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)

        #chrome_options.add_argument('--proxy-server=%s' % PROXY)
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument(f'--user-agent={user_agent}')
        chrome_service = ChromeService(executable_path='/Users/elwynfernandes/Desktop/UEFABot/chromedriver/chromedriver')
        driver = wd.Chrome(service=chrome_service, options=chrome_options)
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 20)

        # 1) Open up Page and initialise Webdriver
        driver.get("https://idpassets.uefa.com/saml/ticket-login.html")
        time.sleep(3)


##        iframe = driver.find_element(By.XPATH, iframe_xpath)
##        driver.switch_to.frame(iframe)
        #time.sleep(random.uniform(1.0, 5.0))

        # 2) Click First Element on Page #
        time.sleep(random.uniform(1.0, 3.0))
##        pre_reg_button_elem = driver.find_element(By.XPATH, pre_reg_button)
##        pre_reg_button_elem.click()

        # 3) Finding Form Elements #
        time.sleep(random.uniform(1.0, 3.0))
        create_account_elem = driver.find_element(By.XPATH, create_account_button)
        create_account_elem.click()

        # 4) Entering Details
        time.sleep(random.uniform(1.0, 3.0))
        email_elem = driver.find_element(By.XPATH, email_xpath)
        password_elem = driver.find_element(By.XPATH, password_xpath)
        first_name_elem = driver.find_element(By.XPATH, first_name_xpath)
        last_name_elem = driver.find_element(By.XPATH, last_name_xpath)
        dob_day_elem = driver.find_element(By.XPATH, dob_day_xpath)
        dob_month_elem = driver.find_element(By.XPATH, dob_month_xpath)
        dob_year_elem =  driver.find_element(By.XPATH, dob_year_xpath)

        # 4.1) Generating Data
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation

        # Ensure at least one character from each category
        upper = random.choice(letters.upper())
        lower = random.choice(letters.lower())
        number = random.choice(digits)
        special = random.choice(special_chars)

        all_chars = letters + digits + special_chars

        remaining_length = 12 - len(upper + lower + number + special)
        remaining_characters = ''.join(random.choice(all_chars) for _ in range(remaining_length))

        password = upper + lower + number + special + remaining_characters

        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        print(password)

        random_day = str(random.randint(1, 31)).zfill(2)  # To ensure 2-digit format
        random_month = str(random.randint(1, 12)).zfill(2)  # To ensure 2-digit format
        random_year = str(random.randint(1976, 2003))
        

        # 5) Send Details into Form
        time.sleep(random.uniform(1.0, 2.0))
        email_elem.send_keys(email)
        time.sleep(random.uniform(1.0, 2.0))
        password_elem.send_keys(password)
        time.sleep(random.uniform(1.0, 2.0))
        first_name_elem.send_keys(first_name)
        time.sleep(random.uniform(1.0, 2.0))
        last_name_elem.send_keys(last_name)
        time.sleep(random.uniform(1.0, 2.0))
        
        dob_day_elem.send_keys(random_day)
        dob_month_elem.send_keys(random_month)
        dob_year_elem.send_keys(random_year)
        time.sleep(random.uniform(1.0, 2.0))




        accept_xpath_elem = driver.find_element(By.XPATH, accept_xpath)
        driver.execute_script('arguments[0].scrollIntoView(true)', accept_xpath_elem)
        time.sleep(random.uniform(1.0, 2.0))
        driver.execute_script("arguments[0].click();", accept_xpath_elem)     
        time.sleep(random.uniform(1.0, 2.0))

        

        email_pref_1_elem = driver.find_element(By.XPATH, email_pref_1)
        driver.execute_script('arguments[0].scrollIntoView(true)', email_pref_1_elem)
        time.sleep(random.uniform(1.0, 2.0))
        email_pref_1_elem.click()
        time.sleep(random.uniform(1.0, 2.0))

        # email_pref_2_elem = driver.find_element(By.XPATH, email_pref_2)
        # driver.execute_script('arguments[0].scrollIntoView(true)', email_pref_2_elem)
        # time.sleep(random.uniform(1.0, 2.0))
        # email_pref_2_elem.click()
        # time.sleep(random.uniform(1.0, 2.0))

    #    national_button_elem = driver.find_element(By.XPATH, national_button_xpath)
    #    national_select_elem = driver.find_element(By.XPATH, national_select_xpath)
    #    national_button_elem.click()
    #    time.sleep(random.uniform(1.0, 2.0))
    #    national_select_elem.click()

        

        create_account_button_2_elem = driver.find_element(By.XPATH, create_account_button_2)
        create_account_button_2_elem.click()


    
        


##        may have captcha at this point

        #6) Next Page

        time.sleep(random.uniform(15.0,20.0))
        chrome_email_options = ChromeOptions()
        chrome_email_options.add_argument("user-data-dir=/Users/elwynfernandes/Library/Application Support/Google/Chrome/Default")
        chrome_email_options.add_argument("--profile-directory=Default")

        chrome_service_email = ChromeService(executable_path='/Users/elwynfernandes/Desktop/UEFABot/chromedriveremail/chromedriver')
        emaildriver = wd.Chrome(service=chrome_service_email, options=chrome_email_options)
        emaildriver.implicitly_wait(10)
        wait = WebDriverWait(emaildriver, 50)
        emaildriver.get("https://outlook.live.com/mail/0/")
        time.sleep(25)

        

        parent_div_xpath = '//div[@class="EeHm8"]/div[1]'

        parent_div_elem = wait.until(EC.presence_of_element_located((By.XPATH, parent_div_xpath)))

        # first_child_div = parent_div_elem.find_element(By.XPATH, './div[1]')
        aria_label = parent_div_elem.get_attribute('aria-label')
        print(aria_label)

        confirmation_code_pattern = r'Here’s your confirmation code: (\d+)'
        match = re.search(confirmation_code_pattern, aria_label)

        if match:
            confirmation_code = match.group(1)
        
        else:
            print("Confirmation code not found.")
            
        

        print("confirm code : ", confirmation_code)
        time.sleep(random.uniform(1.0, 2.0))
        digits = list(confirmation_code)

        time.sleep(3)

        # Append each digit to separate variables
        digit1, digit2, digit3, digit4, digit5, digit6 = digits

        print("Digit 1:", digit1)
        print("Digit 2:", digit2)
        print("Digit 3:", digit3)
        print("Digit 4:", digit4)
        print("Digit 5:", digit5)
        print("Digit 6:", digit6)
        print("Hello")



        time.sleep(random.uniform(1.0, 2.0))

        emaildriver.quit()
        email_code_elem_1 = wait.until(EC.presence_of_element_located((By.XPATH, email_code_xpath_1)))
        email_code_elem_2 = driver.find_element(By.XPATH, email_code_xpath_2)
        email_code_elem_3 = driver.find_element(By.XPATH, email_code_xpath_3)
        email_code_elem_4 = driver.find_element(By.XPATH, email_code_xpath_4)
        email_code_elem_5 = driver.find_element(By.XPATH, email_code_xpath_5)
        email_code_elem_6 = driver.find_element(By.XPATH, email_code_xpath_6)

        time.sleep(random.uniform(1.0, 2.0))
        email_code_elem_1.send_keys(digit1)
        time.sleep(1)
        email_code_elem_2.send_keys(digit2)
        time.sleep(1)
        email_code_elem_3.send_keys(digit3)
        time.sleep(1)
        email_code_elem_4.send_keys(digit4)
        time.sleep(1)
        email_code_elem_5.send_keys(digit5)
        time.sleep(1)
        email_code_elem_6.send_keys(digit6)

        
        time.sleep(3)
        accept_button_email_verify_elem = driver.find_element(By.XPATH, enter_code_accept)
        accept_button_email_verify_elem.click()




##      1) Final Page Xpath's
        time.sleep(8)
        create_yellow_xpath = '//pk-button[@class="pk-button tickets__btn pk-mb--m js-tracking-card js-tracking-link adaptive-width hydrated"]//span[text()="Create your account"]'

        yellow_create_button_xpath_elem = driver.find_element(By.XPATH, create_yellow_xpath)
        driver.execute_script('arguments[0].scrollIntoView(true)', yellow_create_button_xpath_elem)
        time.sleep(10)
        yellow_create_button_xpath_elem.click()
        time.sleep(3)



        address_xpath_elem = wait.until(EC.element_to_be_clickable((By.XPATH, address_xpath)))


        postcode_xpath_elem = driver.find_element(By.XPATH, postcode_xpath)
        city_xpath_elem = driver.find_element(By.XPATH, city_xpath)
        select_country_xpath_elem = driver.find_element(By.XPATH, select_country_xpath)
        click_country_xpath_elem = driver.find_element(By.XPATH, click_country_xpath)
        select_number_xpath_elem = driver.find_element(By.XPATH, select_number_xpath)
        click_number_xpath_elem = driver.find_element(By.XPATH, click_number_xpath)
        phone_number_xpath_elem = driver.find_element(By.XPATH, phone_number_xpath)
        time.sleep(5)
        driver.execute_script('arguments[0].scrollIntoView(true)', address_xpath_elem)
        address_xpath_elem.send_keys(address)
        time.sleep(3)

        driver.execute_script('arguments[0].scrollIntoView(true)', postcode_xpath_elem)
        postcode_xpath_elem.send_keys(postcode)
        time.sleep(3)


        driver.execute_script('arguments[0].scrollIntoView(true)', city_xpath_elem)
        city_xpath_elem.send_keys("London")
        time.sleep(3)


        driver.execute_script('arguments[0].scrollIntoView(true)', select_country_xpath_elem)
        select_country_xpath_elem.click()
        time.sleep(3)
        click_country_xpath_elem.click()
        time.sleep(2)



        driver.execute_script('arguments[0].scrollIntoView(true)', select_number_xpath_elem)
        select_number_xpath_elem.click()
        time.sleep(3)
        click_number_xpath_elem.click()
        time.sleep(2)

        phone_number_xpath_elem.send_keys(number)
        time.sleep(2)
        
        


##      2) Final Page Xpath's
        
        berlin_xpath_elem = driver.find_element(By.XPATH, berlin_xpath)
        cologne_xpath_elem = driver.find_element(By.XPATH, cologne_xpath)
        dortmund_xpath_elem = driver.find_element(By.XPATH, dortmund_xpath)
        dusseldorf_xpath_elem = driver.find_element(By.XPATH, dusseldorf_xpath)
        frankfurt_xpath_elem = driver.find_element(By.XPATH, frankfurt_xpath)
        gel_xpath_elem = driver.find_element(By.XPATH, gel_xpath)
        hamburg_xpath_elem = driver.find_element(By.XPATH, hamburg_xpath)
        leip_xpath_elem = driver.find_element(By.XPATH, leip_xpath)
        mun_xpath_elem = driver.find_element(By.XPATH, mun_xpath)
        stutt_xpath_elem = driver.find_element(By.XPATH, stutt_xpath)

        driver.execute_script('arguments[0].scrollIntoView(true)', berlin_xpath_elem)
        berlin_xpath_elem.click()
        time.sleep(1)
        cologne_xpath_elem.click()
        time.sleep(1)
        dortmund_xpath_elem.click()
        time.sleep(1)
        dusseldorf_xpath_elem.click()
        time.sleep(1)
        frankfurt_xpath_elem.click()
        time.sleep(1)
        gel_xpath_elem.click()
        time.sleep(1)
        hamburg_xpath_elem.click()
        time.sleep(1)
        leip_xpath_elem.click()
        time.sleep(1)
        mun_xpath_elem.click()
        time.sleep(1)
        stutt_xpath_elem.click()
        time.sleep(1)
        
        
        
        england_xpath_elem = driver.find_element(By.XPATH, england_xpath)
        driver.execute_script('arguments[0].scrollIntoView(true)', england_xpath_elem)
        time.sleep(2)
        england_xpath_elem.click()
        time.sleep(2)

        save_button_xpath_elem = driver.find_element(By.XPATH, save_button_xpath)
        driver.execute_script('arguments[0].scrollIntoView(true)', save_button_xpath_elem)
        time.sleep(2)
        save_button_xpath_elem.click()

        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="introduction"]/p')))


    




        time.sleep(3)
        driver.switch_to.default_content()

        result = (first_name, last_name, email, address, postcode, number, random_day, random_month, random_year, confirmation_code, password )
        print(f"Form submitted successfully for {email}")

        # Append the data to the CSV file if the submission is successful
        with open('completed.csv', 'a', newline='') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')
            
            # Check if the file is empty. If empty, write the header row.
            if new_file.tell() == 0:
                csv_writer.writerow(["First Name", "Last Name", "Email", "Address", "Postcode", "Number", "Day", "Month", "Year", "Confirmation Code", "Password"])
            
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
