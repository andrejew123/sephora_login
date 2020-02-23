from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(executable_path=r'/home/iwona/Documents/private_project_ivona/chromedriver')
    context.driver.get('https://www.sephora.pl/secure/user/login.jsp')


def after_scenario(context, scenario):
    context.driver.quit()
