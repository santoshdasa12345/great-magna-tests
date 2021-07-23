#@key-flow-export-plan-page
#@allure.suite:Great_Magna_Export_Plan
#Feature: GreatMagna - User navigate to Export plan Page
#
#   Background:
#
#    Given test authentication is done

#  Scenario Outline: New Visitor should be able to Navigate to Export plan section without entering product and country
#
#  Given "Robert" visited "GreatMagna - Sign Up" page
#  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
#  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
#  Then "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#     |      emailaddress                 | password    |
#     | santoshtesting10008+98851@gmail.com | Testing@123!|
#  #And "Robert" should be able to click on SkipWalkthrough
#
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - About Your Business"
#    And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Business Objectives"
#    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Target Markets Research"
#    And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
#    #And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Target Markets Research"
#    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Adapting Your Product"
#    #And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
#    #And "Robert" decides to click on element "Back" on page "Build An Export Plan - Marketing approach"
#    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Costs And Pricing"
#    And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Funding and Credit"
#    And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Getting Paid"
#    And "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Travel Plan"
#    And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Business Risk"



#   Scenario Outline: New Visitor should be able to Navigate to Export plan section and enter product and country at Target Markets research
#
#  Given "Robert" visited "GreatMagna - Login" page
#  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Login
#  #Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
#  Then "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#     |      emailaddress                 | password    |
#     | santoshtesting10008+9803@gmail.com | Testing@123!|
#    Then "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#    And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - About Your Business"
#    And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Business Objectives"
#    #And "Robert" decides to click on element "Back" on page "Build An Export Plan - Target Markets Research"
#    And "Robert" should be able to enter products "<Vehicle>"
#        Examples: Products and Country
#         | products                 | country      |
#         | Vehicle                  | India      |


#  Scenario Outline: New Visitor should be able to Navigate to Export plan section and enter country at Target Markets research
#
#  Given "Robert" visited "GreatMagna - Sign Up" page
#  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
#  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
#  Then "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#     |      emailaddress                 | password    |
#     | santoshtesting10008+9802@gmail.com | Testing@123!|
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#    And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - About Your Business"
#    And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Business Objectives"
#    And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" should be able to enter products "<Vehicle>" and country "<India>"
##        Examples: Products and Country
#         | products                 | country      |
#         | Vehicle                  | India      |
