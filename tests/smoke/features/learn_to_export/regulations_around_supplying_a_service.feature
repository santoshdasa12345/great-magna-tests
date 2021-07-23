@smoke
@lessons-page
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page

  Background:
    Given test authentication is done

   @allure.link:XOT-593
   @Great-Magna-Lessons
 Scenario:User should be able to view Lesson pages for topic "Regulations around supplying a service" and click top back

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Regulations licensing and logistics" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Regulations around supplying a service" on page "LearnToExport - Regulations licensing and logistics"
    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Regulations around supplying a service"
    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Regulations around supplying a service"
