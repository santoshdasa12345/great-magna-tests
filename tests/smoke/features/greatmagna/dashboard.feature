@smoke
@dashboard-page
@allure.suite:Great_Magna_Dashboard
Feature: GreatMagna - Dashboard Page
   Background:
    Given Test authentication is done

   @allure.link:XOT-020
   @Great-Magna-Dashboard
  Scenario Outline:User should be able to view Dashboard pages

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "<email address>", password "<password>" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" should see following sections
      | sections             |
      | Learn to export      |
      | Where to Export    |
      | Build an export plan |
      Examples: email address and password
          | email address | password |
          | santoshtesting10008+888@gmail.com | Testing@123! |


