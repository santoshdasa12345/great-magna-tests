# -*- coding: utf-8 -*-
"""Selectors for various common page components"""
import copy

from browserpages import ElementType
from browserpages.common_actions import By, Selector

from great_magna_tests_shared.constants import (
    MD5_CHECKSUM_EIG_LOGO,
    MD5_CHECKSUM_EVENTS_BIG_FOOTER_LOGO,
    MD5_CHECKSUM_EVENTS_BIG_HEADER_LOGO,
    MD5_CHECKSUM_GREAT_LOGO,
    MD5_CHECKSUM_INVEST_IN_GREAT,
)

DOMESTIC_HERO_WITH_LINK = {
    "hero": {
        "hero banner": Selector(By.ID, "hero"),
        "title": Selector(By.CSS_SELECTOR, "#hero h1"),
        "view export market guides": Selector(
            By.CSS_SELECTOR, "#hero a", type=ElementType.LINK
        ),
    }
}
DOMESTIC_HERO_WO_LINK = {
    "hero": {
        "hero banner": Selector(By.ID, "hero"),
        "title": Selector(By.CSS_SELECTOR, "#hero h1"),
        # "upskill now":Selector(By.CSS_SELECTOR, "#content > div:nth-child(3) > div > div.cta-container > a"),
    }
}

DOMESTIC_HEADER = {
    "header": {
        # cookie notice
        "itself": Selector(By.CSS_SELECTOR, "#header-cookie-notice", is_visible=False),
        "find out more about cookies": Selector(
            By.CSS_SELECTOR, "#header-cookie-notice a", is_visible=False
        ),
        # global header
        "global header": Selector(By.CSS_SELECTOR, "#great-header-logo"),
        "great global logo": Selector(By.CSS_SELECTOR, "#great-header-logo"),
        # "for uk businesses": Selector(By.ID, "great-global-header-domestic-link"),
        # "for international businesses": Selector(By.ID, "great-global-header-international-link"),
        # header menu
        "header menu": Selector(By.CSS_SELECTOR, ".menu"),
        "invest in great logo": Selector(By.XPATH, "//body/header/div[2]/div/a/img"),
        "advice": Selector(By.ID, "header-advice-desktop", type=ElementType.LINK),
        "markets": Selector(By.ID, "header-markets-desktop", type=ElementType.LINK),
        "services": Selector(By.ID, "header-services-desktop", type=ElementType.LINK),
        "search box": Selector(
            By.ID, "great-header-search-box", type=ElementType.INPUT
        ),
        "search button": Selector(
            By.CSS_SELECTOR,
            "#great-header-search-box ~ button",
            type=ElementType.BUTTON,
        ),
    }
}
COOKIE_BANNER = {
    "cookie banner": {
        "banner": Selector(
            By.CSS_SELECTOR, "div[aria-label='Cookies consent manager']"
        ),
        "accept all cookies": Selector(
            By.CSS_SELECTOR,
            "body > div.ReactModalPortal a[href='#']",
            type=ElementType.LINK,
        ),
        "reject all cookies": Selector(
            By.CSS_SELECTOR,
            "body > div.ReactModalPortal a.button[href$='cookies/']",
            type=ElementType.LINK,
        ),
    }
}
SSO_LOGGED_OUT = {
    "sso links - logged out": {
        "sign in": Selector(By.ID, "header-sign-in-link", is_visible=False)
    }
}

BETA_BAR = {
    "beta bar": {
        "itself": Selector(By.ID, "header-beta-bar"),
        "badge": Selector(By.CSS_SELECTOR, "#header-beta-bar .phase-tag"),
        "message": Selector(By.CSS_SELECTOR, "#header-beta-bar span"),
        "link": Selector(By.CSS_SELECTOR, "#header-beta-bar a"),
    }
}

BREADCRUMBS = {
    "breadcrumbs": {
        "itself": Selector(By.CSS_SELECTOR, ".breadcrumbs"),
        "current page": Selector(
            By.CSS_SELECTOR, ".breadcrumbs li[aria-current='page']"
        ),
        "links": Selector(By.CSS_SELECTOR, ".breadcrumbs a"),
    }
}

ERROR_REPORTING = {
    "error reporting": {
        "itself": Selector(By.CSS_SELECTOR, "section.error-reporting"),
        "report a problem with the page": Selector(
            By.ID, "error-reporting-section-contact-us"
        ),
    }
}

ERP_HEADER = {
    "header": {
        "header itself": Selector(By.CSS_SELECTOR, "header.govuk-header"),
        "skip-link": Selector(
            By.ID, "skip-link", type=ElementType.LINK, is_visible=False
        ),
        "home link": Selector(By.CSS_SELECTOR, "header.govuk-header a"),
        "gov uk logo": Selector(By.CSS_SELECTOR, "header.govuk-header a svg"),
    }
}
ERP_BACK = {
    "go back": {
        "go back": Selector(
            By.CSS_SELECTOR,
            "#content form[method=post] a.govuk-back-link",
            type=ElementType.LINK,
        )
    }
}
ERP_BETA = {
    "beta bar": {
        "beta bar itself": Selector(By.CSS_SELECTOR, "#content div.govuk-phase-banner"),
        "beta": Selector(By.CSS_SELECTOR, "#content div.govuk-phase-banner p strong"),
        "text": Selector(By.CSS_SELECTOR, "#content div.govuk-phase-banner p span"),
        "feedback": Selector(By.CSS_SELECTOR, "#content div.govuk-phase-banner p a"),
    }
}
ERP_BETA_SHORT = {
    "beta bar": {
        "beta bar itself": Selector(By.CSS_SELECTOR, "#content div.govuk-phase-banner"),
        "beta": Selector(By.CSS_SELECTOR, "#content div.govuk-phase-banner p strong"),
        "text": Selector(By.CSS_SELECTOR, "#content div.govuk-phase-banner p span"),
    }
}
ERP_BREADCRUMBS = {
    "breadcrumbs": {
        "breadcrumbs bar": Selector(By.CSS_SELECTOR, "#content nav.breadcrumbs"),
        "first": Selector(
            By.CSS_SELECTOR, "#content nav.breadcrumbs ol li:nth-child(1) a"
        ),
        "second": Selector(
            By.CSS_SELECTOR, "#content nav.breadcrumbs ol li:nth-child(2)"
        ),
    }
}
ERP_SAVE_FOR_LATER = {
    "save for later": {
        "save for later": Selector(
            By.CSS_SELECTOR,
            "button[name=wizard_save_for_later]",
            type=ElementType.BUTTON,
        )
    }
}
ERP_HIERARCHY_CODES = {
    "hierarchy codes": {
        "hierarchy codes heading": Selector(By.ID, "hierarchy-browser"),
        "first level": Selector(
            By.CSS_SELECTOR, "ul.app-hierarchy-tree li.app-hierarchy-tree__section"
        ),
    }
}
ERP_SEARCH_FORM = {
    "form": {
        "form itself": Selector(By.CSS_SELECTOR, "#content form[method='post']"),
        "step counter": Selector(
            By.CSS_SELECTOR, "form[method=post] span.govuk-caption-l"
        ),
        "heading": Selector(By.CSS_SELECTOR, "form[method=post] h1"),
        "find a commodity code information page": Selector(
            By.CSS_SELECTOR, "form[method=post] div.govuk-inset-text a"
        ),
        "search": Selector(By.ID, "id_product-search-term", type=ElementType.INPUT),
        "search button": Selector(
            By.CSS_SELECTOR,
            "#id_product-search-term ~ button[form=search-form]",
            type=ElementType.BUTTON,
        ),
        "submit": Selector(
            By.CSS_SELECTOR,
            "#content > form button.govuk-button",
            type=ElementType.BUTTON,
        ),
    }
}
ERP_SEARCH_RESULTS = {
    "search results": {
        "expand to select": Selector(
            By.CSS_SELECTOR, "h2#search-results-title ~ section a"
        ),
        "select product code": Selector(
            By.CSS_SELECTOR, "h2#search-results-title ~ section button"
        ),
    }
}
ERP_PRODUCT_DETAIL_FORM = {
    "form": {
        "selection form": Selector(By.CSS_SELECTOR, "#content form[method='post']"),
        "step counter": Selector(
            By.CSS_SELECTOR, "form[method=post] span.govuk-caption-l"
        ),
        "heading": Selector(By.CSS_SELECTOR, "form[method=post] h1"),
        "change goods": Selector(
            By.CSS_SELECTOR, "#selected-values-container a", type=ElementType.LINK
        ),
        "continue": Selector(
            By.CSS_SELECTOR,
            "#content > form button.govuk-button",
            type=ElementType.SUBMIT,
        ),
    }
}
ERP_FOOTER = {
    "footer": {
        "footer itself": Selector(By.CSS_SELECTOR, "footer.govuk-footer"),
        "ogl logo": Selector(By.CSS_SELECTOR, "footer.govuk-footer svg"),
        "licence note": Selector(By.CSS_SELECTOR, "footer.govuk-footer span"),
        "crown logo": Selector(
            By.CSS_SELECTOR, "footer.govuk-footer a.govuk-footer__copyright-logo"
        ),
    }
}

DOMESTIC_FOOTER = {
    "footer": {
        # "great footer logo": Selector(By.ID, "great-footer-great-logo"),
        "contact us": Selector(
            By.CSS_SELECTOR, "#great-footer > nav > ul > li:nth-child(1) > a"
        ),
        "privacy and cookies": Selector(
            By.CSS_SELECTOR, "#great-footer > nav > ul > li:nth-child(2) > a"
        ),
        "terms and conditions": Selector(
            By.CSS_SELECTOR, "#great-footer > nav > ul > li:nth-child(3) > a"
        ),
        "performance": Selector(
            By.CSS_SELECTOR, "#great-footer > nav > ul > li:nth-child(5) > a"
        ),
        "department for international trade on gov.uk": Selector(
            By.CSS_SELECTOR, "#great-footer > nav > ul > li:nth-child(6) > a"
        ),
        "go to the page for international businesses": Selector(
            By.ID, "#great-footer > nav > ul > li:nth-child(7) > a"
        ),
        "dit footer logo": Selector(By.ID, "#great-global-footer-logo"),
        "copyright notice": Selector(By.CSS_SELECTOR, "#great-footer-copyright"),
    }
}

FAVICON = Selector(By.CSS_SELECTOR, "link[rel='shortcut icon']")
EXOPPS_FAVICON = Selector(By.CSS_SELECTOR, "link[rel='icon']")
EIG_LOGO = Selector(By.CSS_SELECTOR, "#great-header-logo > img")
SIGN_IN_LINK = Selector(By.ID, "header-sign-in-link")

LOGOS = {
    "eig": {"selector": EIG_LOGO, "md5": MD5_CHECKSUM_EIG_LOGO},
    "great - header": {
        "selector": Selector(
            By.CSS_SELECTOR, "body > header > div.atlas-header__main > div > a"
        ),
        "md5": MD5_CHECKSUM_GREAT_LOGO,
    },
    "great - footer": {
        "selector": Selector(
            By.CSS_SELECTOR,
            "#great-footer > div.atlas-footer__main > div:nth-child(1) > div > img",
        ),
        "md5": MD5_CHECKSUM_GREAT_LOGO,
    },
    "invest in great - header": {
        "selector": Selector(
            By.CSS_SELECTOR, "body > header > div.atlas-header__main > div > a"
        ),
        "md5": MD5_CHECKSUM_INVEST_IN_GREAT,
    },
    "events business is great - header": {
        "selector": Selector(By.CSS_SELECTOR, "header img"),
        "md5": MD5_CHECKSUM_EVENTS_BIG_HEADER_LOGO,
    },
    "events business is great - footer": {
        "selector": Selector(By.CSS_SELECTOR, "#footer_section img"),
        "md5": MD5_CHECKSUM_EVENTS_BIG_FOOTER_LOGO,
    },
}

INTERNATIONAL_HEADER = {
    "header": {
        # cookie notice
        "itself": Selector(By.CSS_SELECTOR, "#header-cookie-notice", is_visible=False),
        "find out more about cookies": Selector(
            By.CSS_SELECTOR, "#header-cookie-notice a", is_visible=False
        ),
        # global header
        "global header": Selector(
            By.CSS_SELECTOR, "body > header > div.atlas-header__main > div"
        ),
        "great global logo": Selector(By.XPATH, "//body/header/div[2]/div/a"),
        # "for uk businesses": Selector(By.ID, "great-global-header-domestic-link"),
        # "for international businesses": Selector(By.ID, "great-global-header-international-link"),
        # Logo
        "invest in great logo": Selector(By.XPATH, "//body/header/div[2]/div/a"),
        # language selector
        # "language selector": Selector(By.ID, "great-header-language-select", type=ElementType.SELECT),
        # main menu
        "header menu": Selector(
            By.CSS_SELECTOR, "body > header > div.atlas-header__main"
        ),
        "invest in the uk": Selector(
            By.LINK_TEXT, "Invest in the UK", type=ElementType.LINK
        ),
        # "expand to the uk": Selector(
        #     By.LINK_TEXT, "Expand to the UK", type=ElementType.LINK
        # ),
        # "invest capital in the uk": Selector(
        #     By.LINK_TEXT, "Invest capital in the UK", type=ElementType.LINK
        # ),
        "buy from the uk": Selector(
            By.LINK_TEXT, "Buy from the UK", type=ElementType.LINK
        ),
        "contact": Selector(By.LINK_TEXT, "Contact", type=ElementType.LINK),
    }
}
INTERNATIONAL_HEADER_WO_LANGUAGE_SELECTOR = copy.deepcopy(INTERNATIONAL_HEADER)
# INTERNATIONAL_HEADER_WO_LANGUAGE_SELECTOR["header"].pop("language selector")

INTERNATIONAL_FOOTER = {
    "footer": {
        "DIT logo": Selector(
            By.CSS_SELECTOR,
            "#great-footer > div.atlas-footer__main > div:nth-child(1) > div > img",
        ),
        "great footer logo": Selector(
            By.CSS_SELECTOR,
            "#great-footer > div.atlas-footer__main > div:nth-child(1) > div",
        ),
        "contact us": Selector(
            By.PARTIAL_LINK_TEXT, "Contact us", type=ElementType.LINK
        ),
        "privacy and cookies": Selector(
            By.PARTIAL_LINK_TEXT, "Privacy and cookies", type=ElementType.LINK
        ),
        "terms and conditions": Selector(
            By.CSS_SELECTOR, "#footer-terms-and-conditions"
        ),
        # "accessibility" : Selector(By.PARTIAL_LINK_TEXT, "Accessibility", type=ElementType.LINK),
        "department for international trade on gov.uk": Selector(
            By.CSS_SELECTOR, "#footer-dit"
        ),
        # "go to the page for uk businesses": Selector(By.CSS_SELECTOR, "#footer-domestic"),
        # "HM Government": Selector(By.CSS_SELECTOR, "#great-global-footer-logo"),
        "copyright notice": Selector(
            By.CSS_SELECTOR, "#great-footer > div.atlas-footer__global > div > p"
        ),
    }
}

INTERNATIONAL_HERO = {
    "hero": {
        "itself": Selector(By.CSS_SELECTOR, "#content > div.atlas-hero"),
        "heading": Selector(By.CSS_SELECTOR, "#content > div.atlas-hero__heading"),
    }
}

INVEST_HEADER = {
    "header": {
        # sub menu
        "header sub menu": Selector(
            By.CSS_SELECTOR, "body > header > div.atlas-subnav > div > nav"
        ),
        "why invest in the uk": Selector(
            By.PARTIAL_LINK_TEXT, "Why invest in the UK?", type=ElementType.LINK
        ),
        "how we can help": Selector(
            By.PARTIAL_LINK_TEXT, "How we can help", type=ElementType.LINK
        ),
        "uk nations and regions": Selector(
            By.PARTIAL_LINK_TEXT, "UK nations and regions", type=ElementType.LINK
        ),
        "sectors": Selector(By.PARTIAL_LINK_TEXT, "Sectors", type=ElementType.LINK),
        "investment opportunities": Selector(
            By.PARTIAL_LINK_TEXT, "Investment opportunities", type=ElementType.LINK
        ),
        "contact": Selector(By.PARTIAL_LINK_TEXT, "Contact", type=ElementType.LINK),
    }
}
# merge Invest header sub-menu with main International header
INVEST_HEADER["header"] = {**INVEST_HEADER["header"], **INTERNATIONAL_HEADER["header"]}

INVEST_HERO = {
    "hero": {
        "self": Selector(By.CSS_SELECTOR, "#content > div.atlas-hero"),
        "heading": Selector(By.CSS_SELECTOR, "#content > div.atlas-hero__heading"),
        "get in touch": Selector(
            By.CSS_SELECTOR,
            "#content > section.atlas-bg.atlas-bg--dark-blue.atlas-colour--white > div > a",
            type=ElementType.LINK,
        ),
    }
}

INVEST_FOOTER = {
    "footer": {
        "great footer logo": Selector(
            By.CSS_SELECTOR,
            "#great-footer > div.atlas-footer__main > div:nth-child(1) > div",
        ),
        "contact us": Selector(
            By.PARTIAL_LINK_TEXT, "Contact us", type=ElementType.LINK
        ),
        "privacy and cookies": Selector(By.CSS_SELECTOR, "#footer-privacy-and-cookies"),
        "terms and conditions": Selector(
            By.CSS_SELECTOR, "#footer-terms-and-conditions"
        ),
        "department for international trade on gov.uk": Selector(
            By.CSS_SELECTOR, "#footer-dit"
        ),
        # "go to the page for uk businesses": Selector(By.ID, "footer-domestic"),
        "dit footer logo": Selector(
            By.CSS_SELECTOR, "#great-footer > div.atlas-footer__global > div > img"
        ),
        "copyright notice": Selector(
            By.CSS_SELECTOR, "#great-footer > div.atlas-footer__global > div > p"
        ),
    }
}

ABOUT_UK_SUBHEADER = {
    "about the uk subheader": {
        "about uk subheader itself": Selector(
            By.CSS_SELECTOR,
            "div.great-sub-header > nav",
        ),
        "overview": Selector(
            By.CSS_SELECTOR,
            "div.great-sub-header > nav li:nth-child(1) a",
        ),
        "why choose the uk": Selector(
            By.CSS_SELECTOR,
            "div.great-sub-header > nav li:nth-child(2) a",
        ),
        "industries": Selector(
            By.CSS_SELECTOR,
            "div.great-sub-header > nav li:nth-child(3) a",
        ),
        "regions": Selector(
            By.CSS_SELECTOR,
            "div.great-sub-header > nav li:nth-child(4) a",
        ),
        "contact us": Selector(
            By.CSS_SELECTOR,
            "div.great-sub-header > nav li:nth-child(5) a",
        ),
    }
}

ABOUT_US_SUBHEADER = {
    "about us subheader": {
        "about us subheader itself": Selector(
            By.CSS_SELECTOR,
            "div.great-sub-header > nav",
        ),
        "overview": Selector(
            By.CSS_SELECTOR,
            "div.great-sub-header > nav li:nth-child(1) a",
        ),
        "contact us": Selector(
            By.CSS_SELECTOR,
            "div.great-sub-header > nav li:nth-child(2) a",
        ),
    }
}

FAS_HEADER = {
    "fas header": {
        "fas header itself": Selector(
            By.CSS_SELECTOR, "body > header > div.atlas-subnav > div"
        ),
        "how we help": Selector(
            By.CSS_SELECTOR,
            "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(1) > a",
        ),
        "find a supplier": Selector(
            By.CSS_SELECTOR,
            "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(2) > a",
        ),
        "contact us": Selector(
            By.CSS_SELECTOR,
            "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(3) > a",
        ),
    }
}

INVEST_IN_THE_UK = {
    "invest in the uk": {
        "itself": Selector(By.CSS_SELECTOR, "#atlas-nav > ul > li:nth-child(1) > a"),
        "why invest in the uk": Selector(
            By.CSS_SELECTOR,
            "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(1) > a",
        ),
        "uk nations and regions": Selector(
            By.CSS_SELECTOR,
            "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(2) > a",
        ),
        "sectors": Selector(
            By.CSS_SELECTOR,
            "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(3) > a",
        ),
        "investment opportunities": Selector(
            By.CSS_SELECTOR,
            "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(4) > a",
        ),
        "how we can help": Selector(
            By.CSS_SELECTOR,
            "body > header > div.atlas-subnav > div > nav > ul > li:nth-child(5) > a",
        ),
    }
}

FAS_HERO = {
    "hero": {
        "itself": Selector(By.CSS_SELECTOR, "#content > div.atlas-hero"),
        "heading": Selector(By.CSS_SELECTOR, "#content > div.atlas-hero__heading"),
    }
}

GREAT_MAGNA_HEADER = {
    "header": {
        # great magna header
        "great magna header": Selector(
            By.CSS_SELECTOR, "#header > div.container.container-fluid"
        ),
        "great magna logo": Selector(By.CSS_SELECTOR, "#header-logo-link"),
        # header menu
        "header menu": Selector(
            By.CSS_SELECTOR, "#header-link-user-profile > div > button"
        ),
        "dashbaord": Selector(
            By.CSS_SELECTOR,
            "#header > div.container.container-fluid > nav > ul > li > a",
        ),
        "learn to export": Selector(
            By.ID, "header-link-learning", type=ElementType.LINK
        ),
        "where to export": Selector(
            By.ID, "header-link-markets", type=ElementType.LINK
        ),
        "make an export plan": Selector(
            By.ID, "header-link-exporting-plan", type=ElementType.LINK
        ),
        "search box": Selector(
            By.ID, "magna-header-search-box", type=ElementType.INPUT
        ),
        "search button": Selector(
            By.CSS_SELECTOR,
            "#magna-header-search-form > button",
            type=ElementType.BUTTON,
        ),
        # sub nav menu
        "personalisation bar": Selector(
            By.CSS_SELECTOR, "#header > div.bg-blue-deep-80.shared-personalisation-bar"
        ),
        "my products": Selector(
            By.CSS_SELECTOR, "#set-product-button > span:nth-child(1) > button"
        ),
        "my markets": Selector(
            By.CSS_SELECTOR, "#set-country-button > span > span > button"
        ),
    }
}

GREAT_MAGNA_FOOTER = {
    "footer": {
        "itself": Selector(By.CSS_SELECTOR, "#footer"),
        "contact us": Selector(
            By.CSS_SELECTOR, "#footer > nav > ul > li:nth-child(1) > a"
        ),
        "privacy and cookies": Selector(
            By.CSS_SELECTOR, "#footer > nav > ul > li:nth-child(2) > a"
        ),
        "terms and conditions": Selector(
            By.CSS_SELECTOR, "#footer > nav > ul > li:nth-child(3) > a"
        ),
        "accessibility": Selector(
            By.CSS_SELECTOR, "#footer > nav > ul > li:nth-child(4) > a"
        ),
        "performance": Selector(
            By.CSS_SELECTOR, "#footer > nav > ul > li:nth-child(5) > a"
        ),
        "department for international trade on gov.uk": Selector(
            By.CSS_SELECTOR, "#footer > nav > ul > li:nth-child(6) > a"
        ),
        "go to the page for international businesses": Selector(
            By.ID, "#footer > nav > ul > li:nth-child(7) > a"
        ),
        "dit footer logo": Selector(
            By.ID, "#footer > div > div.magna-footer__dit-logo > img"
        ),
        "copyright notice": Selector(
            By.CSS_SELECTOR, "#footer > div > div.magna-footer__copy > p"
        ),
    }
}
