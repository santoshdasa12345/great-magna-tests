@lessons-page
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page

  Background:
    Given test authentication is done

   @allure.link:XOT-501
   @Great-Magna-Lessons
  Scenario:User should be able to view lesson pages for topic "Choose which incoterms are right for you" and click continue

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Learn to export"
     And "Robert" decides to click on section "Regulations licensing and logistics" on page "LearnToExport - Learn Categories"
     And "Robert" decides to click on section "Choose which incoterms are right for you" on page "LearnToExport - Regulations licensing and logistics"
#     And "Robert" decides to click on "case study" on page "LearnToExport - Choose the right route to market"
#     And "Robert" decides to click on "close" on page "LearnToExport - Choose the right route to market"
     And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Choose which incoterms are right for you"

 @allure.link:XOT-502
  @Great-Magna-Lessons
 Scenario:User should be able to view Lesson pages for topic "Choose which incoterms are right for you" and click bottom back

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Regulations licensing and logistics" on page "LearnToExport - Learn Categories"
   And "Robert" decides to click on section "Choose which incoterms are right for you" on page "LearnToExport - Regulations licensing and logistics"
    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Choose which incoterms are right for you"
   And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - Choose which incoterms are right for you"


   @allure.link:XOT-503
   @Great-Magna-Lessons
 Scenario:User should be able to view Lesson pages for topic "Choose which incoterms are right for you" and click top back

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Regulations licensing and logistics" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Choose which incoterms are right for you" on page "LearnToExport - Regulations licensing and logistics"
    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Choose which incoterms are right for you"
    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Choose which incoterms are right for you"

@allure.link:XOT-504
   @Great-Magna-Lessons
 Scenario:User should be able to view Lesson pages for topic "Choose which incoterms are right for you" and click view all lessons

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Regulations licensing and logistics" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Choose which incoterms are right for you" on page "LearnToExport - Regulations licensing and logistics"
#    And "Robert" decides to click on section "view all lessons" on page "LearnToExport - Choose which incoterms are right for you"
