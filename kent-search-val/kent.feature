Feature: The search bar is working

  Scenario: look for chem jobs 
     Given we have opened kent jobs
      when we search for "chemistry"
       and scrape the search results
      then we will find a jobs
       and we will close the browser

  Scenario: look for physics job
     Given we have opened kent jobs
      when we search for "physics"
       and scrape the search results
      then we will find a jobs
       and we will close the browser
