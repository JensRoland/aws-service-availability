"""Tests for scraper."""
from unittest import mock

import pytest

from aws_service_availability.scraper import AwsServiceAvailability

CODEDEPLOY = "AWS CodeDeploy"
DEEPRACER = "AWS DeepRacer"
HONEYCODE = "Amazon Honeycode"


def mock_fetch_region_json(_self: AwsServiceAvailability, _region_file_name: str) -> str:
    """Mock fetch_region_json."""
    with open("tests/test-aws-region-map.json", encoding="utf-8") as open_file:
        test_region_data = open_file.read()
    return test_region_data


@pytest.mark.parametrize(
    ("region", "function_name", "expected_found", "expected_missing"),
    [
        ("eu-west-1", "get_supported_services", CODEDEPLOY, HONEYCODE),
        ("eu-west-1", "get_unsupported_services", HONEYCODE, CODEDEPLOY),
        ("eu-north-1", "get_unsupported_services", HONEYCODE, CODEDEPLOY),
        ("us-west-1", "get_supported_services", CODEDEPLOY, HONEYCODE),
        ("us-east-1", "get_unsupported_services", HONEYCODE, CODEDEPLOY),
        ("us-west-2", "get_unsupported_services", DEEPRACER, CODEDEPLOY),
    ],
)
def test_scraper(region, function_name, expected_found, expected_missing):
    """Test the scraper using a previous region map."""
    with mock.patch.object(AwsServiceAvailability, "_fetch_region_json", new=mock_fetch_region_json):
        scraper = AwsServiceAvailability()
        results = getattr(scraper, function_name)(region)
        assert expected_found in results
        assert expected_missing not in results
