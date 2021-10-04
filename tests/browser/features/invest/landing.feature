@invest
@fas-landing-page
@no-sso-email-verification-required
@allure.suite:Invest
Feature: Invest - landing page

  Background:
    Given test authentication is done


  @allure.link:CMS-157
    @invest_11
  Scenario: Visitors should be able to view "Invest - Landing" page
    Given "Robert" visits the "Invest - landing" page

    Then "Robert" should see following sections
      | Sections                     |
      | Header                       |
      | Hero                         |
      | Breadcrumbs                  |
#      | Benefits                     |
      | Sectors                      |
      | High-potential opportunities |
      | How we help                  |
      | Contact us                   |
      | Error reporting              |
      | Footer                       |

@invest_12
  @allure.link:CMS-157
  Scenario Outline: Overseas businesses should be able to learn more about "<selected>" UK Industry
    Given "Robert" visits the "Invest - landing" page

    When "Robert" decides to find out out more about "Invest - <selected> - industry"

    Then "Robert" should be on the "International - <selected> - industry" page

    @dev-only
    Examples: promoted industries available via International site
      | selected                      |
      | Financial services            |
      | Engineering and manufacturing |
      | Technology                    |

    @stage-only
    Examples: promoted industries available via International site
      | selected                            |
      | Financial and professional services |
      | Engineering and manufacturing       |
      | Technology                          |

@invest_13
  @allure.link:CMS-157
  Scenario: Overseas businesses should be able to also learn more about UK Industries other than the promoted ones
    Given "Robert" visits the "Invest - landing" page

    When "Robert" decides to "see more industries"

    Then "Robert" should be on the "International - Industries" page

@invest_14
  @allure.link:CMS-157
  Scenario: Overseas businesses should be able to learn how to set up in the UK
    Given "Robert" visits the "Invest - landing" page

    When "Robert" decides to find out more about "How to expand to the UK"

    Then "Robert" should be on the "Invest - How to set up in the UK" page


 @invest_15
  @HPO
  @dev-only
  Scenario Outline: Overseas businesses should be able to learn about "<selected>" High-Potential Opportunities
    Given "Robert" visits the "Invest - landing" page

    When "Robert" decides to find out more about "<selected>"

    Then "Robert" should be on the "Invest - <selected> - hpo" page

    Examples: HPO pages
      | selected                          |
      | Aquaculture                       |
      | High productivity food production |
      | Lightweight structures            |
      | Photonics and microelectronics    |
      | Rail infrastructure               |
      | Space                             |
      | Sustainable packaging             |

@invest_16
  @HPO
  @stage-only
  Scenario Outline: Overseas businesses should be able to learn about "<selected>" High-Potential Opportunities
    Given "Robert" visits the "Invest - landing" page

    When "Robert" decides to find out more about "<selected>"

    Then "Robert" should be on the "Invest - <selected> - hpo" page

    Examples: HPO pages
      | selected                          |
      | High productivity food production |
      | Lightweight structures            |
      | Rail infrastructure               |


  @invest_New_1

  Scenario Outline: Overseas businesses should be able to learn about "<selected>" High-Potential Opportunities
    Given "Robert" visits the "Invest - landing" page

#    When "Robert" decides to click on "<selected>"
    When "Robert" decides to find out more about "<service>"

#    Then "Robert" should be on the "Invest - <selected> - hpo" page

#    Examples: Landing pages
#      | selected               |
#      | Get Started            |
##      | Invest in the UK       |
#      | Buy from the Uk        |
#      | Contact DIT            |
#   When "Robert" decides to find out more about "<service>"

    Then "Robert" should be on the "<expected_service>" page

    Examples:
      | service          | expected_service             |
      | Get started      | Invest - landing             |
      | Buy from the UK  | International - Fas          |
      | Invest in the UK  | Invest  - Home              |
      | Contact DIT      | International  - Contact Us  |
