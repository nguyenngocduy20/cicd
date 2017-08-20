import xml.etree.ElementTree


e = xml.etree.ElementTree.parse('results.xml').getroot()

fail = int(e.attrib.get('failures'))

errors = int(e.attrib.get('errors'))

# print("Failures: {} --> {}\nErrors: {} --> {}".format(fail, fail != 0, errors, errors != 0))

if fail != 0 or errors != 0:
   print('false')
else:
   print('true')