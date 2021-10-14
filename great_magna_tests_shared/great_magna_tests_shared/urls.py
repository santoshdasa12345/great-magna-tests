# -*- coding: utf-8 -*-
from enum import Enum, unique
from functools import partial
from typing import Union
from urllib.parse import urljoin

from .settings import (
    GREAT_MAGNA_URL,
    SSO_URL,
    SSO_API_URL,
    CMS_API_URL,
    CONTACT_US_URL,
    DIRECTORY_API_URL,
    DOMESTIC_URL,
    ERP_URL,
    EVENTS_URL,
    EXPORT_OPPORTUNITIES_URL,
    FIND_A_BUYER_URL,
    FIND_A_SUPPLIER_URL,
    FORMS_API_URL,
    INTERNATIONAL_URL,
    INVEST_URL,
    ISD_URL,
    LEGACY_CONTACT_US_URL,
    LEGACY_INVEST_URL,
    PROFILE_URL,
    SOO_URL,
)


class Url:
    def __init__(
            self, service_url: str, relative_endpoint: str, *, template: str = None
    ):
        join_endpoint = partial(urljoin, service_url)
        self.relative: str = relative_endpoint
        self.absolute: str = join_endpoint(relative_endpoint)
        self.template: Union[str, None] = template
        self.absolute_template: Union[str, None] = (
            join_endpoint(template) if template else None
        )


class CMSApiUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(CMS_API_URL, endpoint, template=template)


class ContactUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(CONTACT_US_URL, endpoint, template=template)


class DirectoryApiUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(DIRECTORY_API_URL, endpoint, template=template)


class DomesticUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(DOMESTIC_URL, endpoint, template=template)


class ExOppsUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(EXPORT_OPPORTUNITIES_URL, endpoint, template=template)


class ERPUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(ERP_URL, endpoint, template=template)


class FABUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(FIND_A_BUYER_URL, endpoint, template=template)


class FABApiUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(FIND_A_BUYER_URL, endpoint, template=template)


class FASUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(FIND_A_SUPPLIER_URL, endpoint, template=template)


class LegacyFASUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(DOMESTIC_URL + "trade/", endpoint, template=template)


class FormsApiUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(FORMS_API_URL, endpoint, template=template)


class InternationalUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(INTERNATIONAL_URL, endpoint, template=template)


class InvestUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(INVEST_URL, endpoint, template=template)

class InvestAtlasUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(INVEST_URL, endpoint, template=template)

class LegacyInvestUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(LEGACY_INVEST_URL, endpoint, template=template)


class ISDUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(ISD_URL, endpoint, template=template)


class LegacyContactUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(LEGACY_CONTACT_US_URL, endpoint, template=template)


class ProfileUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(PROFILE_URL, endpoint, template=template)


class SOOUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(SOO_URL, endpoint, template=template)


class GreatMagnaUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(GREAT_MAGNA_URL, endpoint, template=template)


class SSOUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(SSO_URL, endpoint, template=template)


class SSOApiUrl(Url):
    def __init__(self, endpoint: str, *, template: str = None):
        super().__init__(SSO_API_URL, endpoint, template=template)


@unique
class URLs(Enum):
    """This Enum is to help discover, refactor, find usage of URLs"""

    def __str__(self) -> str:
        return (
            f"{self._name_} absolute URL: {self.value.absolute} relative "
            f"URL: {self.value.relative}"
        )

    @property
    def absolute(self) -> str:
        return self.value.absolute

    @property
    def relative(self) -> str:
        return self.value.relative

    @property
    def template(self) -> Union[str, None]:
        return self.value.template

    @property
    def absolute_template(self) -> Union[str, None]:
        return self.value.absolute_template

    #Atlas
    # INVEST_ATLAS = InvestAtlasUrl("https://great.uat.uktrade.digital/international/")
    # INVEST_ATLAS_HOW_WE_HELP_EXPAND = InvestAtlasUrl("content/trade/how-we-help-you-buy/")

    # CMS API endpoints
    CMS_API_HEALTHCHECK = CMSApiUrl("healthcheck/")
    CMS_API_HEALTHCHECK_PING = CMSApiUrl("healthcheck/ping/")
    CMS_API_PAGES = CMSApiUrl("api/pages/")
    CMS_API_PAGE_BY_ID = CMSApiUrl(
        "api/pages/{page_id}/", template="api/pages/{page_id}/"
    )
    CMS_API_PAGE_BY_PATH = CMSApiUrl(
        "api/pages/lookup-by-path/{site_id}/{path}",
        template="api/pages/lookup-by-path/{site_id}/{path}",
    )
    CMS_API_PAGE_TYPES = CMSApiUrl("api/pages/types/")
    CMS_API_IMAGES = CMSApiUrl("api/images/")
    CMS_API_DOCUMENTS = CMSApiUrl("api/documents/")

    # UNUSED DEFINITIONS
    # New Contact-Us UI - Domestic & International
    CONTACT_US_DOMESTIC = ContactUrl("triage/domestic/")
    CONTACT_US_DOMESTIC_SUCCESS = ContactUrl(
        "{page}/success/", template="{page}/success/"
    )
    CONTACT_US_FEEDBACK = ContactUrl("feedback/")
    CONTACT_US_FEEDBACK_SUCCESS = ContactUrl("feedback/success/")
    CONTACT_US_EXPORT_OPPORTUNITIES = ContactUrl("triage/export-opportunities/")
    CONTACT_US_EXPORT_OPPORTUNITIES_NO_RESPONSE = ContactUrl(
        "triage/export-opportunities/opportunity-no-response/"
    )
    CONTACT_US_EXPORT_OPPORTUNITIES_NOT_RELEVANT = ContactUrl(
        "triage/export-opportunities/alerts-not-relevant/"
    )
    CONTACT_US_FORM_DOMESTIC = ContactUrl("domestic/")
    CONTACT_US_FORM_DOMESTIC_SUCCESS = ContactUrl("domestic/success/")
    CONTACT_US_EXPORT_ADVICE_BUSINESS = ContactUrl("export-advice/business/")
    CONTACT_US_EXPORT_ADVICE_COMMENT = ContactUrl("export-advice/comment/")
    CONTACT_US_EXPORT_ADVICE_PERSONAL = ContactUrl("export-advice/personal/")
    CONTACT_US_OFFICE_FINDER = ContactUrl("office-finder/")
    CONTACT_US_FORM_DSO = ContactUrl("defence-and-security-organisation/")
    CONTACT_US_FORM_GET_FINANCE_COMPANY_DETAILS = DomesticUrl(
        "get-finance/company-details/"
    )
    CONTACT_US_DOMESTIC_EU_EXIT_CONTACT = DomesticUrl("transition-period/contact/")
    CONTACT_US_DOMESTIC_BREXIT_CONTACT_SUCCESS = DomesticUrl("brexit/contact/success/")
    CONTACT_US_FORM_EVENTS = ContactUrl("events/")
    CONTACT_US_FORM_DOMESTIC_ENQUIRES = ContactUrl("domestic/enquiries/")
    CONTACT_US_FORM_EXPORT_ADVICE = ContactUrl("export-advice/comment/")
    CONTACT_US_FORM_INTERNATIONAL = ContactUrl("international/")
    CONTACT_US_FORM_INTERNATIONAL_SUCCESS = ContactUrl("international/success/")
    CONTACT_US_TRANSITION_PERIOD_CONTACT = DomesticUrl("transition-period/contact/")
    CONTACT_US_TRANSITION_PERIOD_CONTACT_SUCCESS = DomesticUrl(
        "transition-period/contact/success/"
    )
    CONTACT_US_GREAT_ACCOUNT = ContactUrl("triage/great-account/")
    CONTACT_US_GREAT_ACCOUNT_CH_LOGIN = ContactUrl(
        "triage/great-account/companies-house-login/"
    )
    CONTACT_US_GREAT_ACCOUNT_NO_VERIFICATION_EMAIL = ContactUrl(
        "triage/great-account/no-verification-email/"
    )
    CONTACT_US_GREAT_ACCOUNT_NO_VERIFICATION_LETTER = ContactUrl(
        "triage/great-account/no-verification-letter/"
    )
    CONTACT_US_GREAT_ACCOUNT_PASSWORD_RESET = ContactUrl(
        "triage/great-account/password-reset/"
    )
    CONTACT_US_GREAT_ACCOUNT_VERIFICATION_LETTER_CODE = ContactUrl(
        "triage/great-account/verification-letter-code/"
    )
    CONTACT_US_GREAT_ACCOUNT_VERIFICATION_MISSING = ContactUrl(
        "triage/great-account/verification-missing/"
    )
    CONTACT_US_GREAT_SERVICES = ContactUrl("triage/great-services/")
    CONTACT_US_INTERNATIONAL = InternationalUrl("contact/")
    CONTACT_US_INTERNATIONAL_STAGING = ContactUrl("triage/international/")
    CONTACT_US_INTERNATIONAL_EXPORTING_TO_THE_UK = ContactUrl(
        "triage/international/exporting-to-the-uk/"
    )
    CONTACT_US_INTERNATIONAL_BREXIT_CONTACT = InternationalUrl("brexit/contact/")
    CONTACT_US_INTERNATIONAL_BREXIT_CONTACT_SUCCESS = InternationalUrl(
        "brexit/contact/success/"
    )
    CONTACT_US_INTERNATIONAL_TRANSITION_PERIOD_CONTACT = InternationalUrl(
        "transition-period/contact/"
    )
    CONTACT_US_INTERNATIONAL_TRANSITION_PERIOD_CONTACT_SUCCESS = InternationalUrl(
        "transition-period/contact/success/"
    )
    CONTACT_US_LANDING = ContactUrl("triage/location/")
    CONTACT_US_OTHER_DOMESTIC_EU_EXIT = ContactUrl("eu-exit-news/contact/")
    CONTACT_US_OTHER_GET_FINANCE = ContactUrl("get-finance/contact/")
    CONTACT_US_OTHER_INTERNATIONAL_EU_EXIT = ContactUrl(
        "international/eu-exit-news/contact/"
    )

    # SOO Contact-Us pages
    CONTACT_US_SOO_ORGANISATION = ContactUrl(
        "selling-online-overseas/organisation/",
        template="selling-online-overseas/organisation/?market={market}",
    )
    CONTACT_US_SOO_ORGANISATION_DETAILS = ContactUrl(
        "selling-online-overseas/organisation-details/"
    )
    CONTACT_US_SOO_ORGANISATION_YOUR_EXPERIENCE = ContactUrl(
        "selling-online-overseas/your-experience/"
    )
    CONTACT_US_SOO_ORGANISATION_CONTACT_DETAILS = ContactUrl(
        "selling-online-overseas/contact-details/",
        template="selling-online-overseas/contact-details/?market={market}",
    )
    CONTACT_US_SOO_ORGANISATION_CONTACT_APPLICANT = ContactUrl(
        "selling-online-overseas/applicant/"
    )
    CONTACT_US_SOO_ORGANISATION_CONTACT_APPLICANT_DETAILS = ContactUrl(
        "selling-online-overseas/applicant-details/"
    )
    CONTACT_US_SOO_ORGANISATION_SUCCESS = ContactUrl("selling-online-overseas/success/")

    # Directory API
    DIR_API_HEALTHCHECK = DirectoryApiUrl("healthcheck/")
    DIR_API_HEALTHCHECK_PING = DirectoryApiUrl("healthcheck/ping/")
    DIR_API_ENROLMENT = DirectoryApiUrl("enrolment/")
    DIR_API_PRE_VERIFIED_ENROLMENT = DirectoryApiUrl("pre-verified-enrolment/")
    DIR_API_ENROLMENT_TRUSTED_CODE = DirectoryApiUrl("trusted-code/{code}/")
    DIR_API_NOTIFICATIONS_ANONYMOUS_UNSUBSCRIBE = DirectoryApiUrl(
        "notifications/anonymous-unsubscribe/"
    )
    DIR_API_BUYER = DirectoryApiUrl("buyer/")
    DIR_API_BUYER_CSV_DUMP = DirectoryApiUrl("buyer/csv-dump/")
    DIR_API_SUPPLIER_CSV_DUMP = DirectoryApiUrl("supplier/csv-dump/")
    DIR_API_VALIDATE_COMPANY_NUMBER = DirectoryApiUrl("validate/company-number/")
    DIR_API_COMPANIES_HOUSE_PROFILE = DirectoryApiUrl(
        "company/companies-house-profile/"
    )
    DIR_API_SUPPLIER = DirectoryApiUrl("supplier/")
    DIR_API_SUPPLIER_UNSUBSCRIBE = DirectoryApiUrl("supplier/unsubscribe/")
    DIR_API_EXPORT_READINESS_TRIAGE = DirectoryApiUrl("export-readiness/triage/")
    DIR_API_EXPORT_READINESS_ARTICLE_READ = DirectoryApiUrl(
        "export-readiness/article-read/"
    )
    DIR_API_EXPORT_READINESS_TASK_COMPLETED = DirectoryApiUrl(
        "export-readiness/task-completed/"
    )
    DIR_API_EXPORT_OPPORTUNITY_FOOD = DirectoryApiUrl("export-opportunity/food/")
    DIR_API_EXPORT_OPPORTUNITY_LEGAL = DirectoryApiUrl("export-opportunity/legal/")
    DIR_API_PUBLIC_COMPANY = DirectoryApiUrl("public/company/")
    DIR_API_PUBLIC_COMPANY_PROFILE = DirectoryApiUrl(
        "public/company/{companies_house_number}/"
    )
    DIR_API_PUBLIC_CASE_STUDY = DirectoryApiUrl("public/case-study/{id}/")
    DIR_API_SUPPLIER_COMPANY = DirectoryApiUrl("supplier/company/")
    DIR_API_SUPPLIER_COMPANY_CASE_STUDY = DirectoryApiUrl(
        "supplier/company/case-study/"
    )
    DIR_API_SUPPLIER_COMPANY_CASE_STUDY_BY_ID = DirectoryApiUrl(
        "supplier/company/case-study/{id}/"
    )
    DIR_API_SUPPLIER_COMPANY_VERIFY = DirectoryApiUrl("supplier/company/verify/")
    DIR_API_SUPPLIER_COMPANY_VERIFY_COMPANIES_HOUSE = DirectoryApiUrl(
        "supplier/company/verify/companies-house/"
    )
    DIR_API_CONTACT_SUPPLIER = DirectoryApiUrl("contact/supplier/")
    DIR_API_COMPANY_SEARCH = DirectoryApiUrl("company/search/")
    DIR_API_CASE_STUDY_SEARCH = DirectoryApiUrl("case-study/search/")
    DIR_API_SUPPLIER_COMPANY_COLLABORATORS = DirectoryApiUrl(
        "supplier/company/collaborators/"
    )
    DIR_API_SUPPLIER_COMPANY_COLLABORATION_INVITE = DirectoryApiUrl(
        "supplier/company/collaboration-invite/"
    )
    DIR_API_SUPPLIER_COMPANY_COLLABORATION_INVITE_BY_UUID = DirectoryApiUrl(
        "supplier/company/collaboration-invite/{uuid}/"
    )
    DIR_API_SUPPLIER_COMPANY_REMOVE_COLLABORATORS = DirectoryApiUrl(
        "supplier/company/remove-collaborators/"
    )
    DIR_API_SUPPLIER_COMPANY_TRANSFER_OWNERSHIP_INVITE = DirectoryApiUrl(
        "supplier/company/transfer-ownership-invite/"
    )
    DIR_API_SUPPLIER_COMPANY_TRANSFER_OWNERSHIP_INVITE_BY_UUID = DirectoryApiUrl(
        "supplier/company/transfer-ownership-invite/{uuid}/"
    )
    DIR_API_SUPPLIER_GECKO_TOTAL_REGISTERED = DirectoryApiUrl(
        "supplier/gecko/total-registered/"
    )
    DIR_API_ACTIVITY_STREAM = DirectoryApiUrl("activity-stream/")
    DIR_API_EXTERNAL_SUPPLIER_SSO = DirectoryApiUrl("external/supplier-sso/")
    DIR_API_EXTERNAL_SUPPLIER = DirectoryApiUrl("external/supplier/")
    DIR_API_TEST_API_COMPANY = DirectoryApiUrl(
        "/testapi/company/{ch_id_or_name}/",
        template="/testapi/company/{ch_id_or_name}/",
    )

    # Domestic site
    DOMESTIC_ADVICE = DomesticUrl("advice/")
    DOMESTIC_ADVICE_ARTICLE = DomesticUrl(
        "advice/{category}/{slug}/", template="advice/{category}/{slug}/"
    )
    DOMESTIC_API_COMPANY_HOUSE_SEARCH = DomesticUrl(
        "api/internal/companies-house-search/"
    )
    DOMESTIC_COMMUNITY = DomesticUrl("community/")
    DOMESTIC_COMMUNITY_JOIN = DomesticUrl("community/join/")
    DOMESTIC_HEALTHCHECK = DomesticUrl("healthcheck/")
    DOMESTIC_HEALTHCHECK_PING = DomesticUrl("healthcheck/ping/")
    DOMESTIC_SEARCH = DomesticUrl("search/")
    DOMESTIC_SERVICES = DomesticUrl("services/")
    DOMESTIC_SITEMAP = DomesticUrl("sitemap.xml")
    DOMESTIC_LANDING = DomesticUrl("")
    DOMESTIC_LANDING_UK = DomesticUrl("?lang=en-gb")
    DOMESTIC_MARKETS = DomesticUrl("markets/")
    DOMESTIC_MARKETS_FILTERED = DomesticUrl(
        "markets/?sector={sector_id}", template="markets/?sector={sector_id}"
    )
    DOMESTIC_MARKETS_GUIDE = DomesticUrl(
        "markets/{country}/", template="markets/{country}/"
    )
    DOMESTIC_TRADE_FINANCE = DomesticUrl("trade-finance/?lang=en-gb")
    DOMESTIC_INTERNATIONAL = DomesticUrl("international/")
    DOMESTIC_INTERNATIONAL_UK = DomesticUrl("international/?lang=en-gb")
    DOMESTIC_INTERNATIONAL_ZH = DomesticUrl("international/?lang=zh-hans")
    DOMESTIC_INTERNATIONAL_DE = DomesticUrl("international/?lang=de")
    DOMESTIC_INTERNATIONAL_JA = DomesticUrl("international/?lang=ja")
    DOMESTIC_INTERNATIONAL_ES = DomesticUrl("international/?lang=es")
    DOMESTIC_INTERNATIONAL_PT = DomesticUrl("international/?lang=pt")
    DOMESTIC_INTERNATIONAL_AR = DomesticUrl("international/?lang=ar")
    DOMESTIC_TRIAGE_SECTOR = DomesticUrl("triage/sector/")
    DOMESTIC_TRIAGE_EXPORTED_BEFORE = DomesticUrl("triage/exported-before/")
    DOMESTIC_TRIAGE_REGULAR_EXPORTER = DomesticUrl("triage/regular-exporter/")
    DOMESTIC_TRIAGE_ONLINE_MARKETPLACE = DomesticUrl("triage/online-marketplace/")
    DOMESTIC_TRIAGE_COMPANIES_HOUSE = DomesticUrl("triage/companies-house/")
    DOMESTIC_TRIAGE_COMPANY = DomesticUrl("triage/company/")
    DOMESTIC_TRIAGE_SUMMARY = DomesticUrl("triage/summary/")
    DOMESTIC_CUSTOM = DomesticUrl("custom/")
    DOMESTIC_NEW = DomesticUrl("new/")
    DOMESTIC_OCCASIONAL = DomesticUrl("occasional/")
    DOMESTIC_REGULAR = DomesticUrl("regular/")
    DOMESTIC_MARKET_RESEARCH = DomesticUrl("market-research/")
    DOMESTIC_CUSTOMER_INSIGHT = DomesticUrl("customer-insight/")
    DOMESTIC_FINANCE = DomesticUrl("finance/")
    DOMESTIC_BUSINESS_PLANNING = DomesticUrl("business-planning/")
    DOMESTIC_GETTING_PAID = DomesticUrl("getting-paid/")
    DOMESTIC_OPERATIONS_AND_COMPLIANCE = DomesticUrl("operations-and-compliance/")
    DOMESTIC_GET_FINANCE = DomesticUrl("get-finance/?lang=en-gb")
    DOMESTIC_GET_FINANCE_YOUR_DETAILS = DomesticUrl("get-finance/your-details/")
    DOMESTIC_GET_FINANCE_SUCCESS = DomesticUrl("get-finance/contact/thanks/")
    DOMESTIC_GET_FINANCE_HELP = DomesticUrl("get-finance/help/")
    DOMESTIC_STORY_FIRST = DomesticUrl("story/hello-babys-rapid-online-growth/")
    DOMESTIC_STORY_SECOND = DomesticUrl(
        "story/york-bag-retailer-goes-global-via-e-commerce/"
    )
    DOMESTIC_COOKIES = DomesticUrl("cookies/")
    DOMESTIC_TERMS = DomesticUrl("terms-and-conditions/")
    DOMESTIC_PRIVACY = DomesticUrl("privacy-and-cookies/")

    #Exceptional Review Procedure Service
    ERP_LANDING = ERPUrl("")
    ERP_TRIAGE_USER_TYPE = ERPUrl("triage/user-type/")
    ERP_TRIAGE_IMPORT_FROM_OVERSEAS = ERPUrl("triage/import-from-overseas/")
    ERP_SAVE_FOR_LATER = ERPUrl(
        "save-for-later/", template="save-for-later/?return_url={return_url}"
    )
    ERP_BUSINESS_PRODUCT_SEARCH = ERPUrl("business/product-search/")
    ERP_BUSINESS_PRODUCT_DETAIL = ERPUrl(
        "business/product-detail/", template="business/product-detail/#{chapter}"
    )
    ERP_BUSINESS_SALES_VOLUME_BEFORE_BREXIT = ERPUrl(
        "business/sales-volume-before-brexit/",
        template="business/sales-volume-before-brexit/#{chapter}",
    )
    ERP_BUSINESS_SALES_REVENUE_BEFORE_BREXIT = ERPUrl(
        "business/sales-revenue-before-brexit/",
        template="business/sales-revenue-before-brexit/#{chapter}",
    )
    ERP_BUSINESS_SALES_AFTER_BREXIT = ERPUrl(
        "business/sales-after-brexit/",
        template="business/sales-after-brexit/#{chapter}",
    )
    ERP_BUSINESS_MARKET_SIZE_AFTER_BREXIT = ERPUrl(
        "business/market-size-after-brexit/",
        template="business/market-size-after-brexit/#{chapter}",
    )
    ERP_BUSINESS_OTHER_CHANGES_AFTER_BREXIT = ERPUrl(
        "business/other-changes-after-brexit/",
        template="business/other-changes-after-brexit/#{chapter}",
    )
    ERP_BUSINESS_MARKET_SIZE = ERPUrl(
        "business/market-size/", template="business/market-size/#{chapter}"
    )
    ERP_BUSINESS_OTHER_INFORMATION = ERPUrl(
        "business/other-information/", template="business/other-information/#{chapter}"
    )
    ERP_BUSINESS_OUTCOME = ERPUrl(
        "business/outcome/", template="business/outcome/#{chapter}"
    )
    ERP_BUSINESS_BUSINESS_DETAILS = ERPUrl(
        "business/business/", template="business/business/#{chapter}"
    )
    ERP_BUSINESS_PERSONAL_DETAILS = ERPUrl(
        "business/personal/", template="business/personal/#{chapter}"
    )
    ERP_BUSINESS_SUMMARY = ERPUrl(
        "business/summary/", template="business/summary/#{chapter}"
    )
    ERP_BUSINESS_FINISHED = ERPUrl(
        "business/finished/", template="business/finished/#{chapter}"
    )
    ERP_CONSUMER_PRODUCT_SEARCH = ERPUrl("consumer/product-search/")
    ERP_CONSUMER_PRODUCT_DETAIL = ERPUrl(
        "consumer/product-detail/", template="consumer/product-detail/#{chapter}"
    )
    ERP_CONSUMER_CHANGE = ERPUrl(
        "consumer/consumer-change/", template="consumer/consumer-change/#{chapter}"
    )
    ERP_CONSUMER_OTHER_CHANGES_AFTER_BREXIT = ERPUrl(
        "consumer/other-changes-after-brexit/",
        template="consumer/other-changes-after-brexit/#{chapter}",
    )
    ERP_CONSUMER_OUTCOME = ERPUrl(
        "consumer/outcome/", template="consumer/outcome/#{chapter}"
    )
    ERP_CONSUMER_TYPE = ERPUrl("consumer/consumer-type/")
    ERP_CONSUMER_GROUP_DETAILS = ERPUrl("consumer/consumer-group/")
    ERP_CONSUMER_PERSONAL = ERPUrl(
        "consumer/personal/", template="consumer/personal/#{chapter}"
    )
    ERP_CONSUMER_SUMMARY = ERPUrl(
        "consumer/summary/", template="consumer/summary/#{chapter}"
    )
    ERP_CONSUMER_FINISHED = ERPUrl(
        "consumer/finished/", template="consumer/finished/#{chapter}"
    )
    ERP_DEVELOPING_COUNTRY = ERPUrl("developing-country-business/country/")
    ERP_DEVELOPING_COUNTRY_PRODUCT_SEARCH = ERPUrl(
        "developing-country-business/product-search/"
    )
    ERP_DEVELOPING_COUNTRY_PRODUCT_DETAIL = ERPUrl(
        "developing-country-business/product-detail/",
        template="developing-country-business/product-detail/#{chapter}",
    )
    ERP_DEVELOPING_COUNTRY_SALES_VOLUME_BEFORE_BREXIT = ERPUrl(
        "developing-country-business/sales-volume-before-brexit/",
        template="developing-country-business/sales-volume-before-brexit/#{chapter}",
    )
    ERP_DEVELOPING_COUNTRY_SALES_REVENUE_BEFORE_BREXIT = ERPUrl(
        "developing-country-business/sales-revenue-before-brexit/",
        template="developing-country-business/sales-revenue-before-brexit/#{chapter}",
    )
    ERP_DEVELOPING_COUNTRY_SALES_AFTER_BREXIT = ERPUrl(
        "developing-country-business/sales-after-brexit/",
        template="developing-country-business/sales-after-brexit/#{chapter}",
    )
    ERP_DEVELOPING_COUNTRY_MARKET_SIZE_AFTER_BREXIT = ERPUrl(
        "developing-country-business/market-size-after-brexit/",
        template="developing-country-business/market-size-after-brexit/#{chapter}",
    )
    ERP_DEVELOPING_COUNTRY_OTHER_CHANGES_AFTER_BREXIT = ERPUrl(
        "developing-country-business/other-changes-after-brexit/",
        template="developing-country-business/other-changes-after-brexit/#{chapter}",
    )
    ERP_DEVELOPING_COUNTRY_OUTCOME = ERPUrl(
        "developing-country-business/outcome/",
        template="developing-country-business/outcome/#{chapter}",
    )
    ERP_DEVELOPING_COUNTRY_BUSINESS_DETAILS = ERPUrl(
        "developing-country-business/business/",
        template="developing-country-business/business/#{chapter}",
    )
    ERP_DEVELOPING_COUNTRY_PERSONAL_DETAILS = ERPUrl(
        "developing-country-business/personal/",
        template="developing-country-business/personal/#{chapter}",
    )
    ERP_DEVELOPING_COUNTRY_SUMMARY = ERPUrl(
        "developing-country-business/summary/",
        template="developing-country-business/summary/#{chapter}",
    )
    ERP_DEVELOPING_COUNTRY_FINISHED = ERPUrl(
        "developing-country-business/finished/",
        template="developing-country-business/finished/#{chapter}",
    )
    ERP_IMPORTER_IMPORTED_PRODUCT_USAGE = ERPUrl(
        "importer/imported-products-usage/",
        template="importer/imported-products-usage/#{sub_heading}",
    )
    ERP_IMPORTER_PRODUCT_SEARCH = ERPUrl(
        "importer/product-search/",
        template="importer/product-search?product-search-term={term}#search-results-title",
    )
    ERP_IMPORTER_PRODUCT_DETAIL = ERPUrl(
        "importer/product-detail/", template="importer/product-detail/#{sub_heading}"
    )
    ERP_IMPORTER_SALES_VOLUME_BEFORE_BREXIT = ERPUrl(
        "importer/sales-volume-before-brexit/",
        template="importer/sales-volume-before-brexit/#{sub_heading}",
    )
    ERP_IMPORTER_SALES_REVENUE_BEFORE_BREXIT = ERPUrl(
        "importer/sales-revenue-before-brexit/",
        template="importer/sales-revenue-before-brexit/#{sub_heading}",
    )
    ERP_IMPORTER_SALES_AFTER_BREXIT = ERPUrl(
        "importer/sales-after-brexit/",
        template="importer/sales-after-brexit/#{sub_heading}",
    )
    ERP_IMPORTER_MARKET_SIZE_AFTER_BREXIT = ERPUrl(
        "importer/market-size-after-brexit/",
        template="importer/market-size-after-brexit/#{sub_heading}",
    )
    ERP_IMPORTER_OTHER_CHANGES_AFTER_BREXIT = ERPUrl(
        "importer/other-changes-after-brexit/",
        template="importer/other-changes-after-brexit/#{sub_heading}",
    )
    ERP_IMPORTER_PRODUCTION_PERCENTAGE = ERPUrl(
        "importer/production-percentage/",
        template="importer/production-percentage/#{sub_heading}",
    )
    ERP_IMPORTER_WHICH_COUNTRIES = ERPUrl(
        "importer/which-countries/", template="importer/which-countries/#{sub_heading}"
    )
    ERP_IMPORTER_EQUIVALENT_UK_GOODS = ERPUrl(
        "importer/equivalent-uk-goods/",
        template="importer/equivalent-uk-goods/#{sub_heading}",
    )
    ERP_IMPORTER_MARKET_SIZE = ERPUrl(
        "importer/market-size/", template="importer/market-size/#{sub_heading}"
    )
    ERP_IMPORTER_OTHER_INFORMATION = ERPUrl(
        "importer/other-information/",
        template="importer/other-information/#{sub_heading}",
    )
    ERP_IMPORTER_OUTCOME = ERPUrl(
        "importer/outcome/", template="importer/outcome/#{sub_heading}"
    )
    ERP_IMPORTER_BUSINESS_DETAILS = ERPUrl(
        "importer/business/", template="importer/business/#{sub_heading}"
    )
    ERP_IMPORTER_PERSONAL_DETAILS = ERPUrl(
        "importer/personal/", template="importer/personal/#{sub_heading}"
    )
    ERP_IMPORTER_SUMMARY = ERPUrl(
        "importer/summary/", template="importer/summary/#{sub_heading}"
    )
    ERP_IMPORTER_FINISHED = ERPUrl(
        "importer/finished/", template="importer/finished/#{sub_heading}"
    )

    # Events service
    EVENTS_LANDING = Url(EVENTS_URL, "")
    EVENTS_EVENT = Url(
        EVENTS_URL,
        "ehome/index.php?eventid=",
        template="ehome/index.php?eventid={eventid}&",
    )
    EVENTS_REGISTRATION = Url(
        EVENTS_URL,
        "ereg/newreg.php?eventid=",
        template="ereg/newreg.php?eventid={eventid}&",
    )

    # ExOpps UI - Export Opportunities
    EXOPPS_LANDING = ExOppsUrl("")
    EXOPPS_OPPORTUNITY = ExOppsUrl(
        "opportunities/{slug}", template="opportunities/{slug}"
    )
    EXOPPS_SEARCH = ExOppsUrl(
        "opportunities/?s={term}", template="opportunities/?s={term}"
    )
    EXOPPS_SITEMAP = ExOppsUrl("sitemap.xml")

    # Find a Buyer
    FAB_LANDING = FABUrl("")
    FAB_SITEMAP = FABUrl("sitemap.xml")
    FAB_ACCOUNT_CONFIRM_OWNERSHIP_TRANSFER = FABUrl(
        "account/transfer/accept/?invite_key=",
        template="account/transfer/accept/?invite_key={invite_key}",
    )
    FAB_ACCOUNT_CONFIRM_PASSWORD = FABUrl("account/transfer/")
    FAB_ACCOUNT_REMOVE_COLLABORATOR = FABUrl("account/remove-collaborator/")
    FAB_CONFIRM_COMPANY_ADDRESS = FABUrl("verify/letter-confirm/")
    FAB_CONFIRM_IDENTITY = FABUrl("verify/")
    FAB_CONFIRM_IDENTITY_LETTER = FABUrl("verify/letter-send/")
    FAB_COMPANY_PROFILE = FABUrl("company-profile/")
    FAB_HEALTHCHECK = FABUrl("healthcheck/")
    FAB_REGISTER = FABUrl("register/")

    # Find a Supplier
    FAS_CASE_STUDY = FASUrl("case-study/", template="case-study/{number}/")
    FAS_CONTACT_SUPPLIER = FASUrl(
        "suppliers/", template="suppliers/{ch_number}/contact/"
    )
    FAS_CONTACT_SUPPLIER_SUCCESS = FASUrl(
        "suppliers/", template="suppliers/{ch_number}/contact/success/{query}"
    )
    FAS_CONTACT_US = FASUrl("contact/")
    FAS_CONTACT_US_SUCCESS = FASUrl("contact/success/")
    FAS_FEEDBACK = FASUrl("feedback/")
    FAS_HEALTHCHECK = FASUrl("healthcheck/")
    FAS_INDUSTRIES = FASUrl("industries/", template="industries/{industry}/")
    FAS_INDUSTRY_CREATIVE_SERVICES = FASUrl("industries/creative-services/")
    FAS_INDUSTRY_FOOD_AND_DRINK = FASUrl("industries/food-and-drink/")
    FAS_INDUSTRY_HEALTHCARE = FASUrl("industries/healthcare/")
    FAS_INDUSTRY_TECHNOLOGY = FASUrl("industries/technology/")
    FAS_LANDING = FASUrl("")
    FAS_SEARCH = FASUrl("search/", template="search/?q={query}&industries={industries}")
    FAS_SITEMAP = FASUrl("sitemap.xml")
    FAS_SUBSCRIBE = FASUrl("subscribe/")
    FAS_SUBSCRIBE_SUCCESS = FASUrl("subscribe/success/")
    FAS_SUBSCRIBE_AGRICULTURE_PLANTS= FASUrl("search/?q=plants&industries=AGRICULTURE_HORTICULTURE_AND_FISHERIES")

    FAS_SUPPLIER = FASUrl("suppliers/", template="suppliers/{ch_number}/")
    FAS_SUPPLIERS = FASUrl("suppliers/", template="suppliers/{ch_number}/{slug}/")
    FAS_INCOMING_REDIRECT = FASUrl("incoming/", template="incoming/{endpoint}")

    # Legacy FAS industry endpoints before slugs were changed to:
    # healthcare, technology & creative-services respectively
    FAS_INDUSTRIES_HEALTH = LegacyFASUrl("industries/health/")
    FAS_INDUSTRIES_TECH = LegacyFASUrl("industries/tech/")
    FAS_INDUSTRIES_CREATIVE = LegacyFASUrl("industries/creative/")

    # Forms API endpoints
    FORMS_API_HEALTHCHECK = FormsApiUrl("api/healthcheck/")
    FORMS_API_HEALTHCHECK_PING = FormsApiUrl("api/healthcheck/ping/")
    FORMS_API_SUBMISSION = FormsApiUrl("api/submission/")
    FORMS_API_ADMIN = FormsApiUrl("admin/")
    FORMS_API_TESTAPI = FormsApiUrl("testapi/submissions-by-email/{email}/")

    # Gov.UK links
    GOVUK_WILDCARD = Url("https://www.gov.uk/", "{slug}", template="{slug}")

    # New International site
    INTERNATIONAL_LANDING = InternationalUrl("")
    INTERNATIONAL_CONTACT_US = InternationalUrl("contact/")
    INTERNATIONAL_SITEMAP = InternationalUrl("sitemap.xml")
    INTERNATIONAL_ABOUT_UK = InternationalUrl("content/about-uk/")
    INTERNATIONAL_ABOUT_US = InternationalUrl("content/about-us/")
    INTERNATIONAL_FAS = InternationalUrl("/trade/")
    INTERNATIONAL_FAS_CONTACT = InternationalUrl("/invest/contact/")
    INTERNATIONAL_FAS_BUY_FROM_THE_UK = InternationalUrl(
        "content/trade/how-we-help-you-buy/"
    )
    INTERNATIONAL_FAS_HOW_WE_HELP_YOU_BUY = InternationalUrl(
        "content/trade/how-we-help-you-buy/"
    )
    INTERNATIONAL_FAS_TRADE_WHY_BUY_FROM_THE_UK = InternationalUrl(
        "trade/how-we-help-you-buy/why-buy-from-the-uk/"
    )
    INTERNATIONAL_INDUSTRIES = InternationalUrl(
        "content/investment/sectors/",
        template="content/investment/sectors/{industry}/",
    )
    INTERNATIONAL_INDUSTRIES_STAGING = InternationalUrl(
        "content/industries/", template="content/industries/{industry}/"
    )
    INTERNATIONAL_BREXIT_NEWS = InternationalUrl("eu-exit-news/?lang=en")
    INTERNATIONAL_BUY_FROM_THE_UK_CONTACT = InternationalUrl("contact/")
    INTERNATIONAL_CAPITAL_INVEST = InternationalUrl("content/capital-invest/")
    INTERNATIONAL_CAPITAL_INVEST_CONTACT = InternationalUrl(
        "content/capital-invest/contact/"
    )
    INTERNATIONAL_CAPITAL_INVEST_CONTACT_SUCCESS = InternationalUrl(
        "content/capital-invest/contact/success/"
    )
    INTERNATIONAL_CAPITAL_INVEST_HOW_WE_HELP = InternationalUrl(
        "content/capital-invest/how-we-help-you-invest-capital/"
    )
    INTERNATIONAL_CAPITAL_INVEST_OPPORTUNITIES = InternationalUrl(
        "content/opportunities/"
    )
    INTERNATIONAL_INDUSTRY_ADVANCED_MANUFACTURING = InternationalUrl(
        "content/investment/sectors/advanced-manufacturing/"
    )
    INTERNATIONAL_INDUSTRY_AEROSPACE = InternationalUrl(
        "content/investment/sectors/aerospace/"
    )
    INTERNATIONAL_INDUSTRY_AGRI_TECH = InternationalUrl(
        "content/investment/sectors/agri-tech/"
    )
    INTERNATIONAL_INDUSTRY_AGRICULTURAL_TECHNOLOGY = InternationalUrl(
        "content/investment/sectors/agricultural-technology/"
    )
    INTERNATIONAL_INDUSTRY_ASSET_MANAGEMENT = InternationalUrl(
        "content/investment/sectors/asset-management/"
    )
    INTERNATIONAL_INDUSTRY_AUTOMOTIVE = InternationalUrl(
        "content/investment/sectors/automotive/"
    )
    INTERNATIONAL_INDUSTRY_AUTOMOTIVE_RESEARCH_AND_DEVELOPMENT = InternationalUrl(
        "content/investment/sectors/automotive-research-and-development/"
    )
    INTERNATIONAL_INDUSTRY_AUTOMOTIVE_SUPPLY_CHAIN = InternationalUrl(
        "content/investment/sectors/automotive-supply-chain/"
    )
    INTERNATIONAL_INDUSTRY_CARBON_CAPTURE_USAGE_AND_STORAGE = InternationalUrl(
        "content/investment/sectors/carbon-capture-usage-and-storage/"
    )
    INTERNATIONAL_INDUSTRY_CHEMICALS = InternationalUrl(
        "content/investment/sectors/chemicals/"
    )
    INTERNATIONAL_INDUSTRY_GREEN_FINANCE = InternationalUrl(
        "content/investment/sectors/green-finance/"
    )
    INTERNATIONAL_INDUSTRY_GREENER_BUILDINGS = InternationalUrl(
        "content/investment/sectors/greener-buildings/"
    )
    INTERNATIONAL_INDUSTRY_HYDROGEN = InternationalUrl(
        "content/investment/sectors/hydrogen/"
    )
    INTERNATIONAL_INDUSTRY_JET_ZERO_AND_GREEN_SHIPS = InternationalUrl(
        "content/investment/sectors/jet-zero-and-green-ships/"
    )
    INTERNATIONAL_INDUSTRY_SUSTAINABLE_INFRASTRUCTURE = InternationalUrl(
        "content/investment/sectors/sustainable-infrastructure/"
    )
    INTERNATIONAL_INDUSTRY_SCOTLAND = InternationalUrl(
        "content/investment/sectors/scotland/"
    )
    INTERNATIONAL_INDUSTRY_CREATIVE_CONTENT_AND_PRODUCTION = InternationalUrl(
        "content/investment/sectors/creative-content-and-production/"
    )
    INTERNATIONAL_INDUSTRY_CREATIVE_INDUSTRIES = InternationalUrl(
        "content/investment/sectors/creative-industries/"
    )
    INTERNATIONAL_INDUSTRY_CYBER_SECURITY = InternationalUrl(
        "content/investment/sectors/cyber-security/"
    )
    INTERNATIONAL_INDUSTRY_DATA_ANALYTICS = InternationalUrl(
        "content/investment/sectors/data-analytics/"
    )
    INTERNATIONAL_INDUSTRY_DIGITAL_MEDIA = InternationalUrl(
        "content/investment/sectors/digital-media/"
    )
    INTERNATIONAL_INDUSTRY_EDUCATION = InternationalUrl(
        "content/investment/sectors/education/"
    )
    INTERNATIONAL_INDUSTRY_ELECTRICAL_NETWORKS = InternationalUrl(
        "content/investment/sectors/electrical-networks/"
    )
    INTERNATIONAL_INDUSTRY_ENERGY = InternationalUrl(
        "content/investment/sectors/energy/"
    )
    INTERNATIONAL_INDUSTRY_ENERGY_WASTE = InternationalUrl(
        "content/investment/sectors/energy-waste/"
    )
    INTERNATIONAL_INDUSTRY_ENGINEERING_AND_MANUFACTURING = InternationalUrl(
        "content/investment/sectors/engineering-and-manufacturing/"
    )
    INTERNATIONAL_INDUSTRY_FINANCIAL_SERVICES = InternationalUrl(
        "content/investment/sectors/financial-services/"
    )
    INTERNATIONAL_INDUSTRY_FINANCIAL_AND_PROFESSIONAL_SERVICES = InternationalUrl(
        "content/investment/sectors/financial-and-professional-services/"
    )
    INTERNATIONAL_INDUSTRY_FINANCIAL_TECHNOLOGY = InternationalUrl(
        "content/investment/sectors/financial-technology/"
    )
    INTERNATIONAL_INDUSTRY_FOOD_AND_DRINK = InternationalUrl(
        "content/investment/sectors/food-and-drink/"
    )
    INTERNATIONAL_INDUSTRY_FOOD_SERVICE_AND_CATERING = InternationalUrl(
        "content/investment/sectors/food-service-and-catering/"
    )
    INTERNATIONAL_INDUSTRY_FREE_FOODS = InternationalUrl(
        "content/investment/sectors/free-foods/"
    )
    INTERNATIONAL_INDUSTRY_LEGAL_SERVICES = InternationalUrl(
        "content/investment/sectors/legal-services/"
    )
    INTERNATIONAL_INDUSTRY_HEALTH_AND_LIFE_SCIENCES = InternationalUrl(
        "content/investment/sectors/health-and-life-sciences/"
    )
    INTERNATIONAL_INDUSTRY_MARITIME = InternationalUrl(
        "content/investment/sectors/maritime/"
    )
    INTERNATIONAL_INDUSTRY_MEAT_POULTRY_AND_DAIRY = InternationalUrl(
        "content/investment/sectors/meat-poultry-and-dairy/"
    )
    INTERNATIONAL_INDUSTRY_MEDICAL_TECHNOLOGY = InternationalUrl(
        "content/investment/sectors/medical-technology/"
    )
    INTERNATIONAL_INDUSTRY_MOTORSPORT = InternationalUrl(
        "content/investment/sectors/motorsport/"
    )
    INTERNATIONAL_INDUSTRY_NUCLEAR_ENERGY = InternationalUrl(
        "content/investment/sectors/nuclear-energy/"
    )
    INTERNATIONAL_INDUSTRY_OFFSHORE_WIND_ENERGY = InternationalUrl(
        "content/investment/sectors/offshore-wind-energy/"
    )
    INTERNATIONAL_INDUSTRY_OIL_AND_GAS = InternationalUrl(
        "content/investment/sectors/oil-and-gas/"
    )
    INTERNATIONAL_INDUSTRY_PHARMACEUTICAL_MANUFACTURING = InternationalUrl(
        "content/investment/sectors/pharmaceutical-manufacturing/"
    )
    INTERNATIONAL_INDUSTRY_REAL_ESTATE = InternationalUrl(
        "content/investment/sectors/real-estate/"
    )
    INTERNATIONAL_INDUSTRY_RETAIL = InternationalUrl(
        "content/investment/sectors/retail/"
    )
    INTERNATIONAL_INDUSTRY_SPACE = InternationalUrl(
        "content/investment/sectors/space/"
    )
    INTERNATIONAL_INDUSTRY_SPORTS_ECONOMY = InternationalUrl(
        "content/investment/sectors/sports-economy/"
    )
    INTERNATIONAL_INDUSTRY_TECHNOLOGY = InternationalUrl(
        "content/investment/sectors/technology/"
    )
    INTERNATIONAL_HEALTHCHECK_FORMS_API = InternationalUrl("healthcheck/forms-api/")
    INTERNATIONAL_HEALTHCHECK_SENTRY = InternationalUrl("healthcheck/sentry/")
    INTERNATIONAL_REGIONS = InternationalUrl("content/investment/regions/")
    INTERNATIONAL_REGIONS_LONDON = InternationalUrl("content/investment/regionslondon/")
    INTERNATIONAL_REGIONS_MIDLANDS = InternationalUrl(
        "content/investment/regions/midlands/"
    )
    INTERNATIONAL_REGIONS_NORTHERN_IRELAND = InternationalUrl(
        "content/investment/regions/northern-ireland/"
    )
    INTERNATIONAL_REGIONS_SOUTH_ENGLAND = InternationalUrl(
        "content/investment/regions/south-england/"
    )
    INTERNATIONAL_REGIONS_NORTH_ENGLAND = InternationalUrl(
        "content/investment/regions/north-england/"
    )
    INTERNATIONAL_REGIONS_WALES = InternationalUrl("content/investment/regions/wales/")

    # Invest site
    INVEST_LANDING = InvestUrl("")
    INVEST_HEALTHCHECK = InvestUrl("healthcheck/")
    INVEST_CONTACT = InvestUrl("contact/")
    INVEST_CONTACT_SUCCESS = InvestUrl("contact/success/")
    INVEST_SITEMAP = InvestUrl("sitemap.xml")
    INVEST_PIR = InvestUrl("perfectfit/")
    INVEST_PIR_SUCCESS = InvestUrl("perfectfit/success/")
    INVEST_HOME = InvestUrl("international/investment/")
    INVEST_HOW_WE_HELP_YOU_EXPAND = InvestUrl("")
    INVEST_HOW_WE_HELP_YOU = InvestUrl("content/investment/how-we-can-help/")
    INVEST_HOW_WE_CAN_HELP = InternationalUrl(
        "content/investment/how-we-can-help/",
        template="content/investment/how-we-can-help/{guide}/",
    )
    INVEST_HPO = InvestUrl("investment/opportunities")
    INVEST_HPO_CONTACT = InternationalUrl(
        "content/investment/foreign-direct-investment-contact/"
    )
    INVEST_HOW_WE_HELP_EXPAND = InvestUrl("content/capital-investment/how-we-help-you-invest-capital/")
    INVEST_HPO_CONTACT_THANK_YOU = InternationalUrl(
        "content/investment/foreign-direct-investment-contact/success/"
    )
    INVEST_HPO_AMIDS = InternationalUrl(
        "content/investment/opportunities/advanced-manufacturing-innovation-district-scotland-amids/"
    )
    INVEST_HPO_RAIL = InternationalUrl(
        "content/investment/opportunities/rail-in-doncaster/"
    )
    # INVEST_HPO_FOOD = InternationalUrl(
    #     "content/investment/opportunities/food-production/"
    # )
    # INVEST_HPO_HIGH_PRODUCTIVITY_FOOD = InternationalUrl(
    #     "content/investment/opportunities/high-productivity-food-production/"
    # )
    INVEST_HPO_LIGHTWEIGHT = InternationalUrl(
        "content/investment/opportunities/lightweight-structures-in-greater-manchester/"
    )
    INVEST_HPO_AQUACULTURE = InternationalUrl(
        "content/investment/opportunities/sustainable-aquaculture-in-dorset/"
    )
    INVEST_HPO_PHOTONICS = InternationalUrl(
        "content/investment/opportunities/photonics-in-the-south-west/"
    )
    INVEST_HPO_SPACE = InternationalUrl(
        "content/investment/opportunities/space/"
    )
    INVEST_HPO_SUSTAINABLE_PACKAGING = InternationalUrl(
        "content/investment/opportunities/sustainable-packaging/"
    )
    INVEST_HPO_CHEMICALS_IN_THE_HUMBER = InternationalUrl(
        "content/investment/opportunities/chemicals-in-the-humber/"
    )
    INVEST_HPO_CARBON_FIBRE_IN_TEES_VALLEY = InternationalUrl(
        "content/investment/opportunities/carbon-fibre-in-tees-valley/"
    )
    INVEST_HPO_CIRCULAR_ECONOMY_IN_TELFORD = InternationalUrl(
        "content/investment/opportunities/circular-economy-in-telford/"
    )
    INVEST_HPO_CONNECTED_AND_AUTOMATED_MOBILITY= InternationalUrl(
        "content/investment/opportunities/cam-modelling-and-simulation-in-oxfordshire/"
    )
    INVEST_HPO_CONTROLLED_ENVIRONMENT_AGRICULTURE = InternationalUrl(
        "content/investment/opportunities/controlled-environment-agriculture-in-yorkshire/"
    )
    INVEST_HPO_COMPOUND_SEMICONDUCTORS = InternationalUrl(
        "content/investment/opportunities/compound-semiconductors-and-applications-in-south-wales/"
    )
    INVEST_HPO_FOOD_PROCESSING_AUTOMATION = InternationalUrl(
        "content/investment/opportunities/food-processing-automation-in-greater-lincolnshire/"
    )
    INVEST_HPO_FUSION_ENERGY = InternationalUrl(
        "content/investment/opportunities/fusion-energy-in-oxfordshire/"
    )
    INVEST_HPO_HEAT_NETWORKS = InternationalUrl(
        "content/investment/opportunities/heat-networks-in-the-north-east-and-tees-valley/"
    )
    INVEST_HPO_HYDROGEN = InternationalUrl(
        "content/investment/opportunities/hydrogen-in-north-east-scotland/"
    )
    INVEST_HPO_HOWBERY_BUSINESS_PARK = InternationalUrl(
        "content/investment/opportunities/howbery-business-park-in-wallingford-oxfordshire/"
    )
    INVEST_HPO_IMMERSIVE_TECHNOLOGY = InternationalUrl(
        "content/investment/opportunities/immersive-technology-in-the-north-east/"
    )
    INVEST_HPO_INNOVATION_IN_ANIMAL_HEALTH = InternationalUrl(
        "content/investment/opportunities/innovation-in-animal-health-surrey-and-hampshire/"
    )
    INVEST_HPO_MARINE_AUTONOMY = InternationalUrl(
        "content/investment/opportunities/marine-autonomy-in-the-south-west/"
    )
    INVEST_HPO_MINING = InternationalUrl(
        "content/investment/opportunities/mining-in-cornwall/"
    )
    INVEST_HPO_NET_ZERO_TRANSPORT = InternationalUrl(
        "content/investment/opportunities/net-zero-transport-in-coventry-and-warwickshire/"
    )
    INVEST_HPO_OFFSHORE_WIND_FLOATING = InternationalUrl(
        "content/investment/opportunities/offshore-wind-floating-substructures-in-scotland/"
    )
    INVEST_HPO_PLANT_BASED_PROTEIN_PRODUCTS = InternationalUrl(
        "content/investment/opportunities/plant-based-and-alternative-protein-products-in-the-north-east/"
    )
    INVEST_HPO_PRECISION_FARMING = InternationalUrl(
        "content/investment/opportunities/precision-farming-in-telford/"
    )
    INVEST_HPO_SMART_AND_SUSTAINABLE_AVIATION = InternationalUrl(
        "content/investment/opportunities/smart-and-sustainable-aviation-in-south-west-england/"
    )
    INVEST_HPO_SPALDING_BATTERY_ENERGY_STORAGE_SYSTEM= InternationalUrl(
        "content/investment/opportunities/spalding-battery-energy-storage-system-in-lincolnshire/"
    )
    INVEST_HPO_WASTEFRONT_RECYCLING_PLANT = InternationalUrl(
        "content/investment/opportunities/wastefront-recycling-plant-in-sunderland/"
    )

    #
    INVEST_INDUSTRIES = LegacyInvestUrl("industries/")
    INVEST_REGIONS_SCOTLAND = InternationalUrl("content/investment/regions/scotland/")
    INVEST_LEGACY_UK_SETUP_GUIDE = LegacyInvestUrl("uk-setup-guide/")
    INVEST_LEGACY_UK_SETUP_GUIDE_UK_VISAS = LegacyInvestUrl(
        "uk-setup-guide/apply-uk-visa/"
    )
    INVEST_LEGACY_UK_SETUP_GUIDE_ESTABLISH_A_BASE = LegacyInvestUrl(
        "uk-setup-guide/establish-base-business-uk/"
    )
    INVEST_LEGACY_UK_SETUP_GUIDE_HIRE_SKILLED_WORKERS = LegacyInvestUrl(
        "uk-setup-guide/hire-skilled-workers-your-uk-operations/"
    )
    INVEST_LEGACY_UK_SETUP_GUIDE_OPEN_BANK_ACCOUNT = LegacyInvestUrl(
        "uk-setup-guide/open-uk-business-bank-account/"
    )
    INVEST_LEGACY_UK_SETUP_GUIDE_REGISTER_A_COMPANY = LegacyInvestUrl(
        "uk-setup-guide/setup-your-business-uk/"
    )
    INVEST_LEGACY_UK_SETUP_GUIDE_UK_TAX = LegacyInvestUrl(
        "uk-setup-guide/understand-uk-tax-and-incentives/"
    )

    INVEST_UK_SETUP_GUIDE = InternationalUrl(
        "content/investment/how-we-can-help/",
        template="content/investment/how-we-can-help/{guide}/",
    )
    INVEST_UK_SETUP_GUIDE_UK_VISAS = InternationalUrl(
        "content/investment/how-we-can-help/uk-visas-and-migration/"
    )
    INVEST_UK_SETUP_GUIDE_ACCESS_FINANCE = InternationalUrl(
        "content/investment/how-we-can-help/access-finance-in-the-uk/"
    )
    INVEST_UK_SETUP_GUIDE_ESTABLISH_A_BASE = InternationalUrl(
        "content/investment/how-we-can-help/establish-a-base-for-business-in-the-uk/"
    )
    INVEST_UK_SETUP_GUIDE_HIRE_SKILLED_WORKERS = InternationalUrl(
        "content/investment/how-we-can-help/hire-skilled-workers-for-your-uk-operations/"  # noqa
    )
    INVEST_UK_SETUP_GUIDE_OPEN_BANK_ACCOUNT = InternationalUrl(
        "content/investment/how-we-can-help/open-a-uk-business-bank-account/"
    )
    INVEST_UK_SETUP_GUIDE_UK_TAX = InternationalUrl(
        "content/investment/how-we-can-help/uk-tax-and-incentives/"
    )
    INVEST_UK_SETUP_GUIDE_GET_SUPPORT_TO_MOVE_YOUR_TECH_BUSINESS_TO_THE_UK = InternationalUrl(
        "content/investment/how-we-can-help/global-entrepreneur-program/"
    )
    INVEST_UK_SETUP_GUIDE_REGISTER_A_COMPANY_IN_THE_UK = InternationalUrl(
        "content/investment/how-we-can-help/register-a-company-in-the-uk/"  # noqa
    )
    INVEST_UK_SETUP_GUIDE_OPEN_BUSINESS_BANK_ACCOUNT = InternationalUrl(
        "content/investment/how-we-can-help/open-a-uk-business-bank-account/"
    )


    # INVEST_UK_SETUP_GUIDE_DIT_CAPITAL_GAINS = InternationalUrl(
    #     "content/invest/how-to-setup-in-the-uk/uk-capital-gains-tax/"
    # )
    # INVEST_UK_SETUP_GUIDE_DIT_CORPORATION_TAX = InternationalUrl(
    #     "content/invest/how-to-setup-in-the-uk/uk-corporation-tax/"
    # )
    # INVEST_UK_SETUP_GUIDE_DIT_VENTURE_CAPITAL = InternationalUrl(
    #     "content/invest/how-to-setup-in-the-uk/uk-venture-capital-schemes/"
    # )
    # INVEST_UK_SETUP_GUIDE_UK_INCOME_TAX = InternationalUrl(
    #     "content/invest/how-to-setup-in-the-uk/uk-income-tax/"
    # )
    # INVEST_UK_SETUP_GUIDE_UK_INFRASTRUCTURE = InternationalUrl(
    #     "content/invest/how-to-setup-in-the-uk/uk-infrastructure/"
    # )
    INVEST_UK_SETUP_GUIDE_RESEARCH_AND_DEVELOPMENT = InternationalUrl(
        "content/investment/how-we-can-help/research-and-development-rd-support-in-the-uk/"
    )
    # INVEST_WHY_INVEST_IN_THE_UK =InvestUrl("/international/content/investment/why-invest-in-the-uk/")

    INVEST_WHY_INVEST_IN_THE_UK = InvestUrl("investment/")
    INVEST_LEGACY_REGIONS_MIDLANDS = LegacyInvestUrl("uk-regions/midlands/")
    INVEST_LEGACY_REGIONS_NORTHERN_IRELAND = LegacyInvestUrl(
        "uk-regions/northern-ireland/"
    )
    INVEST_LEGACY_REGIONS_SOUTH_ENGLAND = LegacyInvestUrl("uk-regions/south-england/")
    INVEST_LEGACY_REGIONS_NORTH_ENGLAND = LegacyInvestUrl("uk-regions/north-england/")
    INVEST_LEGACY_REGIONS_LONDON = LegacyInvestUrl("uk-regions/london/")
    INVEST_LEGACY_REGIONS_WALES = LegacyInvestUrl("uk-regions/wales/")
    INVEST_LEGACY_REGIONS_SCOTLAND = LegacyInvestUrl("uk-regions/scotland/")

    INVEST_INDUSTRIES_ADVANCED_MANUFACTURING = LegacyInvestUrl(
        "industries/advanced-manufacturing/"
    )
    INVEST_INDUSTRIES_AEROSPACE = LegacyInvestUrl("industries/aerospace/")
    INVEST_INDUSTRIES_AGRI_TECH = LegacyInvestUrl("industries/agri-tech/")
    INVEST_INDUSTRIES_ASSET_MANAGEMENT = LegacyInvestUrl("industries/asset-management/")
    INVEST_INDUSTRIES_AUTOMOTIVE = LegacyInvestUrl("industries/automotive/")
    INVEST_INDUSTRIES_AUTOMOTIVE_RESEARCH_AND_DEVELOPMENT = LegacyInvestUrl(
        "industries/automotive-research-and-development/"
    )
    INVEST_INDUSTRIES_AUTOMOTIVE_SUPPLY_CHAIN = LegacyInvestUrl(
        "industries/automotive-supply-chain/"
    )
    INVEST_INDUSTRIES_CAPITAL_INVESTMENT = LegacyInvestUrl(
        "industries/capital-investment/"
    )
    INVEST_INDUSTRIES_CHEMICALS = LegacyInvestUrl("industries/chemicals/")
    INVEST_INDUSTRIES_CREATIVE_CONTENT_AND_PRODUCTION = LegacyInvestUrl(
        "industries/creative-content-and-production/"
    )
    INVEST_INDUSTRIES_CREATIVE_INDUSTRIES = LegacyInvestUrl(
        "industries/creative-industries/"
    )
    INVEST_INDUSTRIES_DATA_ANALYTICS = LegacyInvestUrl("industries/data-analytics/")
    INVEST_INDUSTRIES_DIGITAL_MEDIA = LegacyInvestUrl("industries/digital-media/")
    INVEST_INDUSTRIES_ELECTRICAL_NETWORKS = LegacyInvestUrl(
        "industries/electrical-networks/"
    )
    INVEST_INDUSTRIES_ENERGY = LegacyInvestUrl("industries/energy/")
    INVEST_INDUSTRIES_ENERGY_WASTE = LegacyInvestUrl("industries/energy-waste/")
    INVEST_INDUSTRIES_FINANCIAL_SERVICES = LegacyInvestUrl(
        "industries/financial-services/"
    )
    INVEST_INDUSTRIES_FINANCIAL_TECHNOLOGY = LegacyInvestUrl(
        "industries/financial-technology/"
    )
    INVEST_INDUSTRIES_FOOD_AND_DRINK = LegacyInvestUrl("industries/food-and-drink/")
    INVEST_INDUSTRIES_FOOD_SERVICE_AND_CATERING = LegacyInvestUrl(
        "industries/food-service-and-catering/"
    )
    INVEST_INDUSTRIES_FREE_FOODS = LegacyInvestUrl("industries/free-foods/")
    INVEST_INDUSTRIES_HEALTH_AND_LIFE_SCIENCES = LegacyInvestUrl(
        "industries/health-and-life-sciences/"
    )
    INVEST_INDUSTRIES_MEAT_POULTRY_AND_DAIRY = LegacyInvestUrl(
        "industries/meat-poultry-and-dairy/"
    )
    INVEST_INDUSTRIES_MEDICAL_TECHNOLOGY = LegacyInvestUrl(
        "industries/medical-technology/"
    )
    INVEST_INDUSTRIES_MOTORSPORT = LegacyInvestUrl("industries/motorsport/")
    INVEST_INDUSTRIES_NUCLEAR_ENERGY = LegacyInvestUrl("industries/nuclear-energy/")
    INVEST_INDUSTRIES_OFFSHORE_WIND_ENERGY = LegacyInvestUrl(
        "industries/offshore-wind-energy/"
    )
    INVEST_INDUSTRIES_OIL_AND_GAS = LegacyInvestUrl("industries/oil-and-gas/")
    INVEST_INDUSTRIES_PHARMACEUTICAL_MANUFACTURING = LegacyInvestUrl(
        "industries/pharmaceutical-manufacturing/"
    )
    INVEST_INDUSTRIES_RETAIL = LegacyInvestUrl("industries/retail/")
    INVEST_INDUSTRIES_TECHNOLOGY = LegacyInvestUrl("industries/technology/")
    INVEST_SECTORS = InvestUrl("content/investment/sectors/")
    INVEST_UK_NATIONS_AND_REGIONS = InvestUrl("content/investment/regions/")

    # ISD -
    ISD_LANDING = ISDUrl("")
    ISD_SEARCH = ISDUrl("search/")

    # Legacy Contact-Us UI
    LEGACY_CONTACT_US_LANDING = LegacyContactUrl("")
    LEGACY_CONTACT_US_HELP = LegacyContactUrl("help/")
    LEGACY_CONTACT_US_FEEDBACK_FORM = LegacyContactUrl("help/FeedbackForm/")
    LEGACY_CONTACT_US_DIRECTORY_FEEDBACK_FORM = LegacyContactUrl(
        "directory/FeedbackForm"
    )

    # FAS/ISD Profile
    PROFILE_API_COMPANIES_HOUSE_SEARCH = ProfileUrl(
        "api/v1/companies-house-search/",
        template="api/v1/companies-house-search/?term={term}",
    )
    PROFILE_API_POSTCODE_SEARCH = ProfileUrl(
        "api/v1/postcode-search/?postcode={postcode}",
        template="api/v1/postcode-search/?postcode={postcode}",
    )
    PROFILE_HEALTHCHECK = ProfileUrl("healthcheck/")
    PROFILE_HEALTHCHECK_PING = ProfileUrl("healthcheck/ping/")
    PROFILE_SOO = ProfileUrl("selling-online-overseas/")
    PROFILE_BUSINESS_PROFILE = ProfileUrl("business-profile/")
    PROFILE_PERSONAL_PROFILE = ProfileUrl("personal-profile/")
    PROFILE_EXOPS_ALERTS = ProfileUrl("export-opportunities/email-alerts/")
    PROFILE_EXOPS_APPLICATIONS = ProfileUrl("export-opportunities/applications/")
    PROFILE_LANDING = ProfileUrl("")
    PROFILE_SITEMAP = ProfileUrl("sitemap.xml")
    PROFILE_ABOUT = ProfileUrl("about/")
    PROFILE_ADMIN_TRANSFER_OWNERSHIP = ProfileUrl("business-profile/admin/transfer/")
    PROFILE_ACCOUNT_ACCEPT_INVITATION = ProfileUrl(
        "account/collaborate/accept/?invite_key={invite_key}",
        template="account/collaborate/accept/?invite_key={invite_key}",
    )
    PROFILE_ACCOUNT_ADD_COLLABORATOR = ProfileUrl("business-profile/admin/invite/")
    PROFILE_ENROL = ProfileUrl("enrol/")
    PROFILE_ENROL_SELECT_BUSINESS_TYPE = ProfileUrl("enrol/business-type/")
    PROFILE_ENROL_RESEND_VERIFICATION_CODE = ProfileUrl(
        "enrol/resend-verification/verification/"
    )
    PROFILE_ENROL_REQUEST_RESEND_VERIFICATION_CODE = ProfileUrl(
        "enrol/resend-verification/resend/"
    )

    PROFILE_ENROL_USER_ACCOUNT = ProfileUrl(
        "enrol/business-type/companies-house/user-account/"
    )
    PROFILE_ENROL_EMAIL_VERIFICATION = ProfileUrl(
        "enrol/business-type/companies-house/verification/"
    )
    PROFILE_ENROL_COMPANIES_HOUSE_SEARCH = ProfileUrl(
        "enrol/business-type/companies-house/company-search/"
    )
    PROFILE_ENROL_BUSINESS_DETAILS = ProfileUrl(
        "enrol/business-type/companies-house/business-details/"
    )
    PROFILE_ENROL_PERSONAL_DETAILS = ProfileUrl(
        "enrol/business-type/companies-house/personal-details/"
    )
    PROFILE_ENROL_FINISHED = ProfileUrl("enrol/business-type/companies-house/finished/")

    PROFILE_ENROL_NON_CH_COMPANY_ENTER_USER_NAME_AND_PASSWORD = ProfileUrl(
        "enrol/business-type/non-companies-house-company/user-account/"
    )
    PROFILE_ENROL_NON_CH_COMPANY_EMAIL_VERIFICATION = ProfileUrl(
        "enrol/business-type/non-companies-house-company/verification/"
    )
    PROFILE_ENROL_NON_CH_COMPANY_ENTER_BUSINESS_DETAILS = ProfileUrl(
        "enrol/business-type/non-companies-house-company/address-search/"
    )
    PROFILE_ENROL_NON_CH_COMPANY_ENTER_PERSONAL_DETAILS = ProfileUrl(
        "enrol/business-type/non-companies-house-company/personal-details/"
    )
    PROFILE_ENROL_NON_CH_COMPANY_FINISHED = ProfileUrl(
        "enrol/business-type/non-companies-house-company/finished/"
    )
    PROFILE_ENROL_NON_CH_REQUEST_TO_VERIFY = ProfileUrl(
        "business-profile/verify/request/"
    )

    PROFILE_ENROL_INDIVIDUAL_START = ProfileUrl("enrol/business-type/individual/start/")
    PROFILE_ENROL_INDIVIDUAL_ENTER_YOUR_EMAIL_AND_PASSWORD = ProfileUrl(
        "enrol/business-type/individual/user-account/"
    )
    PROFILE_ENROL_INDIVIDUAL_EMAIL_VERIFICATION = ProfileUrl(
        "enrol/business-type/individual/verification/"
    )
    PROFILE_ENROL_INDIVIDUAL_UPDATE_YOUR_DETAILS = ProfileUrl(
        "enrol/?backfill-details-intent=true"
    )
    PROFILE_ENROL_INDIVIDUAL_ENTER_YOUR_PERSONAL_DETAILS = ProfileUrl(
        "enrol/business-type/individual/personal-details/"
    )
    PROFILE_ENROL_INDIVIDUAL_FINISHED = ProfileUrl(
        "enrol/business-type/individual/finished/"
    )

    PROFILE_ENROL_OVERSEAS_BUSINESS = ProfileUrl(
        "enrol/business-type/overseas-business/"
    )

    PROFILE_ADMIN = ProfileUrl("business-profile/admin/")
    PROFILE_ADMIN_REMOVE_PROFILE_FROM_ACCOUNT = ProfileUrl(
        "business-profile/admin/disconnect/"
    )
    PROFILE_EDIT_COMPANY_DESCRIPTION = ProfileUrl("business-profile/description/")
    PROFILE_EDIT_COMPANY_BUSINESS_DETAILS = ProfileUrl(
        "business-profile/business-details/"
    )
    PROFILE_PUBLISH_BUSINESS_PROFILE_TO_FAS = ProfileUrl("business-profile/publish/")
    PROFILE_ADD_PRODUCTS_AND_SERVICES = ProfileUrl(
        "business-profile/add-expertise/products-and-services/"
    )
    PROFILE_CASE_STUDY_EDIT = ProfileUrl(
        "business-profile/case-study/{case_number}/details/"
    )
    PROFILE_CASE_STUDY_DETAILS = ProfileUrl("business-profile/case-study/details/")
    PROFILE_CASE_STUDY_IMAGES = ProfileUrl("business-profile/case-study/images/")
    PROFILE_UPLOAD_LOGO = ProfileUrl("business-profile/logo/")
    PROFILE_COMPANY_EDIT_SOCIAL_MEDIA = ProfileUrl("business-profile/social-links/")

    # SOO UI Selling Online Overseas
    SOO_LANDING = SOOUrl("")
    SOO_SITEMAP = SOOUrl("sitemap.xml")
    SOO_SEARCH_RESULTS = SOOUrl("markets/results/")
    SOO_MARKETS_COUNT = SOOUrl("markets/count.json")
    SOO_MARKET_DETAILS = SOOUrl(
        "markets/details/", template="markets/details/{market}/"
    )

    # Trade Barriers
    TRADE_BARRIERS_LANDING = DomesticUrl("report-trade-barrier/")
    TRADE_BARRIERS_REPORT_FORM_ABOUT = DomesticUrl("report-trade-barrier/report/about/")
    TRADE_BARRIERS_REPORT_FORM_PROBLEM_DETAILS = DomesticUrl(
        "report-trade-barrier/report/problem-details/"
    )
    TRADE_BARRIERS_REPORT_FORM_SUMMARY = DomesticUrl(
        "report-trade-barrier/report/summary/"
    )
    TRADE_BARRIERS_REPORT_FORM_FINISHED = DomesticUrl(
        "report-trade-barrier/report/finished/"
    )
    TRADE_BARRIERS_REPORT_FORM_SUCCESS = DomesticUrl(
        "report-trade-barrier/report/success/"
    )

    # SSO UI
    SSO_LANDING = SSOUrl("")
    SSO_EMAIL_CONFIRM = SSOUrl("accounts/confirm-email/")
    SSO_INACTIVE = SSOUrl("accounts/inactive/")
    SSO_LOGIN = SSOUrl("accounts/login/", template="accounts/login/?next={next}")
    SSO_LOGOUT = SSOUrl("accounts/logout/")
    SSO_PASSWORD_CHANGE = SSOUrl("accounts/password/change/")
    SSO_PASSWORD_RESET = SSOUrl("accounts/password/reset/")
    SSO_PASSWORD_SET = SSOUrl("accounts/password/set/")
    SSO_SIGNUP = SSOUrl("accounts/signup/")

    # SSO API
    SSO_API_LANDING = SSOApiUrl("")
    SSO_API_HEALTHCECK = SSOApiUrl("api/v1/healthcheck/")
    SSO_API_HEALTHCHECK_PING = SSOApiUrl("api/v1/healthcheck/ping/")
    SSO_API_USER = SSOApiUrl("api/v1/session-user/")

    # Great Magna Pages
    GREAT_MAGNA_LANDING = GreatMagnaUrl("https://great.dev.uktrade.digital/")
    GREAT_MAGNA_HOME = GreatMagnaUrl("https://great.dev.uktrade.digital/")
    # GREAT_MAGNA_HOME = GreatMagnaUrl("https://great-magna.staging.uktrade.digital/")
    # GREAT_MAGNA_HOME = GreatMagnaUrl("https://magna-beta.great.uktrade.digital/")
    GREAT_MAGNA_START = GreatMagnaUrl("")
    GREAT_MAGNA_SIGNUP = GreatMagnaUrl("signup/", template="/signup/")
    GREAT_MAGNA_SIGNUP_LEARN_TO_EXPORT = GreatMagnaUrl("signup/", template="/signup/?next=/learn/categories/")
    GREAT_MAGNA_SIGNUP_WHERE_TO_EXPORT = GreatMagnaUrl("signup/", template="/signup/?next=/where-to-export/")
    GREAT_MAGNA_SIGNUP_MAKE_AN_EXPORT_PLAN = GreatMagnaUrl("signup/", template="/signup/?next=/export-plan/start/")

    GREAT_MAGNA_LOGIN = GreatMagnaUrl("login/")
    GREAT_MAGNA_FORGOTTEN_PASSWORD = GreatMagnaUrl("https://great.staging.uktrade.digital/sso/accounts/password/reset/")
    GREAT_MAGNA_LEARN_TO_EXPORT = GreatMagnaUrl("learn/categories/")
    GREAT_MAGNA_SEARCH = GreatMagnaUrl("search/")
    GREAT_MAGNA_DASHBOARD = GreatMagnaUrl("dashboard/")
    GREAT_MAGNA_SHOW_ME_AROUND = GreatMagnaUrl("dashboard/")
    GREAT_MAGNA_SIGN_OUT = GreatMagnaUrl("dashboard/")
    GREAT_MAGNA_PROFILE_ABOUT = GreatMagnaUrl("profile/about/")
    GREAT_MAGNA_CONTACT_US = GreatMagnaUrl("contact-us/help/")

    GREAT_MAGNA_WHERE_TO_EXPORT = GreatMagnaUrl("where-to-export/")

    GREAT_MAGNA_LESSONS_GET_STARTED = GreatMagnaUrl("learn/categories/getting-started/")
    GREAT_MAGNA_LESSONS_WHAT_YOULL_FIND_IN_EACH_LESSON = GreatMagnaUrl(
        "learn/categories/getting-started/introduction-learning/what-youll-find-each-lesson/")
    GREAT_MAGNA_LESSONS_INTRODUCTION_TO_LESSONS_AND_LEARNING = GreatMagnaUrl(
        "learn/categories/getting-started/lesson-basics/introduction-lessons-and-learning/")
    GREAT_MAGNA_LESSONS_NEW_LESSON_ADDED = GreatMagnaUrl(
        "learn/categories/getting-started/new-topic-added/new-lesson-added/")
    GREAT_MAGNA_LESSONS_HOW_LESSONS_CAN_HELP = GreatMagnaUrl(
        "learn/categories/getting-started/introduction-learning/how-lessons-can-help-you-make-export-plan/")

    GREAT_MAGNA_LESSONS_IDENTIFY_OPPORTUNITIES_AND_RESEARCH_THE_MARKET = GreatMagnaUrl(
        "learn/categories/market-research/")
    GREAT_MAGNA_LESSONS_CHOOSING_THE_RIGHT_EXPORT_OPPORTUNITIES = GreatMagnaUrl(
        "learn/categories/market-research/evaluate-opportunities/opportunity-right-you/")
    GREAT_MAGNA_LESSONS_MOVE_FROM_ACCIDENTAL_EXPORTING_TO_STRATEGIC_EXPORTING = GreatMagnaUrl(
        "learn/categories/market-research/evaluate-opportunities/move-accidental-exporting-strategic-exporting/")
    GREAT_MAGNA_LESSONS_IN_MARKET_RESEARCH = GreatMagnaUrl(
        "learn/categories/market-research/market-research-approaches/-market-research/")
    GREAT_MAGNA_LESSONS_ONLINE_RESEARCH = GreatMagnaUrl(
        "learn/categories/market-research/market-research-approaches/online-research/")
    GREAT_MAGNA_LESSONS_WORK_OUT_CUSTOMER_DEMAND = GreatMagnaUrl(
        "learn/categories/market-research/calculate-customer-demand/quantifying-customer-demand-how-much-might-you-sell/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_YOUR_MARKET_SIZE_AND_ITS_SEGMENTS = GreatMagnaUrl(
        "learn/categories/market-research/calculate-customer-demand/understand-your-market-size-and-its-segments/")
    GREAT_MAGNA_LESSONS_UNDERSTANDING_THE_COMPETITION = GreatMagnaUrl(
        "learn/categories/market-research/competitor-analysis/understanding-competitor-market-share-and-pricing/")
    GREAT_MAGNA_LESSONS_RESEARCH_CURRENT_MARKET_CONDITIONS = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/research-current-market-conditions/")
    # GREAT_MAGNA_LESSONS_USING_WHAT_YOU_KNOW = GreatMagnaUrl(
    #     "/learn/categories/market-research/calculate-customer-demand/using-what-you-know-to-help-inform-your-positioning-and-competitive-advantage/")
    # GREAT_MAGNA_LESSONS_UNDERSTAND_MARKET_TRENDS = GreatMagnaUrl(
    #     "/learn/categories/market-research/calculate-customer-demand/understand-market-trends/")
    # GREAT_MAGNA_LESSONS_UNDERSTAND_MARKET_BARRIERS = GreatMagnaUrl(
    #     "learn/categories/market-research/research-countries-and-choose-destination-markets/understand-market-barriers/")
    GREAT_MAGNA_LESSONS_EASE_OF_ENTRY_INTO_A_NEW_MARKET = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/how-assess-ease-entry-new-market/")
    GREAT_MAGNA_LESSONS_RESEARCH_LOCAL_INFRASTRUCTURE = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/local-infrastructure/")
    # GREAT_MAGNA_LESSONS_UNDERSTAND_HOW_YOU_MAY_NEED_TO_ADAPT_YOUR_PRODUCT_TO_MEET_INTERNATIONAL_STANDARDS = GreatMagnaUrl(
    #     "learn/categories/market-research/research-countries-and-choose-destination-markets/understand-how-you-may-need-adapt-your-product-meet-international-standards/")
    # GREAT_MAGNA_LESSONS_INFORMATION_YOU_NEED_TO_CHOOSE_A_TARGET_COUNTRY = GreatMagnaUrl(
    #     "learn/categories/market-research/research-countries-and-choose-destination-markets/information-you-need-choose-target-country/")
    GREAT_MAGNA_LESSONS_ADAPTING_YOUR_PRODUCT_OR_SERVICE = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/understand-how-you-may-need-adapt-your-product-meet-international-standards/")
    GREAT_MAGNA_LESSONS_INFORMATION_YOU_NEED_TO_CHOOSE_A_TARGET_COUNTRY = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/information-you-need-choose-target-country/")
    GREAT_MAGNA_LESSONS_CUSTOMER_DEMAND_VS_EASE_OF_ENTRY = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/plot-market-demand-against-ease-entry/")
    GREAT_MAGNA_LESSONS_RESEARCH_FREE_TRADE_AGREEMENTS = GreatMagnaUrl(
        "learn/categories/market-research/research-countries-and-choose-destination-markets/research-free-trade-agreements/")

    GREAT_MAGNA_LESSONS_PREPARE_TO_SELL_INTO_A_NEW_COUNTRY = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/")
    GREAT_MAGNA_LESSONS_CHOOSE_THE_RIGHT_ROUTE_TO_MARKET = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/choose-right-route-market/")
    GREAT_MAGNA_LESSONS_SELLING_DIRECT_TO_YOUR_CUSTOMER = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/sell-direct-your-customer/")
    GREAT_MAGNA_LESSONS_SELLING_WITH_INTERNATIONAL_E_COMMERCE = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/international-e-commerce/")
    GREAT_MAGNA_LESSONS_SETTING_UP_JOINT_VENTURES_ABROAD = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/set-joint-ventures-abroad/")
    GREAT_MAGNA_LESSONS_SETTING_UP_A_FRANCHISE_ABROAD = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/setting-franchise-abroad/")
    GREAT_MAGNA_LESSONS_USING_LICENSING = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/decide-whether-use-licensing/")
    GREAT_MAGNA_LESSONS_SETTING_UP_A_BUSINESS_ABROAD = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/how-set-business-abroad/")
    GREAT_MAGNA_LESSONS_USING_AN_AGENT_OR_DISTRIBUTOR = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/routes-to-market/when-use-agent-or-distributor/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_THE_LOCAL_BUSINESS_CULTURE = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/different-ways-of-doing-business-across-borders/understand-local-business-culture-your-target-market/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_PRODUCT_LIABILITY = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/manage-intellectual-property-and-legal-protection-risk/understanding-product-liability/")
    GREAT_MAGNA_LESSONS_PROTECT_YOUR_INTELLECTUAL_PROPERTY_ABROAD = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/manage-intellectual-property-and-legal-protection-risk/protect-your-intellectual-property-abroad/")
    GREAT_MAGNA_LESSONS_PREPARING_FOR_A_TRADE_MISSION = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-events/how-prepare-trade-mission/")
    GREAT_MAGNA_LESSONS_PREPARING_FOR_A_TRADE_SHOW_AS_AN_ATTENDEE = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-events/how-prepare-trade-show-attendee/")
    GREAT_MAGNA_LESSONS_GETTING_READY_FOR_A_TRADE_SHOW_AS_AN_EXHIBITOR = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-events/how-prepare-trade-show-exhibitor/")
    GREAT_MAGNA_LESSONS_ADAPTING_YOUR_WEBSITE_FOR_AN_INTERNATIONAL_AUDIENCE = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-online/how-adapt-your-website-international-audience/")
    GREAT_MAGNA_LESSONS_UNDERSTANDING_DIGITAL_MARKETING = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-online/understand-digital-marketing/")
    GREAT_MAGNA_LESSONS_USING_ONLINE_MARKETPLACES = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/finding-customers-and-marketing-online/using-online-marketplaces/")
    GREAT_MAGNA_LESSONS_PROTECT_YOUR_BUSINESS_FROM_BRIBERY_AND_CORRUPTION = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/managing-safety-corruption-and-business-integrity-risk/protect-your-business-bribery-and-corruption/")
    GREAT_MAGNA_LESSONS_HOW_TO_OPERATE_WITH_BUSINESS_INTEGRITY = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/managing-safety-corruption-and-business-integrity-risk/operating-business-integrity/")
    GREAT_MAGNA_LESSONS_PROTECT_YOUR_DATA_ABROAD = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/managing-safety-corruption-and-business-integrity-risk/protect-your-data-abroad/")
    GREAT_MAGNA_LESSONS_PITCHING_AND_TENDERING_IN_A_NEW_MARKET = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/winning-bids-and-expansion/pitching-and-tendering-in-a-new-market/")
    GREAT_MAGNA_HOW_TO_DRAFT_A_CONTRACT = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/winning-bids-and-expansion/how-draft-contract/")
    GREAT_MAGNA_LESSONS_USING_SAMPLES_PROTOTYPES_AND_DEMOS = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/winning-bids-and-expansion/using-samples-prototypes-and-demos/")
    GREAT_MAGNA_LESSONS_HOW_TO_HANDLE_PRICE_NEGOTIATIONS = GreatMagnaUrl(
        "learn/categories/prepare-sell-new-country/winning-bids-and-expansion/how-handle-price-negotiations/")

    GREAT_MAGNA_LESSONS_REGULATIONS_LICENSING_AND_LOGISTICS = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/")
    GREAT_MAGNA_LESSONS_HOW_TO_ADAPT_YOUR_LABELLING_AND_PACKAGING = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/get-your-goods-into-the-destination-country/labelling-and-packaging/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_DUTIES_AND_TAXES = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/get-your-goods-into-the-destination-country/understand-duties-and-taxes/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_LOCAL_MARKET_REGULATIONS_FOR_PRODUCTS = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/get-your-goods-into-the-destination-country/understand-local-market-regulations-products/")
    GREAT_MAGNA_LESSONS_USING_COMMODITY_CODES = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/get-your-goods-into-the-destination-country/using-commodity-codes/")
    GREAT_MAGNA_LESSONS_APPLYING_RULES_OF_ORIGIN_TO_YOUR_PRODUCT = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/get-your-goods-into-the-destination-country/applying-rules-of-origin-to-your-product/")
    GREAT_MAGNA_LESSONS_CHOOSE_WHICH_INCOTERMS_ARE_RIGHT_FOR_YOU = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/logistics-and-freight-forwarders/incoterms/")
    GREAT_MAGNA_LESSONS_USING_FREIGHT_FORWARDERS = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/logistics-and-freight-forwarders/freight-forwarders/")
    GREAT_MAGNA_LESSONS_REGULATIONS_AROUND_E_COMMERCE = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/understand-services-rules-and-regulations/regulations-around-e-commerce/")
    GREAT_MAGNA_LESSONS_REGULATIONS_AROUND_SUPPLYING_A_SERVICE = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/understand-services-rules-and-regulations/understand-regulations-around-supplying-service/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_DATA_REGULATIONS_AND_DATA_PROTECTION = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/understand-services-rules-and-regulations/understand-data-regulations-and-data-protection/")
    GREAT_MAGNA_LESSONS_HOW_TO_MAKE_A_UK_CUSTOMS_DECLARATION = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/get-your-good-out-uk/how-make-uk-customs-declaration/")
    GREAT_MAGNA_LESSONS_UNDERSTAND_EXPORT_LICENSING = GreatMagnaUrl(
        "learn/categories/selling-across-borders-product-and-services-regulations-licensing-and-logistics/get-your-good-out-uk/understand-export-licensing/")

    GREAT_MAGNA_LESSONS_FUNDING_FINANCE_AND_GETTING_PAID = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/")
    GREAT_MAGNA_LESSONS_CHOOSE_THE_RIGHT_FUNDING_AND_CREDIT_OPTIONS = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/manage-cash-flow/funding-and-credit-options-doing-business-across-borders/")
    GREAT_MAGNA_LESSONS_AVOID_CASHFLOW_CHALLENGES_WHEN_EXPORTING = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/manage-cash-flow/how-avoid-cashflow-challenges-when-exporting/")
    GREAT_MAGNA_LESSONS_INSURE_AGAINST_NON_PAYMENT = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/get-paid/insure-against-non-payment/")
    GREAT_MAGNA_LESSONS_CREATE_AN_EXPORT_INVOICE = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/get-paid/how-create-export-invoice/")
    GREAT_MAGNA_LESSONS_DECIDE_WHEN_TO_GET_PAID = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/get-paid/decide-when-get-paid-export-orders/")
    GREAT_MAGNA_LESSONS_CHOOSE_THE_RIGHT_PAYMENT_METHOD = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/get-paid/payment-methods-exporters/")
    GREAT_MAGNA_LESSONS_MANAGE_EXCHANGE_RATES = GreatMagnaUrl(
        "learn/categories/funding-financing-and-getting-paid/exchange-rates-and-moving-money/managing-exchange-rates/")

    GREAT_MAGNA_START_PRODUCT_MAKE_AN_EXPORT_PLAN = GreatMagnaUrl("export-plan/start/#/")
    GREAT_MAGNA_START_MARKET_MAKE_AN_EXPORT_PLAN = GreatMagnaUrl("export-plan/start/#/market")
    GREAT_MAGNA_NEW_EXPORT_PLAN = GreatMagnaUrl("export-plan/{page_id}/", template="export-plan/{page_id}/")

    GREAT_MAGNA_EXPORT_PLAN_DASHBOARD = GreatMagnaUrl("export-plan/dashboard/")
    GREAT_MAGNA_UPLOAD_LOGO = GreatMagnaUrl("export-plan/logo")
    GREAT_MAGNA_EXPORT_PLAN_ABOUT_YOUR_BUSINESS = GreatMagnaUrl(
        "export-plan/section/about-your-business/")
    GREAT_MAGNA_EXPORT_PLAN_BUSINESS_OBJECTIVES = GreatMagnaUrl(
        "export-plan/section/business-objectives/")
    GREAT_MAGNA_EXPORT_PLAN_MARKETING_APPROACH = GreatMagnaUrl(
        "export-plan/section/marketing-approach/")
    GREAT_MAGNA_EXPORT_PLAN_TARGET_MARKET_RESEARCH = GreatMagnaUrl(
        "export-plan/section/target-markets-research/")
    GREAT_MAGNA_EXPORT_PLAN_ADAPTING_YOUR_PRODUCT = GreatMagnaUrl(
        "export-plan/section/adapting-your-product/")
    GREAT_MAGNA_EXPORT_PLAN_COSTS_AND_PRICING = GreatMagnaUrl(
        "export-plan/section/costs-and-pricing/")
    GREAT_MAGNA_EXPORT_PLAN_FUNDING_AND_CREDIT = GreatMagnaUrl(
        "export-plan/section/funding-and-credit/")
    GREAT_MAGNA_EXPORT_PLAN_GETTING_PAID = GreatMagnaUrl(
        "export-plan/section/getting-paid/")
    GREAT_MAGNA_EXPORT_PLAN_TRAVEL_PLAN = GreatMagnaUrl(
        "export-plan/section/travel-plan/")
    GREAT_MAGNA_EXPORT_PLAN_BUSINESS_RISK = GreatMagnaUrl(
        "export-plan/section/business-risk/")
