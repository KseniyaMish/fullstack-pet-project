import allure

def attach_response(response):
    allure.attach(
        str(response.status_code),
        name="Status Code",
        attachment_type=allure.attachment_type.TEXT
    )
    allure.attach(
        response.text,
        name="Response Body",
        attachment_type=allure.attachment_type.JSON
    )

def step_request(name):
    return allure.step(f"Send request: {name}")

def step_check_status():
    return allure.step("Check response status code")

def step_validate_body():
    return allure.step("Validate response body content")
