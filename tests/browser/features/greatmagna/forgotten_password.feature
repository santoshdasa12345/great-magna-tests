@Great_Magna_Tests
@forgotten-password-page
@allure.suite:Great_Magna_Forgotten_Password
Feature: GreatMagna -  Forgotten Password Page
  Background:
    Given test authentication is done

  @allure.link:XOT-051
  @Great-Magna-Forgotten-Password
  Scenario Outline: Visitor should be able to click on forgotten password and create new password

  Given "Robert" visited "GreatMagna - Login" page
  When "Robert" decides to click on "forgotten_password"
  And "Robert" decides to accept all cookies
  Then "Robert" decides to enter emailaddress "<emailaddress>" and click on reset password
  And "Robert" should be able to click on reset password link from email "<emailaddress>", "<password>" and enters new password "<newpassword>" and confirm
  And "Robert" should be on the "GreatMagna - About" Page
  Examples: email address and password
     |      emailaddress                 | password    | newpassword  |
     | santoshtesting10008+777@gmail.com | Testing@123!| Test@1234568 |