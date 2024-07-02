import json


def validate_phone(phone_number):
    response = send_to_phone_validation_service(phone_number)
    print (response)
    phone_type = get_phone_type(response)

    
    print(f'The caller is calling from a {phone_type}')

def main():
    phone_number = "19165482837"



    validate_phone(phone_number)

def get_phone_type(response):
    ##TODO Ryan to add code in this method
    ## do something to get phone_type
    phone_type = kdjfdkfjdkfjdkjfdkfj

    return phone_type

def send_to_phone_validation_service(phone_number):
    print(f'Validating phone number:{phone_number}')
    json_str = '''
      {
          "NumberValidateResponse": {
              "Carrier": "ExampleCorp Mobile",
              "City": "Seattle",
              "CleansedPhoneNumberE164": "+12065550142",
              "CleansedPhoneNumberNational": "2065550142",
              "Country": "United States",
              "CountryCodeIso2": "US",
              "CountryCodeNumeric": "1",
              "OriginalPhoneNumber": "+12065550142",
              "PhoneType": "MOBILE",
              "PhoneTypeCode": 0,
              "Timezone": "America/Los_Angeles",
              "ZipCode": "98101"
          }
      }
      '''


    return json_str


if __name__ == "__main__":
    main()
