from streetaddress import StreetAddressFormatter, StreetAddressParser

parser = StreetAddressParser()

print(parser.parse('1st Main Road, 2nd Cross'))
print(parser.parse('1st Main Rd,2nd Cross'))
print(parser.parse('1stMain, 2nd Cr'))
print(parser.parse('1st Main2nd Cross'))

formatter = StreetAddressFormatter()
formatter.append_TH_to_street('1st Main Road, 2nd Cross')
print(formatter.abbrev_direction('1st Main Road, 2nd Cross'))
print(formatter.abbrev_street_avenue_etc('1st Main Road, 2nd Cross'))
