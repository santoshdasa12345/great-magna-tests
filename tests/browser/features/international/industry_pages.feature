@international
@allure.link:ED-3183
@allure.link:ED-4259
@industry-pages
@no-sso-email-verification-required
@allure.suite:International
Feature: INTL - Industry pages

  Background:
    Given test authentication is done


  @allure.link:ED-4260
  Scenario Outline: Buyers should be able to see all expected page elements on "<specific>" page
    Given "Robert" visits the "International - <specific> - industry" page

    Then "Robert" should see following sections
      | Sections                |
      | Hero                    |
#      | Breadcrumbs             |
#      | Industry Breadcrumbs    |
#      | Content                 |
#      | Next steps              |

    Examples: common industries
      | specific                            |
      | Creative industries                 |

#    @full
#    @dev-only
#    Examples: promoted industries
#      | specific                            |
#      | Automotive                          |
#      | Aerospace                           |
#      | Education                           |
#      | Engineering and manufacturing       |
#      | Healthcare and Life Sciences        |
#      | Legal services                      |
#      | Real Estate                         |
#      | Space                               |
#      | Technology                          |
     @full
    @dev-only
    Examples: promoted industries
      | specific                            |
      | Agritech                         |
      | Carbon capture usage and storage         |
      | Chemicals                          |
      | Green Finance       |
      | Greener Buildings       |
      | Hydrogen                      |
      | Jet Zero and green ships                         |
      | Scotland                              |
      | Sustainable infrastructure                         |
#
#    @full
#    @stage-only
#    Examples: promoted industries
#      | specific                            |
#      | Engineering and manufacturing       |
#      | Financial and professional services |
#      | Legal services                      |
#      | Technology                          |

    @wip
    @dev-only
    Examples: missing content
      | specific                            |
      | Energy                              |

#removed breadcrumb from this page so this tests fails
#  @bug
#  @allure.issue:TT-433
#  @fixed
#  @allure.link:ED-4261
#  @breadcrumbs
#  Scenario Outline: Buyers should be able to go back to the "<specific>" page via "<selected>" breadcrumb on the "<specific> Industry" page
#    Given "Robert" visits the "International - <specific> - industry" page
#
#    When "Robert" decides to click on "<breadcrumb>"
#
#    Then "Robert" should be on the "International - <expected>" page
#
#    Examples: promoted industries
#      | specific                      | breadcrumb                 | expected   |
#      | Creative industries           | great.gov.uk international | Landing    |
#      | Engineering and manufacturing | Industries                 | Industries |
#
#    @full
#    @dev-only
#    Examples: promoted industries
#      | specific                     | breadcrumb                 | expected   |
#      | Automotive                   | great.gov.uk international | Landing    |
#      | Aerospace                    | great.gov.uk international | Landing    |
#      | Education                    | great.gov.uk international | Landing    |
#      | Energy                       | great.gov.uk international | Landing    |
#      | Healthcare and Life Sciences | great.gov.uk international | Landing    |
#      | Legal services               | Industries                 | Industries |
#      | Real Estate                  | Industries                 | Industries |
#      | Space                        | Industries                 | Industries |
#      | Technology                   | Industries                 | Industries |
#
#    @full
#    @stage-only
#    Examples: promoted industries
#      | specific                            | breadcrumb                 | expected   |
#      | Financial and professional services | great.gov.uk international | Landing    |
#      | Legal services                      | Industries                 | Industries |
#      | Technology                          | Industries                 | Industries |
