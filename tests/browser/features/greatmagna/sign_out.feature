@Great_Magna_Tests
@sign-out-page
@allure.suite:Great_Magna_Sign_Out
Feature: GreatMagna - Sign out Page
   Background:
    Given test authentication is done

  @allure.link:XOT-029
  @Great-Magna-Sign-Out
  Scenario Outline:Visitor should be able to sign out from the dashboard page

  Given "Robert" visited "GreatMagna - Login" page
  When "Robert" decides to enter email address "<email address>", password "<password>" and click Login
  And "Robert" should be on the "GreatMagna - Dashboard" Page
  #And "Robert" should be able to click on SkipWalkthrough
  Then "Robert" decides to click on element "Menu" on page "GreatMagna - Dashboard"
  And "Robert" decides to click on element "Sign out" on page "GreatMagna - Dashboard"
  And "Robert" should be on the "GreatMagna - Home" page


  Examples: email address and password
      | email address | password |
      | santoshtesting10008+888@gmail.com | Testing@123! |