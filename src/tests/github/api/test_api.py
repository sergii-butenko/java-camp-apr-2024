def test_positive_search_bad_approach():
    # GET requests 
    # URL: /search/repositories
    # query params: q = 'TEST_DATA'
    pass


def test_negative_search_bad_approach():
    # GET requests 
    # URL: /search/repositories
    # query params: q = 'Null'
    pass


@Test JUNIT
def test_positive_search_good_approach():
    # step1 - establish connection to server
    # step2 - send API request with search pattern TEST_DATA
    # validate results
    GitHubAPIClient = GitHubApiClient()
    results = GitHubAPIClient.searchRepos("TEST_DATA")

    assert len(results) != 0 


def test_negative_search_good_approach():
    # step1 - establish connection to server
    # step2 - send API request with search pattern Null
    # validate results
    
    GitHubAPIClient = GitHubApiClient()
    results = GitHubAPIClient.searchRepos("laksjdoifjaoijsdoifaoijsdoifjoaijsdoifjaoijsdofijoaijsdofijaosidjf")

    assert len(results) == 0




