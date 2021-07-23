#@key-flow-page
#@allure.suite:Great_Magna_Sign_Up
#Feature: GreatMagna - Sign up Page
#
#   Background:
#
#    Given test authentication is done
#
#  Scenario Outline: New Visitor should be able to sign up
#
#  Given "Robert" visited "GreatMagna - Sign Up" page
#  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
#  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
#  #Then "Robert" should be on the "GreatMagna - Sign Up" Page
#  #Then "Robert" decides to click "Continue"
#  #Then "Robert" decides to click on section "Continue" on page "GreatMagna - Sign up"
#  Then "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#     |      emailaddress                 | password    |
#     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
#  #And "Robert" should be able to click on SkipWalkthrough
##    Then "Robert" should be able to enter products "<products>" and country "<country>"
##        Examples: Products and Country
##         | products                 | country      |
##         | Vehicle                  | India      |
#    Then "Robert" decides to click on "Learn to export"
#     And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Work out customer demand" on page "LearnToExport - Identify opportunities"
#    And "Robert" should be on the "LearnToExport - Work out customer demand" page
#    And "Robert" decides to watch "25" seconds of the promotional video
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Work out customer demand"
#    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Work out customer demand"
#    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Identify opportunities"
##     And "Robert" should be able to click on Avatar
##     And "Robert" should be able to click on SignOut
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "Data Snapshot" on page "Build An Export Plan - Target Markets Research"
#     #And "Robert" decides to click on section "Open" on page "Build An Export Plan - Target Markets Research"
#    And "Robert" decides to select random checkbox "Age Group" on page "Build An Export Plan - Target Markets Research"
#
