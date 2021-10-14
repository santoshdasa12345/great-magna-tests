@atlas
@landing-page
@allure.suite:Atlas
Feature: Invest Atlas - landing page

  Background:
    Given test authentication is done


  @allure.link:CMS-157
  Scenario: Visitors should be able to view "Invest - Landing" page
    Given "Robert" visits the "Atlas - landing" page

    Then "Robert" should see following sections
      | Sections                     |
      | Header                       |
      | Hero                         |
#      | Breadcrumbs                  |
      | Benefits                     |
      | Sectors                      |
#      | High-potential opportunities |
      | How we help                  |
      | Contact us                   |
#      | Error reporting              |
      | Footer                       |
