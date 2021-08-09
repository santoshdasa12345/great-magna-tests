@domestic
@international_1
@allure.suite:International
Feature: INTL - Updates for non-UK companies on EU Exit

  Background:
    Given test authentication is done



  @news
  @eu-exit
  @failed
  @allure.link:CMS-579
  Scenario: International Visitors should be able to ge to the "Updates for non-UK companies on EU Exit" from "International - Landing" page
    Given at least "1" published "international" news article on "Domestic"
    And "Henry" went to the "International - Landing" page

    When "Henry" decides to "See our updates on EU Exit"

    Then "Henry" should be on the "Domestic - Updates for non UK companies on EU Exit" page
    And "Henry" should see following sections
      | sections        |
      | Header          |
      | Beta Bar        |
      | Hero            |
      | Articles        |
      | Contact us      |
      | Error reporting |
      | Footer          |


