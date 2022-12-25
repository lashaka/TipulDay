import cloudscraper
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import constants as const
class submit_forms(object):

    def __init__(
            self:object,
            websites,
            url,
            formname,
            formphone,
            formemail,
            formcomment,

            ) -> None:
        self.FORM_NAME = formname
        self.FORM_EMAIL = formemail
        self.FORM_COMMENT = formcomment
        self.FORM_PHONE = formphone
        self.SuccessfullForms=0
        self.FailedForms=0  
        self.websites = websites
        self.url = url

    def main(self) -> None:
        print(self.FORM_EMAIL,self.FORM_COMMENT,self.FORM_NAME,self.FORM_PHONE)
        print(const.SUBMIT_FORMS_TEXT)
        if len(self.websites) > 0:
            for website in self.websites:
                try:
                    response = requests.get(website)
                except:
                    print(const.ISSUE_5_TEXT)
                    self.FailedForms += 1
                    continue
                

                soup = BeautifulSoup(response.text, const.HTML_PARSER_TEXT)
                Domain = urlparse(website).netloc
                form_action = soup.find_all(const.HERF_AND_A_TEXT[2]) 
                for data in form_action:
                   action = data.get(const.HERF_AND_A_TEXT[3]) 
                   if action == f"{Domain}{const.HTTPS_HTTP_SLASH_TEXT[2]}" or action == f"{const.HTTPS_HTTP_SLASH_TEXT[0]}{Domain}{const.HTTPS_HTTP_SLASH_TEXT[2]}" or action == f"{const.HTTPS_HTTP_SLASH_TEXT[1]}{Domain}{const.HTTPS_HTTP_SLASH_TEXT[2]}":
                       continue
                   else:
                       try:     
                           if Domain in self.websites:
                               for website in self.websites:
                                   if Domain in self.websites:
                                       self.websites.remove(website)

                                       continue
                           break
                       except:
                           continue
                       
                       
                       
                       

                form_elements = soup.find_all(const.HERF_AND_A_TEXT[4]) + soup.find_all(const.HERF_AND_A_TEXT[5])

                form_data = {}
    
                for element in form_elements:
                    name = element.get(const.HERF_AND_A_TEXT[6])
                    value = element.get(const.HERF_AND_A_TEXT[7])  
                    form_data[name] = value

                for data in form_data:
                    try:
                        if const.FORM_DATA_TEXT[0] in data or const.FORM_DATA_TEXT[4] in data or const.FORM_DATA_TEXT[8] in data or const.FORM_DATA_TEXT[12] in data: 
                            form_data[data] = self.FORM_NAME
                        if const.FORM_DATA_TEXT[1] in data or const.FORM_DATA_TEXT[5] in data or const.FORM_DATA_TEXT[9] in data  or const.FORM_DATA_TEXT[13] in data or const.FORM_DATA_TEXT[16] in data or const.FORM_DATA_TEXT[18] in data:
                            form_data[data] = self.FORM_PHONE
                        if const.FORM_DATA_TEXT[2] in data or const.FORM_DATA_TEXT[6] in data or const.FORM_DATA_TEXT[10] in data or const.FORM_DATA_TEXT[14] in data:
                            form_data[data] = self.FORM_EMAIL
                        if const.FORM_DATA_TEXT[3] in data or const.FORM_DATA_TEXT[7] in data or const.FORM_DATA_TEXT[11] in data  or const.FORM_DATA_TEXT[15] in data or const.FORM_DATA_TEXT[17] in data or const.FORM_DATA_TEXT[19] in data:
                            form_data[data] = self.FORM_COMMENT             
                    except:
                        print(const.ERROR_6_TEXT, website)

                   
                if len(form_data) is 0:
                    print(const.ERROR_7_TEXT)
                    self.FailedForms += 1
                    continue
                else:
                    try:
                        print(const.TRYING_TO_POST, form_data)
                        response = requests.post(website, data=form_data)
                    except:
                        print(const.ERROR_4_TEXT)
                        self.FailedForms += 1
                        continue

                    if response.status_code == 200:  
                        print(const.SUCCESS_200_TEXT + website)
                        self.SuccessfullForms += 1
                        continue
                    else:
                        print(const.ERROR_2_TEXT,response.status_code)
                        self.FailedForms += 1
                        continue
            print("[*] Finished Submitting Forms")
            print('\n\tSuccessfully Filled Forms:', str(self.SuccessfullForms))
            print('\n\tFailed Forms:', str(self.FailedForms))  
        else:
            print(const.ERROR_1_TEXT)

