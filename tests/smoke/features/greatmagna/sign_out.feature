@smoke
@sign-out-page
@allure.suite:Great_Magna_Sign_Out
Feature: GreatMagna - Sign out Page
   Background:
    Given test authentication is done

  @allure.link:XOT-030
  @Great-Magna-Sign-Out
  Scenario:Visitor should be able to sign out from the dashboard page

  Given "Robert" visited "GreatMagna - Login" page
  When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
  And "Robert" should be on the "GreatMagna - Dashboard" Page
  #And "Robert" should be able to click on SkipWalkthrough
  And "Robert" should be able to click on Avatar
  And "Robert" should be able to click on SignOut
  Then "Robert" should be on the "GreatMagna - Login" page
