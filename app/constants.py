__author__ = 'rabia'

from app import settings

#------------ General Constants -----------------
TEXT_ALREADY_EXISTS = "Already Exists"
TEXT_DOES_NOT_EXISTS = "Does Not Exists"
TEXT_OPERATION_SUCCESSFUL = "Data successfully saved"
TEXT_OPERATION_UNSUCCESSFUL = "Operation Unsuccessful"
TEXT_MISSING_PARAMS = "Params are missing"
INVALID_DATA = "Invalid data"

#------------ OpenExchangeRates Api Url -----------------
OPEN_EXCHANGE_RATES_API_URL = 'https://openexchangerates.org/api/latest.json?app_id='+settings.APP_ID
