1. Clone repository.
    ```
    cd <projects_folder>
    git clone git@github.com:andrejew123/sephora_login_feature.git

2. Create virtualenv and install requirements.
    ```
    python3 -m venv venv
    source venv/bin/activate
    cd sephora_login_feature
    pip install -r requirements.txt
    ```

#### Setup for ChromeDriver

 1. Download [ChromeDriver](http://chromedriver.chromium.org/downloads).
 2. Add the path to the folder with ChromeDriver to PATH. Example:
    ```
    export PATH=$PATH:~/Documents/selenium_drivers
    ```

### Run
```
    cd sephora_login_feature
    behave
```