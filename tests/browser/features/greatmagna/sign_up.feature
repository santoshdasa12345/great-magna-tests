@Great_Magna_Tests
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

 @allure.link:XOT-004
 @Great-Magna-signup_1
  Scenario Outline:Visitor should be able to see error message with empty password
  Given "Robert" visited "GreatMagna - Sign Up" page
  When "Robert" decides to enter email address "santoshtesting10008+888880@gmail.com", password "<password> " and click Sign up
  Then "Robert" should be on the "GreatMagna - Sign Up" Page
   And "Robert" should see "<an error message>" on the page
  Examples:
      | password    | an error message                                                   |
#      | letters     | This password contains letters only                                |
#      | abcdefghij  | This password contains letters only    |
#      | abcdefghijk | This password contains letters only                                |
#      | 0123456789  | This password is entirely numeric      |
      | password    | This field may not be blank.                                        |
      | empty       | This field may not be blank.                                        |
#      | password    | This password contains the word 'password'                         |
#      | 123 short   | This password is too short. It must contain at least 10 characters |


  @allure.link:XOT-032
  @Great-Magna-Sign-Up_gen_in_touch
  Scenario: User tries to get in touch on th sign up page

  Given "Robert" visited "GreatMagna - Sign Up" page
  When "Robert" decides to click on "Get in touch"
  Then "Robert" should be on the "Domestic - contact us feedback" Page
