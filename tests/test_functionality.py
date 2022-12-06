from application import application

def test_case1():
    """
    Input Text: Mark Zuckerberg is unveiled to be an alien
    Type: Fake
    Expected Result: 1
    """
    tester = application.test_client()
    response = tester.get("/detector?text=Mark Zuckerberg is unveiled to be an alien")

    assert response.status_code == 200
    assert response.output == 1


def test_case2():
    """
    Input Text: UofT has changed its full name to University of Tears
    Type: Fake
    Expected Result: 1
    """
    tester = application.test_client()
    response = tester.get("/detector?text=UofT has changed its full name to University of Tears")

    assert response.status_code == 200
    assert response.output == 1


def test_case3():
    """
    Input Text: The Federal Reserve will continue to raise interest rates in 2023
    Type: Real
    Expected Result: 0
    """

    tester = application.test_client()
    response = tester.get("/detector?text=The Federal Reserve will continue to raise interest rates in 2023")

    assert response.status_code == 200
    assert response.output == 0


def test_case4():
    """
    Input Text: Salesforce Co-CEO Bret Taylor is going to step down
    Type: Real
    Expected Result: 0
    """
    tester = application.test_client()
    response = tester.get("/detector?text=Salesforce Co-CEO Bret Taylor is going to step down")

    assert response.status_code == 200
    assert response.output == 0

