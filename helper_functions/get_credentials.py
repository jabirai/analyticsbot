import yaml

class get_credentials:
    def __init__(self):
        with open("./required_files/config.yaml", "r") as file:
            credentials = yaml.safe_load(file)
        self.credentials = credentials

    def get_api_key(self):
        """Returns api key that is in config."""
        if self.credentials["openAI"]["api_key"] is not None:
            api_key = self.credentials["openAI"]["api_key"]
            return api_key
        else:
            raise Warning(
                "No API key found in config.yaml, if you are not using openAI models, ignore this warning.")

    def get_db_conn(self):
        """Returns DB uri,db name."""
        return self.credentials["DB"]
