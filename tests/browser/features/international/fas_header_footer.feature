#@international
#  @invest
#@fas
#@header-footer-fas
#  @investment_atlas
#@allure.suite:International
#Feature: FAS - Common header & Footer
#
#  Background:
#    Given test authentication is done
#
#
#  Scenario Outline: Buyers should be able to see correct header & footer on "Find a Supplier - <specific>" page
#    Given "Robert" visits the "Find a Supplier - <specific>" page
#
#    Then "Robert" should see following sections
#      | Sections        |
#      | Header          |
#      | Filters         |
#      | Error reporting |
#      | Footer          |
#
#    Examples:
#      | specific             |
#      | Landing              |
##      | Empty search results |
#
#
#
#  Scenario Outline: Buyers should be able to see correct header & footer on "Find a Supplier - <specific>" page
#    Given "Robert" visits the "Find a Supplier - <specific>" page
#
#    Then "Robert" should see following sections
#      | Sections        |
#      | Header          |
#      | Filters         |
#      | Error reporting |
#      | Footer          |
#
#    Examples:
#      | specific             |
##      | Landing              |
#      | Empty search results |
#
##  @no results found,that's why its failing
#@header-footer-fas_1
#  @invest_fix
#  Scenario: Buyers should be able to see correct header & footer on "Find a Supplier - Search results" page
#    Given "Robert" visits the "Find a Supplier - Landing" page
#
##    When "Robert" searches for companies using "Drilling" keyword in "Mining" sector
#    When "Robert" searches for companies using "Painting" keyword in "any" sector
#
#    Then "Robert" should be on the "Find a Supplier - Search results" page
#    And "Robert" should see following sections
#      | Sections                    |
#      | Header                      |
#      | Subscribe for email updates |
#      | Footer                      |
#
#@header-footer-fas_2
#  @invest_fix
#  Scenario: Buyers should see correct header & footer on "Company Profile" page
#    Given "Robert" searched for companies using "food" keyword in "any" sector
#
#    When "Robert" decides to view "random" company profile
#
#    Then "Robert" should be on the "Find a Supplier - Company profile" page
#    And "Robert" should see following sections
#      | Sections |
#      | Header   |
#      | Footer   |
