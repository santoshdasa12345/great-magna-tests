@Great_Magna_Tests
@getting-paid-page
@Great_Magna_Export_Plan
@allure.suite:Great_Magna_Export_Plan_G_P
Feature: GreatMagna - Getting Paid Page

  Background:
   Given test authentication is done

   @allure.link:XOT-1131
   @Great_Magna_Export_Plan
     @failed_exp_gp_1_gp
  Scenario:User should be able to click on "Payment methods" section and enter Notes

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Payment Methods" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to enter text at "Payment Methods Notes" on page "Build An Export Plan - Getting Paid"

   @allure.link:XOT-1132
   @Great_Magna_Export_Plan
     @failed_exp_gp_112_12
  Scenario:User should be able to click on "Payment Terms" section and enter Notes

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Payment Terms" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to enter text at "Payment Terms Notes" on page "Build An Export Plan - Getting Paid"

   @allure.link:XOT-1133
   @Great_Magna_Export_Plan
     @failed_exp_gp_1
  Scenario:User should be able to click on "Incoterms" section and enter Notes

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Incoterms" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to enter text at "Incoterms Notes" on page "Build An Export Plan - Getting Paid"


   @allure.link:XOT-1134
   @Great_Magna_Export_Plan__lesson_123
     @failed_exp_gp_2
  Scenario:User should be able to click lessons link "Choose the right payment method"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "payment methods lesson" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to click on lesson link "Choose the right payment method" on page "Build An Export Plan - Getting Paid"
#     And "Robert" decides to click on section "Choose the right payment method" on page "Build An Export Plan - Getting Paid"
     And "Robert" should be on the "LearnToExport - Choose the right payment method" page
     And "Robert" decides to click on section "Getting Paid" on page "LearnToExport - Choose the right payment method"


   @allure.link:XOT-1135
   @Great_Magna_Export_Plan_321b
  Scenario:User should be able to click lessons link "Decide when to get paid"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "payment terms lesson" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to click on lesson link "Decide when to get paid" on page "Build An Export Plan - Getting Paid"
#     And "Robert" decides to click on section "Decide when to get paid" on page "Build An Export Plan - Getting Paid"
     And "Robert" should be on the "LearnToExport - Decide when to get paid" page
     And "Robert" decides to click on section "Getting Paid" on page "LearnToExport - Decide when to get paid"

   @allure.link:XOT-1136
   @Great_Magna_Export_Plan_321c
  Scenario:User should be able to click lessons link "Choose which incoterms are right for you"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "incoterms lesson" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to click on lesson link "Choose which incoterms are right for you" on page "Build An Export Plan - Getting Paid"
#     And "Robert" decides to click on section "Choose which incoterms are right for you" on page "Build An Export Plan - Getting Paid"
     And "Robert" should be on the "LearnToExport - Choose which incoterms are right for you" page
     And "Robert" decides to click on section "Getting Paid" on page "LearnToExport - Choose which incoterms are right for you"


  @allure.link:XOT-1137
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar and navigate to "Travel Plan" page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
    And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to click on element "Nav Travel Plan" on page "Build An Export Plan - Getting Paid"
     And "Robert" should be on the "Build An Export Plan - Travel Plan" Page

@allure.link:XOT-1138
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on page "Travel Plan" at the bottom of the page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
  And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
  And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
  And "Robert" decides to click section complete on "Build An Export Plan - Getting Paid"
  And "Robert" decides to click on section "Travel plan" on page "Build An Export Plan - Getting Paid"
  And "Robert" should be on the "Build An Export Plan - Travel plan" page

   @allure.link:XOT-1139
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home and should be on Export plan Home page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Getting Paid"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

@allure.link:XOT-1140
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Top Export plan home in Getting Paid and should be on Export plan dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
  And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
  And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - Getting Paid"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page
#
#@allure.link:XOT-1141
#  @Great-Magna-Sign-Up_1
#  Scenario Outline: New User should be able to navigate to Export Plan and click on "Getting paid" Page and enter the "Add a target market"
#
#  Given "Robert" visited "GreatMagna - Sign Up" page
#  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
#  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
#  Then "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#     |      emailaddress                 | password    |
#     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
#  And "Robert" decides to click on "Build an export plan"
#  And "Robert" "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
#  And "Robert" decides to enter country name "India" on the "Build An Export Plan - Getting Paid" Page

 @allure.link:XOT-1142
   @Great_Magna_Export_Plan_113
  Scenario:User should be able to click on "Incoterms" on Getting Paid page and click on dashboard should see "Getting Paid" as last visited page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
   And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
   And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" should be on the "Build An Export Plan - Getting Paid" Page
    And "Robert" decides to select random item for "Incoterms" on page "Build An Export Plan - Getting Paid"
   And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Getting Paid"
     And "Robert" should see "Getting Paid" text under section "Export Plan" on page "GreatMagna - Dashboard"
