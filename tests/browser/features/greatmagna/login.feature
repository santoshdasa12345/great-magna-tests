@Great_Magna_Tests
@login-page
@allure.suite:Great_Magna_Login
Feature: GreatMagna - Login Page
  Background:
    Given test authentication is done

#   @allure.link:XOT-001
#   @Great-Magna-Login
#     @failure
#  Scenario Outline:Visitor should be able to login with email address and password
#
#  Given "Robert" visited "GreatMagna - Login" page
#  When "Robert" decides to enter email address "<email address>", password "<password>" and click Login
#  Then "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#      | email address | password |
#      | santoshtesting10008+888@gmail.com | Testing@123! |

#   @allure.link:XOT-002
#   @Great-Magna-Login
#  Scenario Outline:Visitor should be able to see error message with invalid email address and password
#  Given "Robert" visited "GreatMagna - Login" page
#  When "Robert" decides to enter email address "<email address>", password "<password>" and click Login
#  Then "Robert" should be on the "GreatMagna - Login" Page
#  Then "Robert" should be able to see error message "Incorrect username or password" at element "incorrect username and password"
#  Examples: email address and password
#      | email address | password |
#      | santoshtesting10008+88@gmail.com | Testing@123! |
#      | santoshtesting10008+7@gmail.com | Testing      |
#
#
#   @allure.link:XOT-003
#   @Great-Magna-Login
#     Scenario Outline:Visitor should be able to see error message with empty email address
#  Given "Robert" visited "GreatMagna - Login" page
#  When "Robert" decides to enter email address " ", password "<password>" and click Login
#  Then "Robert" should be on the "GreatMagna - Login" Page
#  Then "Robert" should be able to see error message "This field may not be blank." at element "email - field may not be blank"
#   Examples: email address and password
#      | password |
#      | Testing@123! |
#
# @allure.link:XOT-004
# @Great-Magna-Login
#     Scenario Outline:Visitor should be able to see error message with empty password
#  Given "Robert" visited "GreatMagna - Login" page
#  When "Robert" decides to enter email address "<email address>", password " " and click Login
#  Then "Robert" should be on the "GreatMagna - Login" Page
#  Then "Robert" should be able to see error message "This field may not be blank." at element "password - field may not be blank"
#   Examples: email address and password
#      | email address |
#      | santoshtesting10008+88@gmail.com |
#

 @allure.link:XOT-004
 @Great-Magna-Login
     Scenario Outline:Visitor should be able to see error message with empty password
  Given "Robert" visited "GreatMagna - Login" page
  When "Robert" decides to enter email address "santoshtesting10008+8888@gmail.com", password "<password> " and click Login
  Then "Robert" should be on the "GreatMagna - Login" Page
   And "Natalia" should see "<an error message>" on the page
#  Then "Robert" should be able to see error message "This field may not be blank." at element "password - field may not be blank"
#   Examples: email address and password
#      | email address |
#      | santoshtesting10008+88@gmail.com |
  Examples:
      | password     | an error message                                                   |
      | letters      | This password contains letters only                                |
      | abcdefghij   | This password contains letters only                                |
      | abcdefghijk  | This password contains letters only                                |
      | 0123456789   | This password is entirely numeric                                  |
      | password     | Passwords don't match                                              |
      | password     | This field is required                                             |
      | empty        | This field is required                                             |
      | password     | This password contains the word 'password'                         |
      | 123 short    | This password is too short. It must contain at least 10 characters |
      | empty        | This field is required                                             |



