"""AWS Service Availability Scraper."""

from typing import Dict, List, Tuple

import json
import os
import time

import requests


class AwsServiceAvailability:
    """AWS Service Availability Scraper."""

    REGION_FILE = "aws-region-map.json"

    def __init__(self, ttl: int = 60 * 60 * 24 * 7):
        """Initialize the scraper."""
        # Create file if it doesn't exist
        if not os.path.isfile(self.REGION_FILE):
            self.region_data = self._fetch_region_json(self.REGION_FILE)
        # Update file if it is older than the TTL (default 1 week)
        else:
            file_age = time.time() - os.path.getmtime(self.REGION_FILE)
            if file_age > ttl:
                self.region_data = self._fetch_region_json(self.REGION_FILE)
            else:
                with open(self.REGION_FILE, encoding="utf-8") as open_file:
                    self.region_data = open_file.read()

    def get_unsupported_services(self, region: str) -> List[str]:
        """Return a list of unsupported services."""
        regions, services, region_map = self.parse_region_json(self.region_data)

        # Invalid input handling
        if region not in regions:
            raise ValueError(f"Error: Region not found: {region}")

        supported_services: List[str] = region_map[region]
        unsupported_services: List[str] = []
        for svc in services:
            if svc not in supported_services:
                unsupported_services.append(svc)
        return unsupported_services

    def get_supported_services(self, region: str) -> List[str]:
        """Return a list of supported services."""
        regions, _services, region_map = self.parse_region_json(self.region_data)

        # Invalid input handling
        if region not in regions:
            raise ValueError(f"Error: Region not found: {region}")

        supported_services: List[str] = region_map[region]
        supported_services.sort()
        return supported_services

    def _fetch_region_json(self, region_file_name: str) -> str:
        """Fetch AWS' own region map."""
        print("Fetching latest region map from AWS...")
        url: str = "https://api.regional-table.region-services.aws.a2z.com/index.json"
        with open(region_file_name, "w", encoding="utf-8") as open_file:
            req = requests.get(url, allow_redirects=True)
            region_data = req.text
            open_file.write(region_data)
        return region_data

    def parse_region_json(self, region_data: str) -> Tuple[List[str], List[str], Dict[str, List[str]]]:
        """Parse AWS' region map JSON."""
        regions: Dict[str, bool] = {}
        services: Dict[str, bool] = {}
        region_map: Dict[str, List[str]] = {}
        data = json.loads(region_data)
        for price in data["prices"]:
            service_name = price["attributes"]["aws:serviceName"].strip()
            regions[price["attributes"]["aws:region"]] = True
            services[service_name] = True
            if not price["attributes"]["aws:region"] in region_map:
                region_map[price["attributes"]["aws:region"]] = []
            region_map[price["attributes"]["aws:region"]].append(service_name)

        services_list: List[str] = list(services.keys())
        services_list.sort()
        regions_list: List[str] = list(regions.keys())
        regions_list.sort()

        return regions_list, services_list, region_map
