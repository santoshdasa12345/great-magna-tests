@lessons-page_ff
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page

  Background:
    Given test authentication is done

   @allure.link:XOT-561
   @Great-Magna-Lessons_ff_1
  Scenario:User should be able to view lesson pages for topic "Using Freight forwarders" and click continue

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Learn to export"
     And "Robert" decides to click on section "Regulations licensing and logistics" on page "LearnToExport - Learn Categories"
     And "Robert" decides to click on section "Using freight forwarders" on page "LearnToExport - Regulations licensing and logistics"
     And "Robert" decides to click on "Open case study" on page "LearnToExport - Regulations around supplying a service"
#     And "Robert" decides to click on "close" on page "LearnToExport - Regulations around supplying a service"
     And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Using freight forwarders"

 @allure.link:XOT-562
   @Great-Magna-Lessons_ff_2
 Scenario:User should be able to view Lesson pages for topic "Using freight forwarders" and click bottom back

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Regulations licensing and logistics" on page "LearnToExport - Learn Categories"
   And "Robert" decides to click on section "Using freight forwarders" on page "LearnToExport - Regulations licensing and logistics"
    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Using freight forwarders"
   And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - Using freight forwarders"


   @allure.link:XOT-563
   @Great-Magna-Lessons_ff_3
 Scenario:User should be able to view Lesson pages for topic "Using freight forwarders" and click top back

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Regulations licensing and logistics" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Using freight forwarders" on page "LearnToExport - Regulations licensing and logistics"
    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Using freight forwarders"
    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Using freight forwarders"

  @allure.link:XOT-564
   @Great-Magna-Lessons
 Scenario:User should be able to view Lesson pages for topic "Using freight forwarders" and click view all lessons

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Regulations licensing and logistics" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Using freight forwarders" on page "LearnToExport - Regulations licensing and logistics"
#    And "Robert" decides to click on section "view all lessons" on page "LearnToExport - Using freight forwarders"
