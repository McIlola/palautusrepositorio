*** Settings ***
Resource  resource.robot
Resource    login.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username    pelle
    Set Password    pelle123
    Set Password Confirmation    pelle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username    pe
    Set Password    pelle123
    Set Password Confirmation    pelle123
    Submit Credentials
    Register Should Fail With Message    Username too short or not only letters

Register With Valid Username And Too Short Password
    Set Username    pelle
    Set Password    pelle1
    Set Password Confirmation    pelle1
    Submit Credentials
    Register Should Fail With Message   Passwords do not match, password too short or password has only letters 

Register With Valid Username And Invalid Password
    Set Username    pelle
    Set Password    pelleeee
    Set Password Confirmation    pelleeee
    Submit Credentials
    Register Should Fail With Message   Passwords do not match, password too short or password has only letters 

Register With Nonmatching Password And Password Confirmation
    Set Username    pelle
    Set Password    pelle123
    Set Password Confirmation    pelleeee
    Submit Credentials
    Register Should Fail With Message   Passwords do not match, password too short or password has only letters 

Register With Username That Is Already In Use
    Set Username    kalle
    Set Password    pelle123
    Set Password Confirmation    pelle123
    Submit Credentials
    Go To Register Page
    Set Username    kalle
    Set Password    pelle123
    Set Password Confirmation    pelle123
    Submit Credentials
    Register Should Fail With Message   Username taken

Login After Successful Registration
    Set Username    pelle
    Set Password    pelle123
    Set Password Confirmation    pelle123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username    pelle
    Set Password    pelle123
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username    pelle
    Set Password    pelle123
    Set Password Confirmation    pelle123
    Submit Credentials
    Register Should Succeed
    Go To Register Page
    Set Username    kalle
    Set Password    pelle123
    Set Password Confirmation    pelleeee
    Submit Credentials
    Register Should Fail With Message   Passwords do not match, password too short or password has only letters 
    Go To Login Page
    Set Username    pelle
    Set Password    pelle123
    Submit Credentials Login
    Login Should Succeed

*** Keywords ***
Register Should Succeed
    Front Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page