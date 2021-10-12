#@functional
#@fas
#@allure.suite:FAS
#Feature: View FAS in various languages
#
#
#  @allure.link:ED-2004
#  @internationalization
#  @i18n
#  @<selected>
#  @no-sso-email-verification-required
#  Scenario Outline: Buyers should be able to view specific FAS pages in "<selected>" language
#    Given "Annette Geissinger" is a buyer
#
#    When "Annette Geissinger" chooses to view following pages in "<selected>" language
#      | page                      |
#      | Find a Supplier - Landing |
#
#    Then the "main" part of the viewed FAS page should be presented in "<expected>" language with probability greater than "<lower limit>"
#      | page                      |
#      | Find a Supplier - Landing |
#
#    Examples:
#      | selected   | expected   | lower limit |
#      | English    | English    | 0.98        |
#
#    @wip
#    Examples: Missing translations
#      | selected   | expected   | lower limit |
#      | French     | French     | 0.98        |
#      | German     | German     | 0.98        |
#      | Portuguese | Portuguese | 0.98        |
#      | Spanish    | Spanish    | 0.98        |
#      | Arabic     | Arabic     | 0.98        |
#      | Chinese    | Chinese    | 0.71        |
