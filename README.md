# QA Automation using Python Language

### API Automation

#### Installation
- Clone repository using **git clone git@github.com:MAhsan133/QAAutomation.git**
- Move to "QAAutomation" directory
- Run command **pip install -r requirements.txt**
#### Framework / Library
- PyTest
- Requests

#### Run command
> python3 -m pytest -qv APIAutomation/test_reqres.py

#### Features

- Read configrations from separate file
- CRUD operation - Happy flow
- Negative / Edge testcases 


### WEB Automation

#### Installation
- Clone repository using **git clone git@github.com:MAhsan133/QAAutomation.git**
- Move to "QAAutomation" directory
- Run command **pip install -r requirements.txt**
#### Framework / Library
- Selenium
- Behave
- nose

#### Run command
> python3 -m behave WebAutomation/amazon_web/

#### Features
- BDD Approach 
- Page Object Model
- Singleton class for single browser initialization 
- Read configuration from environment variablel
- Separate web elements management
- All possible scenarios e.g. Negative / Edge testcases 

> Note: Happy flow is not possible as it requires email / mobile verification