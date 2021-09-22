@Great_Magna_Tests
@costs-and-pricing-page
@Great_Magna_Export_Plan
@allure.suite:Great_Magna_Export_Plan_C_A_P
Feature: GreatMagna - Costs And Pricing Page

   Background:
   Given test authentication is done

  @allure.link:XOT-1091
   @Great_Magna_Export_Plan
  Scenario: User should be able to click on navigation bar and navigate to "Costs And Pricing" page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to click on element "Nav Funding and credit" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" should be on the "Build An Export Plan - Funding and credit" Page

   @allure.link:XOT-1092
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Funding and Credit link" at the bottom of the page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click section complete on "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" should be on the "Build An Export Plan - Funding and Credit" page

   @allure.link:XOT-1093
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home and should be on Export plan Home page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

   @allure.link:XOT-1094
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "No. of units and time" section and select random units and time

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to enter value in "Number of units" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to select random item for "Number of units" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to enter value in "Time frame" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to select random item for "Time Frame" on page "Build An Export Plan - Costs And Pricing"


   @allure.link:XOT-1095
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter "Direct costs"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Product Cost educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Labour Cost educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" enters direct costs price on page "Build An Export Plan - Costs And Pricing"
          | Productcost  | Labourcost    | Additionalmargin |
          |     600      |      35       |         25       |

#    #And "Robert" decides to validate entered text at "Insurance certificate" on page "Build An Export Plan - Adapting Your Product"
#
   @allure.link:XOT-1096
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter "Overhead costs"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Product Adaptation educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Freight and Logistics educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Agent and Distribution fees educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Marketing educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Insurance educational" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" enters overhead costs price on page "Build An Export Plan - Costs And Pricing"
          | Product Adaptation  | Freight and Logistics | Agent and Distribution fees | Marketing | Insurance |
          |        210          |          35           |            44               |     55    |     66    |

    And "Robert" decides to validate entered text at "Insurance certificate" on page "Build An Export Plan - Adapting Your Product"


   @allure.link:XOT-1097
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter "your net price","Local taxes" and "Duty per unit" value
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Net Price educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Net Price example" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Net Price" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Local Taxes educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Local taxes example" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Local taxes" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Duty educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Duty" on page "Build An Export Plan - Costs And Pricing"

   @allure.link:XOT-1098
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter "your net price","Local taxes" and "Duty per unit" value

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Net Price educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Net Price example" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Net Price" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Local Taxes educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Local taxes example" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Local taxes" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on element "Duty educational" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Duty" on page "Build An Export Plan - Costs And Pricing"

   @allure.link:XOT-1099
   @Great_Magna_Export_Plan
  Scenario:User should be able to "select currency" and enter invoicing currency

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to click on section "Manage Exchange Rates" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" should be on the "LearnToExport - Manage Exchange Rates" page
    And "Robert" decides to click on section "Costs And Pricing" on page "LearnToExport - Manage Exchange Rates"
    And "Robert" decides to select random item for "Select Currency" on page "Build An Export Plan - Costs And Pricing"
    And "Robert" decides to enter value in "Gross Price per unit" on page "Build An Export Plan - Costs And Pricing"

@allure.link:XOT-1100
   @Great_Magna_Export_Plan
  @failed_18
  Scenario:User should be able to click on Top Export plan home in Costs And Pricing and should be on Export plan dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

#   @allure.link:XOT-1101
#  @Great-Magna-Sign-Up
#  Scenario Outline: New User should be able to navigate to Export Plan and click on "Travel Plan" Page and enter the "Add Product"
#
#  Given "Robert" visited "GreatMagna - Sign Up" page
#  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
#  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
#  Then "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#     |      emailaddress                 | password    |
#     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
#  And "Robert" decides to click on "Build an export plan"
#  And "Robert" "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
#  And "Robert" decides to enter product name "Flowers" on page "Build An Export Plan - Costs And Pricing"
#  And "Robert" decides to enter country name "Israel" on the "Build An Export Plan - Costs And Pricing" page

      @allure.link:XOT-1102
   @Great_Magna_Export_Plan_1
        @failed_16
  Scenario:User should be able to click "Net Price example" on Costs And Pricing page and click on dashboard should see "Costs And Pricing" as last visited page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" should be on the "Build An Export Plan - Costs And Pricing" Page
    And "Robert" decides to click on element "Net Price example" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Costs And Pricing"
     And "Robert" should see "Costs And Pricing" text under section "Export Plan" on page "GreatMagna - Dashboard"
