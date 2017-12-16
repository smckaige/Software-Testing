from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@given(u'we have opened kent jobs')
def step_impl(context):
    context.browser = webdriver.PhantomJS()
    context.browser.get("http://jobs.kent.edu/cw/en-us/listing/")
    assert "kent" in context.browser.title

@when(u'we search for "{target}"')
def step_impl(context, target):
    assert "kent" in context.browser.title
    input_element = context.browser.find_element_by_id('search-keyword')
    assert input_element != None  
    input_element.clear()
    input_element.send_keys(target)
    input_element.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "kent" in context.browser.title

@when(u'scrape the search results')
def step_impl(context):
    assert "kent" in context.browser.title
    while(len(context.browser.find_elements_by_css_selector('#recent-jobs > p > a'))>0):
        if(context.browser.find_element_by_css_selector('#recent-jobs > p > a').is_displayed()==0):
            break
        context.browser.find_element_by_css_selector('#recent-jobs > p > a').click()
        time.sleep(2)
    result=context.browser.find_element_by_id("search-results-content")
    assert result != None

    items=context.browser.find_elements_by_tag_name("tr")
    assert type(items) is list
    assert len(items) >= 1
    result = []
    for item in items:
        cell = item.find_elements_by_tag_name("td")
        if len(cell) == 5:
            result.append(cell[1].text)
    context.res = result

@then(u'we will find a jobs')
def step_impl(context):
    print(context.res)
    assert len(context.res)>=1

@then(u'we will close the browser')
def step_impl(context):
    context.browser.close()

