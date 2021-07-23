@smoke
@sign-up-page
@allure.suite:Great_Magna_Sign_Up
Feature: GreatMagna - Sign up Page

   Background:

    Given test authentication is done

  @allure.link:XOT-031
  @Great-Magna-Sign-Up
  Scenario Outline: New Visitor should be able to sign up

  Given "Robert" visited "GreatMagna - Sign Up" page
  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
  #Then "Robert" should be on the "GreatMagna - Sign Up" Page
  #Then "Robert" decides to click "Continue"
  #Then "Robert" decides to click on section "Continue" on page "GreatMagna - Sign up"
  Then "Robert" should be on the "GreatMagna - Dashboard" Page
  Examples: email address and password
     |      emailaddress                 | password    |
     | santoshtesting10008+xxxx@gmail.com | Testing@123!|

#  @allure.link:XOT-032
#  @Great-Magna-Sign-Up
#  Scenario: Existing user try to sign up
#
#  Given "Robert" visited "GreatMagna - Sign Up" page
#  When "Robert" decides to enter email address "santoshtesting10008+755@gmail.com", password "Testing@123!" and click Sign up
#  Then "Robert" should be on the "GreatMagna - Sign Up" Page
#  Then "Robert" should be able to see error message "user with this email already exists" at element "user with this email already exists."
##
#@allure.link:XOT-033
#  @Great-Magna-Sign-Up
#  Scenario: New Visitor should not be able to sign up with wrong confirmation code
#
#  Given "Robert" visited "GreatMagna - Sign Up" page
#  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
#  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter wrong code
#  Then "Robert" should be on the "GreatMagna - Sign Up" Page
#  Then "Robert" should be able to see error message "Invalid code" at element "Invalid code" when click "submit"
#   |      emailaddress                 | password    |
#     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
