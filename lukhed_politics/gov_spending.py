from lukhed_basic_utils import requestsCommon as rC

class USSpending:
    def __init__(self):
        """
        https://api.usaspending.gov/docs/endpoints

        https://www.usaspending.gov/data/Basic-API-Training.pdf

        """
        pass

    def get_agency_award_counts(self):
        url = 'https://api.usaspending.gov/api/v2/agency/awards/count/'
        data = rC.request_json(url)

        return data['results']
    


if __name__ == "__main__":
    US = USSpending()
    US.get_agency_award_counts()