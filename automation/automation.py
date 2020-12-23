import re


def read_text(path):
    with open(path,'r') as f:
        text = f.read().strip()
        return text
    
  

def write_emails(text):
    email_pattern1 = r'([\w\.-]+)@([\w\.-]+)'
    
    # checking regex pattern
    emails = re.findall(email_pattern1,text)
    # my regex get the two part of email so I will join them by @
    for i in range(len(emails)):
        emails[i] = '@'.join(emails[i])
    # remove duplication
    emails = list(dict.fromkeys(emails))
    # sorting the emalis by alphapet
    emails.sort()
    result = ''
    for i in emails:
        result+=i+'\n'
    with open('assets/emails.txt','w') as f:
        f.write(f'{result}')




def write_phon_numbers(text):
    phone_pattern_without_extensions = r'([+]??\d{1,3}[-\.\s]??\d{1,3}[-\.\s]??\d{1,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    phone_pattern_with_extensions = r'([+]??\d{1,3}[-\.\s]??\d{1,3}[-\.\s]??\d{1,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})(x\d{1,5})'
    # Lists I will use them for each type of number
    without_paran_list = []
    with_international_number = []
    with_paran_list =[]
    # get the two lists first one all values without extentions(x) and second one values with extentions(x)
    phone_num = re.findall(phone_pattern_without_extensions,text)
    traverer_list=re.findall(phone_pattern_with_extensions,text)
    # my regex for extentions will get list of tupples each tuple will have two variables the numbers before (x) and the
    # numbers after (x) example: tuple ((917)016-7190 , x00972)
    for i in traverer_list:
        phone_num.append(''.join(i))
    
    # I will sparate the phone_num list which have all numbers to three lists one for numbers which have area code, 
    # one for numbers which have international code and one for numbers without international or area code
    for i in phone_num:
        if '(' not in i and '+' not in i and '001' not in i:
            without_paran_list.append(i)
        if '+' in i or '001' in i :
            with_international_number.append(i)
        if '(' in i:
            with_paran_list.append(i)

    # I will add area code (206) for two cases in the begging of the numbers without area code and international code
    # and the second case I will add it for numbers which have international code after the international code.
    for i in range(len(without_paran_list)):
        without_paran_list[i] = '(206)' +without_paran_list[i]

    for i in range(len(with_international_number)):
        if '+' in with_international_number[i]:
            with_international_number[i] =  with_international_number[i].replace('+1-','+1-(206)')
        else:
            with_international_number[i] =  with_international_number[i].replace('001-','001-(206)')

    result_list = without_paran_list + with_international_number + with_paran_list
    # Sorting and remove duplication 
    result_list.sort()
    result_list = list(dict.fromkeys(result_list))
    result = ''
    for i in result_list:
        result+=i+'\n'
    with open('assets/phone_numbers.txt','w') as f:
        f.write(f'{result}')
    


if __name__ == "__main__":
    write_emails(read_text('assets/potential-contacts.txt'))
    write_phon_numbers(read_text('assets/potential-contacts.txt'))