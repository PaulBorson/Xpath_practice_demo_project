Selenium Automation with XPath

This project demonstrates Selenium automation in Python using XPath locators to interact with web elements on two demo websites:

OrangeHRM Demo – Login automation

DemoQA Text Box – Filling a form and validating output

🚀 Features

Automates login on OrangeHRM Demo
.

Automates form submission on DemoQA Text Box
.

Demonstrates multiple XPath techniques:

@attribute

contains()

starts-with()

preceding & following axes

descendant & child axes

Uses assertion to validate form submission.

Includes delays with time.sleep() for demonstration purposes.

🛠️ Technologies Used

Python 3

Selenium WebDriver

webdriver_manager (ChromeDriver manager)

📂 Project Structure
├── automation.py       # Main Selenium script
├── README.md           # Project documentation

⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/selenium-xpath-automation.git
cd selenium-xpath-automation


(Optional) Create a virtual environment:

python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac


Install dependencies:

pip install selenium webdriver-manager

▶️ Usage

Run the script:

python automation.py


Expected output:

Prattoy Paul successfully added

📌 Code Highlights

OrangeHRM login automation:

username_input = driver.find_element(By.XPATH, '//input[@name="username"]')
username_input.send_keys("Admin")

password_input = driver.find_element(By.XPATH,"//input[contains(@placeholder,'Password')]")
password_input.send_keys("admin123")

submit_button = driver.find_element(By.XPATH, '//button')
submit_button.click()


DemoQA form automation:

full_name_input = driver.find_element(By.XPATH, "//input[starts-with(@id,'userN')]")
full_name_input.send_keys("Prattoy Paul")

cur_address=driver.find_element(By.XPATH, '//textarea[@id="permanentAddress"]/preceding :: textarea')
cur_address.send_keys("Dhaka")

per_address=driver.find_element(By.XPATH, '//textarea[@id="currentAddress"]/following :: textarea')
per_address.send_keys("Netrakona")

button_submit = driver.find_element(By.XPATH, '//div[@class="text-right col-md-2 col-sm-12"]/descendant :: button')
button_submit.click()

✅ Requirements

Python 3.8+

Google Chrome (latest version)

Internet connection
