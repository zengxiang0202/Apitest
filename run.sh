cd ./testCase
pytest -s --alluredir ../outFiles/report/tmp --clean-alluredir
allure serve ../outFiles/report/tmp